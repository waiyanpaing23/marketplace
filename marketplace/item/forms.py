from django import forms
from .models import Item

class NewItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('category', 'name', 'description', 'price', 'image')
        widgets = {
        'category' : forms.Select(attrs={
            'class' : 'w-100 py-2 px-3 rounded shadow-sm border-0 mt-2'
        }),
        'name' : forms.TextInput(attrs={
            'class' : 'w-100 py-2 px-3 rounded shadow-sm border-0 mt-2'
        }),
        'description' : forms.Textarea(attrs={
            'class' : 'w-100 py-2 px-3 rounded shadow-sm border-0 mt-2'
        }),
        'price' : forms.TextInput(attrs={
            'class' : 'w-100 py-2 px-3 rounded shadow-sm border-0 mt-2'
        }),
        'image' : forms.FileInput(attrs={
            'class' : 'form-control'
        })
    }
        
class EditItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('name', 'description', 'price', 'image', 'is_sold')
        widgets = {
        'name' : forms.TextInput(attrs={
            'class' : 'w-100 py-2 px-3 rounded shadow-sm border-0 mt-2'
        }),
        'description' : forms.Textarea(attrs={
            'class' : 'w-100 py-2 px-3 rounded shadow-sm border-0 mt-2'
        }),
        'price' : forms.TextInput(attrs={
            'class' : 'w-100 py-2 px-3 rounded shadow-sm border-0 mt-2'
        }),
        'image' : forms.FileInput(attrs={
            'class' : 'form-control'
        })
    }