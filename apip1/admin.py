from django.contrib import admin
from . models import *

# Register your models here.
admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Employee)
admin.site.register(Boss)
admin.site.register(Worker)
admin.site.register(LogEntry)