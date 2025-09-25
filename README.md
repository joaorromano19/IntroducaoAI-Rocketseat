# IntroducaoAI-Rocketseat
Este repositório reúne meus estudos do curso de **Introdução à Inteligência Artificial** da Rocketseat.  
Os códigos estão organizados em duas pastas principais: **AI-Applying** e **AI-Creating**, além de um arquivo `requirements.txt` com as dependências do projeto.

---

## Estrutura do Repositório

- **AI-Applying/**
  - Contém um exemplo de **aplicação prática de IA usando a API da OpenAI**.
  - O código conecta-se ao modelo `gpt-3.5-turbo` e gera respostas baseadas em prompts, retornando um código limpo e de qualidade conforme instruído ao sistema.

- **AI-Creating/**
  - Contém um **notebook (Jupyter/IPython)** com um exemplo de **criação de modelo de IA do zero** usando o dataset *California Housing*, para prever o preço das casas na California usando AI.
  - Principais etapas implementadas:
    - Importação e exploração do dataset  
    - Divisão em treino e teste  
    - Escalonamento dos dados com `StandardScaler`  
    - Treinamento de um modelo de regressão linear (`LinearRegression`)  
    - Predição e avaliação do modelo com `.score()`  

- **requirements.txt**
  - Lista completa de dependências necessárias para rodar os exemplos, incluindo:
    - **openai** – para integração com modelos da OpenAI  
    - **scikit-learn, pandas, numpy, scipy** – para manipulação de dados e machine learning  
    - **jupyter, matplotlib, ipywidgets** – para execução e visualização em notebooks  
    - Outras bibliotecas auxiliares do ecossistema Python  

---

## Como executar

### Clone este repositório:
   git clone https://github.com/joaorromano19/IntroducaoAI-Rocketseat.git
   cd IntroducaoAI-Rocketseat
### Crie um ambiente virtual e ative:

python -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows
### Instale as dependências:

pip install -r requirements.txt

## Para rodar os exemplos:

AI-Applying: configure sua API Key da OpenAI no código e execute o script Python.

AI-Creating: abra o notebook (.ipynb) em um ambiente Jupyter e rode célula por célula.

## Tecnologias utilizadas
- Python 3

- OpenAI API (ChatGPT)

- scikit-learn

- pandas

- numpy

- Jupyter Notebook
