from django import forms

from apps.qualificacao_enjoyer.models import QualificacaoAreaInteligencia, QualificacaoExtraPMPB, QualificacaoPessoal, QualificacaoPMPB

class QualificacaoAreaInteligenciaForm(forms.ModelForm):
    class Meta:
        model = QualificacaoAreaInteligencia
        fields = '__all__'

class QualificacaoExtraPMPBForm(forms.ModelForm):
    class Meta:
        model = QualificacaoExtraPMPB
        fields = '__all__'

class QualificacoaPessoalForm(forms.ModelForm):
    class Meta:
        model = QualificacaoPessoal
        fields = '__all__'

class QualificacaoPMPBForm(forms.ModelForm):
    class Meta:
        model = QualificacaoPMPB
        fields = '__all__'