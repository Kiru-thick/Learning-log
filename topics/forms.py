from django import forms

from .models import Topic,Entry


class TopicForm(forms.ModelForm):
    class Meta():
        model = Topic
        fields = ['text']
        labels = {'text': ''}
        widgets = {'text': forms.TextInput(attrs={'placeholder': 'topic'})}

class EntryForm(forms.ModelForm):
    class Meta():
        model = Entry
        fields = ['text']
        labels = {
            'text': ''
        }
        widgets = {'text': forms.Textarea(attrs={'rows': 5,
                                                 'cols': 30,'placeholder': 'Be appropriate'}) }

