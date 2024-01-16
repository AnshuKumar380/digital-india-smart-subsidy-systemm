from django.contrib import admin
from service.models import Contact, Schemesinfo, Applications
from django.contrib.auth.admin import UserAdmin


class ContactAdmin(admin.ModelAdmin):
    list_display=('name', 'email', 'message')
admin.site.register(Contact, ContactAdmin)

class SchemesinfoAdmin(admin.ModelAdmin):
    list_display=('schemename', 'citizensip', 'State','age', 'gender', 'caste', 'rationcard', 'employmentStatus', 'aadhaarnumber', 'link')
admin.site.register(Schemesinfo, SchemesinfoAdmin)

# class ApplicationsAdmin(admin.ModelAdmin):
#     list_display=('first_name', 'lastname', 'date_of_birth', 'citizensip', 'state',
#         'age', 'gender', 'caste', 'rationcard', 'employmentStatus','aadhaarnumber','schemename')
# admin.site.register(Applications, ApplicationsAdmin)


def approve_applications(modeladmin, request, queryset):
    queryset.update(is_approved=True)

approve_applications.short_description = "Approve selected applications"

class ApplicationsAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'lastname', 'date_of_birth', 'citizensip', 'state',
        'age', 'gender', 'caste', 'rationcard', 'employmentStatus','aadhaarnumber','schemename', 'is_approved']

    def save_model(self, request, obj, form, change):
        # Check if the is_approved checkbox is checked in the admin form
        is_approved = form.cleaned_data.get('is_approved')

        if is_approved:
            obj.is_approved = True
            obj.save()
        else:
            # If not approved, you might want to take some other action or not save at all
            # For example, you can redirect the user to a rejection page or raise an exception
            pass

admin.site.register(Applications, ApplicationsAdmin)



# Register your models here.
