from django.db import models

class Livro(models.Model):
    TIPO_CHOICES = [
        ('FISICO', 'Físico'),
        ('DIGITAL', 'Digital'),
    ]

    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=100)
    ano = models.IntegerField()
    disponivel = models.BooleanField(default=True)
    tipo = models.CharField(
        max_length=10,
        choices=TIPO_CHOICES,
        default='FISICO',
        verbose_name='Tipo de Acervo'
    )

    def __str__(self):
        return f"{self.titulo} - {self.autor}"
