import pyodbc

# Dicionario que contém os dados do banco de dados
def parametros_conexao():
    dicionario_conexao = {
        'server': "tcp:servidor-grupo-estudos-senai-001.database.windows.net,1433",
        'database': "BD_Escola_Senai_Alunos",
        'username': "grupo-master",
        'password': "170812@Lu",
        'driver': "{ODBC Driver 17 for SQL Server}"
        }
    return dicionario_conexao

#Função para conexão com BD
def conectar_bd(dicionario_conexao):
    conn_str = f"DRIVER={dicionario_conexao['driver']};SERVER={dicionario_conexao['server']};DATABASE={dicionario_conexao['database']};UID={dicionario_conexao['username']};PWD={dicionario_conexao['password']}"
    try:
        with pyodbc.connect(conn_str) as conn:
            cursor = conn.cursor()
            #cursor.execute("SELECT @@VERSION;")
            #row = cursor.fetchone()
            return cursor
    except Exception as e:
            return print(f"Erro na conexão: {e}")
    
#Função para cadastrar novos alunos
def insert_tbl_aluno(dicionario_conexao, dicionario_dados):
    cursor = conectar_bd(dicionario_conexao)
    try:
        sql = "INSERT INTO TBL_ALUNO(TB_AL_CPF, TB_AL_NOME,TB_AL_EMAIL,TB_AL_FONE, TB_AL_DATA) VALUES(?,?,?,?,?)"
        cursor.execute(sql, (dicionario_dados['CPF'], dicionario_dados['aluno'], dicionario_dados['email'], dicionario_dados['fone'], dicionario_dados['data']))
        cursor.commit()
    except Exception as e:
        print(f"Erro: {e}")
    finally:
        cursor.close()
        return print('Aluno cadastrado')

#Função para cadastrar novos cursos
def insert_tbl_curso(dicionario_conexao, dicionario_dados):
    cursor = conectar_bd(dicionario_conexao)
    try:
        sql = "INSERT INTO TBL_CURSO(TB_CS_CURSO, TB_CS_REQUISITO,TB_CS_CARGA_HORARIA, TB_CS_PRECO) VALUES(?,?,?,?)"
        cursor.execute(sql, (dicionario_dados['CURSO'], dicionario_dados['REQUISITO'], dicionario_dados['CARGA_HORARIA'], dicionario_dados['PRECO']))
        cursor.commit()
    except Exception as e:
        print(f"Erro: {e}")
    finally:
        cursor.close()
        return print('Curso cadastrado!')

#função para inserir dados em instrutores
def insert_tbl_instrutores(dicionario_conexao, dicionario_dados):
    cursor = conectar_bd(dicionario_conexao)
    try:
        sql = "INSERT INTO TBL_INSTRUTORES(TB_IN_NOME, TB_IN_EMAIL, TB_IN_VALOR_HORA, TB_IN_CERTIFICADOS) VALUES(?,?,?,?)"
        cursor.execute(sql, (dicionario_dados['NOME'], dicionario_dados['EMAIL'], dicionario_dados['VALOR_HORA'], dicionario_dados['CERTIFICADOS']))
        cursor.commit()
    except Exception as e:
        print(f"Erro: {e}")
    finally:
        cursor.close()
        return print('Instrutor cadastrado!')

#função para inserir dados em turma
def insert_tbl_turma(dicionario_conexao, dicionario_dados):
    cursor = conectar_bd(dicionario_conexao)
    try:
        sql = "INSERT INTO TBL_TURMAS(TB_TU_ID_INSTRUTORES, TB_TU_ID_CURSO, TB_TU_DATA_INICIO, TB_TU_DATA_FIM, TB_TU_CARGA_HORARIA) VALUES(?,?,?,?,?)"
        cursor.execute(sql, (dicionario_dados['ID_INSTRUTORES'], dicionario_dados['ID_CURSO'], dicionario_dados['DATA_INICIO'], dicionario_dados['DATA_FIM'], dicionario_dados['CARGA_HORARIA']))
        cursor.commit()
    except Exception as e:
        print(f"Erro: {e}")
    finally:
        cursor.close()
        return print('Turma Cadastrada!')

