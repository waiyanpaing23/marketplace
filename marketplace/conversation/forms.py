from django import forms
from conversation.models import ConversationMessage

class ConversationMessageForm(forms.ModelForm):
    class Meta:
        model = ConversationMessage
        fields = ('content',)
        labels = {
            'content' : ''
        }
        widgets = {
            'content' : forms.TextInput(attrs={
                'class' : 'form-control',
                'placeholder' : 'Send Message',
            })
        }