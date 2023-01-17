# App Angular con Flask come API
Una semplice APP che mostra come far comunicare un server Flask e una applicazione in Angular.

### Argomenti affrontati
- [Servizi](./simpleApp/src/services/manager.service.ts)
- Routing
- Form
- Non vengono salvate le sessioni per accessi futuri

## Inizializzare l'app Angular
Per creare e inizializzare una nuova applicazione Angular e creare l'ambiente di lavoro si scrive `ng new simpleApp`, bisogna prima installare a CLI di Angular con [NPM](https://www.npmjs.com/package/@angular/cli) `npm i @angular/cli -g`. In seguito creo un paio di componenti come quello del login `ng g c login`.<br>
Per questo progetto è importanete installare [Bootstrap](https://getbootstrap.com/) (`ng add @ng-bootstrap/ng-bootstrap`) per lo stile!

### Importante!
- Quando si lavora con le *form* è necessario importare le librerie `FormsModule` e `ReactiveFormsModule` nel file [app.modelues.ts](./simpleApp/src/app/app.module.ts)
- Quando bidogna eseguire richiesta HTTP è necessario importare il modulo `HttpClientModule` da `@angular/common/http` nel file [app.modelues.ts](./simpleApp/src/app/app.module.ts)

## Inizializzare il server Python
Il server Python necessita dei seguenti moduli
| Libreria | Installazione | Richiesta | Descrizione
| --- | --- | :-: | --- |
| [Flask](https://flask.palletsprojects.com/en/2.2.x/) | `pip install Flask` | ✔ | Libreria per avviare il server |
| [CORS](https://flask-cors.readthedocs.io/en/latest/) | `pip install flask-cors` | ✔ | Cross-Origin Resource Sharing, che permette ad Angular d'interagire con il sevrer Flask |
| [dotenv](https://pypi.org/project/python-dotenv/) | `pip install python-dotenv` | ❌ | Qualora si volessero nascondere le credenziali della connessione al Database si possono salvare in un fille `.env` |