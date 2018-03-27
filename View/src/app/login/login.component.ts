import { Component, OnInit } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { AuthService } from '../auth.service';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {

	email : string;
	senha : string;

	constructor(private http: HttpClient, private authService: AuthService) { }

	ngOnInit() {

	}

	submeter(){
		this.authService.login(this.email, this.senha);
	}

	isLoggedIn(){
		return this.authService.isLoggedIn();		
	}

	logout(){
		this.authService.logout();
	}
}
