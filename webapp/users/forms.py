from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column
from .models import OpportunitieBuying, OpportunitieSelling, Features, Condition, RealtorQualities, Proposals, Realtor, TypeBuilding, Services, RealtorImages, PostingImageBuying, PostingImageSelling, Cities, Languages, Special
from django.forms import ModelForm

from django.core.exceptions import ValidationError


PRICE = (
    ('Less than $250,000', 'Less than $250,000'),
    ('$250,000 - $500,00', '$250,000 - $500,00'),
    ('$500,000 - $750,000', '$500,000 - $750,000'),
    ('$750,000 - $1 Million', '$750,000 - $1 Million'),
    ('$1 - $1.5 Million', '$1 - $1.5 Million'),
    ('$1.5 Million and over', '$1.5 Million and over')
)

SIZE = (
    ('under 800 sq ft','under 800 sq ft'),
    ('1000-1500 sq ft','1000-1500 sq ft'),
    ('1500-2000 sq ft','1500-2000 sq ft'),
    ('2000-2500 sq ft','2000-2500 sq ft'),
    ('2500-3000 sq ft','2500-3000 sq ft'),
    ('3000-4000 sq ft','3000-4000 sq ft'),
    ('5000+ sq ft','5000+ sq ft'),
)

URGENCY = (
    (1, 'Fast'),
    (2, 'Medium'),
    (3, 'Slow')
)

USER_TYPE = (
    ('buyer', 'I\'m looking to buy or sell'),
    ('agent', 'I\'m a Realtor'),
)


from crispy_forms.layout import Field

def validate_even(value):
    if value != 'VIPLAUNCH':
        raise forms.ValidationError("That is not a valid promo code!")


class Promocode(forms.Form):
    promo = forms.CharField(validators=[validate_even])


class CustomCheckbox(Field):
    template = 'custom_checkbox.html'


class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)
    user_type = forms.TypedChoiceField(choices=USER_TYPE, label='I am a....')

    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user


class FeaturesForm(forms.Form):
    features = forms.ModelMultipleChoiceField(queryset=Features.objects.all(), required=False, widget=forms.CheckboxSelectMultiple)

class ProposalForm(ModelForm):

    services = forms.ModelMultipleChoiceField(
                                            queryset=Services.objects.all(),
                                            required=False, 
                                            widget=forms.CheckboxSelectMultiple,
                                            label='Check any services below you offer'
                                            )

    class Meta:
        model = Proposals
        fields = (
            "subject",
            "note",
            "services",
            "fee",
        )

        labels = {
            'subject': ('Create a subject for the proposal'),
            'note':('Personal Note to client'),
            'fee':('Fee structure'),
        }


class AgentForm(ModelForm):
    services = forms.ModelMultipleChoiceField(
                                            queryset=Services.objects.all(),
                                            required=False, 
                                            widget=forms.CheckboxSelectMultiple,
                                            label='Check any services below you offer'
                                            )
    cities = forms.ModelMultipleChoiceField(
                                            queryset=Cities.objects.all().order_by('name'),
                                            required=False, 
                                            widget=forms.CheckboxSelectMultiple,
                                            label='Select the cities you work in'
                                            )
    special = forms.ModelMultipleChoiceField(
                                            queryset=Special.objects.all(),
                                            required=False, 
                                            widget=forms.CheckboxSelectMultiple,
                                            label='What makes you special'
                                            )
    languages = forms.ModelMultipleChoiceField(
                                            queryset=Languages.objects.all(),
                                            required=False, 
                                            widget=forms.CheckboxSelectMultiple,
                                            label='Languages you work in'
                                            )      
    building_types = forms.ModelMultipleChoiceField(
                                            queryset=TypeBuilding.objects.all(),
                                            required=False, 
                                            widget=forms.CheckboxSelectMultiple,
                                            label='Building types you work with'
                                            )                                                                                                                           
    class Meta:
        model = Realtor
        fields = (
            "company",
            "work_phone",
            "cell_phone",
            "about_me",
            "why_work",
            "services",
            "cities",
            "special",
            "languages",
            "building_types",
            "website",
        )
        labels = {
            'company': ('What is the name of the agency you work with?'),
            'work_phone': ('Enter your work phone number'),
            'cell_phone': ('Enter your cell phone number'),
            'about_me': ('Provide a short bio about yourself'),
            'why_work': ('List the top reasons why someone should work with you'),
            'services': ('Select the services you provide '),
            'cities': ('Select the cities you work in'),
            'special': ('What makes you special'),
            'languages': ('Languages you work in'),
            'building_types': ('Building types you work with'),
            'website': ('Your website'),
        }

