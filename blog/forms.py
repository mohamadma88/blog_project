from django import forms
from .models import Contact, Comments


class ContactForm(forms.Form):
    name = forms.CharField(max_length=5, label='name')
    email = forms.EmailField(label='email')
    sub = forms.CharField(max_length=100, label='sub')
    text = forms.CharField(max_length=1000, label='text')

    def clean(self):
        name = self.cleaned_data.get('name')
        email = self.cleaned_data.get('email')
        sub = self.cleaned_data.get('sub')
        text = self.cleaned_data.get('text')


class MessageForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'

        widgets = {
            'text': forms.TextInput(attrs={
                "class": "forms-control",
                "placeholder": 'enter your text'})
        }


