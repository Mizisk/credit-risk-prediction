import streamlit as st
import joblib
import numpy as np

# Charger le modèle sauvegardé
model = joblib.load('model.joblib')

# Créer l'interface Streamlit
st.title('Prédiction du Risque de Crédit')

# Demander les caractéristiques du client
age = st.number_input('Âge', min_value=18, max_value=100, value=30)
income = st.number_input('Revenu mensuel', min_value=0, max_value=1_000_000, value=5000)
home_ownership = st.selectbox('Propriétaire de maison', ['RENT', 'MORTGAGE', 'OWN', 'OTHER'])
emp_length = st.number_input('Ancienneté professionnelle', min_value=0, max_value=40, value=5)
loan_intent = st.selectbox('Intention de prêt', ['EDUCATION', 'MEDICAL', 'VENTURE', 'PERSONAL', 'DEBTCONSOLIDATION', 'HOMEIMPROVEMENT'])
loan_grade = st.selectbox('Grade du prêt', ['A', 'B', 'C', 'D', 'E', 'F', 'G'])
loan_amnt = st.number_input('Montant du prêt', min_value=100, max_value=1_000_000, value=5000)
loan_int_rate = st.number_input('Taux d\'intérêt', min_value=0, max_value=30, value=5)

# Convertir les variables catégorielles en numériques (similaire à ce que nous avons fait pour l'entraînement)
home_ownership = {'RENT': 0, 'MORTGAGE': 1, 'OWN': 2, 'OTHER': 3}.get(home_ownership)
loan_intent = {'EDUCATION': 1, 'MEDICAL': 2, 'VENTURE': 3, 'PERSONAL': 4, 'DEBTCONSOLIDATION': 5, 'HOMEIMPROVEMENT': 6}.get(loan_intent)
loan_grade = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7}.get(loan_grade)

# Transformer les données en un tableau
input_data = [age, income, home_ownership, emp_length, loan_intent, loan_grade, loan_amnt, loan_int_rate]

# Prédiction avec le modèle
prediction = model.predict([input_data])

# Affichage de la prédiction
if st.button('Prédire'):
    if prediction[0] == 1:
        st.write("Risque élevé de crédit")
    else:
        st.write("Risque faible de crédit")
