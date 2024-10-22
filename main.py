#importando funções de funcoes_insert.py
from funcoes.funcoes_insert import parametros_conexao
from funcoes.funcoes_insert import insert_tbl_aluno
from funcoes.funcoes_insert import insert_tbl_curso
from funcoes.funcoes_gerais import converter_data
from funcoes.funcoes_insert import insert_tbl_instrutores
from funcoes.funcoes_insert import select_instrutor
from funcoes.funcoes_insert import select_curso
from funcoes.funcoes_insert import insert_tbl_turma
from funcoes.funcoes_insert import select_turma
from funcoes.funcoes_insert import select_aluno
from funcoes.funcoes_insert import insert_tbl_matricula

import pandas as pd

print('------------------------------------------------------------')
print('-------------------------------------------------------------')
print('-------------------------------------------------------------')
print('--------------------Bem vindo ao SymCourse-------------------')
print('-------------------------------------------------------------')
print('-------------------------------------------------------------')
print('-------------------------------------------------------------\n')
print('---------------------Digite a opção desejada:----------------\n')
opcao_desejada = int(input('Digite 1 para cadastrar aluno: \nDigite 2 para cadastrar curso: \nDigite 3 para cadastrar Instrutor: \nDigite 4 para listar os instrutores: \nDigite 5 para listar os cursos: \nDigite 6 para cadastrar Turmas \nDigite 7 para matricular aluno '))

if opcao_desejada == 1:
    #PARA CHAMAR AS FUNÇÕES DOS BLOCOS ACIMA APERTAR SHIFT + ENTER -jupyter-
    #Solicitando dados ao usuário
    CPF = input("Digite o cpf apenas número: ")
    aluno = input("Digite o nome: ")
    email = input('Digite o e-mail: ')
    fone = input('Digite o telefone com ddd apenas número: ')
    dia = int(input('Digite o dia de nascimento: '))
    mes = int(input('Digite o mês de nascimento: '))
    ano = int(input('Digite o ano de nascimento: '))
    #inserindo dados no dicionario de dados 
    dicionario_aluno = {
        'CPF': CPF,
        'aluno': aluno,
        'email': email,
        'fone': fone,
        'data': converter_data(dia, mes, ano)
    }
    #Chamando a função de inserção de dados na tabela Alunos
    param_conex = parametros_conexao() 
    insert_tbl_aluno(param_conex, dicionario_aluno)
elif opcao_desejada == 2:
    #linhas de comando
    #PARA CHAMAR AS FUNÇÕES DOS BLOCOS ACIMA APERTAR SHIFT + ENTER -jupyter-
    #Solicitando dados do curso
    curso = input("Digite o curso: ")
    requisito = input("Digite os requisitos: ")
    carga_horaria = int(input('Digite a carga horária (somente números): '))
    preco = float(input('Digite o preço: '))
    #Cadastrando os dados no dicionario
    dicionario_curso = {
        'CURSO': curso,
        'REQUISITO': requisito,
        'CARGA_HORARIA': carga_horaria,
        'PRECO': preco
    }
    #Chamando a função de inserção de dados na tabela cursos
    param_conex = parametros_conexao() 
    insert_tbl_curso(param_conex, dicionario_curso)
elif opcao_desejada == 3:
    nome = input("Digite o nome do instrutor: ")
    email = input("Digite o email do instrutor: ")
    valor_hora = int(input('Digite o valor hora do instrutor: '))
    certificados = input('Digite os certificados do instrutor: ')
    #Cadastrando os dados no dicionario
    dicionario_instrutor = {
        'NOME': nome,
        'EMAIL': email,
        'VALOR_HORA': valor_hora,
        'CERTIFICADOS': certificados
    }
    #Chamando a função de inserção de dados na tabela instrutores
    param_conex = parametros_conexao() 
    insert_tbl_instrutores(param_conex, dicionario_instrutor)
elif opcao_desejada == 4:
    # compilando resultados de instrutor
    # usando pandas para criar tabela de resultado
    # Emocionado !!
    param_conex = parametros_conexao() 
    lista = select_instrutor(param_conex)
    tabela = pd.DataFrame(lista, columns=['ID_INSTRUTOR', 'NOME_INSTRUTOR', 'EMAIL_INSTRUTOR', 'VALOR_HORA', 'CERTIFICADOS'])
    print(tabela)
