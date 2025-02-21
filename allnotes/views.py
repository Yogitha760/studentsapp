from django.shortcuts import render, redirect
from .forms import NoteForm
from .models import Note



# View Notes
def view_notes(request):
    notes = Note.objects.all()
    return render(request, 'allnotes/view_notes.html', {'notes': notes})

# Add Note
def add_note(request):
    if request.method == "POST":
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_notes')
    else:
        form = NoteForm()
    return render(request, 'allnotes/add_note.html', {'form': form})