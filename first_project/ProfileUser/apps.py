from __future__ import unicode_literals

from django.apps import AppConfig

from django.utils.translation import ugettext_lazy as _

class ProfileuserConfig(AppConfig):
    name = 'ProfileUser'
    # verbose_name = _('ProfileUser')

    def ready(self):
        import ProfileUser.signals