from audioop import reverse
import json
from django.shortcuts import render, redirect
from .models import Question, Comment
from django.contrib.auth.decorators import login_required
from .forms import QuestionForm
from book.models import Book
from django.http import HttpResponseRedirect, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.core.serializers import serialize

@csrf_exempt
def forum(request):
    questions = Question.objects.all()
    select = Book.objects.all()
    context = {
        'questions': questions,
        'books' : select
    }
    print(serialize("json", questions))
    return render(request, 'qna.html', context)

@login_required
@csrf_exempt
def ask_question(request):
    if request.method == "POST":
        form = QuestionForm(request.POST or None)
        if form.is_valid():
            product = form.save(commit=False)
            product.user = request.user
            print(product)  
            product.save()
            print(product) 
            return JsonResponse({'result': 'Success!'})
        else:
            print(form.errors)  
            return JsonResponse({'result': 'Fail!', 'errors': form.errors})
    else:
        form = QuestionForm()
        questions = Question.objects.all()
        return render(request, 'qna.html', {'questions': questions, 'form': form})


@login_required
@csrf_exempt
def add_answer(request, question_id):
    if request.method == 'POST':
        content = request.POST.get('content')
        Comment.objects.create(user=request.user, question_id=question_id, content=content)
        return redirect('qna:forum')
    
@csrf_exempt
def get_question_data(request):
    questions = Question.objects.all()
    data = [{'user_name': question.user.username,'question_title': question.title, 'book_name': question.book.title, 'question': question.content} for question in questions]
    return JsonResponse({'questions': data})

@login_required
@csrf_exempt
def add_comment(request, question_id):
    if request.method == 'POST':
        content = request.POST.get('content')
        question = get_object_or_404(Question, pk=question_id)
        Comment.objects.create(user=request.user, comment=question, content=content)
        print(content)
        return JsonResponse({'result': 'Success!'})
    else:
        return JsonResponse({'result': 'Fail!'})


# def question_detail(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     comments = Comment.objects.filter(comment=question)

#     context = {
#         'question': question,
#         'comments': comments,
#     }

#     return render(request, 'question_detail.html', context)


@csrf_exempt
@login_required
def delete_question(request, id):
    question = get_object_or_404(Question, pk=id)
    if request.user == question.user:
        question.delete()
        return JsonResponse({'result': 'Success!'})
    else:
        return JsonResponse({'result': 'Fail!', 'errors': 'You are not the creator of this question.'})

@csrf_exempt
@login_required
def view_question(request, id):
    question = get_object_or_404(Question, pk=id)
    return render(request, 'view_single_question.html', {'question': question})

@login_required
@csrf_exempt
def add_question_json(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            form = QuestionForm(data)
            if form.is_valid():
                question = form.save(commit=False)
                question.user = request.user
                question.save()
                return JsonResponse({'result': 'Success!', 'id': question.id})
            else:
                return JsonResponse({'result': 'Fail!', 'errors': form.errors.as_json()}, status=400)
        except json.JSONDecodeError:
            return JsonResponse({'result': 'Fail!', 'errors': 'Invalid JSON'}, status=400)
    else:
        return JsonResponse({'result': 'Fail!', 'errors': 'Invalid request method'}, status=405)
    
@login_required
@csrf_exempt
def delete_question_json(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            question_id = data.get("id")
            question = get_object_or_404(Question, pk=question_id)

            if request.user == question.user:
                question.delete()
                return JsonResponse({'result': 'Success!', 'message': 'Question deleted'})
            else:
                return JsonResponse({'result': 'Fail!', 'errors': 'You are not the creator of this question'}, status=403)
        except json.JSONDecodeError:
            return JsonResponse({'result': 'Fail!', 'errors': 'Invalid JSON'}, status=400)
        except Question.DoesNotExist:
            return JsonResponse({'result': 'Fail!', 'errors': 'Question not found'}, status=404)
    else:
        return JsonResponse({'result': 'Fail!', 'errors': 'Invalid request method'}, status=405)