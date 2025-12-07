# 📋 Tâches Restantes - Mon Cacao

## ✅ Ce qui a été fait

Toutes les fonctionnalités prioritaires ont été implémentées :
- ✅ Base de données backend
- ✅ Génération PDF
- ✅ Notifications push
- ✅ Mode hors ligne
- ✅ Authentification renforcée (2FA)
- ✅ PWA
- ✅ Intégration météo
- ✅ Messagerie interne
- ✅ Cartographie
- ✅ Gamification

---

## 🔧 Ce qui reste à faire

### 1. 🔗 **Intégration dans le Dashboard Professionnel** (PRIORITÉ HAUTE)

**Problème** : Les nouvelles pages (messagerie, cartographie, gamification) ne sont pas encore liées depuis le dashboard professionnel.

**Actions à faire** :
- [ ] Ajouter des cartes dans `dashboard-professionnel.html` pour :
  - Messagerie (`messagerie.html`)
  - Cartographie (`cartographie.html`)
  - Gamification (`gamification.html`)
- [ ] Vérifier que toutes les pages existantes sont accessibles

**Fichier à modifier** : `frontend/dashboard-professionnel.html`

---

### 2. 🎨 **Icônes PWA** (PRIORITÉ MOYENNE)

**Problème** : Le `manifest.json` référence des icônes qui n'existent pas encore.

**Actions à faire** :
- [ ] Créer les icônes aux tailles suivantes :
  - `icon-72x72.png`
  - `icon-96x96.png`
  - `icon-128x128.png`
  - `icon-144x144.png`
  - `icon-152x152.png`
  - `icon-192x192.png`
  - `icon-384x384.png`
  - `icon-512x512.png`
  - `badge-72x72.png`
- [ ] Placer les icônes dans le dossier `frontend/`

