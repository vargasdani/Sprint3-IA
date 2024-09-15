import json
import pandas as pd
import pickle
import requests
from flask import Flask, request, render_template, jsonify
from functions.data_transform import completa_dataframe_agricola
import google.generativeai as genai


#aqui, nós apenas carregamos o modelo conforme treinado no notebook Tech_Splinter.ipynb
modelo = pickle.load(open(r'IA\models\random_forest_regressor_model.sav', 'rb'))




#definimos as colunas
colunas_modelo = [
    'Cultura', 'Quantidade_a_ser_Plantada_Toneladas', 'Tipo_de_Solo', 'Tipo_de_Irrigacao', 
    'Frequencia_Irrigacao', 'Temperatura_Media', 'Fertilizante', 'Pragas', 
    'Rotacao_de_Culturas', 'Tecnologia_Utilizada'
]

#utilizamos flask 
app = Flask(__name__, template_folder='template', static_folder='template/assets')

#chave da API do Climatempo
CLIMATEMPO_API_KEY = 'f0ab6c560f54ced16999b37ae243bed5'

#chave da API do Gemini
GEMINI_API_KEY = 'AIzaSyCXJp2GnIVz6d7oBHeXkYUD99vZkuVYzfA'
genai.configure(api_key=GEMINI_API_KEY)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/previsao_safra', methods=['GET'])
def previsao_safra():
    return render_template('previsao_safra.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Recebendo dados do formulário
        cultura = request.form.get('Cultura')
        quantidade = request.form.get('Quantidade_a_ser_Plantada_Toneladas')
        tipo_solo = request.form.get('Tipo_Solo')
        tipo_irrigacao = request.form.get('Tipo_de_Irrigacao')
        fertilizante = request.form.get('Fertilizante')
        temperatura = request.form.get('Temperatura_Media')
        pragas = request.form.get('Pragas')
        pesticidas = request.form.get('Uso_de_Pesticidas')
        tecnologia = request.form.get('Tecnologia_Utilizada')
        rotacao_culturas = request.form.get('Rotacao_de_Culturas')

        # Criando o Df p/ o modelo
        dados_transformados = completa_dataframe_agricola({
            'Cultura': cultura,
            'Quantidade_a_ser_Plantada_Toneladas': quantidade,
            'Tipo_Solo': tipo_solo,
            'Tipo_de_Irrigacao': tipo_irrigacao,
            'Fertilizante': fertilizante,
            'Temperatura_Media': temperatura,
            'Pragas': pragas,
            'Uso_de_Pesticidas': pesticidas,
            'Tecnologia_Utilizada': tecnologia,
            'Rotacao_de_Culturas': rotacao_culturas
        })

        # add colunas faltantes se precisar
        colunas_esperadas_modelo = modelo.feature_names_in_ 
        colunas_faltantes = set(colunas_esperadas_modelo) - set(dados_transformados.columns)

        for coluna in colunas_faltantes:
            dados_transformados[coluna] = 0

        #em ordem
        dados_transformados = dados_transformados[colunas_esperadas_modelo]

        previsao = modelo.predict(dados_transformados)
        previsao_valor = previsao[0]

        #exibe mensagem com previsao
        previsao_mensagem = f"A previsão de produção é {previsao_valor:.1f} toneladas por hectare."

        return render_template('previsao_safra.html', previsao=previsao_mensagem)
    
    except Exception as e:
        return str(e), 400

#rota para previsão do clima usando API Climatempo
@app.route('/previsao_clima', methods=['GET'])
def previsao_clima():
    return render_template('previsao_clima.html')

#buscar cidades
@app.route('/buscar_cidades', methods=['POST'])
def buscar_cidades():
    cidade = request.form['cidade']
    url_cidade = f"http://apiadvisor.climatempo.com.br/api/v1/locale/city?name={cidade}&token={CLIMATEMPO_API_KEY}"

    try:
        response_cidade = requests.get(url_cidade)
        response_cidade.raise_for_status()
        cidades_data = response_cidade.json()

        if cidades_data:
            cidades = [{"id": c['id'], "name": c['name'], "state": c['state'], "country": c['country']} for c in cidades_data]
            return jsonify({"cidades": cidades})
        else:
            return jsonify({"error": "Nenhuma cidade encontrada."})
    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)})

#prevendo clima, urls conforme documentacao do site climatempo
@app.route('/climatempo_predict', methods=['POST'])
def climatempo_predict():
    cidade_id = request.form['cidadeId']
    opcao = request.form['opcao']

    # Montagem da URL com base na opção selecionada
    if opcao == 'hoje':
        url_previsao = f"http://apiadvisor.climatempo.com.br/api/v1/weather/locale/{cidade_id}/current?token={CLIMATEMPO_API_KEY}"
    else:
        url_previsao = f"http://apiadvisor.climatempo.com.br/api/v1/forecast/locale/{cidade_id}/days/15?token={CLIMATEMPO_API_KEY}"

    try:
        response_previsao = requests.get(url_previsao)
        response_previsao.raise_for_status()
        previsao_data = response_previsao.json()

        # Exibir os dados da previsão no console
        print(previsao_data)

        return jsonify({"previsao": previsao_data})
    
    except requests.exceptions.RequestException as e:
        return jsonify({"error": f"Erro na requisição: {str(e)}"}), 500



#funcao para api gemini/chatbot
@app.route('/chatbot_gemini', methods=['POST'])
def chatbot_gemini():
    try:
        prompt = request.form.get('message')  #pega a pergunta do user pelo front

        #definindo modelo  e iniciando 
        model = genai.GenerativeModel("gemini-1.5-pro-latest")
        chat = model.start_chat(history=[]) 

        #envia resposta para front
        response = chat.send_message(prompt)
        
        return jsonify({"response": response.text})

    except Exception as e:
        return jsonify({"error": f"Erro ao conectar ao Google Gemini: {str(e)}"}), 500

@app.route('/chat_gemini', methods=['GET'])
def chat_gemini():
    return render_template('chat_gemini.html')

if __name__ == '__main__':
    app.run(debug=True)