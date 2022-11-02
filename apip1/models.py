from django.db import models

# Create your models here.



class Author(models.Model):
    name = models.CharField(max_length=50)
    city = models.CharField(max_length=50)

    # def __str__(self):
    #     return self.name
    
class Book(models.Model):
    title = models.CharField(max_length=50)
    rating = models.IntegerField(null=True, blank=True)
    writer = models.ForeignKey(Author, on_delete=models.CASCADE)   # (Author, related_name='bok', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return '{}-{}'.format(self.title, self.rating)


