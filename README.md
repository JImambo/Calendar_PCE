# Calendar PCE - Cité d'Exaucement (Belgique)

Ce projet permet de générer automatiquement un fichier de calendrier au format universel `.ics` (iCalendar) basé sur le calendrier annuel 2026 de **Phila Cité d'Exaucement (Belgique)**. Le fichier généré intègre des rappels automatiques et peut être importé directement dans Google Calendar, Apple Calendar ou Outlook.

## 🚀 Fonctionnalités

-   **Lecture stricte du calendrier 2026** (Cultes dominicaux, Prières, École d'Apollos, Séminaires, Sessions *Connaissez-vous Phila ?*).
-   **Configuration automatique de deux rappels par événement** :
    -   Notification J-1 (24 heures avant).
    -   Notification imminente (15 minutes avant).
-   **Gestion des fuseaux horaires** (Europe/Brussels).
-   **Structure sémantique des catégories** pour faciliter l'attribution des couleurs dans Google Agenda (Célébration, Prière, Enseignement, Séminaire).

---

## 🛠️ Installation et Configuration

### 1. Prérequis
Assure-toi d'avoir Python 3.13+ installé.

### 2. Cloner le projet & Configuration de l'environnement
Dans ton terminal :
```bash
# Accéder au dossier du projet
cd Calendar_PCE

# Créer l'environnement virtuel (si pas déjà fait)
python3 -m venv .venv

# Activer l'environnement virtuel
source .venv/bin/activate

# Installer les dépendances requises
pip install icalendar pytz