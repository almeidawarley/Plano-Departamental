export class Perfil {

  constructor(
  	public codigo: number,
    public nome: string,
    public abreviacao: string
  ) {  }

  atualizar(codigo, nome, abreviacao){
  	this.codigo = codigo;
  	this.nome = nome;
  	this.abreviacao = abreviacao;
  }

}
