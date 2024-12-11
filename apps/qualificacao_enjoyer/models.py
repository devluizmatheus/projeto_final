from django.db import models

from stdimage.models import StdImageField

from apps.core.models import Base, Enjoyer

class QualificacaoAreaInteligencia(Base):
    curso_inteligencia = models.CharField('Curso Inteligencia', max_length=255)
    data_conclusao =  models.DateField('Data de Conclusão')
    dados_enjoyers = models.ForeignKey(Enjoyer, on_delete= models.CASCADE, related_name="qualificacao_area_inteligencia")

    class Meta:
        verbose_name = 'Qualificação na Área Inteligência'
        verbose_name_plural = "Qualificações na Área de Inteligência"
    
    def _str_(self):
        return f'Qualificação Área Inteligência de {self.dados_enjoyers.username}'
    
class QualificacaoExtraPMPB(Base):
    nivel_escolaridade = models.CharField('Nível de Escolaridade', max_length=200)
    curso = models.CharField('Curso', max_length=200)
    declaracao_matricula = StdImageField(
        upload_to="declaracao_matricula/",
        variations={
            'thumbnail': (100, 100),
            'medium': (300, 300)
        }
    )
    dados_enjoyers = models.ForeignKey(Enjoyer, on_delete= models.CASCADE, related_name="qualificacao_extra_pmpb")

    class Meta:
        verbose_name = 'Qualificação Extra PMPB'
        verbose_name_plural = "Qualificações Extras da PMPB"

    def _str_(self):
        return f'Qualificação Extra PMPB {self.dados_enjoyers.username}'
    
class QualificacaoPMPB(Base):
    curso_realizados = models.CharField('Cursos de Qualificação', max_length=200)
    data_conclusao = models.DateField('Data de Conclusão')
    dados_enjoyers = models.ForeignKey(Enjoyer, on_delete= models.CASCADE, related_name="qualificacao_pmpb")
    
    class Meta:
        verbose_name = 'Qualificação PMPB'
        verbose_name_plural = "Qualificações PMPB"

    def _str_(self):
        return f'Qualificação da PMPB de {self.dados_enjoyers.username}'
    
class QualificacaoPessoal(Base):
    post_grad = models.CharField('Post/Grad', max_length=200)
    instituicao = models.CharField('Instutuição', max_length=200)
    numero_matricula = models.IntegerField('Número da Matrícula')
    numero_admissao = models.IntegerField("Número de Admissão")
    enderecos = models.TextField('Endereços')
    nome_cpf_pai = models.CharField('Nome e CPF do pai', max_length=255)
    nome_cpf_mae = models.CharField('Nome e CPF da Mãe', max_length=255)
    nome_cpf_irmaos = models.CharField('Nome e CPF dos Irmãos', max_length=255)
    nome_cpf_conjugue = models.CharField('Nome e CPF do conjugue', max_length=255)
    nome_cpf_filhos = models.CharField('Nome e CPF dos filhos', max_length=255)
    dados_enjoyers = models.ForeignKey(Enjoyer, on_delete= models.CASCADE, related_name="qualificacao_pessoal")

    class Meta:
        verbose_name = "Qualificação Pessoal"
        verbose_name_plural = 'Qualificações Pessoais'

    def _str_(self):
        return f'Qualificação Pessoal de {self.dados_enjoyers.username}'
    

