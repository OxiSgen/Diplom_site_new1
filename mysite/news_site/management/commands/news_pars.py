from django.core.management.base import BaseCommand, CommandError
from mysite.news_site.models import News


def funk():
    print("---")

class Command(BaseCommand):
    help = 'News_pars from url to db'

    def add_arguments(self, parser):
        '''
        parser.add_argument('poll_ids', nargs='+', type=int)
        '''

    def handle(self, *args, **options):
        '''
        for poll_id in options['poll_ids']:
            try:
                poll = News.objects.get(pk=poll_id)
            except News.DoesNotExist:
                raise CommandError('Poll "%s" does not exist' % poll_id)

            poll.opened = False
            poll.save()

            self.stdout.write(self.style.SUCCESS('Successfully closed poll "%s"' % poll_id))
        '''