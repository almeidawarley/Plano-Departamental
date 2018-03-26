export class Disciplina {

  constructor(
    public codigo: string,
    public nome: string,
    public perfil: number,
    public chTeorica: number,
    public chPratica: number
  ) {  }

  atualizar(codigo, nome, perfil, chTeorica, chPratica){
  	this.codigo = codigo;
  	this.nome = nome;
  	this.perfil = perfil;
  	this.chTeorica = chTeorica;
  	this.chPratica = chPratica;
  }

}
