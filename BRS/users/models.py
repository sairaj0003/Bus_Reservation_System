from django.db import models

# Models
class Users(models.Model):
    user_id = models.AutoField(primary_key = True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "User Profiles"

    def __str__(self):
        return self.email