from rest_framework import generics, status
from .models import PubliModel
from publi.publiSerializer import PubliSerializer
from rest_framework.status import HTTP_201_CREATED


class PubliListCreateView(generics.ListCreateAPIView):
    # Lists all posts (newest first) and allows creating a new post.
    queryset = PubliModel.objects.all().order_by("-criado_em")
    serializer_class = PubliSerializer


class PubliRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    # Retrieves, updates, or deletes a single post by id.
    queryset = PubliModel.objects.all()
    serializer_class = PubliSerializer