#função para inserir dados em matricula
def insert_tbl_matricula(dicionario_conexao, dicionario_dados):
    cursor = conectar_bd(dicionario_conexao)
    try:
        sql = "INSERT INTO TBL_MATRICULA(TB_MA_ID_TURMA, TB_MA_ID_ALUNO, TB_TU_DATA_MATRICULA) VALUES(?,?,?)"
        cursor.execute(sql, (dicionario_dados['ID_TURMA'], dicionario_dados['ID_ALUNO'], dicionario_dados['DATA_MATRICULA']))
        cursor.commit()
    except Exception as e:
        print(f"Erro: {e}")
    finally:
        cursor.close()
        return print('Aluno Matriculado!')
    
#função para retornar dados da tabela instrutores
def select_instrutor(dicionario_conexao):
    cursor = conectar_bd(dicionario_conexao)
    try:
        lista = []
        sql = "SELECT * FROM [dbo].[TBL_INSTRUTORES]"
        cursor.execute(sql)
        resultados = cursor.fetchall()
        for linha in resultados:
            dic = {
                'ID_INSTRUTOR': linha[0],
                'NOME_INSTRUTOR': linha[1],
                'EMAIL_INSTRUTOR': linha[2],
                'VALOR_HORA': linha[3],
                'CERTIFICADOS': linha[4]
            }
            lista.append(dic)
        return lista
    except Exception as e:
        print(f"Erro: {e}")
    finally:
        cursor.close()

#função para retornar dados da tabela cursos
def select_curso(dicionario_conexao):
    cursor = conectar_bd(dicionario_conexao)
    try:
        lista = []
        sql = "SELECT * FROM [dbo].[TBL_CURSO]"
        cursor.execute(sql)
        resultados = cursor.fetchall()
        for linha in resultados:
            dic = {
                'ID_CURSO': linha[0],
                'NOME_CURSO': linha[1],
                'REQUISITO': linha[2],
                'CARGA_HORARIA': linha[3],
                'PRECO': linha[4]
            }
            lista.append(dic)
        return lista
    except Exception as e:
        print(f"Erro: {e}")
    finally:
        cursor.close()

#função para retornar dados da tabela cursos
def select_turma(dicionario_conexao):
    cursor = conectar_bd(dicionario_conexao)
    try:
        lista = []
        sql = "SELECT T.TB_TU_ID_TURMA, C.TB_CS_CURSO, T.TB_TU_DATA_INICIO, T.TB_TU_DATA_FIM, T.TB_TU_CARGA_HORARIA FROM [dbo].[TBL_TURMAS] AS T INNER JOIN [dbo].[TBL_CURSO] AS C ON T.TB_TU_ID_CURSO = C.TB_CS_ID_CURSO"
        cursor.execute(sql)
        resultados = cursor.fetchall()
        for linha in resultados:
            dic = {
                'ID_TURMA': linha[0],
                'NOME_CURSO': linha[1],
                'DATA_INICIO': linha[2],
                'DATA_FIM': linha[3],
                'CARGA_HORARIA': linha[4]
            }
            lista.append(dic)
        return lista
    except Exception as e:
        print(f"Erro: {e}")
    finally:
        cursor.close()        

#função para retornar dados da tabela alunos
def select_aluno(dicionario_conexao):
    cursor = conectar_bd(dicionario_conexao)
    try:
        lista = []
        sql = "SELECT * FROM [dbo].[TBL_ALUNO]"
        cursor.execute(sql)
        resultados = cursor.fetchall()
        for linha in resultados:
            dic = {
                'ID_ALUNO': linha[0],
                'CPF': linha[1],
                'NOME': linha[2],
                'EMAIL': linha[3],
                'FONE': linha[4],
                'NASCIMENTO': linha[5]
            }
            lista.append(dic)
        return lista
    except Exception as e:
        print(f"Erro: {e}")
    finally:
        cursor.close()        