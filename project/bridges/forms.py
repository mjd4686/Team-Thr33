from django import forms
from .models import Survey
from datetime import datetime
#----------------------------------------------------------------------
#                         Users
#----------------------------------------------------------------------
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    BIRTH_YEAR_CHOICES = ('1920', '1921', '1922', '1923', '1924', '1925', '1926', '1927', '1928', '1929', '1930', '1931', '1932', '1933', '1934',
     '1935', '1936', '1937', '1938', '1939', '1940', '1941', '1942', '1943', '1944', '1945', '1946', '1947', '1948', '1949',
     '1950', '1951', '1952', '1953', '1954', '1955', '1956', '1957', '1958', '1959', '1960', '1961', '1962', '1963', '1964',
     '1965', '1966', '1967', '1968', '1969', '1970', '1971', '1972', '1973', '1974', '1975', '1976', '1977', '1978', '1979',
     '1980', '1981', '1982', '1983', '1984', '1985', '1986', '1987', '1988', '1989', '1990', '1991', '1992', '1993', '1994',
     '1995', '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011',
      '2012', '2013', '2014', '2015', '2016', '2017', '2018')
    
    first_name = forms.CharField(max_length=30, required=True, help_text='Required.')
    last_name = forms.CharField(max_length=30, required=True, help_text='Required.')
    email = forms.EmailField(max_length=254, required=True, help_text='Required. Inform a valid email address.')
    birth_date = forms.DateField(widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES), help_text="Required.", required=True)
    year = forms.IntegerField(label="Graduation Year", help_text="Optional. e.g. 2020", required=False)
    phone = forms.CharField(max_length=10, label="Phone Number", help_text="Optional. e.g. 555-555-5555", required=False)
    school = forms.CharField(max_length=100, help_text="Optional. e.g. UMass Amherst", required=False)
    major = forms.CharField(max_length=100, help_text="Optional. e.g. BS Computer Science", required=False)
    pocchoices = ['Prefer not to answer', 'Asian', 'Black/African', 'Hispanic/Latinx', 'Native American', 'Pacific Islander', 'White']
    poc = forms.ChoiceField(choices=[(x, x) for x in pocchoices], required=True, label="I identify my ethnicity as:")
    genders = ['Prefer not to answer', 'Female', 'Male', 'Non-binary']
    gender = forms.ChoiceField(choices=[(x, x) for x in genders], required=True, label="I identify my gender as:")
    fgchoices = ['Prefer not to answer', 'Yes', 'No']
    firstgen = forms.ChoiceField(choices=[(x, x) for x in fgchoices], required=True, label="Are you a first generation student?", help_text="Are you in the first generation of your family that went to college?")
    transchoices = ['Prefer not to answer', 'Yes', 'No']
    trans = forms.ChoiceField(choices=[(x, x) for x in transchoices], required=True, label="Do you identify as transgender?")
    pronoun = forms.CharField(max_length=20, label="Preferred Pronouns:", help_text="Optional. e.g. He/his, She/her...", required=False)
    info = forms.CharField(max_length=100, label="What is your relation with Student Bridges?", help_text="Optional. e.g. Student Member, Staff, etc.", required=False)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'birth_date', 'email', 'password1', 'password2', 'year', 'phone', 'school', 'major', 'gender', 'poc', 'firstgen', 'info')


class EditProfileForm(forms.ModelForm):
    BIRTH_YEAR_CHOICES = ('1980', '1981', '1982', '1983', '1984', '1985', '1986', '1987', '1988', '1989', '1990', '1991', '1992', '1993', '1994',
     '1995', '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011',
      '2012', '2013', '2014', '2015', '2016', '2017', '2018')
    
    first_name = forms.CharField(max_length=30, required=True, help_text='Required.')
    last_name = forms.CharField(max_length=30, required=True, help_text='Required.')
    email = forms.EmailField(max_length=254, required=True, help_text='Required. Inform a valid email address.')
    birth_date = forms.DateField(widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES), help_text="Required.", required=True)
    year = forms.IntegerField(label="Graduation Year", help_text="Optional. e.g. 2020", required=False)
    phone = forms.CharField(max_length=10, label="Phone Number", help_text="Optional. e.g. 555-555-5555", required=False)
    school = forms.CharField(max_length=100, help_text="Optional. e.g. UMass Amherst", required=False)
    major = forms.CharField(max_length=100, help_text="Optional. e.g. BS Computer Science", required=False)
    pocchoices = ['Prefer not to answer', 'Asian', 'Black/African', 'Hispanic/Latinx', 'Native American', 'Pacific Islander', 'White']
    poc = forms.ChoiceField(choices=[(x, x) for x in pocchoices], required=True, label="I identify my ethnicity as:")
    genders = ['Prefer not to answer', 'Female', 'Male', 'Non-binary']
    gender = forms.ChoiceField(choices=[(x, x) for x in genders], required=True, label="I identify my gender as:")
    fgchoices = ['Prefer not to answer', 'Yes', 'No']
    firstgen = forms.ChoiceField(choices=[(x, x) for x in fgchoices], required=True, label="Are you a first generation student?", help_text="Are you in the first generation of your family that went to college?")
    transchoices = ['Prefer not to answer', 'Yes', 'No']
    trans = forms.ChoiceField(choices=[(x, x) for x in transchoices], required=True, label="Do you identify as transgender?")
    pronoun = forms.CharField(max_length=20, label="Preferred Pronouns:", help_text="Optional. e.g. He/his, She/her...", required=False)
    info = forms.CharField(max_length=100, label="What is your relation with Student Bridges?", help_text="Optional. e.g. Student Member, Staff, etc.", required=False)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'birth_date', 'email', 'year', 'phone', 'school', 'major', 'gender', 'poc', 'firstgen', 'info')

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(EditProfileForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].initial = self.request.user.first_name

class SurveyForm(forms.ModelForm):

    reference = forms.CharField(label='How did you hear about this event?',max_length=150)
    prior_attendee = forms.TypedChoiceField(label='Have you ever been to a Student Bridges event before today?',coerce=lambda x: x =='True', choices=((False, 'No'), (True, 'Yes')))
    suggestion = forms.CharField(label='What kind of events would you like to see from SB next year?',max_length=500)
    rating = forms.ChoiceField(label='On a scale from 1-5, how much did you enjoy the event today?',choices=[(x, x) for x in range(1, 5)], help_text='')
    comments = forms.CharField(label='Any other thoughts or comments?',max_length=500)
    event_name = forms.CharField(label='Event Name', max_length=256, widget=forms.HiddenInput())


    class Meta:
        model = Survey
        fields = ('reference', 'prior_attendee', 'suggestion', 'rating', 'comments')
