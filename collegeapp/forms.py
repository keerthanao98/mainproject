from django import forms

from collegeapp.models import Todo


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ('data',)
