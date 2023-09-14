from  django import forms
from bb.models import E

class EF(forms.ModelForm):
    class Meta:
        model=E
        fields="__all__"