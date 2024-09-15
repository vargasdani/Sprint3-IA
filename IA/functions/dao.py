import cx_Oracle
import json
from datetime import datetime

def conectar_bd():
    dsn = cx_Oracle.makedsn(host='oracle.fiap.com.br', port=1521, sid='ORCL')
    conn = cx_Oracle.connect(user='RM99400', password='060603', dsn=dsn)
    return conn

# Função para inserir cultura com base nos novos campos do dataset
def inserir_cultura(cultura, tipo_solo, tipo_irrigacao, frequencia_irrigacao, temperatura_media, fertilizante, quantidade_plantada, pragas, rotacao_culturas, tecnologia_utilizada):
    try:
        conn = conectar_bd()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO T_CULTURAS (CULTURA, TIPO_SOLO, TIPO_IRRIGACAO, FREQUENCIA_IRRIGACAO, TEMPERATURA_MEDIA, FERTILIZANTE, QUANTIDADE_PLANTADA, PRAGAS, ROTACAO_CULTURAS, TECNOLOGIA_UTILIZADA) "
            "VALUES (:cultura, :tipo_solo, :tipo_irrigacao, :frequencia_irrigacao, :temperatura_media, :fertilizante, :quantidade_plantada, :pragas, :rotacao_culturas, :tecnologia_utilizada)",
            cultura=cultura, tipo_solo=tipo_solo, tipo_irrigacao=tipo_irrigacao, frequencia_irrigacao=frequencia_irrigacao, 
            temperatura_media=temperatura_media, fertilizante=fertilizante, quantidade_plantada=quantidade_plantada, 
            pragas=pragas, rotacao_culturas=rotacao_culturas, tecnologia_utilizada=tecnologia_utilizada)

        cursor.close()
        conn.commit()
        conn.close()

        return "Cultura inserida com sucesso"

    except cx_Oracle.DatabaseError as e:
        return e

def atualizar_cultura(cultura, tipo_solo, tipo_irrigacao, frequencia_irrigacao, temperatura_media, fertilizante, quantidade_plantada, pragas, rotacao_culturas, tecnologia_utilizada):
    if not cultura_existe(cultura):
        print(f"Cultura {cultura} não cadastrada, não é possível alterar!")
        return

    try:
        conn = conectar_bd()
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE T_CULTURAS SET "
            "TIPO_SOLO=:tipo_solo, TIPO_IRRIGACAO=:tipo_irrigacao, FREQUENCIA_IRRIGACAO=:frequencia_irrigacao, TEMPERATURA_MEDIA=:temperatura_media, "
            "FERTILIZANTE=:fertilizante, QUANTIDADE_PLANTADA=:quantidade_plantada, PRAGAS=:pragas, ROTACAO_CULTURAS=:rotacao_culturas, "
            "TECNOLOGIA_UTILIZADA=:tecnologia_utilizada WHERE CULTURA=:cultura",
            tipo_solo=tipo_solo, tipo_irrigacao=tipo_irrigacao, frequencia_irrigacao=frequencia_irrigacao, temperatura_media=temperatura_media, 
            fertilizante=fertilizante, quantidade_plantada=quantidade_plantada, pragas=pragas, rotacao_culturas=rotacao_culturas, 
            tecnologia_utilizada=tecnologia_utilizada, cultura=cultura)

        cursor.close()
        conn.commit()
        conn.close()

        return "Cultura alterada com sucesso"

    except cx_Oracle.DatabaseError as e:
        return e

def inserir_producao(cultura, tipo_solo, tipo_irrigacao, frequencia_irrigacao, producao_estimada, quantidade_plantada):    
    if not cultura_existe(cultura):
        print(f"Cultura {cultura} não cadastrada, não é possível criar um registro de produção para essa cultura.")
        return

    try:
        conn = conectar_bd()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO T_PRODUCAO (CULTURA, TIPO_SOLO, TIPO_IRRIGACAO, FREQUENCIA_IRRIGACAO, PRODUCAO_ESTIMADA, QUANTIDADE_PLANTADA) "
            "VALUES (:cultura, :tipo_solo, :tipo_irrigacao, :frequencia_irrigacao, :producao_estimada, :quantidade_plantada)",
            cultura=cultura, tipo_solo=tipo_solo, tipo_irrigacao=tipo_irrigacao, frequencia_irrigacao=frequencia_irrigacao, 
            producao_estimada=producao_estimada, quantidade_plantada=quantidade_plantada)

        cursor.close()
        conn.commit()
        conn.close()

        return "Registro de produção criado com sucesso"

    except cx_Oracle.DatabaseError as e:
        return e

def exibir_culturas():
    try:
        conn = conectar_bd()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM T_CULTURAS")
        rows = cursor.fetchall()

        columns = [desc[0] for desc in cursor.description]

        cursor.close()
        conn.close()

        culturas = [dict(zip(columns, row)) for row in rows]
        culturas_json = json.dumps(culturas, default=default_serializer, indent=2)

        return culturas_json

    except cx_Oracle.DatabaseError as e:
        return e

def exibir_producao():
    try:
        conn = conectar_bd()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM T_PRODUCAO")
        rows = cursor.fetchall()

        columns = [desc[0] for desc in cursor.description]

        cursor.close()
        conn.close()

        producao = [dict(zip(columns, row)) for row in rows]
        producao_json = json.dumps(producao, default=default_serializer, indent=2)

        return producao_json

    except cx_Oracle.DatabaseError as e:
        return e
