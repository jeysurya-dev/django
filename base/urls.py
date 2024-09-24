from . import views
from django.urls import path

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:question_id>/", views.delete_question, name="delete"),
    path("createQuestion/", views.create_questions, name="create"),
    path("createchoice/", views.create_options, name="createChoice"),
    path("createUserForm/",views.create_UserForm,name="createUserForm"),
    path('userform/', views.userForm, name="user_form"),
    path("user/<int:userid>/",views.delete_userform,name="deleteuserid"),
    path("user/<int:userid>/",views.update_userform,name="updateid"),
]
