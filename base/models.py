from django.db import models
from django.utils import timezone
# Create your models here.
class Questions(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField(default= timezone.now)

    def __str__(self) -> str:
        return str(self.question_text)   
    
    # def was_published_recently(self):
    #     return self.pub_date >= timezone.now - datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Questions, on_delete=models.CASCADE)
    choice_text= models.CharField(max_length=100)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
    
class User(models.Model):
    name = models.CharField(max_length=100)
    email_id = models.CharField(max_length=100)
    phone_no = models.IntegerField()           


      
    

