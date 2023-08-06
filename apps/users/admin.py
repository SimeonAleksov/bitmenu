from django.contrib import admin
from django_tenants.admin import TenantAdminMixin

from apps.users.models import Client
from apps.users.models import Domain
from apps.users.models import Membership
from apps.users.models import Team
from apps.users.models import User


@admin.register(Client)
class ClientAdmin(TenantAdminMixin, admin.ModelAdmin):
    list_display = (
        'name',
        'paid_until',
    )


@admin.register(Domain)
class DomainAdmin(TenantAdminMixin, admin.ModelAdmin):
    pass


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'last_login',
        'is_superuser',
        'username',
        'email',
        'is_staff',
        'is_active',
        'date_joined',
        'created_at',
        'updated_at',
        'company',
        'phone_number',
    )
    list_filter = (
        'last_login',
        'is_superuser',
        'is_staff',
        'is_active',
        'date_joined',
        'created_at',
        'updated_at',
    )
    raw_id_fields = ('groups', 'user_permissions')
    date_hierarchy = 'created_at'


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('id', 'team_name', 'subscription')
    list_filter = ('subscription',)
    raw_id_fields = ('members',)


@admin.register(Membership)
class MembershipAdmin(admin.ModelAdmin):
    list_display = ('id', 'team', 'user', 'customer')
    list_filter = (
        'team',
        'user',
        'customer',
    )
