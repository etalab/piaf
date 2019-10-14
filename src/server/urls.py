from django.urls import path

from .views import ProjectView, DatasetView, DataUpload, LabelView, StatsView, GuidelineView
from .views import ProjectsView, DataDownload

urlpatterns = [
    path('projects/', ProjectsView.as_view(), name='projects'),
    path('projects/<int:project_id>/docs/download',
         DataDownload.as_view(), name='download'),
    path('projects/<int:project_id>/',
         ProjectView.as_view(), name='annotation'),
    path('projects/<int:project_id>/docs/',
         DatasetView.as_view(), name='dataset'),
    path('projects/<int:project_id>/docs/create',
         DataUpload.as_view(), name='upload'),
    path('projects/<int:project_id>/labels/',
         LabelView.as_view(), name='label-management'),
    path('projects/<int:project_id>/stats/',
         StatsView.as_view(), name='stats'),
    path('projects/<int:project_id>/guideline/',
         GuidelineView.as_view(), name='guideline')
]
