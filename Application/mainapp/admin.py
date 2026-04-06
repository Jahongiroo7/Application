from django.contrib import admin
from .models import Application, Category, Worker

@admin.register(Application)
class Application_Admin(admin.ModelAdmin):
    """  """
    list_display = ('name', 'category', 'phone1', 'applicant', 'status')
    list_filter = ('status', 'category', 'created_on')
    search_fields = ('name', 'body', 'phone1', 'phone2')
    list_per_page = 5
@admin.register(Category)
class Category_Admin(admin.ModelAdmin):
    """  """
    list_display = ('name', 'status')
    list_filter = ('status', )
@admin.register(Worker)
class Worker_Admin(admin.ModelAdmin):    
    """  """
    list_display = ('full_name', 'phone1', 'stage', 'status')
    list_filter = ('status',)