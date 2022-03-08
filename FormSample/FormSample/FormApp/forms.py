from logging import PlaceHolder
from django import forms

class UserInfo(forms.Form):
    name = forms.CharField(label="Full Name", max_length=10, min_length=3)
    age = forms.IntegerField(label="Own age")
    mail = forms.EmailField(
        label="Mail address",
        widget=forms.TextInput(attrs={"class": "mail-class", "placeholder": "sample@example.com"}),
    )
    is_married = forms.BooleanField(initial=False)
    birthday = forms.DateField(initial="1990-01-01")
    salary = forms.DecimalField()
    job = forms.ChoiceField(choices=(
        (1, "Permanent"),
        (2, "Temporary"),
        (3, "Student"),
        (4, "No job"),
    ), widget=forms.RadioSelect)
    hobbies = forms.MultipleChoiceField(choices=(
        (1, "Sports"),
        (2, "Reading"),
        (3, "Watch movies"),
        (4, "other")
    ), widget=forms.CheckboxSelectMultiple)
    homepage = forms.URLField(required=False)
    memo = forms.CharField(required=False, widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        super(UserInfo, self).__init__(*args, **kwargs)
        self.fields["job"].widget.attrs["id"] = "id_job"
        self.fields["hobbies"].widget.attrs["class"] = "hobbies_class"

    def clean_homepage(self):
        homepage = self.cleaned_data["homepage"]
        if not homepage.startwith("https"):
            raise forms.ValidationError("Needs https")