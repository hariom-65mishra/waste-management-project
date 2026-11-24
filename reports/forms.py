from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import WasteComplaint

class WasteComplaintForm(forms.ModelForm):
    class Meta:
        model = WasteComplaint
        fields = ['category', 'location', 'landmark', 'urgency', 'description', 'photo']
        widgets = {
            'category': forms.Select(attrs={'class': 'form-input'}),
            'location': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'e.g. Sector 14, Main Road, Block B'}),
            'landmark': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'e.g. Near City Hospital or Water Tank'}),
            'urgency': forms.Select(attrs={'class': 'form-input'}),
            'description': forms.Textarea(attrs={'class': 'form-input', 'rows': 4, 'placeholder': 'Describe the waste issue, estimated size, odor, or safety hazard...'}),
            'photo': forms.ClearableFileInput(attrs={'class': 'form-input file-input', 'accept': 'image/*'}),
        }

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'form-input', 'placeholder': 'Enter your active email'}))
    first_name = forms.CharField(max_length=50, required=True, widget=forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Your Full Name'}))

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'first_name', 'email')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-input', 'placeholder': 'Choose a username'})
        self.fields['username'].help_text = ''
        for field in self.fields.values():
            if 'class' not in field.widget.attrs:
                field.widget.attrs['class'] = 'form-input'
