from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('title/<int:pk>', views.title_questions, name = 'title_ques'),
    path('title/<int:pk>/new', views.new_ques, name='new_ques'),
    path('title/<int:pk>/ques/<int:ques_pk>', views.show_ans, name = 'show_ans'),
    path('title/<int:pk>/ques/<int:ques_pk>/reply', views.post_ans, name='post_ans'),
]