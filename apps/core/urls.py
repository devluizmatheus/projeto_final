from django.urls import path

from apps.core.views import (
    EnjoyerListView,
    EnjoyerDetailView,
    EnjoyerCreateView,
    EnjoyerUpdateView,
    EnjoyerDeleteView
)

from apps.core.views import (
    SelectionListView,
    SelectionDetailView,
    SelectionCreateView,
    SelectionUpdateView,
    SelectionDeleteView,
)

from apps.core.views import (
    SelectionEnjoyerListView,
    SelectionEnjoyerDetailView,
    SelectionEnjoyerCreateView,
    SelectionEnjoyerUpdateView,
    SelectionEnjoyerDeleteView
)

#Enjoyer Url
urlpatterns = [
    path("enjoyer_list/", EnjoyerListView.as_view(), name="enjoyer_list"),
    path("enjoyer_detail/", EnjoyerDetailView.as_view(), name="enjoyer_detail"),
    path("enjoyer_create/", EnjoyerCreateView.as_view(), name="enjoyer_"),

]