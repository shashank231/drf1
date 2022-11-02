from django.urls import path

from apip1 import views

urlpatterns = [
    path('Book/',
        views.BookView.as_view()),
    path('Book/<int:pk>', views.BookDetailsView.as_view()),

    path('Author/', views.AuthorView.as_view()),
    path('Author/<int:pk>', views.AuthorDetailsView.as_view())
]