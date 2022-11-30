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


class Employee(models.Model):
    name = models.CharField(max_length=20)
    age = models.CharField(max_length=3)


class Boss(models.Model):
    name = models.CharField(max_length=20)
    age = models.CharField(max_length=3)
    department = models.CharField(max_length=20)
    salary = models.CharField(max_length=8)
    favemp = models.ForeignKey(Employee, on_delete=models.CASCADE)


class Worker(models.Model):
    name = models.CharField(max_length=20)
    age = models.CharField(max_length=3)
    in_dept = models.CharField(max_length=20)
    salary = models.CharField(max_length=7)
    boss = models.ForeignKey(Boss, null=True, blank=True, on_delete=models.CASCADE)


