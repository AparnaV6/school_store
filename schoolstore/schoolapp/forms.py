from django import forms
from .models import Student


class Studentform(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'dob', 'age', 'gender', 'phone', 'mail_id', 'address',
                  'department', 'courses', 'purpose', 'materials']

