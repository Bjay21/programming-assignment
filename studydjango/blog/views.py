from django.shortcuts import redirect, render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import Http404

from django.utils import timezone
from .forms import CommentForm, CommentModelForm
from .models import Post, Comment
import os
from uuid import uuid4

def post_list(request):
    posts=Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts':posts})

@login_required
def comment_new(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)
    if request.method == 'POST':
        form = CommentModelForm(request.POST, request.FILES)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            messages.success(request, "새 댓글을 저장했습니다.")
            return redirect(post)
    else:
        form = CommentModelForm()
    return render(request, 'blog/comment_form.html', {
        'form': form
        })

def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    comment = Comment.objects.filter(post_id=pk)
    return render(request, 'blog/post_detail.html', {'post': post, 'comment': comment})