from django import forms
from .models import user
"""
class user_form(forms.ModelForm):
	class Meta:
		model=user
		fields=['img']
	def email(self):
			email=self.cleaned_data.get('email')
			if  not "@" in email:
				return forms.ValidationError("invalid email")
			return email
	def password(self):
			pas=self.cleaned_data.get('email')
			if len(re.findAll('[\d+]'))==0:
				return forms.ValidationError("password must have digets")
			if len(re.findAll('[\w+]'))==0:
				return forms.ValidationError("password must have word")
			return pas
"""

from captcha.fields import CaptchaField

class CaptchaTestForm(forms.Form):
    captcha = CaptchaField


