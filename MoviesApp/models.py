from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.username
    
class FavMovies(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE,null=False,blank=False,related_name="user_id")
    movie_id = models.IntegerField()
    movie_title = models.CharField(max_length=250)

    def __str__(self):
        return self.movie_titles
