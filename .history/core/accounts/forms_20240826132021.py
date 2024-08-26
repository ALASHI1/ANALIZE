
from django import forms
from allauth.account.forms import SignupForm

class CustomSignupForm(SignupForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields.pop('username', None)

    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        return user