from django.contrib import admin
from hotelinfo.models import hotelinfo
# Register your models here.
@admin.register(hotelinfo)
class HotelAdmin(admin.ModelAdmin):
    list_display = ['hotel_name','left_home']
    readonly_fields = ['hotel_name','location','pinfen','customer','price','images','city']
    def get_queryset(self, request):
        qs=super(HotelAdmin,self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        else:
            name=request.user.username
            return qs.filter(hotel_name=name)