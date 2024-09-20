from modulo import *

if __name__ == "__main__":
    # instância dos objetos
    endereco_pessoal = Endereco('','','','')
    telefones = Telefone('','','')
    usuario = Pessoa('',0,'','')

    endereco_pessoal.cep = "72.666-666"
    endereco_pessoal.uf = "DF"
    endereco_pessoal.cidade = "Taguatinga"
    endereco_pessoal.bairro = "Campo da Esperança"

    # entrada de dados do usuário
    usuario.nome = input("Informe o nome do usuário: ")
    usuario.idade = int(input("Informe a idade do usuário: "))

    # composição usuário:endereço
    usuario.endereco = endereco_pessoal
    usuario.telefone = telefones

    # saída de dados
    usuario.telefone.pessoal =  input("Informe o telefone pessoal: ")
    usuario.telefone.comercial =  input("Informe o telefone comercial: ")
    usuario.telefone.empresarial =  input("Informe o telefone empresarial: ")

    # entrada de dados do endereço
    usuario.endereco.cep = input("Informe o CEP: ")
    usuario.endereco.uf = input("Informe o UF: ")
    usuario.endereco.cidade = input("Informe a cidade: ")
    usuario.endereco.bairro = input("Informe o bairro: ")
    
    # saída de dados
    print(usuario.obter_info_pessoal())