from django.urls import path

from . import views

app_name = 'calificaciones'

urlpatterns = [
    path('', views.listar_calificaciones, name='listar'),
    path('crear/', views.crear_calificacion, name='crear'),
    path('<int:pk>/editar/', views.editar_calificacion, name='editar'),
    path('<int:pk>/eliminar/', views.eliminar_calificacion, name='eliminar'),
    path('promedio-general/', views.promedio_general, name='promedio_general'),
]
