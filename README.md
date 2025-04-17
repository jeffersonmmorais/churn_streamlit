# 📊 Previsão de Churn com Streamlit

Este projeto é uma aplicação web construída com Streamlit para prever se um cliente irá cancelar um serviço com base em características comportamentais.

## 📁 Estrutura do Projeto

```
churn_app/
├── app.py
├── model.pkl
├── dataset.csv
├── requirements.txt
└── README.md
```

## 🚀 Como rodar o projeto localmente (Windows com Anaconda)

1. Clone este repositório:
```bash
git clone https://github.com/seu-usuario/seu-repo.git
cd seu-repo
```

2. Crie e ative um ambiente Conda:
```bash
conda create -n churn_env python=3.11 -y
conda activate churn_env
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

4. Rode o app:
```bash
streamlit run app.py
```

## 🧠 Tecnologias usadas

- Python
- Scikit-learn
- Pandas
- Streamlit
- Joblib

## 🌐 Deploy

Este app pode ser publicado facilmente na plataforma [Streamlit Cloud](https://streamlit.io/cloud).
