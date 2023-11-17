from django import forms
from django.core.validators import FileExtensionValidator, MaxLengthValidator


class ProfileForm(forms.Form):
    # file = forms.FileField(validators=
    #                        [FileExtensionValidator(allowed_extensions=['png'])]
    #                        )
    # test = forms.CharField(validators=[MaxLengthValidator(limit_value=3)])
    image = forms.ImageField()
