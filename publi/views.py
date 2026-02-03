from rest_framework import generics
from .models import PubliModel
from publi.publiSerializer import PubliSerializer


class PubliListCreateView(generics.ListCreateAPIView):
    # Lists all posts (newest first) and allows creating a new post.
    queryset = PubliModel.objects.all().order_by("-criado_em")
    serializer_class = PubliSerializer

class PubliDetailRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    # Retrieves, updates, or deletes a single post by id.
    queryset = PubliModel.objects.all()
    serializer_class = PubliSerializer
