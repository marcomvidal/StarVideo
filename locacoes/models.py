"""
Models: App 'locacoes'
"""
from django.db import models
from django.core.validators import MinLengthValidator
from django.utils import timezone


class Cliente(models.Model):
    """
    Clientes que locarão os filmes da locadora.
    """
    nome = models.CharField(max_length=255)
    data_nascimento = models.DateField()
    sexo = models.CharField(max_length=1, validators=[MinLengthValidator(1)])
    rg = models.CharField(max_length=9, validators=[MinLengthValidator(9)])
    cpf = models.CharField(max_length=11, validators=[MinLengthValidator(9)])
    foto = models.CharField(max_length=255)
    endereco = models.CharField(max_length=255)
    numero = models.CharField(max_length=10)
    complemento = models.CharField(max_length=50)
    cep = models.CharField(max_length=9)
    ddd = models.CharField(max_length=2)
    telefone = models.CharField(max_length=9)
    email = models.CharField(max_length=255)
    banido = models.BooleanField(default=False)
    usuario = models.ForeignKey('auth.User')

    def __str__(self):
        return self.nome


class Locacao(models.Model):
    """
    Relaciona cliente locador, filmes e usuário que cadastrou a locação.
    """
    data_inicio = models.DateTimeField(default=timezone.now)
    data_fim = models.DateTimeField()
    pago = models.BooleanField(default=False)
    multa = models.DecimalField(max_digits=5, decimal_places=2)
    preco = models.DecimalField(max_digits=5, decimal_places=2)
    cliente = models.ForeignKey('locacoes.Cliente')
    usuario = models.ForeignKey('auth.User')
    status_locacao = models.ForeignKey('locacoes.StatusLocacao')

    def __str__(self):
        return self.usuario+", "+self.data_inicio

    class Meta:
        verbose_name = 'Locação'
        verbose_name_plural = 'Locações'


class StatusLocacao(models.Model):
    """
    Define o estado da locação: 'Realizada', 'Com Pendências', 'Cancelada' e 'Finalizada'
    """
    status_locacao = models.CharField(max_length=100)
    icone = models.CharField(max_length=100)

    def __str__(self):
        return self.status_locacao

    class Meta:
        verbose_name = 'Status da Locação'
        verbose_name_plural = 'Status das Locações'


class Filme(models.Model):
    """
    Reune informações sobre os filmes do acervo.
    """
    titulo = models.CharField(max_length=255)
    sinopse = models.TextField(blank=True, default='')
    quantidade = models.IntegerField()
    data_lancamento = models.DateTimeField(blank=True, null=True)
    blockbuster = models.BooleanField(default=False)
    capa = models.ImageField(upload_to='filmes', blank=True, default='')
    usuario = models.ForeignKey('auth.User')
    classificacao = models.ForeignKey('locacoes.Classificacao')
    genero = models.ForeignKey('locacoes.Genero')
    locacoes = models.ManyToManyField(Locacao)

    def __str__(self):
        return self.titulo


class Classificacao(models.Model):
    """
    Reune informações sobre as classificações etárias de filmes.
    """
    nome = models.CharField(max_length=255)
    idade = models.IntegerField()
    descricao = models.TextField()
    icone = models.CharField(max_length=50)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Classificação'
        verbose_name_plural = 'Classificações'


class Genero(models.Model):
    """
    Reune os gêneros de filmes.
    """
    genero = models.CharField(max_length=100)

    def __str__(self):
        return self.genero

    class Meta:
        verbose_name = 'Gênero'
