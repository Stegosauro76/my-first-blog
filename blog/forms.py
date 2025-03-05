from django import forms
from . import models
 
 
class CreatePost(forms.ModelForm):
        class Meta:
            model = models.Post
            fields = ['title','body'] 


class SearchForm(forms.Form):

    query = forms.CharField(label='Cerca', max_length=100) 