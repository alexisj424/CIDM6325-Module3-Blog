from django import forms
from .models import Post, Comment, Category, Tag

class PostForm(forms.ModelForm):
    title = forms.CharField(
        max_length=200,
        help_text="Enter a concise, descriptive title (10–200 chars).",
        widget=forms.TextInput(attrs={"class": "form-control", "aria-describedby": "titleHelp"})
    )
    body = forms.CharField(
        widget=forms.Textarea(attrs={"rows": 8, "class": "form-control"}),
        help_text="Share your thoughts. Markdown not required."
    )
    category = forms.ModelChoiceField(
        queryset=Category.new_manager.all() if hasattr(Category, "new_manager") else Category.objects.all(),
        required=False,
        widget=forms.Select(attrs={"class": "form-select"})
    )
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        required=False,
        widget=forms.SelectMultiple(attrs={"class": "form-select"})
    )

    class Meta:
        model = Post
        fields = ["title", "body", "category", "tags"]

    def clean_title(self):
        title = self.cleaned_data["title"].strip()
        if len(title) < 10:
            raise forms.ValidationError("Title must be at least 10 characters.")
        return title


class CommentForm(forms.Form):
    text = forms.CharField(
        widget=forms.Textarea(attrs={
            "rows": 3,
            "placeholder": "Write your comment…",
            "class": "form-control"
        }),
        label="",
        max_length=2000
    )


