from rest_framework import generics
from .models import Character, Quote 
from .serializers import CharacterSerializer, QuoteSerializer 
from rest_framework import permissions
from .permissions import IsOwnerOrReadOnly



class CharacterList(generics.ListCreateAPIView):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class CharacterDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer
    permission_classes = [IsOwnerOrReadOnly]


class QuoteList(generics.ListCreateAPIView):
    queryset = Quote.objects.all()
    serializer_class = QuoteSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class QuoteDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Quote.objects.all()
    serializer_class = QuoteSerializer
    permission_classes = [IsOwnerOrReadOnly]