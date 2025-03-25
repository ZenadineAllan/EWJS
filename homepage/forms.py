from django import forms
from .models import Students

class NewStudentForm(forms.ModelForm):
    class Meta:
        model = Students
        fields = (
            'student_name', 'current_class', 'gender', 'dob', 'religion', 'prev_school', 'assessment_no', 
            'parent_name', 'id_no', 'relationship', 'contact_1', 'contact_2', 'res_address', 'associate', 'ass_contact'
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        styling = "w-full px-4 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500"

        for field_name in self.fields:
            self.fields[field_name].widget.attrs['class'] = styling
