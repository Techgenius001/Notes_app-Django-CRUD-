from django.shortcuts import render, redirect, get_object_or_404
from .models import Note

# READ - list all notes
def note_list(request):
    notes = Note.objects.all()
    return render(request, 'notes/note_list.html', {'notes': notes})

# CREATE a note
def note_create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        Note.objects.create(title=title, content=content)
        return redirect('note_list')
    return render(request, 'notes/note_form.html')


# UPDATE a note
def note_update(request, id):
    note = get_object_or_404(Note, id=id)
    if request.method == 'POST':
        note.title = request.POST.get('title')
        note.content = request.POST.get('content')
        note.save()
        return redirect('note_list')
    return render(request, 'notes/note_form.html', {'note': note})


# DELETE a note
def note_delete(request, id):
    note = get_object_or_404(Note, id=id)
    if request.method == 'POST':
        note.delete()
        return redirect('note_list')
    return render(request, 'notes/note_delete.html', {'note': note})