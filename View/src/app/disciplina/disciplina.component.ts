import { Component, OnInit } from '@angular/core';
import { Disciplina } from '../disciplina';
import { HttpClient, HttpHeaders } from '@angular/common/http';

@Component({
  selector: 'app-disciplina',
  templateUrl: './disciplina.component.html',
  styleUrls: ['./disciplina.component.css']
})
export class DisciplinaComponent implements OnInit {
  
  atual : Disciplina; // armazena objeto que aparece para o usuário
  data : any; // recebe os registros que são retornados da base de dados pela API

  modo : string; // Inicial, Cadastrar, Exibir, Editar, Remover
  mensagem : string; // mensagem exibida para o usuário

  constructor(private http: HttpClient) {

  }

  ngOnInit() {
    this.modo = 'Inicial';  
    this.mensagem = 'Olá, bem-vindo às disciplinas!';

  	this.http.get<Disciplina>('http://127.0.0.1:5000/disciplina')
  	.subscribe(data => {this.atual = data;});
    this.getDisciplinas();
  }

  getDisciplinas(){
    this.data = this.http.get('http://127.0.0.1:5000/listadisciplina')
    .subscribe(data => {this.data = data;});
  }

  submeter(){
    if (this.modo == 'Cadastrar'){
      let header = new HttpHeaders();    
      header.append('Content-Type', 'application/json');
    	this.http.post<string>('http://127.0.0.1:5000/rec', JSON.stringify(this.atual), {headers: header})
    	.subscribe(data => alert('OK'));
    }
    if (this.modo == 'Editar'){
      let header = new HttpHeaders();    
      header.append('Content-Type', 'application/json');
      this.http.put<string>('http://127.0.0.1:5000/put', JSON.stringify(this.atual), {headers: header})
      .subscribe(data => alert('OK'));
    }

    this.modo == 'Inicial'
    this.getDisciplinas();
  }

  cadastrar(){
    this.modo = 'Cadastrar';
    this.atual = new Disciplina('','','',0,0);
  }

  exibir(registro){
    this.modo = 'Exibir';
    this.atual = new Disciplina(registro[0], registro[1], registro[2], registro[3], registro[4]);
  }

  editar(registro){
    this.modo = 'Editar';
    this.atual = new Disciplina(registro[0], registro[1], registro[2], registro[3], registro[4]);
  }

  remover(registro){
    let header = new HttpHeaders();    
    header.append('Content-Type', 'application/json');
    this.atual = new Disciplina(registro[0], registro[1], registro[2], registro[3], registro[4]);
    this.http.post<string>('http://127.0.0.1:5000/removerdisciplina', JSON.stringify(this.atual), {headers: header})
    .subscribe(data => alert('OK'));
    this.getDisciplinas();
  }

  conferir(palavra){
    if(palavra == 'botao'){
      return (this.modo  == 'Cadastrar' || this.modo == 'Editar');
    }
    if(palavra == 'formulario'){
      return (this.modo  == 'Cadastrar' || this.modo == 'Editar' || this.modo == 'Exibir');
    }
  }

}
