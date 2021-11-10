from django import forms
from customer.models import Customer

class LogForm(forms.ModelForm):
    class Meta:
        model = Customer 
        fields = ("fname", "email", "dob", "address",) 