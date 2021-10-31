from django.shortcuts import render

from django.views.generic import TemplateView, DetailView, ListView, CreateView

from .models import KookaburraPost, KookaburraSection

# Create your views here.


class GeneralView(ListView):
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


class SectionView(DetailView):
    """
    Each of the SectionViews will have their own blurb and information
    And they will have their own post-retreiving QS's
    """

    model = KookaburraSection
    template_name = "kookaburra/section.html"
    context_object_name = "section"


class PostView(DetailView):
    model = KookaburraPost
    template_name = "kookaburra/post.html"
    context_object_name = "post"


# --------------------------------------- Creation and posting view.
class CreateNewPostView(CreateView):
    """
    Create a new post in a section
    """

    model = KookaburraPost
    fields = ["section", "title", "content"]
    template_name = "kookaburra/new/post.html"

    def get_form_kwargs(self, **kwargs):
        form_kwargs = super().get_form_kwargs()

        return form_kwargs
