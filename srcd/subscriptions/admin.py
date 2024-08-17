from django.contrib import admin

# Register your models here.
from .models import Subscription, UserSubscription, SubscriptionPrice

class SubscriptionPrice(admin.TabularInline):
    model = SubscriptionPrice
    readonly_fields = ['stripe_id']
    can_delete = False
    extra = 0
   

class SubscriptionAdmin(admin.ModelAdmin):
    inlines = [SubscriptionPrice]
    list_display = ['name', "active"]


admin.site.register(Subscription, SubscriptionAdmin)
admin.site.register(UserSubscription)