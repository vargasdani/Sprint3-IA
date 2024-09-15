import pandas as pd

colunas_treinamento_modelo = [
    'Temperatura_Media', 'Cultura_Arroz', 'Cultura_Café', 'Cultura_Milho', 'Cultura_Soja',
    'Quantidade_a_ser_Plantada_Toneladas', 'Tipo_de_Solo_Areia', 'Tipo_de_Solo_Argila', 'Tipo_de_Solo_Silte',
    'Tipo_de_Irrigacao_Aspersão', 'Tipo_de_Irrigacao_Gotejamento', 'Tipo_de_Irrigacao_Sulcos',
    'Frequencia_Irrigacao_Diária', 'Frequencia_Irrigacao_Mensal', 'Frequencia_Irrigacao_Semanal',
    'Fertilizante_Composto', 'Fertilizante_Fósforo', 'Fertilizante_Nitrogênio', 'Fertilizante_Orgânico',
    'Pragas_Ferrugem', 'Pragas_Fungos', 'Pragas_Insetos', 'Rotacao_de_Culturas_Sim', 'Rotacao_de_Culturas_Não',
    'Uso_de_Pesticidas_Alto', 'Uso_de_Pesticidas_Moderado', 'Uso_de_Pesticidas_Baixo',
    'Tecnologia_Utilizada_Alto', 'Tecnologia_Utilizada_Médio', 'Tecnologia_Utilizada_Baixo'
]

def completa_dataframe_agricola(valores):
    df = pd.DataFrame([valores], columns=[
        'Cultura', 'Quantidade_a_ser_Plantada_Toneladas', 'Frequencia_Irrigacao', 'Tipo_de_Solo', 
        'Tipo_de_Irrigacao', 'Fertilizante', 'Temperatura_Media', 'Pragas', 
        'Rotacao_de_Culturas', 'Uso_de_Pesticidas', 'Tecnologia_Utilizada'
    ])
    
    # get_dummies para codificar as variáveis
    df_encoded = pd.get_dummies(df)

    for coluna in colunas_treinamento_modelo:
        if coluna not in df_encoded.columns:
            df_encoded[coluna] = 0


    df_encoded = df_encoded[colunas_treinamento_modelo]
    
    return df_encoded
