import re
import os
import uuid
from django.db import models
from django.core.files import File
from django.db.models.signals import pre_save
from django.forms import ValidationError
from django.utils import timezone
from .validators import MinLengthValidatior, lnglat_validator, ZipCodeValidator
from django.core.urlresolvers import reverse
from studydjango import thumbnail

def myupload_to(instance, filename):
    extension = os.path.splitext(filename)[-1]
    name = uuid.uuid4().hex
    return os.path.join(name[:3], name[3:6], name[6:] + extension)

class Post(models.Model):
    author = models.CharField(max_length=20)
    title = models.CharField(max_length=100,
            validators=[MinLengthValidatior(4)],
            verbose_name='제목')
    content = models.TextField(help_text='Markdown 문법을 써주세요.',
            validators=[MinLengthValidatior(10)])
    photo = models.ImageField(upload_to = myupload_to)
    # tags = models.CharField(max_length=100, blank=True)
    tag_set = models.ManyToManyField('Tag', blank=True)
    lnglat = models.CharField(max_length=50, validators=[lnglat_validator], help_text='경도,위도 포맷으로 입력')
    created_at = models.DateTimeField(default=timezone.now)
    text_field = models.IntegerField(default=10)
    post_code = models.CharField(max_length=6, validators=[ZipCodeValidator(True)])

    def __str__(self):
        return self.author+' - ' + self.title
    def get_absolute_url(self):
        return reverse('blog:post_detail', args=[self.pk])

def on_pre_save(sender, **kwargs):
    post = kwargs['instance']
    if post.photo:
        max_size = 300
        if post.photo.width > max_size or post.photo.height > max_size:
            processed_file = thumbnail(post.photo.file, max_size, max_size, 80)
            post.photo.save(post.photo.name, File(processed_file))

pre_save.connect(on_pre_save, sender=Post)

class Comment(models.Model):
    post = models.ForeignKey(Post)
    author = models.CharField(max_length=20)
    message = models.TextField()
    image = models.ImageField(blank=True, upload_to='image/')

#pre_save.connect(on_pre_save, sender=Comment)
    # def on_pre_save(sender, **kwargs):
    #     post = kwargs['instance']
    #     if post.photo:
    #         max_size = 300
    #         if post.photo.width > max_size or post.photo.height > max_size:
    #             processed_file = thumbnail(post.photo.file, max_size, max_size, 80)
    #             post.photo.save(post.photo.name, File(processed_file))
    #image = models.ImageField(upload_to = myupload_to, blank=True)

class Tag(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name