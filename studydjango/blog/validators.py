import re
import requests
from django.conf import settings
from django.forms import ValidationError
from django.utils.deconstruct import deconstructible
import xmltodict

@deconstructible
class MinLengthValidatior(object):
    def __init__(self, min_length):
        self.min_length = min_length

    def __call__(self, value):
        if len(value) < self.min_length:
            raise ValidationError("{}글자 이상 입력해주세요.".format(self.min_length))

@deconstructible
class ZipCodeValidator(object):
    def __init__(self, is_check_exist = False):
        self.is_check_exist = is_check_exist

    def __call__(self, zip_code):
        if not re.match(r'^\d{5}$', zip_code):
            raise ValidationError('5자리 숫자로 입력해주세요.')
        if self.is_check_exist:
            self.check_exist(zip_code)

    def check_exist(self, zip_code):
        params = {
            'regkey': settings.EPOST_API_KEY,
            'target': 'postNew',
            'query': zip_code,
        }
        xml = requests.get('http://biz.epost.go.kr/KpostPortal/openapi', params=params).text
        response = xmltodict.parse(xml)
        try:
            error = response['error']
        except KeyError:
            pass
        else:
            raise ValidationError('[{error_code}] {message}'.format(**error))

#da1560600eced7fed1470021722002
def lnglat_validator(lnglat):
    if not re.match(r'^(\d+\.?\d*),(\d+\.?\d*)$', lnglat):
        raise ValidationError('Invalid LngLat Type')

def phone_number_validator(value):
    if not re.match(r'^01[06789][1-9]\d{6,7}$', value):
        raise ValidationError("휴대폰 번호를 입력해주세요.")