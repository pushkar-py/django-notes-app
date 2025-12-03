from django.shortcuts import render, redirect

from django.contrib.auth.decorators import login_required


from .models import Note


@login_required
def notes_home(request):
    pinned_notes = Note.objects.filter(user=request.user, is_pinned=True, is_archived=False, is_deleted=False).order_by('-updated_at')
    
    other_notes = Note.objects.filter(user=request.user, is_pinned=False, is_archived=False, is_deleted=False).order_by('-updated_at')

    return render(request, 'notes/home.html', {
        'pinned_notes': pinned_notes,  
        'other_notes' : other_notes
    }) 

@login_required
def create_note(request):
    if request.method == "POST":
        Note.objects.create(
            user=request.user,
            title=request.POST.get('title', ''),
            content=request.POST.get('content', ''),
            color=request.POST.get('color', 'white')
        )
    return redirect('notes_home')    


@login_required
def pin_note(request, id):
    note = Note.objects.get(id=id, user=request.user)
    note.is_pinned = True
    note.save()
    return redirect("notes_home")

@login_required
def unpin_note(request, id):
    note = Note.objects.get(id=id, user=request.user)
    note.is_pinned = False
    note.save()
    return redirect("notes_home")


@login_required
def archive_note(request, id):
    note = Note.objects.get(id=id, user=request.user)
    note.is_archived = True
    note.is_pinned = False
    note.save()
    return redirect("notes_home")


@login_required
def unarchive_note(request, id):
    note = Note.objects.get(id=id, user=request.user)
    note.is_archived = False
    note.save()
    return redirect("notes_home")




@login_required
def delete_note(request, id):
    note = Note.objects.get(id=id, user=request.user)
    note.is_deleted = True
    note.is_pinned = False
    note.is_archived = False
    note.save()
    return redirect("notes_home")

@login_required
def restore_note(request, id):
    note = Note.objects.get(id=id, user=request.user)
    note.is_deleted = False
    note.save()
    return redirect("notes_home")


     
    
    


