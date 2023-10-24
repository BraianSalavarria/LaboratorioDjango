from django.urls import path
from .views import registrar_trabajo_final, registrar_movimiento_tf, asignar_alumno_tf, dar_baja_alumno_tf, listar_tf

app_name = 'proyecto'

urlpatterns = [
    path('registrar_tf/', registrar_trabajo_final, name='registrar_trabajo_final'),
    path('asignar_alumno_tf/', asignar_alumno_tf, name='asignar_alumno_tf'),
    path('baja_alumno_tf/', dar_baja_alumno_tf, name='dar_baja_alumno_tf'),
    path('registrar_movimiento/', registrar_movimiento_tf, name='registrar_movimiento_tf'),
    path('listar_tf/', listar_tf, name='listar_tf')
]
