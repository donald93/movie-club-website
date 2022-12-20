from django.contrib import admin

from .models import *

# Register your models here.

admin.site.register(Session)
admin.site.register(CategoryPoll)
admin.site.register(PollResponses)
admin.site.register(Category)
admin.site.register(Movie)