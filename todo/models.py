from django.db import models

CHOICE = (('danger','high'),('warning','normal'),('primary','low'))

class TodoModel(models.Model):
    title = models.CharField(max_length=100)
    contents = models.TextField()
    priority = models.CharField(
        max_length=50,
        choices = CHOICE,
        null = True
    )
    duedate = models.DateField()

#管理画面のobjectをタイトルと一致して表示
    def __str__(self):
        return self.title

