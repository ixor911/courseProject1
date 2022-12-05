from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone


class Gender(models.Model):
    name = models.CharField(blank=False, null=False, max_length=20)

    def __str__(self):
        return self.name


class Word(models.Model):
    word = models.CharField(blank=False, null=False, max_length=50)
    translation = models.JSONField()
    publishDate = models.DateTimeField(auto_now_add=True, editable=False, null=False)
    lastRead = models.DateTimeField(null=False)

    def __str__(self):
        return self.word


class WordGroup(models.Model):
    name = models.CharField(blank=False, null=False, max_length=50)
    description = models.TextField(blank=True, null=True)
    words = models.ManyToManyField(Word)

    def __str__(self):
        return self.name


class Result(models.Model):
    word = models.ForeignKey(Word, on_delete=models.SET_NULL, null=True)
    date = models.DateTimeField(auto_now=True, editable=False)

    # 1 - no mistakes
    # 2 - some mistakes
    # 3 - full mistake
    status = models.PositiveSmallIntegerField(editable=False, null=False)


class User(AbstractUser):
    image = models.ImageField(blank=True, null=False, default='/static/defaultUserIcon.png', upload_to='media/')
    place = models.CharField(blank=True, null=True, max_length=50)
    other = models.TextField(blank=True, null=True)

    gender = models.ForeignKey(Gender, on_delete=models.SET_NULL, null=True, blank=True)
    words = models.ManyToManyField(Word)
    wordGroups = models.ManyToManyField(WordGroup)
    results = models.ManyToManyField(Result)

    blocks = models.JSONField(default=dict)
    friends = models.JSONField(default=dict)
    Massages = models.JSONField(default=dict)
    def __str__(self):
        return self.username


class Message(models.Model):
    content = models.TextField(blank=False, null=True)
    date = models.DateTimeField(auto_now_add=True, editable=False, null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    asStory = models.BooleanField(editable=False, null=False, default=False)

    def __str__(self):
        return self.user.name + ": " + self.content


