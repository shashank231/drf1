from django.db import models

# class MyCustomManager(models.Manager):
    
#     def create(self, **kwargs):
#         obj = super().create(**kwargs)
#         self.log_changes('created', obj)
#         return obj
    
#     def update(self, obj, **kwargs):
#         obj = super().update(obj, **kwargs)
#         self.log_changes('updated', obj)
#         return obj
    
#     def delete(self, obj):
#         super().delete(obj)
#         self.log_changes('deleted', obj)
        
#     def log_changes(self, action, obj):
#         model_name = self.model.__name__
#         instance_id = obj.id
#         log_entry = LogEntry(action=action, model=model_name, instance_id=instance_id)
#         log_entry.save()


class LogEntry(models.Model):
    action = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    instance_id = models.PositiveIntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)


class Author(models.Model):
    name = models.CharField(max_length=50)
    city = models.CharField(max_length=50)

    # objects = MyCustomManager()

    def __str__(self):
        return self.name
    
class Book(models.Model):
    title = models.CharField(max_length=50)
    rating = models.IntegerField(null=True, blank=True)
    writer = models.ForeignKey(Author, on_delete=models.CASCADE)   # (Author, related_name='bok', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return '{}-{}'.format(self.title, self.rating)


class Employee(models.Model):
    name = models.CharField(max_length=20)
    age = models.CharField(max_length=3)
    salary_class = models.CharField(max_length=1, choices=(
        ('l', 'low'), ('m', 'medium'), ('h', 'high')
    ), default='l')


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


