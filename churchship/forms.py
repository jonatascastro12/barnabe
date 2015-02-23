from django.forms.models import ModelForm
from churchship.models import Church

class ChurchForm(ModelForm):
    class Meta:
        model = Church
        exclude = ('church_mother', 'is_mother', 'type', 'logo_original', 'logo_crop_data')