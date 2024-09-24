from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Choice , Questions,User
from .form import QuestionsForm,ChoiceForm,UserForm
# Create your views here.

def index(request):
    data = Choice.objects.all()
    return render(request,"home.html",{"choicedata":data})     


def delete_question(request,question_id):
    que = Questions.objects.get(id = question_id)
    que.delete()
    return redirect("index")

def create_questions(request):
    form = QuestionsForm()
    if request.method == "POST":
        text = form.cleaned_data["question_text"]
        question = Questions()
        question.question_text = text
        question.save()
        return redirect("createChoice")
        
    return render(request, "create.html",{"emptyform":form})

def create_options(request):
   
    if request.method == "POST":
        form = ChoiceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = ChoiceForm()
    return render(request, "choice.html",{"form":form})

def create_UserForm(request):

    form= UserForm()
    

    if request.method == "POST":
       form = UserForm(request.POST)
       if form.is_valid():
           form.save()
           return HttpResponse("The data is saved")
       
    return render(request,"createform.html",{"form":form})

    
def userForm(request):
    data = User.objects.all()
    return render(request,"UserForm.html",{"userdata":data})     

def delete_userform(request,userid):
    username = User.objects.get(id=userid)
    username.delete()
    return redirect("user_form")

def update_userform(request,userid):
    value = User.objects.get(id=userid)
    value.update()
    return redirect("user_form")  




