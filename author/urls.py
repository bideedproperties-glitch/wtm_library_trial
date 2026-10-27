from django.urls import path
from .views import author_view,update_author,delete_author, author_details

urlpatterns = [
    path("display/",author_view,name="display_authors"),
    # path("create-author/",author_entry,name="create_author"),
    path("update-author/<str:author_pk>/",update_author,name="update_author"),
    path("delete-author/<str:author_id>/",delete_author,name="delete_author"),
    path("view-author-details/<str:author_id>/",author_details,name="details"),

]
