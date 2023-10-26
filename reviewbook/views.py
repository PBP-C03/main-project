from django.shortcuts import render, redirect
from book.models import Book
from reviewbook.models import Review
from reviewbook.forms import ReviewForm
from django.http import HttpResponseNotFound, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

@login_required(login_url='/login')
def show_main(request, id):
    book = Book.objects.get(pk = id)
    reviews = Review.objects.filter(book = book)
    review = Review.objects.get(user=request.user)
    context: {
        'book': book,
        'reviews': reviews,
        'review': review,
    }

    return render(request, "main.html", context)

@csrf_exempt
def add_review_ajax(request):
    if request.method == 'POST':
        rating = request.POST.get("rating")
        review = request.POST.get("review")
        user = request.user

        new_review = Review(rating=rating, review=review, user=user)
        new_review.save()

        return HttpResponse(b"CREATED", 201)
    return HttpResponseNotFound()

@csrf_exempt
def delete_review_ajax(request, id):
    if request.method == 'DELETE':
        review = Review.objects.get(pk = id)
        review.delete()
        return HttpResponse(b"DELETED", status=200)
    return HttpResponseNotFound()