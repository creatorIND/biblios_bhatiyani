"""
Book model for tracking reading progress.
Requirements: title, author, pages, summary, genre, cover_image, status, current_page, user, timestamps
"""

from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator


class Book(models.Model):
    """
    Book model for user's reading list
    """

    # Status choices as specified
    STATUS_CHOICES = [
        ("want_to_read", "Want to Read"),
        ("reading", "Reading"),
        ("finished", "Finished"),
    ]

    # Genre choices as specified
    GENRE_CHOICES = [
        ("fiction", "Fiction"),
        ("non_fiction", "Non-Fiction"),
        ("mystery", "Mystery"),
        ("romance", "Romance"),
        ("sci_fi", "Sci-Fi"),
        ("biography", "Biography"),
        ("self_help", "Self Help"),
        ("history", "History"),
        ("fantasy", "Fantasy"),
        ("thriller", "Thriller"),
        ("other", "Other"),
    ]

    # Required fields
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    pages = models.IntegerField(validators=[MinValueValidator(1)])

    # Optional fields
    summary = models.TextField(blank=True, null=True)
    genre = models.CharField(max_length=20, choices=GENRE_CHOICES, default="other")
    cover_image = models.ImageField(
        upload_to="book_covers/",
        blank=True,
        null=True,
        help_text="Optional book cover image",
    )

    # Reading progress fields
    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default="want_to_read"
    )
    current_page = models.IntegerField(default=0, validators=[MinValueValidator(0)])

    # Relationship
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="books"
    )

    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "books"
        ordering = ["-created_at"]  # Newest books first
        verbose_name = "Book"
        verbose_name_plural = "Books"

    def __str__(self):
        return f"{self.title} by {self.author}"

    @property
    def progress_percentage(self):
        # Calculate reading progress as percentage
        if self.pages and self.pages > 0:
            current = self.current_page or 0
            return min(round((current / self.pages) * 100, 2), 100)
        return 0

    @property
    def pages_remaining(self):
        # Calculate remaining pages to read
        if self.pages:
            current = self.current_page or 0
            return max(self.pages - current, 0)
        return 0

    def save(self, *args, **kwargs):
        """Override save to ensure current_page doesn't exceed total pages."""
        # Ensure current_page is not None
        if self.current_page is None:
            self.current_page = 0

        # Ensure current_page doesn't exceed total pages
        if self.pages and self.current_page > self.pages:
            self.current_page = self.pages

        # Auto-update status based on progress (only if not manually set)
        if self.pages and self.current_page >= self.pages:
            self.status = "finished"
        elif self.current_page > 0 and self.status == "want_to_read":
            self.status = "reading"

        super().save(*args, **kwargs)
