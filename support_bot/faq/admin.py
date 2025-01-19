from django.contrib import admin
from .models import FAQ, SuggestedFAQ, UnmatchedQuestion

@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ('question', 'answer')

@admin.register(UnmatchedQuestion)
class UnmatchedQuestionAdmin(admin.ModelAdmin):
    list_display = ('question', 'created_at')

@admin.register(SuggestedFAQ)
class SuggestedFAQAdmin(admin.ModelAdmin):
    list_display = ('question', 'answer', 'created_at', 'is_approved')
    list_filter = ('is_approved',)
    actions = ['approve_selected', 'reject_selected']

    def approve_selected(self, request, queryset):
        queryset.update(is_approved=True)
    approve_selected.short_description = "Approve selected suggested FAQs"

    def reject_selected(self, request, queryset):
        queryset.update(is_approved=False)
    reject_selected.short_description = "Reject selected suggested FAQs"