from django import forms
from django.contrib.auth.forms import AuthenticationForm
# We import YOUR specific model name here
from .models import ImageHistory

# ==========================================
# 1. THE IMAGE UPLOAD FORM (Now linked to ImageHistory)
# ==========================================
class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = ImageHistory
        fields = ['image']
        # Styling the file input
        widgets = {
            'image': forms.FileInput(attrs={'class': 'form-control'})
        }

# ==========================================
# 2. THE LOGIN FORM (Your Navy Design)
# ==========================================
class UserLoginForm(AuthenticationForm):
    # Add the "Remember Me" field
    remember_me = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={
        'id': 'remember'
    }))

    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)
        
        # Style the Username field
        self.fields['username'].widget.attrs.update({
            'id': 'email', 
            'placeholder': 'Enter your email',
            'class': 'custom-input' 
        })

        # Style the Password field
        self.fields['password'].widget.attrs.update({
            'id': 'password', 
            'placeholder': 'Enter your password',
            'class': 'custom-input'
        })