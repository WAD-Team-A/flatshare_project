from django import forms
from django.utils.timezone import now
from flatshare.models import Flat, Address


class AddAddressForm(forms.ModelForm):
    help_text=("Please enter an address for your flat")
    flat_no = forms.CharField()
    house_no = forms.IntegerField()
    street = forms.CharField()
    city = forms.CharField()
    province = forms.CharField()
    postcode = forms.CharField()
    country = forms.CharField()

    class Meta:
        model = Address
        fields = ('flat_no','house_no', 'street', 'city', 'province', 'postcode', 'country')


class AddFlatForm(forms.ModelForm):
    help_text = ("Please enter flat details.")
    name = forms.CharField()
    address = AddAddressForm
    rent = forms.IntegerField(initial=0)
    description = forms.TextInput()
    image1 = forms.ImageField()
    image2 = forms.ImageField()
    available_from = forms.DateField(initial=now())
    #likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)
    class Meta:
        model = Flat
        fields = ('name','address', 'rent', 'description', 'image1', 'image2', 'available_from')


# class PageForm(forms.ModelForm):
#     title = forms.CharField(max_length=128,
#     help_text="Please enter the title of the page.")
#     url = forms.URLField(max_length=200,
#     help_text="Please enter the URL of the page.")
#     views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
#     class Meta:
#         model = Page
# What fields do we want to include in our form?
# This way we don't need every field in the model present.
# Some fields may allow NULL values; we may not want to include them.
# Here, we are hiding the foreign key.
# we can either exclude the category field from the form,
exclude = ('category',)
# or specify the fields to include (don't include the category field).
#fields = ('title', 'url', 'views')