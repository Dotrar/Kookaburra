from django.shortcuts import render

from django.views import generic as django_generic
from django.views.generic import edit as django_edit
from .models import KookaburraPost, KookaburraSection, KookaburraComment
from . import forms as k_forms
from . import operations as k_operations

# Create your views here.


class GeneralView(django_generic.ListView):
    """
    The "General" view is for all posts, and especially posts that
    don't have a home. It's provided as a "general chat" area.

    It doesn't quite capture the same information as a KookaburraSection
    as it is effectively a "Non-KookaburraSection, KookaburraSection"
    """

    model = KookaburraPost
    template_name = "kookaburra/general.html"
    context_object_name = "general_posts"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["sections"] = KookaburraSection.objects.all()
        return context


class SectionView(django_generic.DetailView):
    """
    Each of the SectionViews will have their own blurb and information
    And they will have their own post-retreiving QS's
    """

    model = KookaburraSection
    template_name = "kookaburra/section.html"
    context_object_name = "section"


class PostView(django_generic.UpdateView):
    """
    This is a DetailView of a specific Post, which is the meat of the forum,
    it has a form mixin for attaching comments to the post.
    """

    model = KookaburraPost
    template_name = "kookaburra/post.html"
    context_object_name = "post"

    form_class = k_forms.AddCommentForm

    def form_valid(self, form):
        k_operations.add_comment(
            self.object, form["content"].value(), self.request.user
        )
        return super().form_valid(form)


# --------------------------------------- Creation and posting view.
class CreateNewPostView(django_generic.CreateView):
    """
    Create a new post in a section
    """

    model = KookaburraPost
    fields = [
        "section",
        "title",
        "content",
    ]
    template_name = "kookaburra/new/post.html"

    def get_initial(self):
        initial = super().get_initial()
        initial["author"] = self.request.user

        section_slug = self.kwargs.get("slug", None)
        initial["section"] = KookaburraSection.objects.filter(slug=section_slug).first()
        return initial


class CreateNewPostCommentView(django_generic.CreateView):
    """
    Comment on a previous post
    """

    model = KookaburraComment
    fields = ["content"]
    template_name = "Kookaburra/new/comment.html"

    def get_initial(self):
        initial = super().get_initial()
        return initial
