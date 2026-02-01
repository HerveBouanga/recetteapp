from django.shortcuts import get_object_or_404, redirect, render
from .models import Recette
from .forms import RecetteForm
from django.contrib.auth.decorators import login_required


def home(request):
    if request.method == 'POST':
        form = RecetteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
            
    else:
        form = RecetteForm()

    recettes = Recette.objects.all()
    return render(request, 'recette/index.html', {
        'recettes': recettes, 
        'formulaire': form
    })


@login_required
def supprimer_recette(request, id):
    recette = get_object_or_404(Recette, id=id)
    recette.delete()
    return redirect('home')