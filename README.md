# 🇨🇮 CI Tourist Guide Bot

**Votre compagnon touristique intelligent pour explorer la Côte d'Ivoire.**

CI Tourist Guide Bot est un bot Telegram conçu pour faciliter la découverte de la Côte d'Ivoire. Il permet aux utilisateurs de rechercher des lieux touristiques, de découvrir des restaurants et des hôtels, et d'obtenir des conseils personnalisés grâce à l'intelligence artificielle.

Le projet combine l'API Telegram, un modèle d'IA générative et des données de recherche géolocalisée pour proposer une expérience touristique accessible directement depuis Telegram.

## ✨ Fonctionnalités

- **Recherche de lieux touristiques** : hôtels, restaurants, attractions et autres points d'intérêt.
- **Assistant touristique IA** : réponses et recommandations générées avec Groq et le modèle `llama-3.3-70b-versatile`.
- **Recherche géolocalisée** : découverte de lieux à proximité de l'utilisateur.
- **Localisation GPS** : partage de position et accès aux emplacements sur Google Maps.
- **Support multilingue** : interaction en français et en anglais.
- **Interface Telegram** : accès aux fonctionnalités directement depuis une conversation Telegram.

## 🛠️ Stack technique

| Technologie | Utilisation |
|---|---|
| Python 3.x | Langage principal |
| python-telegram-bot 22.7 | Gestion du bot Telegram |
| Groq API | Intelligence artificielle conversationnelle |
| Llama 3.3 70B Versatile | Modèle de langage |
| SerpAPI | Recherche de lieux et données Google Maps |
| Google Maps | Consultation des emplacements |

## 📋 Prérequis

Avant de commencer, assurez-vous de disposer des éléments suivants :

- Python installé sur votre machine.
- Git pour récupérer le projet.
- Un compte Telegram.
- Une clé API Groq.
- Une clé API SerpAPI.

## 🚀 Installation

### 1. Cloner le dépôt

```bash
git clone https://github.com/VOTRE_USERNAME/bot-touriste-ci.git
cd bot-touriste-ci
```

Remplacez `VOTRE_USERNAME` par votre nom d'utilisateur GitHub.

### 2. Créer un environnement virtuel

Sous Windows :

```bash
python -m venv .venv
.venv\Scripts\activate
```

Sous Linux ou macOS :

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Installer les dépendances

```bash
pip install -r requirements.txt
```

### 4. Configurer les variables d'environnement

Créez un fichier `.env` à la racine du projet en vous inspirant de `.env.example`.

Ajoutez les variables suivantes :

```env
TOKEN=votre_token_telegram
CLE_API=votre_cle_groq
SERPAPI_KEY=votre_cle_serpapi
```

Remplacez les valeurs d'exemple par vos véritables clés API.

**Sécurité :** ne partagez jamais vos clés API et ne publiez jamais votre fichier `.env` sur GitHub. Utilisez un fichier `.gitignore` pour exclure ce fichier du dépôt.

### 5. Lancer le bot

Exécutez la commande suivante depuis la racine du projet :

```bash
python Bot.py
```

Ouvrez ensuite votre bot sur Telegram et envoyez la commande `/start`.

> Vérifiez que le nom du fichier principal correspond bien à `Bot.py` dans votre projet. Sous Linux, les noms de fichiers sont sensibles à la casse.

## 🔑 Obtenir les clés API

| Service | Utilité | Lien |
|---|---|---|
| Telegram BotFather | Création et gestion du bot Telegram | [Créer un bot](https://t.me/BotFather) |
| Groq | Accès à l'API d'intelligence artificielle | [Console Groq](https://console.groq.com/) |
| SerpAPI | Recherche de lieux et données cartographiques | [Site SerpAPI](https://serpapi.com/) |

Consultez les conditions et les quotas en vigueur auprès de chaque fournisseur avant utilisation.

## 💬 Commandes disponibles

| Commande | Description |
|---|---|
| `/start` | Démarrer le bot et découvrir ses fonctionnalités |
| `/aide` | Afficher les instructions d'utilisation |
| `/help` | Afficher l'aide en anglais ou selon la configuration du bot |
| `/about` | Obtenir des informations sur le projet |
| `/localisation` | Accéder à la fonctionnalité de partage de position |

## 🧭 Exemples d'utilisation

### Rechercher des lieux

Vous pouvez envoyer des demandes en langage naturel, par exemple :

- `Hôtels à Abidjan`
- `Restaurants à Yopougon`
- `Attractions touristiques à Grand-Bassam`
- `Lieux à visiter à Assinie`

### Découvrir les lieux à proximité

1. Lancez la commande `/localisation`.
2. Partagez votre position GPS lorsque Telegram le propose.
3. Demandez, par exemple, `Quels sont les restaurants près de moi ?`

### Poser des questions touristiques

L'assistant peut également être interrogé sur des sujets tels que :

- Les plats traditionnels ivoiriens.
- Les destinations touristiques à découvrir.
- Les périodes recommandées pour visiter certaines régions.
- Les moyens de transport disponibles à Abidjan.
- Les activités culturelles et les sites historiques.

Les réponses dépendent des données accessibles et des capacités des services utilisés.

## 🔒 Sécurité et bonnes pratiques

- Stockez les clés API dans des variables d'environnement.
- Ne versionnez jamais les fichiers contenant des secrets.
- Évitez d'exposer les informations personnelles des utilisateurs dans les journaux.
- Surveillez les quotas et les limites des API externes.
- Gérez les erreurs de connexion et les réponses indisponibles des services tiers.

## 🗺️ Perspectives d'évolution

Quelques améliorations envisageables :

- Ajouter des recommandations touristiques personnalisées.
- Enrichir le catalogue des destinations ivoiriennes.
- Intégrer des filtres par budget, catégorie et distance.
- Améliorer la détection automatique de la langue.
- Déployer le bot sur une plateforme d'hébergement accessible en continu.

## 👨‍💻 Auteur

**Edgar Yao**

Étudiant en développement informatique, intéressé par le développement logiciel, l'intelligence artificielle et la création de solutions numériques utiles.

## 📄 Licence

Ce projet est distribué sous licence MIT. Consultez le fichier `LICENSE` pour connaître les conditions d'utilisation et de redistribution.

---

*Développé avec Python pour rendre la découverte de la Côte d'Ivoire plus simple et accessible.* 🇨🇮
