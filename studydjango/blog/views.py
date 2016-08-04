from django.shortcuts import redirect, render
from blog.forms import CommentModelForm
from .models import Post, Comment

def post_list(request):
    posts=Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts':posts})

def comment_new(request):
    if request.method == 'POST':
        form = CommentModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/post')
    else:
        form = CommentModelForm()
    return render(request, 'blog/comment_form.html', {
        'form': form
        })

def post_detail(request, pk):
    posts = Post.objects.filter(pk=pk)
    comment=Comment.objects.filter(post_id=pk)
    return render(request, 'blog/post_detail.html', {'posts': posts, 'comment': comment})