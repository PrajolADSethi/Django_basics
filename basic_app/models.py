from django.db import models

# Create your models here.
class Blog(models.Model):
    CHOICES = (
    ('Technology','Technology'),
    ('Enterpreneur','Enterpreneur'),
    ('Marketing' , 'Marketing')
    )
    title= models.CharField(max_length=200)
    date = models.DateField(auto_now_add=True)
    desc = models.CharField(max_length=200)
    category = models.CharField(choices=CHOICES, max_length =200)

    def __str__(self):
        return self.title

class Questions(models.Model):
    question = models.CharField(max_length=200)
    published = models.DateTimeField('date published')

    def __str__(self):
        return self.question


class Choice(models.Model):
    question = models.ForeignKey(Questions,on_delete=models.CASCADE)
    answer= models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.answer


        
