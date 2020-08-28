from django.db import models


from board.models import Post

# Create your models here.
class MyPlace(models.Model):

    content = models.ForeignKey(Post,
                            on_delete=models.CASCADE,
                            null=True)

    def __str__(self):
        return self.place