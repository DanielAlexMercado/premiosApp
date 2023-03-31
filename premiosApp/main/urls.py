from django.urls import path

from . import views


app_name = 'main'
urlpatterns = [
    #example: /main/
    path('', views.IndexView.as_view(), name='index'),
    #example: /main/id/
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    #example: /main/id/results
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    #example: /main/id/vote
    path('<int:question_id>/vote/', views.vote, name='vote'),
]