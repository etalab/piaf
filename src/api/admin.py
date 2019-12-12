from django.contrib import admin

from .models import Label, Document, Project
from .models import DocumentAnnotation, SequenceAnnotation, Seq2seqAnnotation, Seq2seqAnnotationResponse
from .models import TextClassificationProject, SequenceLabelingProject, Seq2seqProject


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'project_type', 'randomize_document_order')
    ordering = ('project_type',)
    search_fields = ('name',)


# admin.site.register(Project, ProjectAdmin)
