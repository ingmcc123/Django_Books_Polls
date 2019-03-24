from django.contrib import admin
from polls.models import Question, Choice

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        ('질문하기', {'fields': ['question_text']}),
        ('작성시간', {'fields': ['pub_date']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date')
    search_fields = ['question_text']

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
