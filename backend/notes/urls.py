from django.urls import path
from .views import (
    NoteCreateView, 
    NoteDeleteView, 
    NotesDetailView, 
    NoteList, 
    NoteUpdateView
)

app_name = "notes"
urlpatterns = [
    path('', NoteList.as_view(), name='your_model_list'),
    path('create/', NoteCreateView.as_view(), name='your_model_create'),
    path('<int:pk>/update/', NoteUpdateView.as_view(), name='your_model_update'),
    path('<int:pk>/delete/', NoteDeleteView.as_view(), name='your_model_delete'),
    path('<int:pk>/', NotesDetailView.as_view(), name='your_model_detail'),
]
