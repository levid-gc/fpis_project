from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from .models import Team, UserProfile


class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'exact_type', 'was_added_recently')


class ProfileInline(admin.StackedInline):
    model = UserProfile
    #fk_name = 'user'
    max_num = 1
    can_delete = False


class CustomUserAdmin(UserAdmin):
    inlines = [ProfileInline,]


admin.site.register(Team, TeamAdmin)
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)


