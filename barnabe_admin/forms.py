from bootstrap3_datetime.widgets import DateTimePicker
from django.forms.fields import DateField
from django.utils.translation import ugettext as _
from django_localflavor_br.forms import BRCPFField, BRZipCodeField, BRPhoneNumberField
from form_utils.forms import BetterModelForm
from input_mask.contrib.localflavor.br.widgets import BRCPFInput, BRZipCodeInput, BRPhoneNumberInput
from membership.models import Member, Person


class MemberForm(BetterModelForm):
    baptism_date = DateField(widget=DateTimePicker(options={"format": "DD/MM/YYYY",
                                       "pickTime": False}), label=_('Baptism date'))
    admission_date = DateField(widget=DateTimePicker(options={"format": "DD/MM/YYYY",
                                       "pickTime": False}), label=_('Admission date'))
    class Meta:
        model=Member
        fieldsets=[('Member Information', {'fields': ['previous_church', 'baptism_date', 'baptism_place',
                                                        'admission_date', 'member_function', 'situation', 'church']}),
                    ]
        exclude=['person']

class PersonForm(BetterModelForm):
    cpf = BRCPFField(required=False, label='CPF', widget=BRCPFInput)
    zipcode = BRZipCodeField(required=False, label=_('Zipcode'), widget=BRZipCodeInput)
    phone1 = BRPhoneNumberField(required=False, label=_('Phone 1'), widget=BRPhoneNumberInput)
    phone2 = BRPhoneNumberField(required=False, label=_('Phone 2'), widget=BRPhoneNumberInput)
    birth_date = DateField(widget=DateTimePicker(options={"format": "DD/MM/YYYY",
                                       "pickTime": False}), label=_('Birth date'))

    class Meta:
        model = Person
        fieldsets = [('Personal Information', {'fields': ['name', 'cpf', 'rg', 'birth_date', 'gender', 'blood_type', 'photo']}),
                     ('Contact Information', {'fields': ['email', 'address_line', 'neighborhood', 'city', 'state',
                                                'zipcode', 'phone1', 'phone2']}),
                     ('Ocupation Information', {'fields': ['profession', 'work_place']}),
                     ('Family Information', {'fields': ['father_name', 'mother_name', 'marital_status', 'spouse',
                                                        'has_child', 'how_many_child']}),
                    ]