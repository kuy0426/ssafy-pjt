from django.core.management.base import BaseCommand
from movies.services.tmdb import sync_popular

class Command(BaseCommand):
    help = "TMDB 인기 영화 여러 페이지를 DB에 저장합니다."

    def add_arguments(self, parser):
        parser.add_argument(
            "--pages",
            type=int,
            default=3,
            help="가져올 페이지 수 (1페이지≈20편). 예) --pages 5"
        )

    def handle(self, *args, **options):
        pages = options["pages"]
        self.stdout.write(f"인기 영화 {pages}페이지 동기화 시작…")
        sync_popular(max_pages=pages)
        self.stdout.write(self.style.SUCCESS("✅ 완료!"))
