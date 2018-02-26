from django.db import models
from django.utils import timezone
# Create your models here.
from datetime import datetime

class Artical(models.Model):
    title=models.CharField(max_length=200)
    author=models.CharField(max_length=20)
    post_date=models.DateTimeField(default=timezone.now)
    content=models.TextField()
    category=models.CharField(max_length=100)
    describe=models.TextField()
    count=models.IntegerField(default=0)
    class Meta:
        ordering=('-post_date',)
    def __unicode__(self):
        return self.title

class Say(models.Model):
    content=models.TextField()
    post_date = models.DateTimeField(default=timezone.now)
    class Meta:
        ordering=('-post_date',)
    def __unicode__(self):
        return self.title

class Riji(models.Model):
    content=models.TextField()
    post_date = models.DateTimeField(default=timezone.now)
    img = models.ImageField(max_length=100, upload_to="image", default=u"image/default.png", verbose_name=u'头像')
    class Meta:
        ordering = ('-post_date',)

    def __unicode__(self):
        return self.title
class Xc(models.Model):
    img = models.ImageField(max_length=100, upload_to="img", default=u"img/default.png", verbose_name=u'相册')
    miaoshu=models.TextField()
    post_date = models.DateTimeField(default=timezone.now)
    height=models.IntegerField(default=200)
    class Meta:
        ordering = ('-post_date',)

    def __unicode__(self):
        return self.title