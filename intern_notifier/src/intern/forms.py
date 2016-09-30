from django import forms

from .models import Profile,Domain

class DateInput(forms.DateInput):
    input_type = 'date'

#Contact form 
class ContactForm(forms.Form):
    name = forms.CharField(required = True)
    email = forms.EmailField(required = True)
    message = forms.CharField(required = True, widget = forms.Textarea)

#Profile form
class ProfileForm(forms.ModelForm):
    #username = forms.CharField(widget=forms.TextInput(attrs={'readonly': 'readonly'}))
    dob = forms.DateField(widget = DateInput(),required=False, label="DOB")
    GENDER_TYPES = (('1','Male'),('2','Female'))
    gender = forms.TypedChoiceField(choices=GENDER_TYPES, widget=forms.RadioSelect, coerce=int, required=False)

    def clean(self):
        path = self.cleaned_data.get('profileimage', False)
        path = str(path)
        list = ['png', 'jpg', 'jpeg']
        ext = path.split('.')[-1]
        if ext not in list:
            raise forms.ValidationError("Please select image in " + ", ".join(list) + " format only.")
            print ext
        return self.cleaned_data

    class Meta:
        model =  Profile
        fields = ['profileimage', 'firstname', 'lastname', 'gender', 'dob']

#Domain form
class DomainForm(forms.ModelForm):
    DOMAIN_OPTIONS = (
        ('Python','Python'),
        ('Java','Java'),
        ('Php','Php'),
        ('Data Science','Data Science'),
        ('Data Structure','Data Structure'),
        )
    domain = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple(attrs={'class':'checkbox'}), choices=DOMAIN_OPTIONS, required=True)
    class Meta:
        model = Domain
        fields = ['domain']