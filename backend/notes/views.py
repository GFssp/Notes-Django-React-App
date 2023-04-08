from rest_framework.generics import (
    ListAPIView, 
    CreateAPIView, 
    UpdateAPIView,
    DestroyAPIView,
    RetrieveAPIView 
)
from .models import Notes
from .serializers import NotesSerializer

class NoteList(ListAPIView):
    queryset = Notes.objects.all()
    serializer_class = NotesSerializer

class NoteCreateView(CreateAPIView):
    serializer_class = NotesSerializer

class NoteUpdateView(UpdateAPIView):
    queryset = Notes.objects.all()
    serializer_class = NotesSerializer

class NoteDeleteView(DestroyAPIView):
    queryset = Notes.objects.all()
    serializer_class = NotesSerializer
    #http_method_names = ['delete']

class NotesDetailView(RetrieveAPIView):
    queryset = Notes.objects.all()
    serializer_class = NotesSerializer
    