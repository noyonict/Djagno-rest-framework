from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Question(models.Model):
    title = models.TextField()
    status = models.CharField(default='inactive', max_length=10)
    create_by = models.ForeignKey(User, on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    # @property
    # def choices(self):
    #     return self.choice_set.all()


class Choice(models.Model):
    question = models.ForeignKey('mcq.Question', on_delete=models.CASCADE)
    text = models.CharField(max_length=40)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.text

    # @property
    # def choice(self):
    #     return self.choice_set.all()
