from django.db import models
from django_extensions.db.models import TitleSlugDescriptionModel


# Create your models here.
class HelloWorld(TitleSlugDescriptionModel, models.Model):
    def slugify_function(self, content):
        """
        This function will be used to slugify
        the title (default `populate_from` field)
        """
        return content.replace("_", "-").lower()
