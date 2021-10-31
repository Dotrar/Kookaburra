from django.urls import path
from .views import SectionView, PostView, GeneralView

urlpatterns = [
    path("", GeneralView.as_view()),
    path("<slug:slug>", SectionView.as_view(), name="section-detail"),
    path("post/<int:pk>", PostView.as_view(), name="post-detail"),
]
