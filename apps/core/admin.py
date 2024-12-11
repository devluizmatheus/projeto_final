from django.contrib import admin
from .models import (
    Selection,
    Enjoyer,
    SelectionEnjoyer,
)

from apps.dados_enjoyer.models import DadosPatrimoniais, DadosPessoais, DadosSociais

from apps.qualificacao_enjoyer.models import QualificacaoAreaInteligencia, QualificacaoExtraPMPB, QualificacaoPessoal, QualificacaoPMPB

@admin.register(DadosPatrimoniais)
class DadosPatrimoniaisAdmin(admin.ModelAdmin):
    list_display = ('id', 'dados_enjoyer', 'moradia', 'veiculos', 'empresas', 'cnpj')
    search_fields = ('dados_enjoyer__username', 'moradia', 'veiculos', 'empresas')
    list_filter = ('ativo', 'criados')

@admin.register(DadosPessoais)
class DadosPessoaisAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'data_nascimento', 'sexo', 'CPF', 'dados_enjoyer')
    search_fields = ('nome', 'CPF', 'dados_enjoyer__username')
    list_filter = ('sexo', 'ativo', 'criados')

@admin.register(DadosSociais)
class DadosSociaisAdmin(admin.ModelAdmin):
    list_display = ('id', 'facebook', 'instagram', 'emails', 'outras_redes', 'dados_enjoyers')
    search_fields = ('facebook', 'instagram', 'emails', 'dados_enjoyers__username')
    list_filter = ('ativo', 'criados')

@admin.register(Selection)
class SelectionAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'descricao', 'data_inicio', 'data_fim', 'status')
    search_fields = ('titulo', 'descricao')
    list_filter = ('status', 'data_inicio', 'data_fim')

@admin.register(Enjoyer)
class EnjoyerAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'primeiro_nome', 'sobrenome')
    search_fields = ('username', 'email', 'primeiro_nome', 'sobrenome')
    list_filter = ('ativo', 'criados')

@admin.register(SelectionEnjoyer)
class SelectionEnjoyerAdmin(admin.ModelAdmin):
    list_display = ('id', 'selection_key', 'enjoyer_key', 'status', 'data_inscricao')
    search_fields = ('selection_key__titulo', 'enjoyer_key__username')
    list_filter = ('status', 'data_inscricao')

@admin.register(QualificacaoAreaInteligencia)
class QualificacaoAreaInteligenciaAdmin(admin.ModelAdmin):
    list_display = ('id', 'curso_inteligencia', 'data_conclusao', 'dados_enjoyers')
    search_fields = ('curso_inteligencia', 'dados_enjoyers__username')
    list_filter = ('data_conclusao', 'ativo')

@admin.register(QualificacaoExtraPMPB)
class QualificacaoExtraPMPBAdmin(admin.ModelAdmin):
    list_display = ('id', 'nivel_escolaridade', 'curso', 'dados_enjoyers')
    search_fields = ('nivel_escolaridade', 'curso', 'dados_enjoyers__username')
    list_filter = ('ativo', 'criados')

@admin.register(QualificacaoPMPB)
class QualificacaoPMPBAdmin(admin.ModelAdmin):
    list_display = ('id', 'curso_realizados', 'data_conclusao', 'dados_enjoyers')
    search_fields = ('curso_realizados', 'dados_enjoyers__username')
    list_filter = ('data_conclusao', 'ativo')

@admin.register(QualificacaoPessoal)
class QualificacaoPessoalAdmin(admin.ModelAdmin):
    list_display = ('id', 'post_grad', 'instituicao', 'numero_matricula', 'numero_admissao', 'dados_enjoyers')
    search_fields = ('post_grad', 'instituicao', 'dados_enjoyers__username')
    list_filter = ('ativo', 'criados')
