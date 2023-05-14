from django import forms

class BookIdForm(forms.Form):
    book_id = forms.IntegerField()