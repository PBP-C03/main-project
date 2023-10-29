from django.urls import include, path
from qna.views import forum, ask_question, add_answer, get_question_data, add_comment
from django.contrib.auth import views as auth_views
from . import views
app_name = 'qna'

urlpatterns = [
    path('forum/', forum, name='forum'),
    path('ask_question/', ask_question, name='ask_question'),
    path('add_answer/<int:question_id>/', add_answer, name='add_answer'),
    path('get_question_data/', get_question_data, name='get_question_data'),
    path('add_comment/<int:questionId>/', add_comment, name='add_comment'),
    path('delete_question/<int:id>/', views.delete_question, name='delete_question'),
    path('question/<int:id>/', views.view_question, name='view_question'),
    path('accounts/', include('django.contrib.auth.urls')),
    # path('question/<int:question_id>/', views.question_detail, name='question_detail'),
]
