from django.db import models

# Create your models here.

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    dob = models.DateField(blank=True, null=True)
    # profile_pic = models.ImageField()

    def __str__(self):
        self.full_name = self.first_name+' '+self.last_name
        return self.full_name


class Blog(models.Model):

    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


