from django.db import models


class Contato(models.Model):
    nome = models.CharField('nome', max_length=30)
    email = models.EmailField('email')
    telefone = models.CharField('telefone', max_length=11)

    def __str__(self):
        return self.nome
