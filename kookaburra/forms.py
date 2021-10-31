from django import forms
from . import models as models


class AddCommentForm(forms.ModelForm):
    """
    Comment Field on a Post, allowing for people to respond
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # clear out initial data
        self.fields["content"].value = ""

    class Meta:
        model = models.KookaburraComment
        fields = ["content"]
