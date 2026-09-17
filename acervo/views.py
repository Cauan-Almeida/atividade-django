from django.shortcuts import render, redirect
from django.db.models import Q
from .models import Livro
from .forms import LivroForm

def lista_livros(request):
    livros = Livro.objects.all().order_by('titulo')
    nome = request.GET.get('nome', '').strip()
    tipo = request.GET.get('tipo', '').strip()
    categoria = request.GET.get('categoria', '').strip()

    if nome:
        livros = livros.filter(Q(titulo__icontains=nome) | Q(autor__icontains=nome))
    if tipo:
        livros = livros.filter(tipo=tipo)
    if categoria:
        livros = livros.filter(categoria=categoria)

    context = {
        'livros': livros,
        'nome': nome,
        'tipo_selecionado': tipo,
        'categoria_selecionada': categoria,
        'tipos': Livro.TIPO_CHOICES,
        'categorias': Livro.CATEGORIA_CHOICES,
    }
    return render(request, 'acervo/lista.html', context)

def novo_livro(request):
    if request.method == 'POST':
        form = LivroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista')
    else:
        form = LivroForm()
    return render(request, 'acervo/form.html', {'form': form})