Sobre o projeto: 

Durante o Workshop de introdução de tema do nosso Challenge, o host pareceu interessar-se 
pelo tema de Agronegócio, porém ainda não havia muitas iniciativas nesse eixo com o nome da empresa. 

Viemos resolver isso. 

O termo “Agronegócio” se refere a união de atividades interligadas a área agrícola ou pecuária. 
Num país agroexportador como o Brasil, o Agronegócio é um dos setores mais impactantes, capaz de 
movimentar cerca de 20% do mercado de trabalho, contribuir com o crescimento do PIB e, somente com 
seu volume de produção e exportação, ganha relevância internacionalmente.

Nosso clima favorece a agricultura, porém, ainda assim, é necessário tomar cuidado com a 
degradação do solo; e, por isso, existem atualmente muitas indústrias focadas no envolvimento da 
tecnologia no campo, como são os exemplos de agrotóxicos ou até de monitoramento climático geral do 
país como uma estratégia que os produtores possam adquirir para mitigar desperdício na hora de 
produção (com o ciclo produtivo) e aumentar a sustentabilidade. Porém, essa previsão é feita de forma 
geral, não personalizada para cada fazenda unicamente, sejam elas de pequenos ou grandes produtores, 
o que acaba dificultando o planejamento de produção. Tal imprevisibilidade das safras devido a 
generalização de índices climáticos e não ser devidamente analisado junto a outros fatores como histórico 
e pragas diminui a eficiência da gestão agrícola pois pode trazer problemas a gestão de estoques,
desperdício e até mesmo nos preços de comodities.

E é nisso, que nosso grupo entra com uma solução; queremos prestar serviço e tornar a previsão 
de safras personalizável para cada fazenda, reduzindo perdas e custos, aumentando a performance do 
plantio e melhorando a previsibilidade de resultados (vendas, lucro, fluxo de caixa...). Impactando desde 
agricultores de pequena escala a grandes produtores agrícolas.

Nosso projeto pivotou e nossos objetivos aumentaram, além de analisar dados históricos (que seriam de produção), será possível também um serviço de consulta ao clima
atual e para os próximos 7 dias, visando diminuir que desastres climaticos atingam as plantações e com a nossa integração com a API do Gemini, teremos uma espécie de Chatbot
disponibilizado para que o produtor rural possa tirar suas dúvidas relacionadas ao ramo agricola também.

Juntaremos todas essas funcionalidades e disponibilizaremos para nosso usuário final através de um aplicativo com a interface intuitiva e amigavel.
Próximos passo:
-Juntas todas as integrações;
-Transformar o resultado de um json para um formato tabular colorido;
-Aumentar o dataset com dados fidedígnos;
-Juntar com o Dianóstico por imagem 

Requirements:
- Flask (pip install flask)
- Pandas (pip install pandas)
- Numpy (pip install numpy)
- Requests(pip install requests)
- Sklearn (pip install scikit-learn==1.2.2)
- Google.generativeai (pip install google.generativeai)
- Pickle (pip install pickle)
Para instalar essas bibliotecas no seu computador:
1. Abra o terminal (cmd)
2. Digite o código ao lado de cada biblioteca e pressione Enter
3. Faça o processo para todas as bibliotecas

Para rodar o projeto:
- Abra o projeto no seu VSCode
- Abra o arquivo 'app.py'
- Dentro do arquivo, em qualquer lugar, clique com o botão direito do mouse -> Run Python -> Run Python File in Terminal
- O console irá abrir e mostrará algo como "* Running on http://127.0.0.1:5000"
- No console, coloque o mouse em cima do link e pressione Ctrl + Clique


Por favor, confira se o link abriu corretamente em seu navegador, a página inicial deve ser assim: 
- ![image](https://github.com/user-attachments/assets/4464afa3-63fd-4cc4-ba02-c4e9d256a9d2)

Depois, voce poderá escolher dentro de todas as funcionalidades de nosso sistema, como testar nossa integração com a API do CLIMATEMPO(lembrando que é um requisito da gratuita, ser apenas por cidsdes):
Para o dia de hoje:
![image](https://github.com/user-attachments/assets/086b0104-9b6b-43a8-8385-e9d0f7df586b)

Ou, se preferir, para 7 dias: 
![image](https://github.com/user-attachments/assets/3a47d12e-c5c3-492e-8f67-8c721a7c5c18)

Voce também poderá testar nossa integração com a API do Gemini, faça a pergunta (de preferencia relacionada a agricultura) que desejar por lá! 
![image](https://github.com/user-attachments/assets/bb210550-256e-4b49-9563-1ecf27a2b80e)

Por fim, voce pode testar a nossa IA, basta preencher alguns campos que vão ser levados em consideração para dizermos qual a previsão de produção que voce/sua fazenda terá por hectares! 
![image](https://github.com/user-attachments/assets/9521d808-e1df-4932-a69d-6b94d72b0caa)

