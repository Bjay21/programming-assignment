from django.shortcuts import redirect, render, get_object_or_404
from django.utils import timezone
from .forms import CommentForm
from .models import Post, Comment
import os
from uuid import uuid4

def post_list(request):
    posts=Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts':posts})

def comment_new(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)
    if request.method == 'POST':
        form = CommentForm(request.POST, request.FILES)
        if form.is_valid():
            comment = form.save(False, post_pk)
            #comment.image = request.FILES['image']
            comment.save()
            return redirect('blog:post_detail', post_pk)
    else:
        form = CommentForm()
    return render(request, 'blog/comment_form.html', {
        'form': form
        })

def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    comment = Comment.objects.filter(post_id=pk)
    return render(request, 'blog/post_detail.html', {'post': post, 'comment': comment})