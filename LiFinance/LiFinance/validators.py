import django.contrib.auth.password_validation as pv
from django.utils.translation import gettext as _

class SimilarValidator(pv.UserAttributeSimilarityValidator):
    def get_error_message(self):
        return _("Пароль очень похож на логин")


class MinLengthValidator(pv.MinimumLengthValidator):
    def get_error_message(self):
        return _("Пароль должен содержать как минимум 8 символов")
    

class CommonValidator(pv.CommonPasswordValidator):
    def get_error_message(self):
        return _("Пароль слишком распространный")