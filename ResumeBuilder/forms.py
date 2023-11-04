from django import forms

class Heading(forms.Form):
    name = forms.CharField()
    mobile_number = forms.CharField()
    email_id = forms.CharField()
    location = forms.CharField()
    summary = forms.Textarea()

class Skills(forms.Form):
    skill_name = forms.CharField()
    strength = forms.IntegerField(max_value=10)

class ExtraCurriculars(forms.Form):
    name = forms.CharField()
    role = forms.CharField()

class Projects(forms.Form):
    name = forms.CharField()
    start_duration = forms.DateField()
    end_duration = forms.DateField()
    about = forms.Textarea()

class Education(forms.Form):
    name = forms.CharField()
    start_diration = forms.DateField()
    end_duration = forms.DateField()
    score = forms.IntegerField()
    course_name = forms.CharField()