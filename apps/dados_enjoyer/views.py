from apps.core.views import BaseCreateView, BaseDeleteView, BaseDetailView, BaseListView, BaseUpdateView

from django.urls import reverse_lazy

from apps.dados_enjoyer.models import DadosPatrimoniais, DadosPessoais, DadosSociais

from apps.dados_enjoyer.forms import DadosSociaisForm, DadosPessoaisForm, DadosPatrimoniaisForm


# Dados Patrimoniais
class DadosPatrimoniaisListView(BaseListView):
    model = DadosPatrimoniais
    form = DadosPatrimoniaisForm

class DadosPatrimoniaisDetailView(BaseDetailView):
    model = DadosPatrimoniais
    form = DadosPatrimoniaisForm

class DadosPatrimoniaisCreateView(BaseCreateView):
    model = DadosPatrimoniais
    form = DadosPatrimoniaisForm

class DadosPatrimoniaisUpdateView(BaseUpdateView):
    model = DadosPatrimoniais
    form = DadosPatrimoniaisForm

class DadosPatrimoniaisDeleteView(BaseDeleteView):
    model = DadosPatrimoniais
    form = DadosPatrimoniaisForm


# Dados Pessoais
class DadosPessoaisListView(BaseListView):
    model = DadosPessoais
    form = DadosPessoaisForm

class DadosPessoaisDetailView(BaseDetailView):
    model = DadosPessoais
    form = DadosPessoaisForm

class DadosPessoaisCreateView(BaseCreateView):
    model = DadosPessoais
    form = DadosPessoaisForm

class DadosPessoaisUpdateView(BaseUpdateView):
    model = DadosPessoais
    form = DadosPessoaisForm

class DadosPessoaisDeleteView(BaseDeleteView):
    model = DadosPessoais
    form = DadosPessoaisForm


# Dados Sociais
class DadosSociaisListView(BaseListView):
    model = DadosSociais
    form = DadosSociaisForm

class DadosSociaisDetailView(BaseDetailView):
    model = DadosSociais
    form = DadosSociaisForm

class DadosSociaisCreateView(BaseCreateView):
    model = DadosSociais
    form = DadosSociaisForm

class DadosSociaisUpdateView(BaseUpdateView):
    model = DadosSociais
    form = DadosSociaisForm

class DadosSociaisDeleteView(BaseDeleteView):
    model = DadosSociais
    form = DadosSociaisForm
