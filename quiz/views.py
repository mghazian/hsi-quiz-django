from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def serve_quiz_view(request):
    return render(request, 'quiz')

def return_questions(request):
    return HttpResponse()