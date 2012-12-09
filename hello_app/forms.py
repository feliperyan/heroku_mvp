import floppyforms as forms
from captcha.fields import ReCaptchaField

class FeedbackForm(forms.Form):
    
    name = forms.CharField(required=True,\
        widget=forms.TextInput(attrs={'placeholder': 'FirstName LastName'}))
    
    email = forms.EmailField(required=True,\
        widget=forms.EmailInput(attrs={'placeholder': 'john@example.com'}))

    wantsServicesXchange = forms.BooleanField(required=False, \
        label='I am interested in swapping skills and services.', widget=forms.CheckboxInput(attrs={'class': 'inline'}) )
    wantsGoodsXchange = forms.BooleanField(required=False, label='I am interested in swapping things')
    wantsCharityXchange = forms.BooleanField(required=False, label='I am interested in charity work?')
    wantsLocationXchange = forms.BooleanField(required=False, label='Are you interested in the locations bit?')
    wantsBadges = forms.BooleanField(required=False, label='Are you interested in badges?')

    comments = forms.CharField(widget=forms.Textarea(attrs={'rows':3, 'cols':60}), required=False)

    captcha = ReCaptchaField(attrs={'theme' : 'white'})