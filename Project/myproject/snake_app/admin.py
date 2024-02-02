from django.contrib import admin
from snake_app.models import user,snake
from .models import DeepLearningModel

# Register your models here.
admin.site.register(user)
admin.site.register(snake)
admin.site.register(DeepLearningModel)
