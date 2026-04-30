from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.urls import include, path
from django.shortcuts import render


@login_required
def inicio(request):
    return render(request, 'inicio.html')


urlpatterns = [
    path('', inicio, name='inicio'),
    path('calificaciones/', include('calificaciones_nombre_estudiante.urls')),
    path(
        'login/',
        auth_views.LoginView.as_view(template_name='registration/login.html'),
        name='login',
    ),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('admin/', admin.site.urls),
]
