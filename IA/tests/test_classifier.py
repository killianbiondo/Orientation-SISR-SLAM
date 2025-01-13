import pytest
from src.classifier import classify_text

def test_classify_text():
    assert classify_text("Gestion de serveurs et sécurité réseau.") == "SISR"
    assert classify_text("Création d'une application web.") == "SLAM"
    assert classify_text("Je m'intéresse à la virtualisation.") == "SISR"
    assert classify_text("Développement de base de données.") == "SLAM"
    assert classify_text("Sans préférence claire.") == "Indéterminé"