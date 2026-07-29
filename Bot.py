import os
import json
import requests
from dotenv import load_dotenv
from telegram.ext import Application, CommandHandler, MessageHandler, filters
from openai import OpenAI
from telegram import KeyboardButton, ReplyKeyboardMarkup
import sys

sys.stdout.reconfigure(encoding="utf-8")

# import des clé
load_dotenv()
token = os.getenv("TOKEN")
cle_api = os.getenv("CLE_API")
cle_serpapi = os.getenv("SERPAPI_KEY")


# mes fonctions creer
def ia_decide_action(question):

    prompt = f"""Tu es un assistant qui décide de l'action qu'il faut executer.

    Question: {question}

    Réponds UNIQUEMENT par un seul mot:

    - "RECHERCHE" si l'utilisateur cherche des LIEUX SPÉCIFIQUES:
    * Hotels, restaurants, bars, cafés, magasins
    * Attractions touristiques, musées, monuments
    * Services: banques, pharmacies, hôpitaux, stations-service
    
    - "REPONSE" si c'est une question GÉNÉRALE:
    * Conseils de sécurité, quartiers dangereux/sûrs
    * Culture, traditions, histoire
    * Gastronomie (plats typiques)
    * Conseils de voyage
    * Questions "comment", "pourquoi", "quelle est"

    - "LOCALISATION" si c'est une question qui demande d'avoi la localisation de l'utilisateur :
    * Conseils ou proposition d'endroits
    * donner des resultats a proximité de moi
    * donner des resultats si le lieu n'est pas précisé

    
    EXEMPLES:
    - "quartiers dangereux" → REPONSE (conseil)
    - "restaurants Yopougon" → RECHERCHE (lieu)
    - "comment se déplacer" → REPONSE (conseil)
    - "hotels près de moi" → LOCALISATION (lieu)

    Un seul mot: RECHERCHE ,REPONSE ou LOCALISATION."""

    try:
        client = OpenAI(
            api_key=cle_api,
            base_url="https://api.groq.com/openai/v1",
        )
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.1,
            max_tokens=10,
        )

        decision = response.choices[0].message.content.strip().upper()
        return decision

    except Exception as e:
        error_message = str(e).lower()

        if "rate_limit" in error_message or "quota" in error_message:
            return "QUOTA_DEPASSE"
        elif "insufficient_quota" in error_message:
            return "QUOTA_DEPASSE"
        elif "invalid_api_key" in error_message:
            return "CLE_INVALIDE"
        else:
            print(f"⚠️ Erreur IA décision: {e}")
            return "ERREUR_IA"


# DEBUT
async def start(update, context):

    prenom = update.message.from_user.first_name
    await update.message.reply_text(f""" Comment puis je vous aider, {prenom} ? """)


# prendre la localisation de l'utilisateur
async def localisation(update, context):
    keyboard = [[KeyboardButton(" Partager ma localisation", request_location=True)]]
    reply_markup = ReplyKeyboardMarkup(
        keyboard, one_time_keyboard=True, resize_keyboard=True
    )

    await update.message.reply_text(
        " Cliquez sur le bouton ci-dessous pour partager votre localisation 👇🏾",
        reply_markup=reply_markup,
    )


async def recevoir_localisation(update, context):
    user_location = update.message.location
    latitude = user_location.latitude
    longitude = user_location.longitude

    print(f"Localisation reçue: Lat={latitude}, Lon={longitude}")

    context.user_data["latitude"] = latitude
    context.user_data["longitude"] = longitude

    await update.message.reply_text(
        f" Merci pour votre localisation ! 😇\n\n"
        f"Je peux maintenant vous recommander des lieux près de vous.\n\n"
        f"Essayez : 'Hôtels près de moi' ou 'Restaurants à proximité'"
    )


async def aide(update, context):
    await update.message.reply_text(
        """
    ❔*AIDE - CI tourist Guide Bot*

    *Posez vos questions naturellement !*
    *Exemples :*
    "Hôtels à Abidjan"
    "Où manger de l'attiéké ?"
    "Visiter Grand-Bassam"
    "Taxi vers l'aéroport"
    "Météo aujourd'hui"

    *Je comprends :*
    ✓ Questions simples ou détaillées
    ✓ Français et English
    ✓ Localisation approximative

    *⌨️ Commandes :*
    /start - Recommencer
    /help - Aide
    /about - À propos
    /localisation - Partager votre localisation

    *Astuce :* Plus vous êtes précis, mieux je vous aide ! 😉              
                                    
                                    """,
        parse_mode="Markdown",
    )


