from datetime import datetime, timedelta
from icalendar import Calendar, Event, Alarm
import pytz

def create_precise_calendar():
    cal = Calendar()
    # Correction ici : utilisation de guillemets doubles pour éviter le conflit avec l'apostrophe
    cal.add('prodid', "-//Phila Cité d'Exaucement//Belgique//FR")
    cal.add('version', '2.0')
    
    # Zone horaire de la Belgique
    tz = pytz.timezone('Europe/Brussels')
    
    # -------------------------------------------------------------------------
    # Fonction de création d'événement avec rappels et couleur personnalisée
    # -------------------------------------------------------------------------
    def add_phila_event(summary, start_dt, end_dt, color_name):
        event = Event()
        event.add('summary', summary)
        event.add('dtstart', start_dt)
        event.add('dtend', end_dt)
        event.add('location', "Phila Cité d'Exaucement, Belgique")
        
        # Ajout d'une catégorie textuelle pour aider Google Calendar à mapper la couleur
        event.add('categories', [color_name.upper()])
        
        # Rappel 1 : 15 minutes avant l'activité
        alarm_15m = Alarm()
        alarm_15m.add('action', 'DISPLAY')
        alarm_15m.add('description', f"Rappel imminent : {summary}")
        alarm_15m.add('trigger', timedelta(minutes=-15))
        event.add_component(alarm_15m)
        
        # Rappel 2 : 24 heures avant l'activité
        alarm_24h = Alarm()
        alarm_24h.add('action', 'DISPLAY')
        alarm_24h.add('description', f"Rappel J-1 : {summary}")
        alarm_24h.add('trigger', timedelta(days=-1))
        event.add_component(alarm_24h)
        
        cal.add_component(event)

    # -------------------------------------------------------------------------
    # JUIN 2026
    # -------------------------------------------------------------------------
    for j in [7, 14, 21, 28]:
        add_phila_event("Culte dominical", tz.localize(datetime(2026, 6, j, 10, 0)), tz.localize(datetime(2026, 6, j, 11, 30)), "Celebration")
    
    for j in [4, 11, 18, 25]:
        add_phila_event("Prière matinale", tz.localize(datetime(2026, 6, j, 5, 0)), tz.localize(datetime(2026, 6, j, 6, 0)), "Priere")
        add_phila_event("Prière du soir", tz.localize(datetime(2026, 6, j, 21, 30)), tz.localize(datetime(2026, 6, j, 22, 30)), "Priere")

    # -------------------------------------------------------------------------
    # JUILLET 2026
    # -------------------------------------------------------------------------
    for j in [5, 12, 19, 26]:
        add_phila_event("Culte dominical", tz.localize(datetime(2026, 7, j, 10, 0)), tz.localize(datetime(2026, 7, j, 11, 30)), "Celebration")
    
    for j in [2, 9, 23, 30]:
        add_phila_event("Prière matinale", tz.localize(datetime(2026, 7, j, 5, 0)), tz.localize(datetime(2026, 7, j, 6, 0)), "Priere")
        add_phila_event("Prière du soir", tz.localize(datetime(2026, 7, j, 21, 30)), tz.localize(datetime(2026, 7, j, 22, 30)), "Priere")
        
    for j in [14, 15, 16]:
        add_phila_event("Séminaire", tz.localize(datetime(2026, 7, j, 21, 30)), tz.localize(datetime(2026, 7, j, 22, 30)), "Seminaire")

    # -------------------------------------------------------------------------
    # AOÛT 2026
    # -------------------------------------------------------------------------
    for j in [2, 9, 16, 23, 30]:
        add_phila_event("Culte dominical", tz.localize(datetime(2026, 8, j, 10, 0)), tz.localize(datetime(2026, 8, j, 11, 30)), "Celebration")
        
    for j in [6, 13, 20, 27]:
        add_phila_event("Prière matinale", tz.localize(datetime(2026, 8, j, 5, 0)), tz.localize(datetime(2026, 8, j, 6, 0)), "Priere")
        add_phila_event("Prière du soir", tz.localize(datetime(2026, 8, j, 21, 30)), tz.localize(datetime(2026, 8, j, 22, 30)), "Priere")
        
    for j in [28, 29]:
        add_phila_event("Connaissez-vous Phila?", tz.localize(datetime(2026, 8, j, 21, 30)), tz.localize(datetime(2026, 8, j, 22, 30)), "Enseignement")

    # -------------------------------------------------------------------------
    # SEPTEMBRE 2026
    # -------------------------------------------------------------------------
    for j in [6, 13, 20, 27]:
        add_phila_event("Culte dominical", tz.localize(datetime(2026, 9, j, 10, 0)), tz.localize(datetime(2026, 9, j, 11, 30)), "Celebration")
        
    for j in [3, 10, 17, 24]:
        add_phila_event("Prière matinale", tz.localize(datetime(2026, 9, j, 5, 0)), tz.localize(datetime(2026, 9, j, 6, 0)), "Priere")
        add_phila_event("Prière du soir", tz.localize(datetime(2026, 9, j, 21, 30)), tz.localize(datetime(2026, 9, j, 22, 30)), "Priere")
        
    add_phila_event("Connaissez-vous Phila?", tz.localize(datetime(2026, 9, 1, 21, 30)), tz.localize(datetime(2026, 9, 1, 22, 30)), "Enseignement")
    
    for j in [8, 15, 22, 29]:
        add_phila_event("École d'Apollos", tz.localize(datetime(2026, 9, j, 21, 30)), tz.localize(datetime(2026, 9, j, 22, 30)), "Enseignement")

    # -------------------------------------------------------------------------
    # OCTOBRE 2026
    # -------------------------------------------------------------------------
    for j in [4, 11, 18, 25]:
        add_phila_event("Culte dominical", tz.localize(datetime(2026, 10, j, 10, 0)), tz.localize(datetime(2026, 10, j, 11, 30)), "Celebration")
        
    for j in [1, 8, 15, 22, 29]:
        add_phila_event("Prière matinale", tz.localize(datetime(2026, 10, j, 5, 0)), tz.localize(datetime(2026, 10, j, 6, 0)), "Priere")
        add_phila_event("Prière du soir", tz.localize(datetime(2026, 10, j, 21, 30)), tz.localize(datetime(2026, 10, j, 22, 30)), "Priere")
        
    for j in [6, 13, 20, 27]:
        add_phila_event("École d'Apollos", tz.localize(datetime(2026, 10, j, 21, 30)), tz.localize(datetime(2026, 10, j, 22, 30)), "Enseignement")

    # -------------------------------------------------------------------------
    # NOVEMBRE 2026
    # -------------------------------------------------------------------------
    for j in [1, 15, 22, 29]:
        add_phila_event("Culte dominical", tz.localize(datetime(2026, 11, j, 10, 0)), tz.localize(datetime(2026, 11, j, 11, 30)), "Celebration")
        
    add_phila_event("Culte dominical", tz.localize(datetime(2026, 11, 8, 10, 0)), tz.localize(datetime(2026, 11, 8, 11, 30)), "Celebration")
    add_phila_event("Séminaire", tz.localize(datetime(2026, 11, 8, 21, 30)), tz.localize(datetime(2026, 11, 8, 22, 30)), "Seminaire")
    
    for j in [12, 19, 26]:
        add_phila_event("Prière matinale", tz.localize(datetime(2026, 11, j, 5, 0)), tz.localize(datetime(2026, 11, j, 6, 0)), "Priere")
        add_phila_event("Prière du soir", tz.localize(datetime(2026, 11, j, 21, 30)), tz.localize(datetime(2026, 11, j, 22, 30)), "Priere")
        
    for j in range(2, 8):
        add_phila_event("Séminaire (Session Spéciale)", tz.localize(datetime(2026, 11, j, 21, 30)), tz.localize(datetime(2026, 11, j, 22, 30)), "Seminaire")
        
    for j in [10, 17, 24]:
        add_phila_event("École d'Apollos", tz.localize(datetime(2026, 11, j, 21, 30)), tz.localize(datetime(2026, 11, j, 22, 30)), "Enseignement")

    # -------------------------------------------------------------------------
    # DÉCEMBRE 2026
    # -------------------------------------------------------------------------
    for j in [6, 13, 27]:
        add_phila_event("Culte dominical", tz.localize(datetime(2026, 12, j, 10, 0)), tz.localize(datetime(2026, 12, j, 11, 30)), "Celebration")
        
    add_phila_event("Culte d'action de grâce", tz.localize(datetime(2026, 12, 20, 10, 0)), tz.localize(datetime(2026, 12, 20, 11, 30)), "Celebration")
    
    for j in [3, 10, 17, 24, 31]:
        add_phila_event("Prière matinale", tz.localize(datetime(2026, 12, j, 5, 0)), tz.localize(datetime(2026, 12, j, 6, 0)), "Priere")
        add_phila_event("Prière du soir", tz.localize(datetime(2026, 12, j, 21, 30)), tz.localize(datetime(2026, 12, j, 22, 30)), "Priere")
        
    for j in [1, 8, 15, 22, 29]:
        add_phila_event("École d'Apollos", tz.localize(datetime(2026, 12, j, 21, 30)), tz.localize(datetime(2026, 12, j, 22, 30)), "Enseignement")

    # -------------------------------------------------------------------------
    # Écriture du fichier final
    # -------------------------------------------------------------------------
    output_file = "calendrier_pce_belgique_2026.ics"
    with open(output_file, 'wb') as f:
        f.write(cal.to_ical())
        
    print(f"[✔] Le fichier '{output_file}' a été généré avec succès.")

if __name__ == "__main__":
    # Correction ici du nom de la fonction appelée
    create_precise_calendar()