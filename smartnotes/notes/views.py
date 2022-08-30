from django.shortcuts import render
from .models import Notes
# Create your views here.

def list(request):
    all_notes = Notes.object.all()
    return render(request, 'notes/notes_list.html', {'notes': all_notes})


