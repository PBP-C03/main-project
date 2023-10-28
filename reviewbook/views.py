from django.shortcuts import render, redirect
from django.urls import reverse
from book.models import Book
from reviewbook.models import Review
from reviewbook.forms import ReviewForm
from django.http import HttpResponseNotFound, HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.core import serializers

@login_required(login_url='/login')
def show_review(request, id):
    book = Book.objects.get(pk = id)
    reviews = Review.objects.filter(book = book)
    totalRating = 0
    for r in reviews: 
        totalRating += r.rating
    if len(reviews) > 0:
        average_rating = totalRating / len(reviews)
    else:
        average_rating = 0
    context = {
        'book': book,
        'reviews': reviews,
        'average': average_rating,
    }
    return render(request, "review.html", context)


def get_reviews(request, id):
    book = Book.objects.get(pk = id)
    review = Review.objects.filter(book=book)
    return HttpResponse(serializers.serialize('json', review))

def get_user_review(request, id):
    book = Book.objects.get(pk = id)
    review = Review.objects.filter(user=request.user, book=book)
    return HttpResponse(serializers.serialize('json', review))

def edit_review(request, id, reviewId):
    review = Review.objects.get(pk = reviewId)
    form = ReviewForm(request.POST or None, instance=review)

    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse("reviewbook:show_review"))
    
    context = {'form': form}
    return render(request, "review.html", context)

@csrf_exempt
def add_review(request, id):
    if request.method == 'POST':
        rating = request.POST.get("rating")
        review = request.POST.get("review")
        user = request.user
        book = Book.objects.get(pk = id)

        new_review = Review(rating=rating, review=review, user=user, book=book)
        new_review.save()

        return HttpResponse(b"CREATED", 201)
    return HttpResponseNotFound()

@csrf_exempt
def delete_review(request, id, reviewId):
    if request.method == 'DELETE':
        review = Review.objects.get(pk = reviewId)
        review.delete()
        return HttpResponse(b"DELETED", status=200)
    return HttpResponseNotFound()