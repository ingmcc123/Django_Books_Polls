from django.apps import AppConfig


class BooksConfig(AppConfig):
    name = 'books'

    # 애플리케이션 리스트에서 이름 설정
    verbose_name = '공부할 때 참고한 도서'
