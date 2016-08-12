from django import forms
from blog.models import Comment, Post, myupload_to
from django.db import models

class CommentModelForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['message','image']

class UploadFieldForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()

class CommentForm(forms.Form):
    #post = models.ForeignKey(Post)
    message = forms.CharField(widget=forms.Textarea, label="message", max_length=100)
    author = forms.CharField(label="author", max_length=10)
    image = forms.ImageField(label="image", required=False)
    def save(self, commit, Post_pk):
        comment = Comment(message=self.cleaned_data['message'], author=self.cleaned_data['author'], image=self.cleaned_data['image'])
        #이게 무슨 뜻인지?,
        comment.post_id = Post_pk
        if commit:
            comment.save()
        return comment
        #     def on_pre_save(sender, **kwargs):
        # post = kwargs['instance']
        # if post.photo:
        #     max_size = 300
        #     if post.photo.width > max_size or post.photo.height > max_size:
        #         processed_file = thumbnail(post.photo.file, max_size, max_size, 80)
        #         post.photo.save(post.photo.name, File(processed_file))
        # return comment
