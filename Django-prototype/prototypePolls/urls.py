from django.urls import path

from . import views

app_name = 'prototypePolls'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('plot1/', views.plot1, name='plot1'),
    path('logPlotAll', views.logPlotAll, name='logPlotAll'),
    path('logPlotAll/', views.logPlotAll, name='logPlotAll'),
    path('logPlot/<str:name>', views.logPlot, name='logPlot'),
    path('logPlot/<str:name>/', views.logPlot, name='logPlot')

]
