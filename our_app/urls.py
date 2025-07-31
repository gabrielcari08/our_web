from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name="home"),
    path('album/', views.album, name="album"),
    path('videos/', views.videos, name="videos"),
    path('counter/', views.counter, name="counter"),
    path('cards/', views.cards, name="cards"),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
