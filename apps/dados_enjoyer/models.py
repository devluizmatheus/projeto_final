from django.db import models

from stdimage.models import StdImageField

from apps.core.models import Base, Enjoyer

class DadosPatrimoniais(Base):
    moradia = models.TextField('Moradia(s)')
    veiculos = models.TextField('Veículo(s)')
    empresas = models.TextField('Empresa(s)')
    cnpj = models.IntegerField('CNPJ')
    dados_enjoyer = models.ForeignKey(Enjoyer, on_delete= models.CASCADE, related_name="dados_patrimoniais")

    class Meta:
        verbose_name = 'Dado Patrimonial'
        verbose_name_plural = 'Dados Pratrimoniais'

    def __str__(self):
        return f'Dados Patrimoniais de {self.dados_enjoyer.username}'
    
class DadosPessoais(Base):
    nome = models.CharField('Nome', max_length=100)
    data_nascimento = models.DateField()
    sexo = models.CharField('Sexo', max_length=60)
    CPF = models.CharField('CPF', max_length=200)
    estado_civil = models.CharField('Estado Civil', max_length=100)
    telefones = models.CharField('Número de Telefone', max_length=100)
    foto_pessoal = StdImageField(
        upload_to='foto_pessoal/',
        variations= {
            'thumbnail': (100, 100),
            'medium': (300, 300),
        }
    )
    dados_enjoyer = models.ForeignKey(Enjoyer, on_delete=models.CASCADE, related_name='dados_pessoais')
    
    class Meta:
        verbose_name = 'Dado Pessoal'
        verbose_name_plural = 'Dados Pessoais'

    def __str__(self):
        return f'Dados Pessoais de {self.dados_enjoyer.username}'
    
class DadosSociais(Base):
    facebook = models.CharField('Facebook', max_length=200)
    instagram = models.CharField('Instagram', max_length=200)
    emails = models.CharField('Emails', max_length=200)
    outras_redes = models.CharField('Outras Redes', max_length=200)
    dados_enjoyers = models.ForeignKey(Enjoyer, on_delete= models.CASCADE, related_name="dados_sociais")    

    class Meta:
        verbose_name = 'Dado Social'
        verbose_name_plural = 'Dados Sociais'

        
    def __str__(self):
        return f'Dados Sociais de {self.dados_enjoyers.username}'
