import json
from django.utils.translation import ugettext as _

class BarnabeError(Exception):
    def __init__(self):
        pass

    def __str__(self):
        return self.msg

    def response_error(self):
        return json.dumps({'error_msg': self.msg, 'error': self.error})


class ImageNotJpgOrPngError(BarnabeError):
    error = "IMAGE_NOT_JPG_OR_PNG"
    msg = _('Only jpg and png format is permitted.')

class ImageNotRecognized(BarnabeError):
    error = "IMAGE_NOT_RECOGNIZED"
    msg = _('The file is not a image or corrupted.')

class ImageLessThan512(BarnabeError):
    error = 'IMAGE_LESS_THAN_512x512'
    msg = _('Image must be at least 512x512 resolution.')

class GetRequestNotPermitted(BarnabeError):
    error = "GET_REQUEST_NOT_PERMITTED"
    msg = _('Get request is not permitted.')
