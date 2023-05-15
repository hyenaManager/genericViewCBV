from django.urls import path
from .views import PublisherListView,PublisherDetailView,BookList,PublisherBookList,api_check

urlpatterns = [
    path("publishers/", PublisherListView.as_view()),
    path("publisherDetail<int:pk>/", PublisherDetailView.as_view()),
    path("bookList/",BookList.as_view()),
    path("book/<publisher>/",PublisherBookList.as_view()),
    path("api_check",api_check),
]