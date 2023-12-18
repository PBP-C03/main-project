import json
from django.shortcuts import get_object_or_404, render
from book.models import Book
from reviewbook.models import Review
from reviewbook.forms import ReviewForm, EditReviewForm
from django.http import HttpResponseNotFound, HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.core import serializers

@login_required(login_url='/login')
def show_review(request, id):
    book = Book.objects.get(pk = id)
    reviews = Review.objects.filter(book = book)
    form = ReviewForm()
    editForm = EditReviewForm()
    totalRating = 0
    for r in reviews: 
        totalRating += r.rating
    if len(reviews) > 0:
        average_rating = totalRating / len(reviews)
    else:
        average_rating = 0
    try:
        review = get_object_or_404(Review, book=book, user=request.user)
        context = {
        'book': book,
        'reviews': reviews,
        'review': review,
        'average': average_rating,
        'form': form,
        'editForm': editForm,
        }
    except:
        context = {
            'book': book,
            'reviews': reviews,
            'average': average_rating,
            'form': form,
            'editForm': editForm,
        }
    return render(request, "review.html", context)


def get_reviews(request, id):
    book = Book.objects.get(pk = id)
    review = Review.objects.filter(book=book)
    return HttpResponse(serializers.serialize('json', review))

def get_reviews_rating(request, id, rating):
    book = Book.objects.get(pk=id)
    review = Review.objects.filter(book=book, rating=rating)
    return HttpResponse(serializers.serialize('json', review))

def get_user_review(request, id):
    book = Book.objects.get(pk = id)
    review = Review.objects.filter(user=request.user, book=book)
    return HttpResponse(serializers.serialize('json', review))

def edit_review(request, id, reviewId):
    review = get_object_or_404(Review, pk = reviewId)
    if request.method == "POST":
        form = EditReviewForm(request.POST or None, instance=review)
        if form.is_valid():
            review = form.save(commit=False)
            review.save()
            return HttpResponse(b"UPDATED", status=200)
    else:
        form = EditReviewForm(instance=review)

@csrf_exempt
def add_review(request, id):
    if request.method == 'POST':
        rating = request.POST.get("rating")
        review = request.POST.get("review")
        user = request.user
        username = request.user.username
        book = Book.objects.get(pk = id)

        new_review = Review(rating=rating, review=review, user=user, username=username, book=book)
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

def create_review_flutter(request, id):
    if request.method == 'POST':
        data = json.loads(request.body)

        new_review = Review.objects.create(
            user = request.user,
            username = request.user.username,
            rating = int(data["rating"]),
            review = data["review"],
            book = Book.objects.get(pk = id)
        )

        new_review.save()

        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)