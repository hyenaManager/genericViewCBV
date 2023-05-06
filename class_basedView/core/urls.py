from django.urls import path
from .views import PublisherListView,PublisherDetailView,BookList

urlpatterns = [
    path("publishers/", PublisherListView.as_view()),
    path("publisherDetail<int:pk>/", PublisherDetailView.as_view()),
    path("bookList/",BookList.as_view()),
]