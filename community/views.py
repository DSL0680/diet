from django.urls import reverse
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import PostForm
from django.contrib.auth.decorators import login_required
from django.http import Http404

@login_required
def post_edit(request, id):
    post = get_object_or_404(Post, id=id)

    if post.author != request.user:  # 게시물의 작성자와 현재 사용자가 다른 경우
        raise Http404  # 404 에러를 발생시킴

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save()
            return redirect('view_post', id=id)
    else:
        form = PostForm(instance=post)

    # 취소 버튼을 누르면 이전 게시물 보기 페이지로 돌아갑니다.
    cancel_url = reverse('view_post', args=[id])

    return render(request, 'post_edit.html', {'form': form, 'cancel_url': cancel_url})

@login_required
def post_delete(request, id):
    post = get_object_or_404(Post, id=id)

    if post.author != request.user:  # 게시물의 작성자와 현재 사용자가 다른 경우
        raise Http404  # 404 에러를 발생시킴

    if request.method == 'POST':
        post.delete()
        return redirect('community')
    
    return render(request, 'post_delete.html', {'post': post})


@login_required
def community(request):
    posts = Post.objects.all()
    return render(request, 'community.html', {'posts': posts})

def view_post(request, id):
    post = Post.objects.get(id=id)
    return render(request, 'view_post.html', {'post': post})

def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('community')
    else:
        form = PostForm()
    return render(request, 'create_post.html', {'form': form})


