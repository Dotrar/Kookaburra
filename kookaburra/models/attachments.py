from django.db import models

from . import posts as kookaburra_posts


class KookaburraAttachment(models.Model):
    """
    Abstract base attachment, which could be a type
    of image, file, or link to another post.

    Attachments are mainly attached to a post, but they could
    also be linked to a specific comment, which is handy if the
    file is considered to be kept 'in place'
    """

    post = models.ForeignKey(kookaburra_posts.KookaburraPost, on_delete=models.CASCADE)
    comment = models.ForeignKey(
        kookaburra_posts.PostComment, on_delete=models.SET_NULL, null=True
    )

    class Meta:
        abstract = True


class FileAttachment(KookaburraAttachment):
    """
    A file has been attached to a post
    """


class ImageAttachment(KookaburraAttachment):
    """
    An image has been attached to a post
    """
