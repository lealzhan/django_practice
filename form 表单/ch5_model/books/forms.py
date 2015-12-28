from django import forms

class AddForm(forms.Form):
    a = forms.IntegerField()
    b = forms.IntegerField()
    c = forms.IntegerField()
    d = forms.CharField()

    def clean_a(self): #selfdefined input check
        a = self.cleaned_data['a']
        if a < 0:
            raise forms.ValidationError("a must be a positive number")
        return a
