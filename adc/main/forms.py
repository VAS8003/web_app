from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label=False,max_length=100, required=True, widget=forms.TextInput(attrs={'placeholder': 'Ваш ПІБ', 'style': 'border: none; border-bottom: 1px solid black; width: 400px;font-size: 18px;'}))
    email = forms.EmailField(label=False,max_length=100, required=True, widget=forms.EmailInput(attrs={'placeholder': 'Ваш Email', 'style': 'border: none; border-bottom: 1px solid black; width: 400px;font-size: 18px;'}))
    phone = forms.CharField(label=False, max_length=20, widget=forms.TextInput(attrs={'placeholder': 'Ваш телефон', 'style': 'border: none; border-bottom: 1px solid black; width: 400px;font-size: 18px;'}))