elif opcao_desejada == 5:
    # compilando resultados de instrutor
    # usando pandas para criar tabela de resultado
    # Emocionado !!
    param_conex = parametros_conexao() 
    lista = select_curso(param_conex)
    tabela = pd.DataFrame(lista, columns=['ID_CURSO', 'NOME_CURSO', 'REQUISITO', 'CARGA_HORARIA', 'PRECO'])
    print(tabela)
elif opcao_desejada == 6:
    # Informando curso e instrutores disponíveis
    param_conex = parametros_conexao()
    lista = select_curso(param_conex)
    tabela = pd.DataFrame(lista, columns=['ID_CURSO', 'NOME_CURSO', 'REQUISITO', 'CARGA_HORARIA', 'PRECO'])
    print(tabela)
    #recebendo dados do curso
    id_curso = int(input("Digite o ID do curso: "))
    lista2 = select_instrutor(param_conex)
    tabela2 = pd.DataFrame(lista2, columns=['ID_INSTRUTOR', 'NOME_INSTRUTOR', 'EMAIL_INSTRUTOR', 'VALOR_HORA', 'CERTIFICADOS'])
    print(tabela2)
    #recebendo dados de id_instrutor da turma
    id_instrutor = int(input("Digite o ID do Instrutor: "))
    #recebendo dados de inicio e final da turma
    dia_curso_inicio = int(input("Digite o dia do inicio do curso: "))
    mes_curso_inicio = int(input("Digite o mês do inicio do curso: "))
    ano_curso_inicio = int(input("Digite o ano do inicio do curso: "))
    dia_curso_final = int(input("Digite o dia do final do curso: "))
    mes_curso_final = int(input("Digite o mês do final do curso: "))
    ano_curso_final = int(input("Digite o ano do final do curso: "))
    carga_horaria = int(input("Digite a carga horária"))
    data_inicial = converter_data(dia_curso_inicio, mes_curso_inicio, ano_curso_inicio)
    data_final = converter_data(dia_curso_final, mes_curso_final, ano_curso_final)
    #Cadastrando os dados no dicionario
    dicionario_turma = {
        'ID_INSTRUTORES': id_instrutor,
        'ID_CURSO': id_curso,
        'DATA_INICIO': data_inicial,
        'DATA_FIM': data_final,
        'CARGA_HORARIA': carga_horaria 
    }
    insert_tbl_turma(param_conex, dicionario_turma)
#Efetuar Matricula
elif opcao_desejada == 7:
    param_conex = parametros_conexao()
    #pesquisando turmas abertas
    lista = select_turma(param_conex)
    tabela = pd.DataFrame(lista, columns=['ID_TURMA', 'NOME_CURSO', 'DATA_INICIO', 'DATA_FIM', 'CARGA_HORARIA'])
    print(tabela)
    #recebendo dados da turma
    id_turma = int(input("Digite o ID da turma: "))
    #pesquisando alunos
    lista2 = select_aluno(param_conex)
    tabela2 = pd.DataFrame(lista2, columns=['ID_ALUNO', 'CPF', 'NOME', 'EMAIL', 'FONE', 'NASCIMENTO'])
    print(tabela2)
    #recebendo dados da turma
    id_aluno = int(input("Digite o ID da turma: "))
    dia_matricula = int(input("Digite o dia da matricula: "))
    mes_matricula = int(input("Digite o mês da matricula: "))
    ano_matricula = int(input("Digite o ano da matricula: "))
    #convertendo data
    data_matricula = converter_data(dia_matricula, mes_matricula, ano_matricula)
    #Cadastrando os dados no dicionario
    dicionario_matricula = {
        'ID_TURMA': id_turma,
        'ID_ALUNO': id_aluno,
        'DATA_MATRICULA': data_matricula
    }
    insert_tbl_matricula(param_conex, dicionario_matricula)
else:
    #linhas de comando
    print('Opção inválida!')