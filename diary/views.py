from django.shortcuts import render, redirect, get_object_or_404
from .models import Diary
from .forms import DiaryForm
from django.contrib.auth.decorators import login_required


def diary_detail(request, diary_id):
    diary = get_object_or_404(Diary, id=diary_id, user=request.user)
    return render(request, 'diary_detail.html', {'diary': diary})

def diary_update(request, diary_id):
    diary = get_object_or_404(Diary, id=diary_id, user=request.user)
    if request.method == 'POST':
        form = DiaryForm(request.POST, request.FILES ,instance=diary)
        if form.is_valid():
            form.save()
            return redirect('diary_detail', diary_id=diary_id)
    else:
        form = DiaryForm(instance=diary)
    
    return render(request, 'diary_update.html', {'form': form, 'diary': diary})

def diary_delete(request, diary_id):
    diary = get_object_or_404(Diary, id=diary_id, user=request.user)
    if request.method == 'POST':
        diary.delete()
        return redirect('diary_list')
    
    return render(request, 'diary_delete.html', {'diary': diary})

@login_required
def diary_list(request):
    diaries = Diary.objects.filter(user=request.user)
    return render(request, 'diary_list.html', {'diaries': diaries})

def diary_create(request):
    if request.method == 'POST':
        form = DiaryForm(request.POST, request.FILES)
        if form.is_valid():
            diary = form.save(commit=False)
            diary.user = request.user
            diary.save()
            return redirect('diary_list')
    else:
        form = DiaryForm()
    
    return render(request, 'diary_create.html', {'form': form})
