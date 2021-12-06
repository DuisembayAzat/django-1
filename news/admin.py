from django.contrib import admin
from .models import Articles
# Register your models here.
#после тога ка мы создали таблицу и мигрировали ее нужно зарегестрировать ее здесь чтобы она отобразилась на сайте

admin.site.register(Articles)