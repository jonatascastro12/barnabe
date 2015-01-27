from bootstrap3_datetime.widgets import DateTimePicker
from django.forms.fields import DateField, ImageField
from django.forms.models import ModelForm, inlineformset_factory
from membership.models import Member, Person
from membership.widgets import JCropImageWidget


class MemberForm(ModelForm):
    baptismDt = DateField(widget=DateTimePicker(options={"format": "DD/MM/YYYY",
                                       "pickTime": False}), label="Data de Batismo")
    class Meta:
        model = Member
        exclude = ['person']

class PersonForm(ModelForm):
    class Meta:
        model = Person

class PersonMainForm(ModelForm):
    birthDt = DateField(widget=DateTimePicker(options={"format": "DD/MM/YYYY",
                                       "pickTime": False}), label="Data de Nascimento")
    photo = ImageField(widget=JCropImageWidget(attrs={'ratio': 1}))

    class Meta:
        model = Person
        exclude = ['member', 'user', 'phone1', 'phone2', 'address_line', 'city', 'state', 'neighborhood', 'photo_original', 'photo_crop_data']

class PersonContactForm(ModelForm):
    class Meta:
        model = Person
        exclude = ['member', 'user', 'name', 'birthDt', 'email', 'cpf', 'gender', 'photo', 'photo_original', 'photo_crop_data']
