from django import forms

from .models import Item

InputClasses = 'w'
class NewItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('category', 'name', 'description', 'price', 'image',)

        widgets = {
            'category': forms.Select(attrs={
                'class': InputClasses
            }),

            'name': forms.TextInput(attrs={
                'class': InputClasses
            }),

            'description': forms.Textarea(attrs={
                'class': InputClasses
            }),

            
            'price': forms.TextInput(attrs={
                'class': InputClasses
            }),

            
            'image': forms.FileInput(attrs={
                'class': InputClasses
            })

            
        }


class EditItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('name', 'description', 'price', 'image', 'is_sold')

        widgets = {

            'name': forms.TextInput(attrs={
                'class': InputClasses
            }),

            'description': forms.Textarea(attrs={
                'class': InputClasses
            }),

            
            'price': forms.TextInput(attrs={
                'class': InputClasses
            }),

            
            'image': forms.FileInput(attrs={
                'class': InputClasses
            })

            
        }