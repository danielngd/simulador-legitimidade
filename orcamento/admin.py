from django.contrib import admin

from orcamento.models import (Produto, Imposto, Estado)

class ProdutoAdmin(admin.ModelAdmin):
    pass

class ImpostoAdmin(admin.ModelAdmin):
    pass

class EstadoAdmin(admin.ModelAdmin):
    pass


admin.site.register(Produto, ProdutoAdmin)
admin.site.register(Imposto, ImpostoAdmin)
admin.site.register(Estado, EstadoAdmin)
