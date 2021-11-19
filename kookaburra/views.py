from django.shortcuts import get_object_or_404, redirect

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic as django_generic

from .models import KookaburraPost, KookaburraSection, KookaburraComment
from . import forms as k_forms
from . import operations as k_operations

# Create your views here.


class KookaburraView(LoginRequiredMixin):
    """
    Needed for main view, provides the login-required
    as well as section views and other favourite items
    """

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["sections"] = KookaburraSection.objects.all()
        return context


class GeneralView(KookaburraView, django_generic.ListView):
    """
    The "General" view is for all posts, and especially posts that
    don't have a home. It's provided as a "general chat" area.

    It doesn't quite capture the same information as a KookaburraSection
    as it is effectively a "Non-KookaburraSection, KookaburraSection"
    """

    model = KookaburraPost
    template_name = "kookaburra/general.html"
    context_object_name = "general_posts"


class SectionView(KookaburraView, django_generic.DetailView):
    """
    Each of the SectionViews will have their own blurb and information
    And they will have their own post-retreiving QS's
    """

    model = KookaburraSection
    template_name = "kookaburra/section.html"
    context_object_name = "section"


class PostView(KookaburraView, django_generic.DetailView):
    """
    url: post/1234

    This is a DetailView of a specific Post, which is the meat of the forum,
    it has a form mixin for attaching comments to the post.
    """

    model = KookaburraPost
    template_name = "kookaburra/post.html"
    context_object_name = "post"

    # form_class = k_forms.AddCommentForm

    def get_context_data(self, **kwargs):
        """
        We add a comment_form to the detail view.
        """
        context = super().get_context_data(**kwargs)
        context["comment_form"] = k_forms.AddCommentForm(initial={})
        return context


# ============================================
# --------------------------------------- Creation and posting view.


class CommentOnPostView(LoginRequiredMixin, django_generic.CreateView):
    model = KookaburraComment
    fields = ["content"]

    def form_valid(self, form):
        # breakpoint()
        post = get_object_or_404(KookaburraPost, **self.kwargs)
        k_operations.add_comment(post, form["content"].value(), self.request.user)
        return redirect(post.get_absolute_url())


class CreateNewPostView(LoginRequiredMixin, django_generic.CreateView):
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
        section_slug = self.kwargs.get("slug", None)
        initial["section"] = KookaburraSection.objects.filter(slug=section_slug).first()
        return initial

    def get_form(self):
        form = super().get_form()
        form["section"].field.required = False
        form["section"].field.empty_label = "General"
        return form

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class CreateNewSectionView(LoginRequiredMixin, django_generic.CreateView):
    """
    Create a new section
    """

    model = KookaburraSection
    fields = [
        "name",
        "slug",
        "description",
    ]
    template_name = "kookaburra/new/post.html"

    def get_initial(self):
        initial = super().get_initial()
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
