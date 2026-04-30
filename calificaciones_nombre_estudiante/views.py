from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.db.models import Avg
from django.shortcuts import get_object_or_404, redirect, render

from .forms import CalificacionForm, RegistroUsuarioForm
from .models import Calificacion


def registrar_usuario(request):
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            login(request, usuario)
            return redirect('inicio')
    else:
        form = RegistroUsuarioForm()

    return render(
        request,
        'registration/registro.html',
        {'form': form},
    )


@login_required
def listar_calificaciones(request):
    calificaciones = Calificacion.objects.all().order_by('nombre_estudiante', 'asignatura')
    promedio_general_valor = Calificacion.objects.aggregate(
        promedio_general=Avg('promedio')
    )['promedio_general']

    return render(
        request,
        'calificaciones/listar.html',
        {
            'calificaciones': calificaciones,
            'promedio_general': promedio_general_valor,
        },
    )


@login_required
def crear_calificacion(request):
    if request.method == 'POST':
        form = CalificacionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('calificaciones:listar')
    else:
        form = CalificacionForm()

    return render(
        request,
        'calificaciones/crear.html',
        {'form': form},
    )


@login_required
def editar_calificacion(request, pk):
    calificacion = get_object_or_404(Calificacion, pk=pk)

    if request.method == 'POST':
        form = CalificacionForm(request.POST, instance=calificacion)
        if form.is_valid():
            form.save()
            return redirect('calificaciones:listar')
    else:
        form = CalificacionForm(instance=calificacion)

    return render(
        request,
        'calificaciones/editar.html',
        {
            'form': form,
            'calificacion': calificacion,
        },
    )


@login_required
def eliminar_calificacion(request, pk):
    calificacion = get_object_or_404(Calificacion, pk=pk)

    if request.method == 'POST':
        calificacion.delete()
        return redirect('calificaciones:listar')

    return render(
        request,
        'calificaciones/eliminar.html',
        {'calificacion': calificacion},
    )


@login_required
def promedio_general(request):
    promedio_general_valor = Calificacion.objects.aggregate(
        promedio_general=Avg('promedio')
    )['promedio_general']

    return render(
        request,
        'calificaciones/promedio_general.html',
        {'promedio_general': promedio_general_valor},
    )
