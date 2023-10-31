from django.urls import path

from apip1 import views

urlpatterns = [
    path('Book/',
        views.BookView.as_view()),
    path('Book/<int:pk>', views.BookDetailsView.as_view()),

    path('Author/', views.AuthorView.as_view()),
    path('Author/<int:pk>', views.AuthorDetailsView.as_view()),
    
    path('Worker/', views.W2View.as_view()),
    path('Worker/<int:pk>', views.W1View.as_view()),
    path('Employeeret/<int:pk>', views.EmployeeRetrieve.as_view()),
]