#-*- coding: utf-8  -*-
from __future__ import unicode_literals
from  django.core.urlresolvers import reverse
from django.db import models

# Create your models here.

class QuestionSession(models.Model):
    title = models.CharField(max_length=100)
    def __str__(self):
        return self.title
class Question (models.Model):
    question_session = models.ForeignKey(QuestionSession, on_delete=models.CASCADE)
    question_text = models.TextField()
    submission_date = models.DateTimeField (auto_now_add=True,verbose_name="وقت الاضافة")

