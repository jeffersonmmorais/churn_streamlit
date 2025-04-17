#Importar dependências
import streamlit as st
import pandas as pd
import joblib

#Carregar o modelo
model = joblib.load("model.pkl")

# Interface de usuário
st.title("Previsão de Churn")

dias_sem_login = st.slider("Dias sem login", 0, 60, 5)
qtd_suportes = st.slider("Qtd de chamados", 0, 10, 1)
tempo_uso = st.slider("Tempo de uso (horas)", 0, 300, 100)

#Previsão 
if st.button("Prever"):
    dados = pd.DataFrame([[dias_sem_login, qtd_suportes, tempo_uso]],
                         columns=["dias_sem_login", "qtd_suportes_abertos", "tempo_uso_plataforma"])
    prob = model.predict_proba(dados)[0][1]
    st.metric("Probabilidade de Churn", f"{prob:.2%}")
    if prob > 0.5:
        st.warning("⚠️ Alto risco de churn!")
    else:
        st.success("✅ Baixo risco de churn.")
