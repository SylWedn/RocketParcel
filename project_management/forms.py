from django import forms
from .models import Category, Packagedb


# creation forms from model structure
class AddPostForm(forms.ModelForm):
    class Meta:
        model = Packagedb
        fields = '__all__'
    # cat = forms.ModelChoiceField(queryset=Category.objects.all(), label='Category')


class UploadFileForm(forms.Form):
    file = forms.FileField(label='File')
