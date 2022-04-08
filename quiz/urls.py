from django.urls import path
import views

urlpatterns = [
    path('quiz', views.serve_quiz_view),
    path('questions', views.return_questions)
]