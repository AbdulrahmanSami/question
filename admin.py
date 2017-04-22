from django.contrib import admin
from .models import Question,QuestionSession
# Register your models here.
class QuestionAdmin(admin.ModelAdmin):
    fields = ['question_text','question_session']
admin.site.register(Question,QuestionAdmin)
class QustionSessionAdmin(admin.ModelAdmin):
    fields = ['title']
admin.site.register(QuestionSession,QustionSessionAdmin)