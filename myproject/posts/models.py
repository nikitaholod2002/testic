from django.db import models
from authorization.models import User

class Post (models.Model):
    name = models.CharField(max_length=100)
    full_text = models.TextField()
    like= models.IntegerField(default=0)
    user_email = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Comment (models.Model):
    text = models.TextField()
    user_email = models.ForeignKey(User, on_delete=models.CASCADE)
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return self.text