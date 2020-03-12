from django.contrib import admin

from .models import Article, ParagraphBatch, Paragraph
from .models import Question, Answer


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('name', 'theme', 'audience')
    ordering = ('name',)
    search_fields = ('name',)


class ParagraphBatchAdmin(admin.ModelAdmin):
    list_display = ('user', 'participated_at', 'status')
    ordering = ('status',)
    search_fields = ('status',)


class ParagraphAdmin(admin.ModelAdmin):
    list_display = ('article', 'batch', 'text', 'status')
    ordering = ('article',)
    search_fields = ('name',)


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('paragraph', 'text', 'created_at', 'status', 'report_count')
    ordering = ('created_at', 'report_count')


class AnswerAdmin(admin.ModelAdmin):
    list_display = ('user', 'question_text', 'text', 'created_at',)
    ordering = ('created_at', 'user')
    search_fields = ('text', 'user__email', 'user__first_name', 'user__last_name', 'user__username')

    def question_text(self, obj):
        return obj.question.text
    question_text.short_description = 'Question'


admin.site.register(Article, ArticleAdmin)
admin.site.register(ParagraphBatch, ParagraphBatchAdmin)
admin.site.register(Paragraph, ParagraphAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)
