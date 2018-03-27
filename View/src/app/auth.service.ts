import * as moment from "moment";
import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Router} from '@angular/router';

@Injectable()
export class AuthService {

    constructor(private http: HttpClient, private router: Router) {

    }

    login(email:string, password:string ) {
        return this.http.post('http://127.0.0.1:5000/login', {'login': email, 'senha':password})
        .subscribe(data => {this.setSession(data);});
    }
          
    private setSession(authResult) {
        alert
        if(!authResult['sucesso']){
            alert('Erro no login, tente novamente');
        }else{
            const expiresEm = moment().add(authResult['expiraEm'],'second');
            localStorage.setItem('id_token', authResult['token']);
            localStorage.setItem("expires_at", JSON.stringify(expiresEm.valueOf()));
            //this.router.navigate(['/disciplinas']);
        }
    }          

    logout() {
        localStorage.removeItem("id_token");
        localStorage.removeItem("expires_at");
    }

    public isLoggedIn() {
        return moment().isBefore(this.getExpiration());
    }

    isLoggedOut() {
        return !this.isLoggedIn();
    }

    getExpiration() {
        const expiration = localStorage.getItem("expires_at");
        const expiraEm = JSON.parse(expiration);
        return moment(expiraEm);
    }    
}