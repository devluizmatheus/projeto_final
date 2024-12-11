from apps.core.views import BaseCreateView, BaseDeleteView, BaseDetailView, BaseListView, BaseUpdateView

from apps.qualificacao_enjoyer.models import QualificacaoAreaInteligencia, QualificacaoExtraPMPB, QualificacaoPessoal, QualificacaoPMPB

from apps.qualificacao_enjoyer.forms import QualificacaoAreaInteligenciaForm, QualificacaoExtraPMPBForm, QualificacaoPMPBForm, QualificacaoPessoalForm


# Qualificação Área de Inteligência
class QualificacaoAreaInteligenciaListView(BaseListView):
    model = QualificacaoAreaInteligencia
    form = QualificacaoAreaInteligenciaForm

class QualificacaoAreaInteligenciaDetailView(BaseDetailView):
    model = QualificacaoAreaInteligencia
    form = QualificacaoAreaInteligenciaForm

class QualificacaoAreaInteligenciaCreateView(BaseCreateView):
    model = QualificacaoAreaInteligencia
    form = QualificacaoAreaInteligenciaForm

class QualificacaoAreaInteligenciaUpdateView(BaseUpdateView):
    model = QualificacaoAreaInteligencia
    form = QualificacaoAreaInteligenciaForm

class QualificacaoAreaInteligenciaDeleteView(BaseDeleteView):
    model = QualificacaoAreaInteligencia
    form = QualificacaoAreaInteligenciaForm


# Qualificação Extra PMPB
class QualificacaoExtraPMPBListView(BaseListView):
    model = QualificacaoExtraPMPB
    form = QualificacaoExtraPMPBForm

class QualificacaoExtraPMPBDetailView(BaseDetailView):
    model = QualificacaoExtraPMPB
    form = QualificacaoExtraPMPBForm

class QualificacaoExtraPMPBCreateView(BaseCreateView):
    model = QualificacaoExtraPMPB
    form = QualificacaoExtraPMPBForm

class QualificacaoExtraPMPBUpdateView(BaseUpdateView):
    model = QualificacaoExtraPMPB
    form = QualificacaoExtraPMPBForm

class QualificacaoExtraPMPBDeleteView(BaseDeleteView):
    model = QualificacaoExtraPMPB
    form = QualificacaoExtraPMPBForm


# Qualificação Pessoal
class QualificacaoPessoalListView(BaseListView):
    model = QualificacaoPessoal
    form = QualificacaoPessoalForm

class QualificacaoPessoalDetailView(BaseDetailView):
    model = QualificacaoPessoal
    form = QualificacaoPessoalForm

class QualificacaoPessoalCreateView(BaseCreateView):
    model = QualificacaoPessoal
    form = QualificacaoPessoalForm

class QualificacaoPessoalUpdateView(BaseUpdateView):
    model = QualificacaoPessoal
    form = QualificacaoPessoalForm

class QualificacaoPessoalDeleteView(BaseDeleteView):
    model = QualificacaoPessoal
    form = QualificacaoPessoalForm


# Qualificação PMPB
class QualificacaoPMPBListView(BaseListView):
    model = QualificacaoPMPB
    form = QualificacaoPMPBForm

class QualificacaoPMPBDetailView(BaseDetailView):
    model = QualificacaoPMPB
