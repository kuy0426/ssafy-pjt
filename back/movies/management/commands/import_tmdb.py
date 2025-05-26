from django.core.management.base import BaseCommand
from movies.services.tmdb import sync_movie

class Command(BaseCommand):
    help = 'TMDB API로 영화 정보를 가져와 동기화합니다.'

    def add_arguments(self, parser):
        parser.add_argument(
            'tmdb_ids',
            nargs='+',
            type=int,
            help='동기화할 TMDB 영화 ID 목록'
        )

    def handle(self, *args, **options):
        for mid in options['tmdb_ids']:
            movie = sync_movie(mid)
            self.stdout.write(self.style.SUCCESS(
                f"[OK] {movie.original_title} (ID={movie.tmdb_id}) synced"
            ))
