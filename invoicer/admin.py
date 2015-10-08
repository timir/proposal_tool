from django.contrib import admin
from nested_inline.admin import NestedStackedInline, NestedModelAdmin
from.models import   Client, City, Mall, Proposal, Item, AvailableDate

class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'telephone')


class AvailableDateInline(NestedStackedInline):
    model = AvailableDate
    extra = 1 
    fk_name = 'client_name'

    
#    def get_extra (self, request, obj=None, **kwargs):
#        """Dynamically sets the number of extra forms. 0 if the related object
#        already exists or the extra configuration otherwise."""
#        if obj:
#            # Don't add any extra forms if the related object already exists.
#            return 0
#        return self.extra  

class ItemInline(NestedStackedInline):
    model = Item
    extra = 1 
    fk_name = 'client_name'
    inlines = [AvailableDateInline]
    
#    def get_extra (self, request, obj=None, **kwargs):
#        """Dynamically sets the number of extra forms. 0 if the related object
#        already exists or the extra configuration otherwise."""
#        if obj:
#            # Don't add any extra forms if the related object already exists.
#            return 0
#        return self.extra
 
    
  
class ProposalAdmin(NestedModelAdmin): 
    model = Proposal
    list_display = ('client_name', 'created_date')   
    
    inlines = [ItemInline]
    
    
    
admin.site.register(Client, ClientAdmin)
admin.site.register(City)
admin.site.register(Mall)
admin.site.register(Proposal, ProposalAdmin)
