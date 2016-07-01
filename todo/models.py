from __future__ import unicode_literals

from django.db import models


# Create your models here.



class Todo(models.Model):
    task = models.CharField(max_length=300, blank=False, null=False)
    done = models.BooleanField(default=False)
    date_created  = models.DateTimeField(auto_now_add=True)
    description  = models.CharField(max_length=300, blank=True, null=True)



    def get_update_url(self):
        return 'todo_create', [self.pk]


