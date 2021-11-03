from django.urls import path
from .views import (
    SectionView,
    PostView,
    GeneralView,
    CreateNewPostView,
    CreateNewSectionView,
    CommentOnPostView,
)

urlpatterns = [
    path("", GeneralView.as_view(), name="general-view"),
    path("<slug:slug>", SectionView.as_view(), name="section-detail"),
    path("new/<slug:slug>", CreateNewPostView.as_view(), name="new-post-view"),
    path("section/", CreateNewSectionView.as_view(), name="new-section-view"),
    # Relating to Posts and  Comments:
    path("new/", CreateNewPostView.as_view(), name="new-post-view"),
    path("post/<int:pk>", PostView.as_view(), name="post-detail"),
    path("post/<int:pk>/comment", CommentOnPostView.as_view(), name="post-comment"),
]
