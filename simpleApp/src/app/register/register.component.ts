import { HttpClient, HttpHeaders, HttpParams } from '@angular/common/http';
import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { Router } from '@angular/router';
import { Data } from 'src/models/request.model';
import { ManagerService } from 'src/services/manager.service';

@Component({
  selector: 'app-register',
  templateUrl: './register.component.html',
  styleUrls: ['./register.component.css']
})
export class RegisterComponent implements OnInit {
  form!: FormGroup;
  errorMessage!: string;
  statusCode!: number;

  constructor(
    private fb: FormBuilder,
    private http: HttpClient,
    private router: Router,
    private manager: ManagerService
  ) { }

  ngOnInit(): void {
    // Controllo se l'utente ha gia' eseguito il login
    if (this.manager.getUser.id != -1) this.router.navigate(['/dashboard']);
    
    // Inizializzo la form
    this.form = this.fb.group({
      email: ["", [Validators.required, Validators.email]],
      name: ["", [Validators.required]],
      surname: ["", [Validators.required]],
      password: ["", [Validators.required]],
      borndate: ["", [Validators.required]],
      // Dichiaro che questo input non e' obbligatorio
      info: [""],
      // Definisco il valore di default dei "radio buttons"
      gender: ["male", [Validators.required]]
    })
  }

  submit() {
    // Creo l'oggetto che verra' inviaro al server Flask con le credenziali delll'utente
    let body: HttpParams = new HttpParams().appendAll({
      'email': this.form.value.email,
      'firstname': this.form.value.name,
      'lastname': this.form.value.surname,
      'password': this.form.value.password,
      'borndate': this.form.value.borndate,
      'info': this.form.value.info,
      'gender': this.form.value.gender
    });

    // Eseguo la richiesta in POST
    this.http.post<Data>('http://127.0.0.1:3000/api/register', '', {
      headers: new HttpHeaders({
        'Content-Type': 'application/json'
      }),
      params: body,
      responseType: "json"
    }).subscribe(data => {
      // Aspetto la risposta del server e comunico all'utente la risposta
      if (data.statusCode == 200) {
        // Invio le informazioni dell'utente alle pagine in ascolto
        this.manager.setUser(data.data);

        // Reindirizzo l'utente alla sua dashboard
        this.router.navigate(['/dashboard']);
      } else {
        this.statusCode = data.statusCode;
        this.errorMessage = data.errorMessage;
      }
    });
  }
}
