"""
Models: App 'locacoes'
"""
from django.db import models
from django.core.validators import MinLengthValidator
from django.utils import timezone
from datetime import date


class Cliente(models.Model):
    """
    `Clientes` que locarão os filmes da locadora.
    """
    nome = models.CharField(max_length=255)
    data_nascimento = models.DateField()
    rg = models.CharField(max_length=12, validators=[MinLengthValidator(12)])
    cpf = models.CharField(max_length=14, validators=[MinLengthValidator(14)])
    foto = models.ImageField(upload_to='clientes/', blank=True, default='')
    endereco = models.CharField(max_length=255)
    numero = models.CharField(max_length=10)
    complemento = models.CharField(max_length=50)
    cep = models.CharField(max_length=10)
    cidade = models.CharField(max_length=255)
    uf = models.CharField(max_length=2)
    ddd = models.CharField(max_length=2)
    telefone = models.CharField(max_length=10)
    email = models.CharField(max_length=255)
    banido = models.BooleanField(default=False)
    usuario = models.ForeignKey('auth.User')

    def idade(self):
        hoje = date.today()
        return hoje.year - self.data_nascimento.year - ((hoje.month, hoje.day) < (self.data_nascimento.month, self.data_nascimento.day))

    def __str__(self):
        return self.nome


class Filme(models.Model):
    """
    Reune informações sobre os `filmes` do acervo.
    """
    titulo = models.CharField(max_length=255)
    sinopse = models.TextField(blank=True, default='')
    quantidade = models.IntegerField()
    data_lancamento = models.DateTimeField(blank=True, null=True)
    blockbuster = models.BooleanField(default=False)
    capa = models.ImageField(upload_to='filmes/', blank=True, default='')
    usuario = models.ForeignKey('auth.User')
    classificacao = models.ForeignKey('locacoes.Classificacao')
    genero = models.ForeignKey('locacoes.Genero')

    def __str__(self):
        return self.titulo

    def subtrai_quantidade(self):
        """
        Subtrai uma unidade da quantidade total do acervo de um `filme` e
        persiste a alteração no banco de dados.
        """
        self.quantidade = self.quantidade - 1
        self.save()

    def repoe_quantidade(self):
        """
        Subtrai uma unidade da quantidade total do acervo de um `filme` e
        persiste a alteração no banco de dados.
        """
        self.quantidade = self.quantidade + 1
        self.save()


class Classificacao(models.Model):
    """
    Reune informações sobre as `classificações etárias` de filmes.
    """
    nome = models.CharField(max_length=255)
    idade = models.IntegerField()
    descricao = models.TextField()
    icone = models.ImageField(upload_to='classificacoes/', blank=True, default='')

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Classificação'
        verbose_name_plural = 'Classificações'


class Genero(models.Model):
    """
    Reune os `gêneros` de filmes.
    """
    genero = models.CharField(max_length=100)

    def __str__(self):
        return self.genero

    class Meta:
        verbose_name = 'Gênero'


class Locacao(models.Model):
    """
    Relaciona cliente `locador`, filmes e usuário que cadastrou a locação.
    """
    data_inicio = models.DateTimeField(default=timezone.now)
    data_fim = models.DateTimeField()
    pago = models.BooleanField(default=False)
    multa = models.DecimalField(max_digits=5, decimal_places=2)
    preco = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    total = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    cliente = models.ForeignKey('locacoes.Cliente', null=True)
    usuario = models.ForeignKey('auth.User')
    status_locacao = models.ForeignKey('locacoes.StatusLocacao')
    filmes = models.ManyToManyField(Filme)

    def __str__(self):
        return "#" + str(self.pk) + " - " + str(self.data_inicio) + " " + self.usuario.first_name

    def estado_locacao(self):
        if (self.status_locacao == 1):
            return '<a class="text-primary"><i class="' + self.status_locacao.icone + '"></i> ' + self.status_locacao.status_locacao + '</a>'
        elif (self.status_locacao == 2):
            return '<a class="text-warning"><i class="' + self.status_locacao.icone + '"></i> ' + self.status_locacao.status_locacao + '</a>'
        elif (self.status_locacao == 3):
            return '<a class="text-danger"><i class="' + self.status_locacao.icone + '"></i> ' + self.status_locacao.status_locacao + '</a>'
        else:
            return '<a class="text-success"><i class="' + self.status_locacao.icone + '"></i> ' + self.status_locacao.status_locacao + '</a>'

    def soma_valor_filme(self):
        self.preco = self.preco + 8

    def subtrai_valor_filme(self):
        self.preco = self.preco - 8

    def soma_multa(self):
        return self.preco + self.multa


    class Meta:
        verbose_name = 'Locação'
        verbose_name_plural = 'Locações'


class StatusLocacao(models.Model):
    """
    Define o `estado da locação`: 'Realizada', 'Com Pendências', 'Cancelada' e 'Finalizada'
    """
    status_locacao = models.CharField(max_length=100)
    icone = models.CharField(max_length=100)

    def __str__(self):
        return self.status_locacao

    class Meta:
        verbose_name = 'Status da Locação'
        verbose_name_plural = 'Status das Locações'
