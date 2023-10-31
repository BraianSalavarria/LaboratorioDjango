from django.urls import path
from .views import registrar_comicion, asignar_docente_comicion, registrar_evaluacion_formal, registrar_tribunal
from .views import asignar_docente_tribunal, registrar_evaluacion_tf, listar_tribunales

app_name = 'evaluacion'

urlpatterns = [

    path('registrar_comicion/', registrar_comicion, name='registrar_comicion'),
    path('asignar_docente_comicion/', asignar_docente_comicion, name='asignar_docente_comicion'),
    path('registrar_evaluacion_formal/', registrar_evaluacion_formal, name='registrar_evaluacion_formal'),
    path('registrar_tribunal/', registrar_tribunal, name='registrar_tribunal'),
    path('asignar_docente_tribunal/', asignar_docente_tribunal, name='asignar_docente_tribunal'),
    path('registrar_evaluacion_tf/', registrar_evaluacion_tf, name='registrar_evaluacion_tf'),
    path('lista_tribunales/', listar_tribunales, name='lista_tribunales'),
]
