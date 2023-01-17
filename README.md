# App Angular con Flask come API
Una semplice APP che mostra come far comunicare un server Flask ed una applicazione in Angular.

### Argomenti affrontati
- [Servizi](./simpleApp/src/services/manager.service.ts)
- Routing
- Form
- Non vengono salvate le sessioni per accessi futuri

## Inizializzare l'app Angular
Per creare ed inizializza una nuova applicazione Angular e creare l'ambiente di lavoro si scive `ng new simpleApp`, bisogna prima installare a CLI di Angular con [NPM](https://www.npmjs.com/package/@angular/cli) `npm i @angular/cli -g`. In seguito creo un paio di componenti come quello del login `ng g c login`.<br>
Per questo progetto e' importanete installare [Bootstrap](https://getbootstrap.com/) (`ng add @ng-bootstrap/ng-bootstrap`) per lo stile!

### Importante!
- Quando si lavora con le *form* e' necessario importare le librerie `FormsModule` e `ReactiveFormsModule` nel file [app.modelues.ts](./simpleApp/src/app/app.module.ts)
- Quando bidogna eseguire richiesta HTTP e' necessario importare il modulo `HttpClientModule` da `@angular/common/http` nel file [app.modelues.ts](./simpleApp/src/app/app.module.ts)

## Inizializzare il server Python
Il server Python necessita dei seguenti moduli
| Libreria | Installazione | Richiesta | Descrizione
| --- | --- | :-: | --- |
| [Flask](https://flask.palletsprojects.com/en/2.2.x/) | `pip install Flask` | ✔ | Libreria per avviare il server
| [CORS](https://flask-cors.readthedocs.io/en/latest/) | `pip install flask-cors` | ✔ | Cross-Origin Resource Sharing, che permette ad Angular di interagire con il sevrer Flask
| [dotenv](https://pypi.org/project/python-dotenv/) | `pip install python-dotenv` | ❌ | Qualora si volessero nascondere le credenziali della connessione al Database si possono salvare in un fille `.env`

# Il progetto non funziona?
![Bitbucket open issues](https://img.shields.io/bitbucket/issues/CappuCitti/Simple-Angular-app-with-Flask-API?style=flat-square)
![Bitbucket open pull requests](https://img.shields.io/bitbucket/pr/CappuCitti/Simple-Angular-app-with-Flask-API?style=flat-square)<br>
Se il progetto non dovesse funzionare apri una [issue](https://github.com/CappuCitti/Simple-Angular-app-with-Flask-API/issues/new) descrivendo il problema!