**Outils recommandés** : 
- [PWA Asset Generator](https://github.com/onderceylan/pwa-asset-generator)
- [RealFaviconGenerator](https://realfavicongenerator.net/)

---

### 3. 🔑 **Configuration des Clés API** (PRIORITÉ MOYENNE)

**Problème** : Les clés API ne sont pas configurées.

**Actions à faire** :

#### A. API Météo (OpenWeatherMap)
- [ ] Obtenir une clé API sur [openweathermap.org](https://openweathermap.org/api)
- [ ] Remplacer `YOUR_OPENWEATHER_API_KEY` dans `frontend/js/weather.js`

#### B. Notifications Push (VAPID)
- [ ] Générer des clés VAPID (si nécessaire pour notifications push)
- [ ] Remplacer `YOUR_VAPID_PUBLIC_KEY` dans `frontend/js/notifications.js`
- [ ] Configurer les clés côté serveur dans `backend/api_server.py`

**Fichiers à modifier** :
- `frontend/js/weather.js`
- `frontend/js/notifications.js`
- `backend/api_server.py` (si nécessaire)

---

### 4. 🔄 **Intégration de la Gamification** (PRIORITÉ MOYENNE)

**Problème** : Le système de gamification existe mais n'est pas automatiquement déclenché par les actions utilisateur.

**Actions à faire** :
- [ ] Ajouter l'attribution de points lors de :
  - Soumission de données (`soumettre.html`)
  - Consultation de conseils (`conseils.html`)
  - Utilisation de prédictions (`prediction.html`)
  - Amélioration du score écologique (`score-ecologique.html`)
- [ ] Ajouter l'attribution de badges automatique
- [ ] Afficher les notifications de points/badges obtenus

**Fichiers à modifier** :
- `frontend/js/script.js`
- `frontend/prediction.html`
- `frontend/soumettre.html`
- `frontend/conseils.html`
- `frontend/score-ecologique.html`

---

### 5. 🌤️ **Intégration de la Météo** (PRIORITÉ MOYENNE)

**Problème** : Le service météo existe mais n'est pas affiché dans les pages pertinentes.

**Actions à faire** :
- [ ] Afficher la météo dans `dashboard-professionnel.html`
- [ ] Afficher la météo dans `index.html` (page producteur)
- [ ] Ajouter des recommandations météo dans les conseils
- [ ] Intégrer la météo dans les prédictions

**Fichiers à modifier** :
- `frontend/dashboard-professionnel.html`
- `frontend/index.html`
- `frontend/prediction.html`

---

### 6. 📱 **Service Worker dans toutes les pages** (PRIORITÉ BASSE)

**Problème** : Le Service Worker n'est enregistré que dans `index.html`.

**Actions à faire** :
- [ ] Ajouter l'enregistrement du Service Worker dans toutes les pages principales :
  - `dashboard-professionnel.html`
  - `auth.html`
  - `user-type-selection.html`
  - Autres pages importantes

**Fichiers à modifier** : Toutes les pages HTML principales

---

### 7. 🔐 **Intégration 2FA dans l'interface** (PRIORITÉ BASSE)

**Problème** : Le backend supporte la 2FA mais l'interface utilisateur n'est pas complète.

**Actions à faire** :
- [ ] Ajouter un bouton "Activer 2FA" dans les paramètres/profil
- [ ] Créer une page/modale pour activer la 2FA avec QR code
- [ ] Ajouter la vérification 2FA lors de la connexion
- [ ] Créer une page de réinitialisation de mot de passe

**Fichiers à créer/modifier** :
- `frontend/auth.html` (améliorer)
- `frontend/settings.html` (nouveau fichier, optionnel)

---

### 8. 📊 **Amélioration des Rapports PDF** (PRIORITÉ BASSE)

**Problème** : Les rapports PDF sont basiques.

**Actions à faire** :
- [ ] Ajouter des graphiques dans les PDF
- [ ] Améliorer le design des rapports
- [ ] Ajouter plus de statistiques
- [ ] Créer des rapports personnalisables

**Fichier à modifier** : `backend/pdf_generator.py`

---

### 9. 🧪 **Tests et Validation** (PRIORITÉ HAUTE)

**Problème** : Aucun test n'a été effectué.

**Actions à faire** :
- [ ] Tester la création de compte
- [ ] Tester la connexion avec 2FA
- [ ] Tester la génération de PDF
- [ ] Tester le mode hors ligne
- [ ] Tester la messagerie
- [ ] Tester la cartographie
- [ ] Tester la gamification
- [ ] Tester la synchronisation des données
- [ ] Tester sur différents navigateurs
- [ ] Tester sur mobile

---

### 10. 📚 **Documentation Utilisateur** (PRIORITÉ BASSE)

**Problème** : Pas de guide utilisateur.

**Actions à faire** :
- [ ] Créer un guide d'utilisation pour les producteurs
- [ ] Créer un guide d'utilisation pour les professionnels
- [ ] Ajouter des tooltips/aide contextuelle dans l'interface
- [ ] Créer une FAQ

**Fichiers à créer** :
- `docs/GUIDE_PRODUCTEUR.md`
- `docs/GUIDE_PROFESSIONNEL.md`
- `docs/FAQ.md`

---

### 11. 🐛 **Corrections de Bugs Potentiels** (PRIORITÉ HAUTE)

**Actions à faire** :
- [ ] Vérifier que toutes les pages se chargent correctement
- [ ] Vérifier que les liens fonctionnent
- [ ] Vérifier la compatibilité avec l'ancien système localStorage
- [ ] Vérifier les erreurs dans la console du navigateur
- [ ] Corriger les erreurs de linting

---

### 12. 🎯 **Optimisations** (PRIORITÉ BASSE)

**Actions à faire** :
- [ ] Optimiser les images
- [ ] Minifier les fichiers CSS/JS pour la production
- [ ] Ajouter un système de cache pour les API
- [ ] Optimiser les requêtes à la base de données
- [ ] Ajouter la compression gzip

---

## 📊 Priorisation

### 🔴 **URGENT** (À faire en premier)
1. Intégration dans le Dashboard Professionnel
2. Tests et Validation
3. Corrections de Bugs Potentiels

### 🟡 **IMPORTANT** (À faire ensuite)
4. Configuration des Clés API
5. Intégration de la Gamification
6. Intégration de la Météo
7. Icônes PWA

### 🟢 **OPTIONNEL** (Peut être fait plus tard)
8. Service Worker dans toutes les pages
9. Intégration 2FA dans l'interface
10. Amélioration des Rapports PDF
11. Documentation Utilisateur
12. Optimisations

---

## 🚀 Prochaines Étapes Recommandées

1. **Commencer par** : Ajouter les liens vers les nouvelles pages dans le dashboard professionnel
2. **Ensuite** : Tester toutes les fonctionnalités
3. **Puis** : Configurer les clés API
4. **Enfin** : Améliorer l'intégration (gamification, météo)

---

*Document généré le : Décembre 2024*

