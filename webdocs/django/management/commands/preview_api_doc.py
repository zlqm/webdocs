import os
from django.core.management import BaseCommand
from webdocs.preview.flask_app import app


class Command(BaseCommand):
    help = 'preview local openapi doc'

    def add_arguments(self, parser):
        parser.add_argument('doc_path', help='')

    def handle(self, *args, **options):
        os.environ.setdefault('API_DOC', options['doc_path'])
        app.run()
