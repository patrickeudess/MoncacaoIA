#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def verifier_corrections():
    print("🔍 VÉRIFICATION DES CORRECTIONS")
    print("=" * 40)
    
    try:
        with open('frontend/js/script.js', 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Vérifier les corrections appliquées
        corrections = [
            ("Prix dynamique dans updateCalculationDetails", 
             "parseFloat(document.getElementById('prix_a').value)" in content),
            ("Coût dynamique dans updateCalculationDetails", 
             "parseFloat(document.getElementById('cout_prod').value)" in content),
            ("Prix dynamique dans simulatePrediction", 
             "parseFloat(document.getElementById('prix_a').value)" in content)
        ]
        
        for description, appliquee in corrections:
            status = "✅" if appliquee else "❌"
            print(f"{status} {description}")
        
        # Vérifier les valeurs codées en dur restantes
        hardcoded = [
            ("const price = 1000", "const price = 1000" in content),
            ("const cost = 55000", "const cost = 55000" in content),
            ("const prix_kg = 750", "const prix_kg = 750" in content)
        ]
        
        print("\n🔍 VALEURS CODÉES EN DUR RESTANTES:")
        for description, presente in hardcoded:
            status = "⚠️" if presente else "✅"
            print(f"{status} {description}")
            
    except Exception as e:
        print(f"❌ Erreur: {e}")

if __name__ == "__main__":
    verifier_corrections()
