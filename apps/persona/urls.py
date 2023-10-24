from django.urls import path
from .views import registrar_alumno, registrar_docente, registrar_ascesor, dar_baja

app_name = 'persona'

urlpatterns = [
    path('registrar_alumno/', registrar_alumno, name='registrar_alumno'),
    path('registrar_docente/', registrar_docente, name='registrar_docente'),
    path('registrar_ascesor/', registrar_ascesor, name='registrar_ascesor'),
    path('dar_baja/', dar_baja, name='dar_baja'),

]
