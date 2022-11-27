from django.db import models

class user_data(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

class webhook_data(models.Model):
    time = models.DateTimeField(auto_now_add=False)
    data = models.JSONField()
    user_data = models.ForeignKey(user_data, on_delete=models.CASCADE,null=True,blank=True)
