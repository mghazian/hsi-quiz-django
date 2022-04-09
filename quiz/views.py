import json
import random
import os
from django.http import HttpResponse
from django.shortcuts import render

def __read_questions():
    questions = []
    with open(os.path.dirname(__file__) + '/data/questions.json', 'r') as file:
        quiz_json = json.load(file)
        for i in range(len(quiz_json['questions'])):
            item = quiz_json['questions'][i]

            choices = list(map(
                lambda j: {
                    "content": item['choices'][j],
                    "is_correct": int(j == item['answer'])
                },
                range(len(item['choices']))
            ))

            questions.append({
                "query": item['query'],
                "choice": choices
            })
    
    return questions

def __enumerate(array):
    for i in range(len(array)):
        array[i]['no'] = i + 1

    return array

# Create your views here.
def serve_quiz_view(request):
    questions = random.sample(__read_questions(), 2)
    for item in questions:
        random.shuffle(item['choice'])
        item['choice'] = __enumerate(item['choice'])
    
    random.shuffle(questions)
    questions = __enumerate(questions)

    return render(request, "quiz.html", { "question": questions })

def serve_admin_view(request):
    questions = __enumerate(__read_questions())
    for item in questions:
        item['choice'] = __enumerate(item['choice'])
    
    return render(request, "admin.html", { "questions": questions })