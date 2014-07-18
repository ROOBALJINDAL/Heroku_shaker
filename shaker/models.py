from django.db import models

# Create your models here.
class User(models.Model):
    username=models.CharField(max_length=20)
    password=models.CharField(max_length=20)
    highscore=models.BigIntegerField()
    def __str__(self):
        string="Password: " +self.password + "      username: " + self.username + "     Highscores: " + str(self.highscore)
        return string
