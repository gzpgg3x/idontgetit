from rango.models import UserProfile
from django.contrib.auth.models import User
from django import forms
from rango.models import Page, Category, Fantasy

class CategoryForm(forms.ModelForm):
    # name = forms.CharField(max_length=128, help_text="Please enter the Question:")
    name = forms.CharField(max_length=300, help_text="Please enter the Question:", widget=forms.widgets.Textarea(attrs={'class': 'categoryText'}))
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)

    # An inline class to provide additional information on the form.
    class Meta:
        # Provide an association between the ModelForm and a model
        model = Category

class PageForm(forms.ModelForm):
    title = forms.CharField(max_length=128, help_text="Please enter your name:")
    #url = forms.URLField(max_length=200, help_text="Please enter your answer:")
    url = forms.URLField(max_length=200, widget=forms.HiddenInput())
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    mylikes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)    

    class Meta:
        # Provide an association between the ModelForm and a model
        model = Page

        # What fields do we want to include in our form?
        # This way we don't need every field in the model present.
        # Some fields may allow NULL values, so we may not want to include them...
        # Here, we are hiding the foreign key.
        fields = ('title', 'url', 'views','mylikes')

    # def clean(self):
    #     cleaned_data = self.cleaned_data
    #     url = cleaned_data.get('url')

    #     # If url is not empty and doesn't start with 'http://', prepend 'http://'.
    #     if url and not url.startswith('http://'):
    #         url = 'http://' + url
    #         cleaned_data['url'] = url

    #     return cleaned_data

class FantasyForm(forms.ModelForm):
    entry = forms.CharField(max_length=500, help_text="Please enter your fanatasy:")
    # title = forms.CharField(max_length=128, help_text="Please enter your name:")
    # url = forms.URLField(max_length=200, help_text="Please enter your answer:")
    # views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    # mylikes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)    

    class Meta:
        # Provide an association between the ModelForm and a model
        model = Fantasy

        # What fields do we want to include in our form?
        # This way we don't need every field in the model present.
        # Some fields may allow NULL values, so we may not want to include them...
        # Here, we are hiding the foreign key.
        fields = ('entry',)

    def clean(self):
        cleaned_data = self.cleaned_data
        url = cleaned_data.get('url')

        # # If url is not empty and doesn't start with 'http://', prepend 'http://'.
        # if url and not url.startswith('http://'):
        #     url = 'http://' + url
        #     cleaned_data['url'] = url

        # return cleaned_data        

class UserForm(forms.ModelForm):
    username = forms.CharField(help_text="Please enter a username.")
    email = forms.CharField(help_text="Please enter your email.")
    password = forms.CharField(widget=forms.PasswordInput(), help_text="Please enter a password.")

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

class UserProfileForm(forms.ModelForm):
    website = forms.URLField(help_text="Please enter your website.", required=False)
    picture = forms.ImageField(help_text="Select a profile image to upload.", required=False)

    class Meta:
        model = UserProfile
        fields = ['website', 'picture']