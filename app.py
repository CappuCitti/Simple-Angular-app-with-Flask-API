
from flask import Flask, jsonify, request
from flask_cors import CORS

from os import getenv
from dotenv import load_dotenv
load_dotenv()

import pymssql as sql


# Importo le credenziali per SQL e connetto il database
db_server = getenv("SQL_SERVER")
db_user = getenv("SQL_USERNAME")
db_password = getenv("SQL_PASSWORD")
db_name = getenv("SQL_DATABASE")
conn = sql.connect(db_server, db_user, db_password, db_name)

# Inizializzo il server Flask
app = Flask(__name__)
CORS(app)

# Funzione per controllare se l'email delll'utente e' presente nel Database
def user_exists(email):
  q = 'SELECT * FROM users WHERE email = %(e)s'
  cursor = conn.cursor(as_dict=True)
  cursor.execute(q, params={"e": email})
  res = cursor.fetchall()
  if len(res) < 1:
    return False
  return True

def get_user(email):
  q = 'SELECT * FROM users WHERE email = %(email)s'
  cursor = conn.cursor(as_dict=True)
  cursor.execute(q, params={"email": email})
  res = cursor.fetchall()
  return res


@app.route('/')
def info():
  return jsonify({"app-version": "0.0.1"})

@app.route('/api/register', methods=['POST'])
def register():
  user_params = {
    "email": request.args.get('email'),
    "password": request.args.get('password'),
    "firstname": request.args.get('firstname'),
    "lastname": request.args.get('lastname'),
    "borndate": request.args.get('borndate'),
    "info": request.args.get('info'),
    "gender": request.args.get('gender'),
  }

  data = {
    "statusCode": 200,
    "errorMessage": "",
    "data": {}
  }

  # Controllo se tutti i parametri sono stati inseriti nella richiesta
  if None not in [*user_params.values()]:
    # Controllo se l'utente esiste gia'
    if not user_exists(user_params["email"]):
      # Inserisco l'utente nel database
      cursor = conn.cursor(as_dict=True)
      q = 'INSERT INTO users (email, password, first_name, last_name, born_date, info, gender) VALUES (%(email)s, %(password)s, %(firstname)s, %(lastname)s, %(borndate)s, %(info)s, %(gender)s)'
      cursor.execute(q, params=user_params)
      conn.commit()

      # Restituisco l'utente
      data["data"] = get_user(user_params['email'])
    else:
      data["statusCode"] = 403
      data["errorMessage"] = "User already exists"
  else:
    data["statusCode"] = 400
    data["errorMessage"] = 'Missing values in the request'

  return jsonify(data)

@app.route('/api/login', methods=['POST'])
def login():
  # Prendo gli argomenti richiesti
  email = request.args.get('email')
  password = request.args.get('password')

  data = {
    "statusCode": 200,
    "errorMessage": "",
    "data": {}
  }

  # Controllo se nono stati passati tutti i parametri richiesti
  if None not in [email, password]:
    # Prendo le informazioni dell'utente
    q = 'SELECT * FROM users WHERE email = %(e)s'
    cursor = conn.cursor(as_dict=True)
    cursor.execute(q, params={"e": email})
    res = cursor.fetchall()

    # Controllo se l'utente esiste
    if len(res) < 1:
      data["statusCode"] = 404
      data["errorMessage"] = "No user was found with that email"
    elif not (res[0]["password"] == password):
      data["statusCode"] = 403
      data["errorMessage"] = "Wrong password"
    else:
      data["data"] = res
  else:
    data['statusCode'] = 400
    data['errorMessage'] = "No email or password provided"
  
  return jsonify(data)

@app.route('/api/details', methods=['GET'])
def get_details():
  email = request.args.get("email")

  # Prendo tutti gli utente con la email richiesta
  res = get_user(email)

  data = {
    "statusCode": 200,
    "errorMessage": "",
    "data": {}
  }

  # Controllo se l'utente esiste
  if len(res) < 1:
    data["statusCode"] = 404
    data["errorMessage"] = "User not found"
  else:
    # Restituisco l'utente
    data["data"] = res
  return jsonify(data) 


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True, port=3000)