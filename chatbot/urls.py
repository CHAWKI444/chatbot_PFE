from django.urls import path
from . import views

urlpatterns = [
    path('run-ingest/', views.run_ingest, name='run_ingest'),
    path('ingest-form/', views.ingest_form, name='ingest_form'),
    path('', views.chatbot_query, name='chatbot_query'),  # Cette route gère l'URL racine de "chatbot/"
    path('upload/', views.upload_fichier, name='upload_fichier'),
]