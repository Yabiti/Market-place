from django import forms

from .models import item

class NewItemForm(forms.ModelForm):
    class Meta:
        model = item
        fields = ('category', 'name', 'price', )