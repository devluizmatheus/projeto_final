from django.db import models

class Base(models.Model):
    criados = models.DateField('Criação', auto_now_add=True)
    modificados = models.DateField('Atualização', auto_now=True)
    ativo = models.BooleanField('Ativo?', default=True)

    class Meta:
        abstract = True

class Selection(Base):
    STATUS_CHOICES = [
        ('ativo', 'Ativo'),
        ('inativo', 'Inativo'),
    ]
    titulo = models.CharField('Título', max_length=200)
    descricao = models.TextField('Descrição')
    requisitos = models.TextField('Requisitos')
    data_inicio = models.DateField('Data de Início')
    data_fim = models.DateField('Data de Fim')
    status = models.CharField('Status', max_length=10, choices=STATUS_CHOICES, default='ativo')

    class Meta:
        verbose_name = 'Processo Seletivo'
        verbose_name_plural = 'Processos Seletivos'

    def __str__(self):
        return self.titulo
    
class Enjoyer(Base):
    STATUS_CHOICES = [
        ('inscrito', 'Inscrito'),
        ('aprovado', 'Aprovado'),
        ('reprovado', 'Reprovado')
    ]
    username = models.CharField('Username', max_length=100)
    password = models.CharField('Senha', max_length=100)
    primeiro_nome = models.CharField('First Name', max_length=200)
    sobrenome = models.CharField('Last Name', max_length=200)
    email = models.EmailField(unique=True)

    class Meta:
        verbose_name = 'Enjoyer'
        verbose_name_plural = 'Enjoyers'

    def __str__(self):
        return self.username
    
class SelectionEnjoyer(Base):
    STATUS_CHOICES = [
        ('em andamento', 'Em Andamento'),
        ('aprovado', 'Aprovado'),
        ('rejeitado', 'Rejeitado'),
    ]
    selection_key = models.ForeignKey(Selection, on_delete=models.CASCADE, related_name='candidaturas')
    enjoyer_key = models.ForeignKey(Enjoyer, on_delete=models.CASCADE, related_name='candidaturas')
    status = models.CharField('Status', max_length=15, choices=STATUS_CHOICES, default='em andamento')
    data_inscricao = models.DateTimeField('Data da Inscrição', auto_now_add=True)

    class Meta:
        verbose_name = 'Candidatura'
        verbose_name_plural = 'Candidaturas'
        unique_together = ('selection_key', 'enjoyer_key')

    def __str__(self):
        return f'{self.enjoyer_key.username} - {self.selection_key.titulo}' #obs: antes que eu me esqueça isso serve para combinar os mome e titulo por ex: Luiz Matheus - Desenvolvedor Backend nessa linha 