async def about(update, context):
    await update.message.reply_text(
        """* ❔À PROPOS - CITourBot*

    *Votre assistant touristique IA*

    Je suis un guide virtuel intelligent qui vous aide à découvrir la Côte d'Ivoire.

    * Mes Services*
    • Trouver des hôtels et hébergements
    • Recommander des restaurants
    • Découvrir les attractions touristiques
    • S'informer sur les transports
    • Consulter la météo en temps réel
    • Obtenir des conseils pratiques

    * Couverture*
    Toute la Côte d'Ivoire, de Abidjan à Korhogo, en passant par Grand-Bassam, Yamoussoukro et bien d'autres destinations.

    * Mes Atouts*
    ✓ Gratuit et accessible à tous
    ✓ Disponible 24h/24, 7j/7
    ✓ Réponses instantanées
    ✓ Données actualisées régulièrement
    ✓ Support français et anglais

    *Confidentialité*
    Vos conversations sont privées et sécurisées.

    *Sources*
    OpenStreetMap • Wikipedia • OpenWeatherMap

    

    Made with love for Côte d'Ivoire""",
        parse_mode="Markdown",
    )


def demander_a_ia(question):

    question = question.strip()

    print(f"Question IA générale : {question}")

    prompt = f"""Tu es un guide touristique expert de la Côte d'Ivoire.
    Tu réponds aux questions GÉNÉRALES sur:
    - Culture et traditions ivoiriennes
    - Histoire du pays
    - Conseils de voyage (quoi apporter, meilleure période, budget)
    - Gastronomie locale (plats typiques, où les trouver)
    - Transports et déplacements
    - Sécurité et santé
    - Informations pratiques

    RÈGLES:
    1. Réponds dans la MÊME LANGUE que la question (français ou anglais)
    2. Sois précis, informatif et pratique
    3. Donne des conseils concrets et utiles
    4. Si la question concerne des lieux spécifiques (hotels, restaurants, attractions), 
    explique à l'utilisateur de reformuler sa question pour chercher des lieux précis
    5. Structure ta réponse clairement avec des paragraphes
    6. Reste naturel et conversationnel

    Question : {question}"""

    try:
        client = OpenAI(
            api_key=cle_api,
            base_url="https://api.groq.com/openai/v1",
        )

        print("IA génère la réponse...")
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "system", "content": prompt},
                {"role": "user", "content": question},
            ],
            temperature=0.5,
        )

        raw_content = response.choices[0].message.content.strip()
        print(raw_content)

        return raw_content

    except Exception as e:
        error_message = str(e).lower()

        if "rate_limit" in error_message or "quota" in error_message:
            return "❌ **Quota dépassé**\n\nLe service IA a atteint sa limite quotidienne de tokens.\nVeuillez réessayer plus tard ou contacter le développeur."
        elif "insufficient_quota" in error_message:
            return "❌ **Quota dépassé**\n\nLe service IA a atteint sa limite quotidienne de tokens.\nVeuillez réessayer plus tard ou contacter le développeur."
        elif "invalid_api_key" in error_message:
            return "❌ **Erreur de configuration**\n\nLa clé API est invalide. Contactez le développeur."
        else:
            print(f"⚠️ Erreur IA réponse: {e}")
            return f"❌ **Erreur technique**\n\nUne erreur s'est produite lors du traitement de votre demande.\nDétails: {str(e)}"


def chercher_sur_serpapi(question_utilisateur, lat=None, long=None):

    if not cle_serpapi:
        return "Clé SerpAPI manquante. Ajoutez SERPAPI_KEY dans .env"

    url = "https://serpapi.com/search"

    if lat and long:
        params = {
            "engine": "google_maps",
            "q": question_utilisateur,
            "ll": f"@{lat},{long},15z",
            "api_key": cle_serpapi,
        }
        print(f"🔍 Recherche près de ({lat}, {long})")
    else:
        params = {
            "engine": "google_maps",
            "q": question_utilisateur + " Côte d'Ivoire",
            "api_key": cle_serpapi,
        }
        print(f"🔍 Recherche générale")

    try:
        reponse = requests.get(url, params=params, timeout=15)
        data = reponse.json()

        resultats = data.get("local_results")

        if not resultats:
            return "Aucun résultat trouvé."

        print(" resultats trouvé ✅")
        return resultats

    except Exception as e:
        return f"Erreur: {str(e)}"


