from django.shortcuts import render, redirect
from app1.models import Adresses
from app1.forms import GensForm


# page principale
def gens(request):
    a = Adresses.objects.all()
    return render(request, 
                  'app1/gens.html',
                  {'gens' : a})


# détail d'une seule entrée de la bdd
def gens_detail(request, id):
    a = Adresses.objects.get(id=id)
    return render(request,
                  'app1/gens_detail.html',
                  {'gens' : a})


# création d'une entrée bdd
def gens_create(request):
    if request.method == 'POST':
        form = GensForm(request.POST)
        if form.is_valid():
            gens = form.save()
            return redirect('gens-detail', gens.id)
    else:
        form = GensForm()

    return render(request, 
                'app1/gens_create.html', 
                {'form' : form})


# changer une entrée de la bdd
def gens_change(request, id):
    gens = Adresses.objects.get(id=id)

    if request.method == 'POST':
        form = GensForm(request.POST, instance=gens)
        if form.is_valid():
            form.save()
            return redirect('gens-detail', gens.id)

    else:
        form = GensForm(instance=gens)
    
    return render(request,
           'app1/gens_change.html', 
           {'form' : form})


# supprimer une entrée de la bdd
def gens_delete(request, id):
    try:
        gens = Adresses.objects.get(id=id)
    except:
        gens = None

    if request.method == 'POST':
        gens.delete()
        gens = None
        
    return render(request, 
                  'app1/gens_delete.html',
                  {'gens' : gens})