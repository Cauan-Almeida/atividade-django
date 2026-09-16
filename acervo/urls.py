from django.urls import path
from . import views

urlpatterns = [
    path(
        'livros/',
        views.lista_livros,
        name='lista'
    ),
    path(
        'cadastrar/',
        views.novo_livro,
        name='cadastrar'
    )
]