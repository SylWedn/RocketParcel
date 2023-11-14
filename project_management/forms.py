from django import forms
from .models import Category


class AddPostForm(forms.Form):
    title = forms.CharField(max_length=255, label='Title')
    slug = forms.SlugField(max_length=255, label='URL')
    content = forms.CharField(widget=forms.Textarea(), required=False, label='Content')
    is_published = forms.BooleanField(label='Status')
    cat = forms.ModelChoiceField(queryset=Category.objects.all(), label='Category')

