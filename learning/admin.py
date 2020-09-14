from django.contrib import admin

# Register your models here.
from .models import User   # 這邊一定要匯入User，感謝RelaxOP提醒
from django.contrib.auth.admin import UserAdmin

@admin.register(User)
class newUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'name', 'sex','email','phone','is_active','is_staff')
    list_filter = ('username','sex',)

#留言板
