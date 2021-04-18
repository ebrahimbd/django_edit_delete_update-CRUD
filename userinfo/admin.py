from django.contrib import admin


from . models import Savedata

admin.site.register(Savedata)

from . models import *

 
admin.site.register(Hotel)
 
 





class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'title', 'description' , 'city' , 'address' ,'birth_date')

# Register the admin class with the associated model
admin.site.register(Author, AuthorAdmin)



class AmiAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'first_name' , 'last_name' , 'date_joined' ,'is_active')

# Register the admin class with the associated model
admin.site.register(Ami, AmiAdmin)


class studentAdmin(admin.ModelAdmin):
    list_display = [ 'first_name', 'lastname',  'email']

admin.site.register(student, studentAdmin)

 