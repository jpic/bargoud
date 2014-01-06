from optparse import make_option

import soundcloud

from django.core.management.base import BaseCommand, CommandError
from django.conf import settings


class Command(BaseCommand):
    args = '<...>'
    help = 'Update data'

    """
    option_list = BaseCommand.option_list + (
        make_option('--template',
            action='store',
            default='',
            help='Delete poll instead of closing it'
        ),
    )
    """

    def handle(self, *args, **options):
        self.verbosity = int(options.get('verbosity'))

        client = soundcloud.Client(client_id=settings.SOUNDCLOUD_CLIENT_ID)
        tracks = client.get('/users/%s/tracks' % settings.SOUNDCLOUD_USER_ID,
                            limit=50)

        if self.verbosity >= 1:
            print 'Cms_Update complete'
