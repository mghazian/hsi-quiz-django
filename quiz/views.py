import json
import random
import os
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def serve_quiz_view(request):
    
    def x(no, answer_index, content):
        return {
            "no": no,
            "content": content,
            "is_correct": answer_index == no
        }

    questions = []

    with open(os.path.dirname(__file__) + '/data/questions.json', 'r') as file:
        quiz_json = json.load(file)
        questions = []
        sample = random.sample(quiz_json['questions'], 2)
        for i in range(len(sample)):
            item = sample[i]

            choices = list(map(
                lambda j: {
                    "content": item['choices'][j],
                    "is_correct": int(j == item['answer'])
                },
                range(len(item['choices']))
            ))

            random.shuffle(choices)
            
            for j in range(len(choices)):
                choices[j]['no'] = j + 1

            questions.append({
                "no": i + 1,
                "query": item['query'],
                "choice": choices
            })

    return render(request, "quiz.html", { "question": questions })

def return_questions(request):
    return HttpResponse()