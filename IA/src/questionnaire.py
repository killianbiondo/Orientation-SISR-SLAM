import streamlit as st
import matplotlib.pyplot as plt
from classifier import classify_text, get_scores  # On importe get_scores depuis classifier.py

# Interface utilisateur
st.title("Orientation SISR ou SLAM")

st.write("Répondez aux questions ou décrivez vos intérêts techniques pour obtenir une orientation.")

response = st.text_area("Décrivez vos intérêts techniques :")

if st.button("Classifiez"):
    # Classification
    orientation = classify_text(response)
    st.write(f"Vous êtes davantage orienté(e) vers : **{orientation}**")

    # Calcul des scores via la fonction get_scores
    sisr_score, slam_score = get_scores(response)

    # Calcul des pourcentages
    total_score = sisr_score + slam_score
    if total_score == 0:  # Si les deux scores sont à 0
        sisr_percentage = 0
        slam_percentage = 0
    else:
        sisr_percentage = (sisr_score / total_score) * 100
        slam_percentage = (slam_score / total_score) * 100

    # Affichage d'un graphique camembert
    st.write("Voici la répartition des scores sous forme de graphique camembert :")
    fig, ax = plt.subplots()

    # Données du graphique
    labels = ['SISR', 'SLAM']
    sizes = [sisr_percentage, slam_percentage]
    colors = ['#00bfff', '#32cd32']  # Bleu pour SISR, Vert pour SLAM

    # Création du graphique en camembert
    ax.pie(sizes, labels=labels, autopct='%1.1f%%', colors=colors, startangle=90, wedgeprops={'edgecolor': 'black'})

    # Égale les axes pour que le camembert soit bien circulaire
    ax.axis('equal')

    # Titre du graphique
    ax.set_title('Répartition des scores (SISR vs SLAM)')

    # Affichage du graphique dans l'interface
    st.pyplot(fig)