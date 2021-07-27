"""URL patterns for learning_logs"""

from django.urls import path

from . import views

app_name = 'learning_logs'
urlpatterns = [
    path('', views.index, name='index'), #home page
    path('topics/', views.topics, name='topics'), # page showing all topics
    path('topics/<int:topic_id>/', views.topic, name='topic'), # page for a single topic
]