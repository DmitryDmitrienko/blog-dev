from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

import datetime
from transliterate import slugify

class Menu(models.Model):
    link = models.CharField(max_length = 500)
    name = models.CharField(max_length = 200)
    sub_menu = models.ForeignKey("Menu", blank = True, null = True)

    def __str__(self):
        return self.name

class Сategory(models.Model):
    name = models.CharField(max_length = 200)
    symbol_code = models.CharField(max_length = 200)

    def save(self, *args, **kwargs):
        if not self.pk:
            self.symbol_code = slugify(self.name)
        super(Сategory, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

class Project(models.Model):
    name = models.CharField(max_length = 200)
    symbol_code = models.CharField(max_length = 200)
    anons = models.TextField()
    detail = models.TextField()
    date = models.DateTimeField('date published')
    author = models.ForeignKey(User)
    category = models.ForeignKey(Сategory)
    website = models.CharField(max_length = 100)
    other_project = models.ForeignKey("Project")
    on_main = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if not self.pk:
            self.symbol_code = slugify(self.name)
        super(Project, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

class PreInform(models.Model):
    icon = models.CharField(max_length = 50)
    name = models.CharField(max_length = 100)
    text = models.TextField()
    link = models.CharField(max_length = 200)

    def __str__(self):
        return self.name

class Clients(models.Model):
    name = models.CharField(max_length = 100)
    pic = models.ImageField(upload_to = 'clint_folder/')

    def __str__(self):
        return self.name

class Social(models.Model):
    name = models.CharField(max_length = 100)
    icon = models.CharField(max_length = 100)
    link = models.CharField(max_length = 100)

    def __str__(self):
        return self.name

class Contact(models.Model):
    name = models.CharField(max_length = 100)
    email = models.EmailField(max_length = 254)
    subject = models.CharField(max_length = 200)
    message = models.TextField()

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length = 50)
    symbol_code = models.CharField(max_length = 50)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.pk:
            self.symbol_code = slugify(self.name)
        super(Tag, self).save(*args, **kwargs)

class Post(models.Model):
    name = models.CharField(max_length = 200)
    symbol_code = models.CharField(max_length = 200)
    date = models.DateTimeField('date post')
    anons = models.TextField()
    detail = models.TextField()
    tasg = models.ForeignKey(Tag)
    category = models.ForeignKey(Сategory)
    related_post = models.ForeignKey("Post")

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.pk:
            self.symbol_code = slugify(self.name)
        super(Post, self).save(*args, **kwargs)