class OpportunityBuyingForm(ModelForm):
    choice = Features.objects.all()
    budget = forms.TypedChoiceField(choices=PRICE, label='What is your price range?')
    sq_ft = forms.TypedChoiceField(choices=SIZE, label='I’m looking for a house with a square footage of:')
    urgency = forms.TypedChoiceField(choices=URGENCY, coerce=int, label='Buying Urgency')
    features = forms.ModelMultipleChoiceField(
                                            queryset=Features.objects.all(),
                                            required=False, 
                                            widget=forms.CheckboxSelectMultiple,
                                            label='What are some features you are looking for in your new home?'
                                            )
    condition = forms.ModelMultipleChoiceField(
                                            queryset=Condition.objects.all(),
                                            required=False, 
                                            widget=forms.CheckboxSelectMultiple,
                                            label='Condition of home, Choose all that apply'
                                            )
    realtorqualities = forms.ModelMultipleChoiceField(
                                            queryset=RealtorQualities.objects.all(),
                                            required=False,
                                            widget=forms.CheckboxSelectMultiple,
                                            label='What are the most important qualities your Realtor must have? Select all that apply'
                                            )

    class Meta:
        model = OpportunitieBuying
        fields = (
            "bathrooms",
            "bedrooms",
            "budget",
            "sq_ft",
            "looking_for",
            "notes_to_agent",
            "notes_about",
            "insite1",
            "insite2",
            "insite3",
            "insite4",
            "urgency",
            "investment",)

        labels = {
            'bedrooms': ('How many bedrooms would you like?'),
            'bathrooms': ('How many bathrooms would you like?'),
            'looking_for': ('Tell us what you’re looking for in your new home.'),
            'notes_to_agent': ('Notes to Real Estate Agent'),
            'notes_about': ('What type of home are you looking for? (Ex. Rancher, condo, loft, tear down, fixer-upper,  try to explain your vision)'),
            'insite1': ('The specific neighborhoods or neighborhood types that I like are: '),
            'insite2': ('Special interests I have that may dictate the area or lifestyle I am pursuing are:'),
            'insite3': ('Special requests I have as a parent or pet owner are:'),
            'insite4': ('The reasons for my move are:'),

            
        }
        help_texts = {
            'looking_for': ('EX: A mudroom  is really important and a fenced yard, or, we need to be close to the subway'),
            'notes_to_agent': ('(share details of your story so that your potential realtor can get a feel for your personality, and for your motivations and inspiration for the move/purchase)'),
        }
     
class OpportunitySellingForm(ModelForm):

    sq_ft = forms.TypedChoiceField(choices=SIZE, label='What size is the house you are selling?')
    urgency = forms.TypedChoiceField(choices=URGENCY, coerce=int, label='Buying Urgency')
    features = forms.ModelMultipleChoiceField(
                                            queryset=Features.objects.all(),
                                            required=False, 
                                            widget=forms.CheckboxSelectMultiple,
                                            label='Select any features in you home.'
                                            )

    realtorqualities = forms.ModelMultipleChoiceField(
                                            queryset=RealtorQualities.objects.all(),
                                            required=False,
                                            widget=forms.CheckboxSelectMultiple,
                                            label='What are the most important qualities your Realtor must have? Select all that apply'
                                            )
    building_types = forms.ModelMultipleChoiceField(
                                            queryset=TypeBuilding.objects.all(),
                                            required=False, 
                                            widget=forms.CheckboxSelectMultiple,
                                            label='What type of building is your home?'
                                            )

    class Meta:
        model = OpportunitieSelling
        fields = ("bathrooms",
                "bedrooms",
                "sq_ft",
                "year_built",
                "building_types",
                "asking_price",
                "unique_value",
                "details",
                "love",
                "realtorqualities",
                "notes_to_agent",
                "urgency",
                "phone",
                "features"
                )
        labels = {
            'bedrooms':('How many bedrooms are in your home?'),
            'bathrooms':('How many bathrooms are in your home?'),
            'year_built':('What year was your home built in?'),
            'building_types': ('What type of building is your home?'),
            'unique_value':('Are there other specific features about your property that add unique value?'),
            'details':('Are there specific physical details about your home that you feel add unique value to your property?'),
            'love':('What else do you love about your home?'),
            'realtorqualities':('What are the most important qualities your Realtor must have? Select all that apply'),
            'notes_to_agent':('Notes to agent'),
        
        }
        help_texts = {
            'details': ('EX “the layout of the kitchen is perfect for cooking and entertaining”, “the master ensuite shower has an amazing view of the lake”, “there are old growth trees in our backyard”, “my living room has an old stone fireplace”'),
            'unique_value': (' EX “We live at the end of a cul-de-sac that is really safe for our kids”, “we have tons of hummingbirds who visit our flower garden”, our condo deck overlooks the harbor”, “the apartment was formerly owned by Prince”'),
            'love': ('Ex: “my patio hottub is completely private”, “my allotted parking spot is really extra wide”'),
        }

class AgentProposalForm(forms.Form):
    message = forms.CharField()


class ImageForm(ModelForm):
    profile = forms.ImageField (required=False)
    cover = forms.ImageField (required=False)

    class Meta:
        model = RealtorImages
        fields = ('profile', 'cover')


class UserEdit(forms.Form):
    email = forms.CharField()
    first_name = forms.CharField()
    last_name = forms.CharField()

class PostingImageBuyingForm(ModelForm):
    image = forms.ImageField(required=False)

    class Meta:
        model = PostingImageBuying
        fields = ('image', )

class PostingImageSellingForm(ModelForm):
    image = forms.ImageField(required=False)

    class Meta:
        model = PostingImageSelling
        fields = ('image', )