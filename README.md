# 🇨🇮 CI Tourist Guide Bot

Bot Telegram intelligent pour découvrir la Côte d'Ivoire.

## 🌟 Fonctionnalités

- 🔍 Recherche de lieux (hôtels, restaurants, attractions)
- 🤖 Conseils touristiques avec IA (Groq - llama-3.3-70b)
- 📍 Recherche géolocalisée
- 🗺️ Localisation GPS sur Google Maps
- 🌍 Support français et anglais

## 🛠️ Technologies

- Python 3.x
- python-telegram-bot v22.7
- Groq API (llama-3.3-70b-versatile)
- SerpAPI (Google Maps)

## 📦 Installation

1. Cloner le repo:

```bash
git clone https://github.com/VOTRE_USERNAME/bot-touriste-ci.git
cd bot-touriste-ci
```

2. Créer un environnement virtuel:

```bash
python -m venv .venv
.venv\Scripts\activate
```

3. Installer les dépendances:

```bash
pip install -r requirements.txt
```

4. Créer un fichier `.env` (voir `.env.example`):

```
TOKEN=votre_token_telegram
CLE_API=votre_cle_groq
SERPAPI_KEY=votre_cle_serpapi
```

5. Lancer le bot:

```bash
python Bot.py
```

## 🔑 Obtenir les clés API

- **Telegram Bot**: [@BotFather](https://t.me/botfather)
- **Groq API**: [console.groq.com](https://console.groq.com)
- **SerpAPI**: [serpapi.com](https://serpapi.com) (250 recherches/mois gratuites)

## 📝 Commandes disponibles

- `/start` - Démarrer le bot
- `/aide` ou `/help` - Afficher l'aide
- `/about` - À propos du bot
- `/localisation` - Partager votre position

## 💡 Utilisation

**Rechercher des lieux:**

- "Hôtels à Abidjan"
- "Restaurants à Yopougon"
- "Attractions à Grand-Bassam"

**Recherche géolocalisée:**

- Partager votre localisation avec `/localisation`
- Puis demander: "Restaurants près de moi"

**Questions générales:**

- "Quels sont les plats typiques ivoiriens?"
- "Quelle est la meilleure période pour visiter?"
- "Comment se déplacer à Abidjan?"

## 👨‍💻 Auteur

Edgar Yao

## 📄 Licence

MIT
