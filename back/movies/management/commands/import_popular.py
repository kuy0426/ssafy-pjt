# movies/management/commands/import_popular.py

from django.core.management.base import BaseCommand
from movies.services.tmdb import sync_popular

class Command(BaseCommand):
    help = 'TMDB 인기 영화 여러 페이지를 가져와 동기화합니다.'

    def add_arguments(self, parser):
        parser.add_argument(
            '--pages',
            type=int,
            default=1,
            help='가져올 페이지 수 (한 페이지당 약 20개 영화)'
        )

    def handle(self, *args, **options):
        pages = options['pages']
        self.stdout.write(f"Importing popular movies, pages=1..{pages}")
        sync_popular(max_pages=pages)
        self.stdout.write(self.style.SUCCESS("✅ Done importing popular movies."))
