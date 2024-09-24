from django import forms
from .models import Questions, Choice, User

class QuestionsForm(forms.Form):
    question_text = forms.CharField(max_length=200)


class ChoiceForm(forms.ModelForm):
    question = forms.ModelChoiceField(queryset= Questions.objects.all(), label="Select Question")

    class Meta:
        model = Choice
        fields = ["question","choice_text","votes"]

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = "__all__"