async def reponse_a_afficher(update, question, lat=None, long=None):
    """Afficher les résultats de recherche avec photos et GPS"""
    lieux = chercher_sur_serpapi(question, lat, long)

    if not lieux:
        await update.message.reply_text("Aucun résultat trouvé.")
    else:
        for lieu in lieux:
            # Créer lien Google Maps
            gps = lieu.get("gps_coordinates", {})
            lien_gps = ""
            if gps:
                lat_lieu = gps.get("latitude")
                lon_lieu = gps.get("longitude")
                if lat_lieu and lon_lieu:
                    lien_gps = f"https://maps.google.com/?q={lat_lieu},{lon_lieu}"

            # Préparer le texte avec le lien GPS
            texte = f"""{lieu.get('title', 'Nom inconnu')}
            ----------------------------------
            💰 prix : {lieu.get('price', 'Non spécifié')}
            ⭐ note : {lieu.get('rating', 'N/A')}/5
            📍 localisation : {lieu.get('address', 'Non disponible')}
            📞 contact : {lieu.get('phone', 'Non disponible')}
            🗺️ GPS : {lien_gps if lien_gps else 'Non disponible'}"""

            # Envoyer 1 seul message (photo + texte)
            url_image = lieu.get("thumbnail")
            if url_image:
                try:
                    await update.message.reply_photo(photo=url_image, caption=texte)
                except Exception as e:
                    print(f"⚠️ Erreur photo: {e}")
                    await update.message.reply_text(texte)
            else:
                await update.message.reply_text(texte)


async def gestion_message(update, context):
    message = update.message.text

    # localisastion
    latitude = context.user_data.get("latitude")
    longitude = context.user_data.get("longitude")
    print(f"Message utilisateur : {message}")

    print(f" analyse du message : {message}")
    decision = ia_decide_action(message)
    print(f"Décision: {decision}")

    # Gérer les erreurs de l'IA
    if decision == "QUOTA_DEPASSE":
        await update.message.reply_text(
            "❌ **Service temporairement indisponible**\n\n"
            "Le quota de l'IA est épuisé pour aujourd'hui.\n"
            "Veuillez réessayer plus tard. 🙏"
        )
        return

    elif decision == "CLE_INVALIDE":
        await update.message.reply_text(
            "❌ **Erreur de configuration**\n\n"
            "Le bot est mal configuré . Contactez le développeur."
        )
        return

    elif decision == "ERREUR_IA":
        await update.message.reply_text(
            "❌ **Erreur technique**\n\n"
            "Une erreur s'est produite. Veuillez réessayer."
        )
        return

    if decision == "RECHERCHE":
        await update.message.reply_text("🔍 Recherche en cours...")
        await reponse_a_afficher(update, message, latitude, longitude)

    elif decision == "LOCALISATION":
        if latitude and longitude:
            print("l'utilisateur a partagé sa localisation")
            await update.message.reply_text("🔍 Recherche près de vous...")
            await reponse_a_afficher(update, message, latitude, longitude)
        else:
            print("l'utilisateur n'a pas partagé sa localisation")
            await update.message.reply_text(
                "📍 Partagez votre localisation avec /localisation pour des résultats à proximité"
            )
            await reponse_a_afficher(update, message, None, None)

    else:
        reponse = demander_a_ia(message)
        await update.message.reply_text(reponse)


# gestion erreur
async def erreur(update, context):
    print(f"Une erreur s'est produite : {context.error}")
    
    # Vérifier que update existe avant d'envoyer un message
    if update and update.message:
        try:
            await update.message.reply_text(
                "Désolé, une erreur est survenue. Veuillez réessayer plus tard."
            )
        except Exception as e:
            print(f"Impossible d'envoyer le message d'erreur: {e}")


if __name__ == "__main__":
    app = Application.builder().token(token).build()
    print("Bot Lancé ✅")
    # commandes
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("aide", aide))
    app.add_handler(CommandHandler("about", about))
    app.add_handler(CommandHandler("localisation", localisation))

    # gestion des messages texte
    app.add_handler(MessageHandler(filters.LOCATION, recevoir_localisation))
    app.add_handler(MessageHandler(filters.TEXT, gestion_message))

    # gestion des erreurs
    app.add_error_handler(erreur)

    app.run_polling(poll_interval=5)
