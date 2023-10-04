from django import forms
from django.contrib.auth.forms import UserCreationForm

from agency.models import Redactor, Newspaper


class NewspaperSearchForm(forms.Form):
    title = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Search by title..."}),
    )


class NewspaperForm(forms.ModelForm):
    class Meta:
        model = Newspaper
        fields = ['title', 'content', 'topics', 'publishers']


class TopicSearchForm(forms.Form):
    title = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Search by name..."}),
    )


class RedactorForm(UserCreationForm):
    first_name = forms.CharField(max_length=50, required=True)
    last_name = forms.CharField(max_length=50, required=True)

    class Meta(UserCreationForm):
        model = Redactor
        fields = UserCreationForm.Meta.fields + (
            "first_name",
            "last_name",
            "years_of_experience",
            "workplace",
            "email",
        )


class RedactorSearchForm(forms.Form):
    username = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={"placeholder": "Search by username..."}
        ),
    )
