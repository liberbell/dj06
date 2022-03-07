from django import forms

class UserInfo(forms.Form):
    name = forms.CharField(label="Full Name")
    age = forms.IntegerField(label="Own age")
    mail = forms.EmailField(label="Mail address")
    is_married = forms.BooleanField()
    birthday = forms.DateField()
    salary = forms.DecimalField()
    job = forms.ChoiceField(choices=(
        (1, "Permanent"),
        (2, "Temporary"),
        (3, "Student"),
        (4, "No job")
    ))
    hoby = forms.MultipleChoiceField(choices=(
        (1, "Sports"),
        (2, "Reading"),
        (3, "Watch movies"),
        (4, "other")
    ))
    homepage = forms.URLField(required=False)
    memo = forms.CharField(required=False, widget=forms.Textarea)