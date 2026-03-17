<h1 align="center">📊 Análise de Dados - CEAPS</h1>
<h3 align="center">Cota para Exercício da Atividade Parlamentar dos Senadores</h3>

<p align="center">
<img src="https://img.shields.io/badge/Python-Data%20Analysis-blue">
<img src="https://img.shields.io/badge/Pandas-Data%20Wrangling-orange">
<img src="https://img.shields.io/badge/Plotly-Data%20Visualization-purple">
<img src="https://img.shields.io/badge/Streamlit-Dashboard-red">
<img src="https://img.shields.io/badge/Prophet-Forecasting-green">
<img src="https://img.shields.io/badge/Status-Em%20Desenvolvimento-yellow">
</p>

<hr>

<h2>📌 Sobre o Projeto</h2>

<p>
Este projeto tem como objetivo realizar uma análise completa dos dados da 
<b>Cota para Exercício da Atividade Parlamentar dos Senadores (CEAPS)</b>, 
abrangendo desde o tratamento dos dados até a previsão de gastos futuros.
</p>

<p>
O projeto foi desenvolvido como parte de um desafio prático de <b>Data Science</b>, dividido em etapas:
</p>

<ul>
<li><b>Dia 1:</b> Limpeza e tratamento dos dados</li>
<li><b>Dia 2:</b> Análise exploratória e visualização</li>
<li><b>Dia 3:</b> Forecasting (previsão de gastos)</li>
</ul>

<hr>

<h2>🗂 Fonte dos Dados</h2>

<p>
Os dados utilizados são públicos e disponibilizados pelo 
<b>Senado Federal</b> através do portal de <b>Dados Abertos</b>.
</p>

<ul>
<li>CEAPS - Cota para Exercício da Atividade Parlamentar dos Senadores</li>
</ul>

<p>Os dados incluem:</p>

<ul>
<li>Nome do senador</li>
<li>Tipo de despesa</li>
<li>Fornecedor</li>
<li>Valor reembolsado</li>
<li>Data do documento</li>
</ul>

<hr>

<h2>🧹 Dia 1 - Limpeza e Tratamento de Dados</h2>

<p>
Nesta etapa foi realizada a preparação do dataset para análise.
</p>

<ul>
<li>Remoção de valores inconsistentes</li>
<li>Tratamento de valores nulos</li>
<li>Padronização de colunas</li>
<li>Conversão de tipos de dados</li>
<li>Formatação de valores monetários</li>
</ul>

<p>
O objetivo foi garantir a qualidade e confiabilidade dos dados para as etapas seguintes.
</p>

<hr>

<h2>📊 Dia 2 - Análise Exploratória (EDA)</h2>

<p>
Após o tratamento dos dados, foi realizada uma análise exploratória para entender o comportamento dos gastos.
</p>

<p><b>Principais análises:</b></p>

<ul>
<li>Top 10 senadores com maiores gastos</li>
<li>Distribuição de gastos por tipo de despesa</li>
<li>Evolução dos gastos ao longo dos anos</li>
</ul>

<p><b>Visualizações utilizadas:</b></p>

<ul>
<li>Gráficos de barras (ranking de gastos)</li>
<li>Gráficos de pizza (distribuição)</li>
<li>Gráficos de linha (tendência ao longo do tempo)</li>
</ul>

<p>
As visualizações foram desenvolvidas com <b>Plotly</b> e integradas ao <b>Streamlit</b>.
</p>

<hr>

<h2>📈 Dia 3 - Forecasting (Previsão de Gastos)</h2>

<p>
Nesta etapa foi desenvolvido um modelo de previsão utilizando séries temporais.
</p>

<ul>
<li>Uso do dataset agregado por data (ds) e valor (y)</li>
<li>Aplicação do modelo <b>Prophet</b></li>
<li>Treinamento com dados históricos</li>
<li>Previsão dos gastos para os próximos 90 dias</li>
</ul>

<p>
O modelo permitiu visualizar tendências futuras e possíveis variações nos gastos dos senadores.
</p>

<hr>

<h2>🛠 Tecnologias Utilizadas</h2>

<ul>
<li><b>Python</b></li>
<li><b>Pandas</b> – manipulação de dados</li>
<li><b>Plotly</b> – visualização interativa</li>
<li><b>Streamlit</b> – criação de dashboard</li>
<li><b>Prophet</b> – previsão de séries temporais</li>
<li><b>Git & GitHub</b> – versionamento</li>
</ul>

<hr>

<h2>🎯 Resultados</h2>

<p>
O projeto permitiu:
</p>

<ul>
<li>Transformar dados brutos em informações estruturadas</li>
<li>Identificar padrões de gastos parlamentares</li>
<li>Criar visualizações interativas</li>
<li>Desenvolver um modelo de previsão de dados</li>
</ul>

<hr>

<h2>🚀 Próximos Passos</h2>

<ul>
<li>Implementar sistema de recomendação (Machine Learning)</li>
<li>Melhorar a interface do dashboard</li>
<li>Adicionar métricas de avaliação (RMSE, MAPE)</li>
</ul>

<hr>

<h2>👨‍💻 Autor</h2>

<p>
<b>Cleyton Eneias</b><br>
</p>
