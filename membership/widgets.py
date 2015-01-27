from django.forms.widgets import Widget, FileInput, ClearableFileInput, CheckboxInput, FILE_INPUT_CONTRADICTION
from django.template.context import Context
from django.template.loader import get_template
from django.core.files.storage import default_storage
from django.core.files.uploadedfile import InMemoryUploadedFile
from StringIO import StringIO
from PIL import Image
try:
    import json
except ImportError:
    import simplejson as json
from barnabe.settings import MEDIA_URL
from django.conf import settings

class JCropImageWidget(ClearableFileInput):
    ratio = '0'
    jquery_alias = None

    def __init__(self, *args, **kwargs):
        if 'attrs' in kwargs:
            if 'ratio' in kwargs['attrs']:
                self.ratio = kwargs['attrs'].pop('ratio')
            if 'jquery_alias' in kwargs['attrs']:
                self.jquery_alias = kwargs['attrs'].pop('jquery_alias')

        return super(JCropImageWidget, self).__init__(*args, **kwargs)

    def value_from_datadict(self, data, files, name):
        return super(JCropImageWidget, self).value_from_datadict(data,
                                                                   files,
                                                                   name)

    def render(self, name, value, attrs=None):
        t = get_template("jcrop/jcrop_image_widget.html")
        substitutions = {
            "input_name": name,
            "image_value": value,
            "image_crop_data_value": value.instance.photo_crop_data if value is not None else "",
            "image_original_value": value.instance.photo_original if value is not None else "",
            "ratio": self.ratio,
            "jquery_alias": self.jquery_alias,
            "MEDIA_URL": settings.MEDIA_URL,
            "JCROP_IMAGE_THUMBNAIL_DIMENSIONS": getattr(
                settings, "JCROP_IMAGE_THUMBNAIL_DIMENSIONS", "62x62"
            ),
            "JCROP_IMAGE_WIDGET_DIMENSIONS": getattr(
                settings, "JCROP_IMAGE_WIDGET_DIMENSIONS", "320x320"
            ),
        }
        c = Context(substitutions)

        if (not value):
            clearable_input_render = super(JCropImageWidget, self).render(
                name, value, attrs
            )
        else:
            clearable_input_render = ""
        return clearable_input_render + t.render(c)

    class Media:
        css = {
            'all': ('css/jquery.Jcrop.min.css', ),
        }

        js = ('js/jquery.color.js', 'js/jquery.Jcrop.min.js', 'js/fancy-image-upload-widget.js', )
