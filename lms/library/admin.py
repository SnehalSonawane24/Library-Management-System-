from django.contrib import admin
from library.models import Book, BookGenre, BookReview, StudentFeedback

# Register your models here.
@admin.register(BookGenre)
class BookGenreAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "author", "genre", "edition", "published_date")
    search_fields = ("title", "author")
    list_filter = ("genre", "published_date")


@admin.register(BookReview)
class BookReviewAdmin(admin.ModelAdmin):
    list_display = ("id", "book", "student", "rating", "created_at")
    search_fields = ("book__title", "student__email")
    list_filter = ("rating", "created_at")


@admin.register(StudentFeedback)
class StudentFeedbackAdmin(admin.ModelAdmin):
    list_display = ("id", "student", "created_at")
    search_fields = ("student__email",)
    list_filter = ("created_at",)