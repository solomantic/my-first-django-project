from django.contrib import admin

# Register your models here.
from .models import Question, Choice

class ChoiceInline(admin.TabularInline):
	model = Choice
	extra = 3

class QuestionAdmin(admin.ModelAdmin):
	#fields = ['pub_date', 'question_text']
	fieldsets = [
		('Question', 			{'fields': ['question_text', 'slugfd']}),
		('Date information', 	{'fields': ['pub_date'], 'classes': ['collapse']}),
	]
	inlines = [ChoiceInline]
	list_display = ('question_text', 'pub_date', 'was_published_recently','slugfd')
	list_filter = ['pub_date']
	search_fields = ['question_text']


admin.site.register(Question, QuestionAdmin)