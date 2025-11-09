from django.contrib import admin

from hello.models import HelloWorld


# Register your models here.
@admin.register(HelloWorld)
class HelloWorldAdmin(admin.ModelAdmin):
    pass
