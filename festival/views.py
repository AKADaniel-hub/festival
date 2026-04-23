from django.shortcuts import render
from .models import Palco, Dia, Concerto
from django.shortcuts import render, get_object_or_404

def index_view(request):
    return render(request, 'festival/index.html')


def palcos_view(request):
    palcos = Palco.objects.all()
    context = {'palcos': palcos}
    return render(request, 'festival/palcos.html', context)

def dias_view(request):
    dias = Dia.objects.all().order_by('data')
    context = {'dias': dias}

    return render(request, 'festival/dias.html', context)



def concerto_view(request, id):
    concerto = get_object_or_404(Concerto, id=id)

    context = {'concerto': concerto}

    return render(request, 'festival/concerto.html', context)