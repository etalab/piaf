from django.contrib import admin

from .models import Article, ParagraphBatch, Paragraph
from .models import Question, Answer


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('name',)
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
    list_display = ('paragraph', 'text', 'created_at',)
    ordering = ('text',)


class AnswerAdmin(admin.ModelAdmin):
    list_display = ('user', 'question', 'text')
    ordering = ('question',)
    search_fields = ('question',)


admin.site.register(Article, ArticleAdmin)
admin.site.register(ParagraphBatch, ParagraphBatchAdmin)
admin.site.register(Paragraph, ParagraphAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)
