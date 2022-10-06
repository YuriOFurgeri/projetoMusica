from django.shortcuts import render
from .models import *
from django.forms import ModelForm
from django.shortcuts import redirect


class MusicaForm(ModelForm):
    class Meta:
        model = Musica
        fields =['musica','autor','album','anoPublicacao']


def musica_list(request, template_name='musica_list.html'):
    musica = Musica.objects.all()
    return render(request, template_name, {'lista': musica})

def musica_new(request, template_name='musica_form.html'):
    form = MusicaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('musica_list')
    return render(request, template_name, {'form': form})
