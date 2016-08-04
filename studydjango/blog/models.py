import re
from django.db import models
from django.forms import ValidationError
from django.utils import timezone
from .validators import MinLengthValidatior, lnglat_validator, ZipCodeValidator

class Post(models.Model):
    author = models.CharField(max_length=20)
    title = models.CharField(max_length=100,
            validators=[MinLengthValidatior(4)],
            verbose_name='제목')
    content = models.TextField(help_text='Markdown 문법을 써주세요.',
            validators=[MinLengthValidatior(10)])
    # tags = models.CharField(max_length=100, blank=True)
    tag_set = models.ManyToManyField('Tag', blank=True)
    lnglat = models.CharField(max_length=50, validators=[lnglat_validator], help_text='경도,위도 포맷으로 입력')
    created_at = models.DateTimeField(default=timezone.now)
    text_field = models.IntegerField(default=10)
    post_code = models.CharField(max_length=6, validators=[ZipCodeValidator(True)])
    def __str__(self):
        return self.author+' - ' + self.title

class Comment(models.Model):
    post = models.ForeignKey(Post)
    author = models.CharField(max_length=20)
    message = models.TextField()




class Tag(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name