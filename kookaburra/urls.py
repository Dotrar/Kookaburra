from django.urls import path
from .views import SectionView, PostView, GeneralView, CreateNewPostView

urlpatterns = [
    path("", GeneralView.as_view(), name="general-view"),
    path("<slug:slug>", SectionView.as_view(), name="section-detail"),
    path("post/<int:pk>", PostView.as_view(), name="post-detail"),
    path("new/<slug:slug>", CreateNewPostView.as_view(), name="new-post-view"),
]
