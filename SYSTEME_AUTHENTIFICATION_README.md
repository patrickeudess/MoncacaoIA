# 🔐 SYSTÈME D'AUTHENTIFICATION MON CACAO

## 🌱 Vue d'ensemble

Le système d'authentification de MON CACAO a été entièrement refactorisé pour offrir une sécurité renforcée, une gestion des données conforme au RGPD, et une expérience utilisateur améliorée.

---

## 🚀 Fonctionnalités principales

### ✅ **Inscription sécurisée**
- Validation des emails et mots de passe
- Hachage sécurisé des mots de passe (SHA-256)
- Vérification des doublons (username/email)
- Acceptation obligatoire de la politique de données

### ✅ **Connexion sécurisée**
- Authentification par email/mot de passe
- Gestion des sessions avec tokens
- Protection contre les attaques par force brute
- Déconnexion automatique après inactivité

### ✅ **Gestion des comptes**
- Profils utilisateurs complets
- Mise à jour des informations personnelles
- Changement de mot de passe sécurisé
- Suppression de compte avec effacement des données

### ✅ **Conformité RGPD**
- Politique de gestion des données complète
- Consentement explicite requis
- Droits des utilisateurs respectés
- Traçabilité des consentements

---

## 📁 Structure des fichiers

```
📦 MON CACAO/
├── 🔐 auth_system.py          # Module d'authentification principal
├── 🎨 login_interface.py      # Interface d'inscription/connexion
├── 📋 POLITIQUE_GESTION_DONNEES.md  # Politique RGPD
├── 🧪 test_auth_system.py     # Tests du système
├── 🚀 cacao1.py              # Application principale (modifiée)
└── 📊 data.sqlite             # Base de données (mise à jour)
```

---

## 🗄️ Base de données

### **Table `users`**
```sql
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username VARCHAR(50) UNIQUE NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    region VARCHAR(100),
    user_type VARCHAR(20) DEFAULT 'agriculteur',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    consent_gdpr BOOLEAN DEFAULT FALSE
);
```

### **Table `user_sessions`**
```sql
CREATE TABLE user_sessions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    session_token VARCHAR(100) UNIQUE NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    expires_at TIMESTAMP NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users (id)
);
```

### **Table `login_attempts`**
```sql
CREATE TABLE login_attempts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    email VARCHAR(100) NOT NULL,
    ip_address VARCHAR(45),
    attempted_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    success BOOLEAN DEFAULT FALSE
);
```

---

## 🔧 Utilisation

### **1. Démarrage de l'application**
```bash
streamlit run cacao1.py
```

### **2. Création d'un compte**
- Cliquer sur "📝 Inscription"
- Remplir le formulaire complet
- Accepter la politique de données
- Valider l'inscription

### **3. Connexion**
- Cliquer sur "🔑 Connexion"
- Saisir email et mot de passe
- Accéder à l'application

### **4. Déconnexion**
- Cliquer sur "🚪 Déconnexion"
- Session fermée automatiquement

---

## 🛡️ Sécurité

### **Mots de passe**
- **Minimum 8 caractères**
- **Au moins une majuscule**
- **Au moins une minuscule**
- **Au moins un chiffre**
- **Au moins un caractère spécial**

### **Protection des comptes**
- **Blocage temporaire** après 5 tentatives échouées
- **Sessions expirées** après 24h d'inactivité
- **Hachage sécurisé** des mots de passe
- **Validation stricte** des entrées

### **Données personnelles**
- **Chiffrement** des informations sensibles
- **Accès limité** aux données
- **Audit** des connexions
- **Suppression** sur demande

---

## 🧪 Tests

### **Exécution des tests**
```bash
python test_auth_system.py
```

### **Tests inclus**
- ✅ Création de la base de données
- ✅ Inscription d'utilisateurs
- ✅ Connexion et déconnexion
- ✅ Validation des données
- ✅ Gestion des profils
- ✅ Sécurité des sessions

---

## 📊 Statistiques utilisateurs

Le système fournit des statistiques détaillées :
- **Nombre total d'utilisateurs**
- **Utilisateurs actifs**
- **Utilisateurs vérifiés**
- **Nouveaux utilisateurs par mois**

---

## 🔄 Migration depuis l'ancien système

### **Données existantes**
- Les utilisateurs existants peuvent se reconnecter
- Les données de production sont conservées
- Les sessions sont migrées automatiquement

### **Nouveaux utilisateurs**
- Doivent accepter la politique RGPD
- Profils complets requis
- Validation renforcée des données

---

## 🚨 Dépannage

### **Problèmes courants**

#### **1. Erreur de connexion**
```
❌ Email ou mot de passe incorrect
```
**Solution :** Vérifier les identifiants et réessayer

#### **2. Compte bloqué**
```
❌ Compte temporairement bloqué
```
**Solution :** Attendre 15 minutes et réessayer

#### **3. Session expirée**
```
❌ Session invalide ou expirée
```
**Solution :** Se reconnecter

#### **4. Validation échouée**
```
❌ Format d'email invalide
```
**Solution :** Vérifier le format de l'email

---

## 📞 Support

### **En cas de problème**
1. **Vérifier** les logs d'erreur
2. **Tester** avec le script de test
3. **Consulter** la documentation
4. **Contacter** l'équipe technique

### **Logs utiles**
- **Connexions** : `login_attempts`
- **Sessions** : `user_sessions`
- **Utilisateurs** : `users`

---

## 🔮 Évolutions futures

### **Fonctionnalités prévues**
- 🔐 **Authentification à deux facteurs**
- 📧 **Vérification par email**
- 🔄 **Récupération de mot de passe**
- 📱 **Notifications push**
- 🌐 **Connexion sociale**

### **Améliorations de sécurité**
- 🛡️ **Détection d'anomalies**
- 📍 **Géolocalisation des connexions**
- ⏰ **Horaires d'accès**
- 🔒 **Chiffrement end-to-end**

---

## 📝 Notes de version

### **Version 2.0** (Actuelle)
- ✅ Système d'authentification complet
- ✅ Conformité RGPD
- ✅ Interface utilisateur moderne
- ✅ Tests automatisés
- ✅ Documentation complète

### **Version 1.0** (Précédente)
- ✅ Authentification basique
- ✅ Gestion des sessions simples
- ✅ Interface Streamlit

---

## 🎯 Conclusion

Le nouveau système d'authentification de MON CACAO offre :
- **Sécurité renforcée** pour les utilisateurs
- **Conformité légale** avec le RGPD
- **Expérience utilisateur** améliorée
- **Maintenance simplifiée** pour les développeurs
- **Évolutivité** pour les futures fonctionnalités

**🚀 Prêt pour la production !**
