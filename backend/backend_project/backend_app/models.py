from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(null=True, unique=True)
    password = models.CharField(null=True)
    # token = token.CharField(null=True)

    def __str__(self):
        return self.username


class Url(models.Model):
    title = models.CharField(null=True)
    long_url = models.CharField(null=True)
    short_url = models.CharField(null=True)

    user_id = models.ForeignKey(User, on_delete=models.CASCADE, to_field='username')


    def __str__(self):
        return self.title

