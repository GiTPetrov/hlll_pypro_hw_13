from django.db import models


class QuoteAuthor(models.Model):
    author_name = models.CharField(max_length=100)
    author_birthdate = models.DateField()
    author_birthplace = models.CharField(max_length=100)
    author_description = models.TextField()

    def __str__(self):
        return self.author_name


class Quote(models.Model):
    quote_text = models.CharField(max_length=300)
    quote_author = models.ForeignKey(QuoteAuthor, blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.quote_text
