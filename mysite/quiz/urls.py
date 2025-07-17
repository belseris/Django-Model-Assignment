from django.urls import path
from . import views

urlpatterns = [
    path('quiz/question/', views.get_question, name="get_question"),
    path('quiz/question/create/', views.create_question, name='create_question')
]
