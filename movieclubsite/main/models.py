from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Session(models.Model):
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return "Session" + str(self.pk)

class CategoryPoll(models.Model):
    open_date = models.DateField()
    close_date = models.DateField(null=True, blank=True)
    session = models.OneToOneField(Session, on_delete=models.CASCADE)

    def __str__(self):
        return "Session" + str(self.session.pk) + " poll"

class PollResponses(models.Model):
    category_poll = models.ForeignKey(CategoryPoll, on_delete=models.CASCADE)
    submitter = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    response = models.CharField(max_length=2550)

    def __str__(self):
        return "Poll Response Submitted By " + self.submitter.get_username() + " For Poll " + str(self.category_poll.pk)

class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=2000, null=True, blank=True)
    submitter = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    selected = models.BooleanField(default=False)

    def __str__(self):
        return self.name + " " + self.description
 
class Movie(models.Model):
    name = models.CharField(max_length=255)
    release_year = models.IntegerField(null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    submitter = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    multiplier = models.IntegerField()
    watched = models.BooleanField(default=False)

    def __str__(self):
        return self.name
