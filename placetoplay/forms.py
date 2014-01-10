from django import forms
from django.forms import ModelForm
from django.core.validators import MaxLengthValidator, MinValueValidator, MaxValueValidator
from django.forms.extras.widgets import SelectDateWidget
from bootstrap3_datetime.widgets import DateTimePicker
from placetoplay.models import User, UserExtension, Groups

SKILL_CHOICES = (
        ("No prior experience", "No prior experience"),
        ("Novice", "Novice"),
        ("Intermediate", "Intermediate"),
        ("Skilled", "Skilled"),
        ("Expert", "Expert")
    )

SKILL_CHOICES_GROUP = (
        ("No prior experience", "No prior experience"),
        ("Novice", "Novice"),
        ("Intermediate", "Intermediate"),
        ("Skilled", "Skilled"),
        ("Expert", "Expert"),
        ("All skill levels welcome", "All skill levels welcome")
    )

YEARS = ('2013', '2014', '2015')

valid_time_formats = ['%I:%M %p']

#creating forms based on User model and UserExtension model here
#class Userform(forms.Form):
#    username = forms.CharField(required=True, validators=[MaxLengthValidator(30)])
#    first_name = forms.CharField(required=False, validators=[MaxLengthValidator(30)])
#    last_name = forms.CharField(required=False, validators=[MaxLengthValidator(30)])
#    email = forms.EmailField(required=True, validators=[MaxLengthValidator(50)])
#    password = forms.CharField(required=True, widget=forms.PasswordInput, validators=[MaxLengthValidator(50)])
#    confirm_password = forms.CharField(required=True, widget=forms.PasswordInput, validators=[MaxLengthValidator(50)])
#    region = forms.CharField(required=False, validators=[MaxLengthValidator(50)])#DON'T FOGET TO CHANGE THIS TO CHOICEFIELD LATER
#    game_preference = forms.CharField(required=True, validators=[MaxLengthValidator(50)])
#    second_preference = forms.CharField(required=False, validators=[MaxLengthValidator(50)])
#    third_preference = forms.CharField(required=False, validators=[MaxLengthValidator(50)])
#    habits_and_characteristics = forms.CharField(required=False, widget=forms.Textarea, validators=[MaxLengthValidator(255)])
#    experience = forms.ChoiceField(required=False, widget=forms.Select, choices=SKILL_CHOICES)
#    phone = forms.CharField(required=False, validators=[MaxLengthValidator(11)])
#    facebook = forms.URLField(required=False)
#    #profile_picture = forms.CharField(required=False, validators=[MaxLengthValidator(100)], widget=forms.FileInput)
#    # ask about profile_picture; is there a field to allow user to select picture from his/her own filepath?

class Userform(ModelForm):
    #confirm_password = forms.CharField(required=True, widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']
        widgets = {'password': forms.PasswordInput}

class UserformEdit(Userform):
    class Meta(Userform.Meta):
        exclude = ('password',)

class UserformSignin(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, widget=forms.PasswordInput)
    #class Meta(Userform.Meta):
    #    exclude = ('first_name', 'last_name', 'email', 'confirm_password') <-- excluding confirm pass doesn't work

class UserExtform(ModelForm):
    class Meta:
        model = UserExtension
        fields = ['city', 'game_pref1', 'game_pref2', 'game_pref3', 'characteristics', 'skill', 'phone', 'image_path']

class groupSignup(ModelForm):
    class Meta:
        model = Groups
        fields = ['name', 'region', 'games', 'special_rules', 'skill_level', 'email', 'private_group', 'address', 'schedule_date', 'schedule_time', 'schedule_event']
        widgets = {
            'schedule_time': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'skill_level': forms.Select(choices=SKILL_CHOICES_GROUP),
            'schedule_date': SelectDateWidget(years=YEARS),
        }

#class groupForm(forms.Form):
#    group_name = forms.CharField(required=True, validators=[MaxLengthValidator(100)])
#    region = forms.CharField(required=False, validators=[MaxLengthValidator(50)])
#    games_we_play = forms.CharField(required=True, validators=[MaxLengthValidator(255)])#come back to this later if you have time; select menu of all games maybe?
#    house_rules = forms.CharField(required=False, widget=forms.Textarea)
#    average_skill_level = forms.ChoiceField(required=True, widget=forms.Select, choices=SKILL_CHOICES_GROUP)
#    group_email = forms.EmailField(required=False, validators=[MaxLengthValidator(50)])
#    private_group = forms.BooleanField(required=False)
#    #group_picture = forms.CharField(required=False, validators=[MaxLengthValidator(100)], widget=forms.FileInput)
#    address = forms.CharField(required=True, validators=[MaxLengthValidator(99)])
#    event_date = forms.DateField(required=True, widget=SelectDateWidget(years=YEARS))
#    event_time = forms.TimeField(required=True, widget=forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}, format="%I:%M %p"))
#    event = forms.CharField(required=True, widget=forms.Textarea)