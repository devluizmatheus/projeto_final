from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from django.urls import reverse_lazy

from .models import Enjoyer, SelectionEnjoyer, Selection

from .forms import SelectionEnjoyerForm, SelectionForm, EnjoyerForm

# Base View
class BaseListView(ListView):
    template_name = 'base_list_view.html'
    context_object_name = 'objects'

class BaseDetailView(DetailView):
    template_name = 'base_detail_view.html'
    context_object_name = 'object'

class BaseCreateView(CreateView):
    template_name = 'base_create_view.html'
    success_url = reverse_lazy('base_list_view.html')

class BaseUpdateView(UpdateView):
    template_name = 'base_update_view.html'
    success_url = reverse_lazy('base_list_view.html')

class BaseDeleteView(DeleteView):
    template_name = 'base_delete_view.html'
    success_url = reverse_lazy('base_list_view.html')

#Enjoyer View
class EnjoyerListView(BaseListView):
    model = Enjoyer
    form =  EnjoyerForm

class EnjoyerDetailView(BaseDetailView):
    model = Enjoyer
    form = EnjoyerForm

class EnjoyerCreateView(BaseCreateView):
    model = Enjoyer
    form = EnjoyerForm

class EnjoyerUpdateView(BaseUpdateView):
    model = Enjoyer
    form = EnjoyerForm

class EnjoyerDeleteView(BaseDeleteView):
    model = Enjoyer
    form = EnjoyerForm

#Selection View
class SelectionListView(BaseListView):
    model = Selection
    form = SelectionForm

class SelectionDetailView(BaseDetailView):
    model = Selection
    form = SelectionForm

class SelectionCreateView(BaseCreateView):
    model = Selection
    form = SelectionForm

class SelectionUpdateView(BaseUpdateView):
    model = Selection
    form = SelectionForm

class SelectionDeleteView(BaseDeleteView):
    model = Selection
    form = SelectionForm

#SelectionEnjoyer View
class SelectionEnjoyerListView(BaseListView):
    model = SelectionEnjoyer
    form = SelectionEnjoyerForm

class SelectionEnjoyerDetailView(BaseDetailView):
    model = SelectionEnjoyer
    form = SelectionEnjoyerForm

class SelectionEnjoyerCreateView(BaseCreateView):
    model = SelectionEnjoyer
    form = SelectionEnjoyerForm

class SelectionEnjoyerUpdateView(BaseUpdateView):
    model = SelectionEnjoyer
    form = SelectionEnjoyerForm

class SelectionEnjoyerDeleteView(BaseDeleteView):
    model = SelectionEnjoyer
    form = SelectionEnjoyerForm