"""
Operations module

This works as an domain layer between the interface (ie views and forms) and the data
(ie models)

This file outlines a number of operations that can be commonly used in the forums
"""
from . import models as k_models
from django.conf import settings
from typing import Optional


def add_comment(
    post: k_models.KookaburraPost, content: str, author: settings.AUTH_USER_MODEL
) -> Optional[k_models.KookaburraComment]:
    """
    Add a comment to a post, doing some checks beforehand.
    """
    # Check that the post is allowed to comment
    if not post.commenting_allowed:
        return

    # Check that the author is allowed to comment

    # Check that the content does not contain swears or abusive language

    comment = k_models.KookaburraComment.objects.create(
        content=content, author=author, parent=post
    )

    return comment
