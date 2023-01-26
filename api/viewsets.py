# viewsets
from rest_framework import viewsets
from api.serializers import ContatoSerializer
from core.models import Contato


class ContatoViewSet(viewsets.ModelViewSet):
    serializer_class = ContatoSerializer
    queryset = Contato.objects.all()
