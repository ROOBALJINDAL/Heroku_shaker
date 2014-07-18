from django.db import models

# Create your models here.
class User(models.Model):
    username=models.CharField(max_length=20)
    password=models.CharField(max_length=20)
    
    #easyscore=models.BigIntegerField(default=20)
    #mediumscore=models.BigIntegerField(default=20)
    #hardscore=models.BigIntegerField(default=20)
    highscore=models.BigIntegerField()
    
    '''def __str__(self):
        string="<br>ID:  " + str(self.id) + "<br>USERNAME:  " + self.username + "<br>PASSWORD: " +self.password
        +"<br>EASY: "+ str(self.easyscore)+"<br>MEDIUM: "+ str(self.mediumscore)
        +"<br>HARD: "+ str(self.hardscore)+"<br>HIGHSCORES: "+ str(self.highscore)
        return string'''
    
    def __str__(self):
        string="<br>ID:  " + str(self.id) + "<br>USERNAME:  " + self.username + "<br>PASSWORD: " +self.password +"<br>HIGHSCORES: "+ str(self.highscore)
        return string
