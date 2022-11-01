import django


from django import forms
from .models import Libro, Comment

class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = '__all__'

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = '__all__'