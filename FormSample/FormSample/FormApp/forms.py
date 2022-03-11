from dataclasses import fields
from logging import PlaceHolder
from wsgiref.validate import validator
from django import forms
from django.core import validators
from .models import Post

def check_name(value):
    if value == "abcde":
        raise validators.ValidationError("Cant regist the name.")

class UserInfo(forms.Form):
    name = forms.CharField(label="Full Name", max_length=10, min_length=3, validators=[check_name])
    age = forms.IntegerField(label="Own age", validators=[validators.MinValueValidator(15, message="input over 15")])
    mail = forms.EmailField(
        label="Mail address",
        widget=forms.TextInput(attrs={"class": "mail-class", "placeholder": "sample@example.com"}),
    )
    verify_mail = forms.EmailField(
        label="Verify Mail address",
        widget=forms.TextInput(attrs={"class": "mail-class", "placeholder": "sample@example.com"})
    )
    is_married = forms.BooleanField(initial=False, required=False)
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
        if not homepage.startswith("https"):
            raise forms.ValidationError("Needs https")

    def clean(self):
        cleaned_data = super().clean()
        mail = cleaned_data['mail']
        verify_mail = cleaned_data['verify_mail']
        if mail != verify_mail:
            raise forms.ValidationError("not match email")

class BaseForm(forms.ModelForm):
    def save(self, *args, **kwargs):
        print(f'Form: {self.__class__.__name__} execute!')
        return super(BaseForm, self).save(*args, **kwargs)

class PostModelForm(BaseForm):
    name = forms.CharField(label="name")
    title = forms.CharField(label="title")
    memo = forms.CharField(
        label="memo",
        widget=forms.Textarea(attrs={"rows":30, "cols":20})
    )
    class Meta:
        model = Post
        fields = '__all__'
        # fields =["name", "title"]
        # exclude = ["title"]
    
    def save(self, *args, **kwargs):
        obj = super(PostModelForm, self).save(commit=False, *args, **kwargs)
        obj.name = obj.name.upper()
        print(type(obj))
        print("Save obj.")
        obj.save()
        return obj