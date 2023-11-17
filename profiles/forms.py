from django import forms
from django.core.validators import FileExtensionValidator


class ProfileForm(forms.Form):
    image = forms.FileField(validators=
                            [FileExtensionValidator(allowed_extensions=['png'])]
                            )
