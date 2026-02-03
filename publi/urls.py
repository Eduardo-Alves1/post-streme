from django.urls import path
from . import views


urlpatterns = [
    path("publicacoes/", views.PubliListCreateView.as_view(), name="publi-list-create"),
    path(
        "publicacoes/<int:pk>/",
        views.PubliDetailRetrieveUpdateDestroyView.as_view(),
        name="publi-detail",
    ),
]
