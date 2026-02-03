## Autopercepção de Saúde na PNS: Análise Estatística e ML

### Sobre

Projeto da disciplina de **Descoberta de Ccnhecimento em Bancos de Dados e Mineração de Dados**

### Resumo do Trabalho

Este trabalho apresenta uma análise dos fatores associados à autopercepção de saúde a partir dos dados da Pesquisa Nacional de Saúde (PNS) do ano de 2019, com foco na interpretação do fenômeno e na identificação de variáveis relevantes. Inicialmente, foram selecionadas variáveis de maneira manual com base na literatura. Em seguida, empregou-se um modelo de regressão logística ordinal para avaliar a contribuição estatística dessas variáveis na explicação da variável resposta. Complementarmente, modelos baseados em aprendizado de máquina, incluindo árvores de decisão e o algoritmo CatBoost, foram utilizados como ferramentas exploratórias para análise de importância das variáveis e identificação de padrões nos dados. A partir dos resultados obtidos, discute-se o papel dos principais determinantes socioeconômicos, demográficos e de condições de saúde na autopercepção dos indivíduos.

### Base de dados

A base de dados utilizada nesse projeto foi a PNS - 2019, disponibilizada para download no link abaixo: [Download](https://www.ibge.gov.br/estatisticas/downloads-estatisticas.html?caminho=PNS/2019/Microdados/Dados)

### Notebook

0. Exploração: Notebook dedicado à análise exploratória das features do conjunto de dados.
1. Processor: Responsável por explorar e tratar a PNS 2019, realizando a criação de labels, ajuste de cabeçalhos e o merge do dicionário da PNS com o conjunto de dados.
2. Processor_clean: Aplicação das transformações finais para o preparo do conjunto de dados utilizado na construção do trabalho.
3. LogisticRegressor: Utilizado para ranquear as principais features selecionadas na etapa anterior de processamento.
4. CatBoost: Aplicação do algoritmo CatBoostRegressor utilizando o dataset filtrado manualmente e também o conjunto de features ranqueadas pelo Logistic Regressor.
5. DecisionTree: Implementação de uma árvore de decisão, mesmo fora do escopo principal do problema, com o objetivo de demonstrar um modelo não compatível com a natureza ordinal da variável resposta.
6. Dbscan: Utilização do algoritmo DBSCAN para a criação de clusters a partir do dataset filtrado manualmente na etapa 2, refinando os registros para posterior uso no CatBoost (etapa 4).
7. Generate Raw PNS: Para gerar a pns tratada

### Ordem de RUN

- Para rodar o código basta rodar primeiramente o **generate_raw_pns** e dps o **processor_clean**, isso já cria os conjuntos de dados para rodar os notebook de decision tree, catboost, logistcregressor dbscan.

### Diagrama Geral do Trabalho

![texto alternativo]("./img/diagrama_etapas_old.drawio.png")
