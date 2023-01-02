from django import forms
from .models import Employee, Position

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        # fields = '__all__'
        fields = (
            'family_name', 
            'given_name', 
            'preferred_name', 
            'emp_code', 
            'mobile_no', 
            'position',
        )

        # Customizing the form -- doesn't work!!!
        def __init__(self, *args, **kwargs):
            super(EmployeeForm, self).__init__(*args, **kwargs)
            self.fields['position'].empty_label = "Select"
            # self.fields['emp_code'].required = False