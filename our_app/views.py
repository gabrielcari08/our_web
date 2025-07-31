from django.shortcuts import render
from datetime import datetime, timedelta

# Create your views here.

def home(request):
    
    return render(request, "our_app/home.html")

def album(request):
    
    return render(request, "our_app/album.html")

def videos(request):
    
    return render(request, "our_app/videos.html")

def counter(request):
    
    # Define la fecha de inicio
    start_date = datetime(2024, 6, 6, 0, 0, 0) # Año, Mes, Día, Hora, Minuto, Segundo

    # Obtiene la fecha y hora actual
    now = datetime.now()

    # Calcula la diferencia de tiempo
    time_difference = now - start_date

    # Extrae días, segundos totales y calcula horas y minutos
    days = time_difference.days
    seconds = time_difference.total_seconds()
    hours = int(seconds // 3600) % 24 # Horas completas en el día actual
    minutes = int(seconds % 3600 // 60) # Minutos completos en la hora actual
    
    # También podemos calcular horas y minutos totales si queremos:
    total_hours = int(seconds // 3600)
    total_minutes = int(seconds // 60)

    # Prepara el contexto para la plantilla
    context = {
        'start_date': start_date,
        'days': days,
        'hours': hours,
        'minutes': minutes,
        'total_hours': total_hours, # Opcional: total de horas
        'total_minutes': total_minutes, # Opcional: total de minutos
    }
    return render(request, "our_app/counter.html", context)

def cards(request):
    
    return render(request, "our_app/card.html")