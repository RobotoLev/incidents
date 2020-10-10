from django.contrib import admin
from django.contrib.auth.models import User, Group
from django.contrib.auth.admin import UserAdmin

from access.admin import AccessModelAdmin, AccessControlMixin
from . import models


# Register your models here.


admin.site.unregister(User)
# admin.site.unregister(Group)


@admin.register(User)
class AccessUserAdmin(AccessControlMixin, UserAdmin):
    def get_readonly_fields(self, request, obj=None):
        readonly_fields = super(AccessUserAdmin, self).get_readonly_fields(request, obj) or []
        if request.user.is_superuser:
            return readonly_fields
        if not obj:
            return readonly_fields
        restrict = ['is_superuser', 'last_login', 'date_joined', 'is_active']
        if obj.pk != request.user.pk:
            restrict = ['is_superuser', 'last_login', 'date_joined', 'is_active', 'password', 'email']
        return [f for f in readonly_fields if f not in restrict] + restrict

    def get_list_display(self, request):
        fields = super(AccessUserAdmin, self).get_list_display(request) or []
        if request.user.is_superuser:
            return fields
        restrict = ['password', 'email']
        return [f for f in fields if f not in restrict]

    def _fieldsets_only(self, fieldsets, only):
        ret = []
        for nm, params in fieldsets:
            if 'fields' not in params:
                ret.append((nm, params))
                continue
            fields = []
            for f in params['fields']:
                if f in only:
                    fields.append(f)
            pars = {}
            pars.update(params)
            pars['fields'] = fields
            ret.append((nm, pars))
        return ret

    def get_fieldsets(self, request, obj=None):
        fieldsets = list(super(AccessUserAdmin, self).get_fieldsets(request, obj)) or []
        fields = self.get_fields(request, obj=obj)
        return self._fieldsets_only(fieldsets, fields)

    def get_fields(self, request, obj=None):
        fields = list(super(AccessUserAdmin, self).get_fields(request, obj)) or []
        exclude = ['user_permissions']
        if not request.user.is_superuser:
            if obj:
                if obj.pk == request.user.pk:
                    exclude = ['is_staff', 'password', 'email', 'groups', 'user_permissions']
                else:
                    exclude = ['password', 'email', 'user_permissions']
        return [f for f in fields if f not in exclude]

    def save_model(self, request, obj, form, change):
        obj.is_staff = True
        return super(AccessUserAdmin, self).save_model(request, obj, form, change)


@admin.register(models.Profile)
class ProfileAdmin(AccessModelAdmin):
    pass


@admin.register(models.CommunicationsType)
class CommunicationsTypeAdmin(AccessModelAdmin):
    fields = ['name']
    list_display = ['name']


@admin.register(models.Communications)
class CommunicationsAdmin(AccessModelAdmin):
    fields = ['type', 'parameters']
    # list_display = ['type', 'parameters']


@admin.register(models.IncidentType)
class IncidentTypeAdmin(AccessModelAdmin):
    pass


@admin.register(models.Incident)
class IncidentAdmin(AccessModelAdmin):
    fields = ['communications_object', 'start_date', 'end_date', 'type', 'additional_info']
    list_display = ['communications_object', 'start_date', 'end_date', 'type', 'additional_info']
