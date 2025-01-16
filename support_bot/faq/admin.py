from django.contrib import admin
from .models import FAQ, UnmatchedQuestion

@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ('question', 'answer')

@admin.register(UnmatchedQuestion)
class UnmatchedQuestionAdmin(admin.ModelAdmin):
    list_display = ('question', 'created_at')