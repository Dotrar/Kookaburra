from django.db import models
from django.conf import settings
from django.shortcuts import reverse
from taggit.managers import TaggableManager

# Create your models here.


class KookaburraSection(models.Model):
    """
    A Section of the fourm is like a "sub-forum" idea, it will contain Posts.

    it also has a blurb and some rich text to title it.
    reverse FKs:
    - posts
    """

    name = models.CharField(max_length=100)
    description = models.TextField()
    slug = models.SlugField()

    # Metadata can be used to store some configuration things, such as theme colour, fa-icon
    metadata = models.JSONField(blank=True, default=dict)

    coordinator = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="coordinates_sections",
        on_delete=models.SET_NULL,
        null=True,
    )

    # Members are a list of users that are in the group
    members = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name="sections_member"
    )

    # Followers are people who want to stay in touch with what is going on in the section
    followers = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name="sections_following"
    )
    # Everyone should be allowed to comment and post new things in the section.

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("section-detail", kwargs={"slug": self.slug})


class KookaburraPost(models.Model):
    """
    Base post class for Kookaburra Forums, Works like a regular discussion

    It is posted in a Section, and would contain Comments, along
    with its actual body data.

    It will also be able to be followed, and various locks can be applied.

    reverse FKs:
    - attachments - KookaburraAttachment
    - comments
    """

    # define types of posts here. TYPE = ("full name","short name")
    GENERAL_DISCUSSION = "General Discussion"

    # this class is of type GENERAL_DISCUSSION
    type = GENERAL_DISCUSSION
    tags = TaggableManager()

    # Parent section, None = general.
    section = models.ForeignKey(
        KookaburraSection,
        on_delete=models.SET_NULL,
        null=True,
        related_name="posts",
        default=None,
    )

    # Literal Content of the post.
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # The user who created it. None = anonymous or previously deleted.
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        related_name="posts",
        null=True,
    )
    # People who are interested in when this post receives changes.
    followers = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name="posts_following"
    )

    # Metadata can be used to store some bits of information; such as last user.
    metadata = models.JSONField(blank=True, default=dict)

    # permissions TODO
    commenting_allowed = models.BooleanField(default=True)

    def __str__(self):
        return f'"{self.title}" (in {self.section})'

    def get_absolute_url(self):
        # TODO: gently include the slug here. By that, we can include it
        # as often as possible to make human readable links, but we
        # will ignore it as often as possible because of human error.
        return reverse("post-detail", kwargs={"pk": self.id})

    @property
    def preview(self):
        """
        This is what's given in the preview when looking at posts in a list view.
        """
        return self.content

    @property
    def typename(self):
        return self.type

    @property
    def typename_short(self):
        "Just return the second word in type"
        return self.type.split(" ")[-1]


class KookaburraComment(models.Model):
    """

    reverse FKs:
    - attachment - KookaburraAttachment
    """

    # comments can have images and files attached to them. (one per comment)

    parent = models.ForeignKey(
        KookaburraPost, on_delete=models.CASCADE, related_name="comments"
    )
    content = models.TextField(max_length=1024)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Re:"{self.parent.title[:15]}.." >> "{self.content[:15]}"'
