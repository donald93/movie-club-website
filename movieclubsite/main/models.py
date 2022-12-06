from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Session(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()

class CategoryPoll(models.Model):
    open_date = models.DateField()
    close_date = models.DateField()
    session = models.OneToOneField(Session, on_delete=models.CASCADE)

class PollResponses(models.Model):
    category_poll = models.ForeignKey(CategoryPoll, on_delete=models.CASCADE)
    submitter = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    response = models.CharField(max_length=2550)

class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=2000)
    submitter = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    selected = models.BooleanField(default=False)

class Movie(models.Model):
    name = models.CharField(max_length=255)
    release_year = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    submitter = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    multiplier = models.IntegerField()
    watched = models.BooleanField(default=False)


