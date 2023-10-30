from django.urls import path

from .views import registrar_alumno, registrar_docente, registrar_ascesor, dar_baja_alumno, dar_baja_docente
from .views import dar_baja_ascesor

app_name = 'persona'

urlpatterns = [
    path('registrar_alumno/', registrar_alumno, name='registrar_alumno'),
    path('registrar_docente/', registrar_docente, name='registrar_docente'),
    path('registrar_ascesor/', registrar_ascesor, name='registrar_ascesor'),
    path('dar_baja_alumno/', dar_baja_alumno, name='dar_baja_alumno'),
    path('dar_baja_docente/', dar_baja_docente, name='dar_baja_docente'),
    path('dar_baja_ascesor/', dar_baja_ascesor, name='dar_baja_ascesor')

]
