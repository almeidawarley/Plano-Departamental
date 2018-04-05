import { Component, OnInit } from '@angular/core';
import { Disciplina } from '../disciplina';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { FormGroup, FormControl, Validators } from '@angular/forms';

@Component({
  selector: 'app-disciplina',
  templateUrl: './disciplina.component.html',
  styleUrls: ['./disciplina.component.css']
})
export class DisciplinaComponent implements OnInit {
  
  atual : Disciplina;
  data : any;
  perfis: any;

  modo : string; // Inicial, Cadastrar, Editar, Remover
  mensagem : string;
  erro: string;
  alerta: string;

  constructor(private http: HttpClient) {

  }

  ngOnInit() {
    this.mensagem = 'Olá, bem-vindo ao cadastro de disciplinas!';
    this.alerta = 'alert-info';
    this.erro = '';
    this.atual = new Disciplina('','',0,0,0);
    this.atualizar();
  }

  validar(){
    if (this.atual.codigo.length != 6){
      this.erro += "<br> > O campo código deve possuir seis dígitos ";
    }
    if (this.atual.nome.length < 5){
      this.erro += "<br> > O campo nome deve possuir mais que cinco dígitos ";
    }
    let retorno = this.atual.codigo.length == 6 && this.atual.nome.length >= 5;

    return retorno;    
  }

  cancelar(){
    this.mensagem = 'Ação de ' + this.modo + ' cancelada';
    this.modo = 'Inicial';
    this.alerta = 'alert-info';
  }

  submeter(){
    if(this.validar()){
      if (this.modo == 'Cadastrar'){
        let header = new HttpHeaders();    
        let self = this;
        header.append('Content-Type', 'application/json');
        header.append('Authorization', 'abcde');
      	this.http.post<string>('http://127.0.0.1:5000/disciplina/', JSON.stringify(this.atual), {headers: header})
      	.subscribe(data => {self.atualizar();});
        this.mensagem = 'Disciplina cadastrada com sucesso!';
        this.alerta = 'alert-success';
      }
      if (this.modo == 'Editar'){
        let header = new HttpHeaders();    
        let self = this;
        header.append('Content-Type', 'application/json');
        this.http.put<string>('http://127.0.0.1:5000/disciplina/', JSON.stringify(this.atual), {headers: header})
        .subscribe(data => {self.atualizar();});
        this.mensagem = 'Disciplina editada com sucesso!';
        this.alerta = 'alert-success';
      }
      if(this.modo == 'Remover'){
        let header = new HttpHeaders();
        let self = this;   
        header.append('Content-Type', 'application/json');
        this.http.delete<string>('http://127.0.0.1:5000/disciplina' + '/' + this.atual.codigo, {headers: header})
        .subscribe(data => {self.atualizar();});
        this.mensagem = 'Disciplina removida com sucesso!';
        this.alerta = 'alert-success';
      }
    }else{
      this.erro = "Erro na validação dos dados! Por favor, corrija os seguintes campos:" + this.erro;
    }
  }

  atualizar(){
    this.modo = 'Inicial';
    this.http.get('http://127.0.0.1:5000/disciplina/')
    .subscribe(data => {this.data = data['mensagem'];});
    this.http.get('http://127.0.0.1:5000/perfil/').
    subscribe(data => {this.perfis = data['mensagem'];});
  }

  cadastrar(){
    this.modo = 'Cadastrar';
    this.mensagem = 'Cadastro em processo';
    this.alerta = 'alert-warning';
    this.atual.atualizar('','','',0,0);
  }

  editar(registro){
    this.modo = 'Editar';
    this.mensagem = 'Edição em processo';
    this.alerta = 'alert-warning';
    this.atual.atualizar(registro['codigo'], registro['nome'], registro['perfil'], registro['chTeorica'], registro['chPratica']);
  }

  remover(registro){
    this.modo = 'Remover';    
    this.mensagem = 'Remoção em processo';
    this.alerta = 'alert-warning';
    this.atual.atualizar(registro['codigo'], registro['nome'], registro['perfil'], registro['chTeorica'], registro['chPratica']);
  }

  conferir(palavra){
    if(palavra == 'mostrarFormulario'){
      return (this.modo  == 'Cadastrar' || this.modo == 'Editar' || this.modo == 'Remover');
    }
    if(palavra == 'editarCodigo'){
      return (this.modo == 'Cadastrar');
    }
    if(palavra == 'editarFormulario'){
      return (this.modo == 'Cadastrar' || this.modo == 'Editar');
    }
    if(palavra == 'mostrarAviso'){
      return this.data == undefined;
    }
  }
}
