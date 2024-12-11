from django import forms


from apps.dados_enjoyer.models import DadosPatrimoniais, DadosPessoais, DadosSociais

class DadosPatrimoniaisForm(forms.ModelForm):
    class Meta:
        model = DadosPatrimoniais
        fields = '__all__'
    
class DadosPessoaisForm(forms.ModelForm):
    class Meta:
        model = DadosPessoais
        fields = '__all__'

class DadosSociaisForm(forms.ModelForm):
    class Meta: 
        model = DadosSociais
        fields = '__all__'