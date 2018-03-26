import { Component, OnInit } from '@angular/core';
import { Perfil } from '../perfil';
import { HttpClient, HttpHeaders } from '@angular/common/http';

@Component({
  selector: 'app-perfil',
  templateUrl: './perfil.component.html',
  styleUrls: ['./perfil.component.css']
})
export class PerfilComponent implements OnInit {

  atual : Perfil; // armazena objeto que aparece para o usuário
  data : any; // recebe os registros que são retornados da base de dados pela API

  modo : string; // Inicial, Cadastrar, Editar, Remover
  mensagem : string; // mensagem exibida para o usuário
  erro: string;
  alerta: string;

  constructor(private http: HttpClient) { }

  ngOnInit() {
  	this.mensagem = 'Olá, bem-vindo ao cadastro de perfis!';
    this.alerta = 'alert-info';
    this.erro = '';
    this.atual = new Perfil(0,'','');
    this.atualizar();
  }

  validar(){
    /*if (this.atual.codigo.length != 6){
      this.erro += "<br> > O campo código deve possuir seis dígitos ";
    }
    if (this.atual.nome.length < 5){
      this.erro += "<br> > O campo nome deve possuir mais que cinco dígitos ";
    }
    let retorno = this.atual.codigo.length == 6 && this.atual.nome.length >= 5;

    return retorno;*/
    return true;    
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
      	this.http.post<string>('http://127.0.0.1:5000/perfil/0', JSON.stringify(this.atual), {headers: header})
      	.subscribe(data => {self.atualizar();});
        this.mensagem = 'Perfil cadastrado com sucesso!';
        this.alerta = 'alert-success';
      }
      if (this.modo == 'Editar'){
        let header = new HttpHeaders();    
        let self = this;
        header.append('Content-Type', 'application/json');
        this.http.put<string>('http://127.0.0.1:5000/perfil/0', JSON.stringify(this.atual), {headers: header})
        .subscribe(data => {self.atualizar();});
        this.mensagem = 'Perfil editado com sucesso!';
        this.alerta = 'alert-success';
      }
      if (this.modo == 'Remover'){
        let header = new HttpHeaders();
        let self = this;   
        header.append('Content-Type', 'application/json');
        this.http.delete<string>('http://127.0.0.1:5000/perfil' + '/' + this.atual.codigo, {headers: header})
        .subscribe(data => {self.atualizar();});
        this.mensagem = 'Perfil removido com sucesso!';
        this.alerta = 'alert-success';
      }
    }else{
      this.erro = "Erro na validação dos dados! Por favor, corrija os seguintes campos:" + this.erro;
    }
  }

  atualizar(){
    this.modo = 'Inicial';
    this.http.get('http://127.0.0.1:5000/perfil')
    .subscribe(data => {this.data = data['mensagem'];});
  }

  cadastrar(){
    this.modo = 'Cadastrar';
    this.mensagem = 'Cadastro em processo';
    this.alerta = 'alert-warning';
    this.atual.atualizar(0,'','');
  }

  editar(registro){
    this.modo = 'Editar';
    this.mensagem = 'Edição em processo';
    this.alerta = 'alert-warning';
    this.atual.atualizar(registro['codigo'], registro['perfilNome'], registro['abreviacao']);
  }

  remover(registro){
    this.modo = 'Remover';
    this.mensagem = 'Remoção em processo';
    this.alerta = 'alert-warning';
    this.atual.atualizar(registro['codigo'], registro['perfilNome'], registro['abreviacao']);    
  }

  conferir(palavra){
    if(palavra == 'exibirCodigo'){
      return (this.modo == 'Editar');
    }
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
