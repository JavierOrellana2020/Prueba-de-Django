from django.contrib import admin
from .models import Producto
from .models import Marca
from .models import Categoria
from .models import Sucursal

class productoAdmin(admin.ModelAdmin):
	list_display 		= ['codigo', 
							'marca', 'categoria',
							'descripcion',
							'stock', 'precioCosto',
							'precioVenta']
	list_display_links 	= ['codigo', 'descripcion']

	list_filter			= ['descripcion']
	
	search_fields		= ['codigo', 'descripcion']

admin.site.register(Producto, productoAdmin)


class MarcaAdmin(admin.ModelAdmin):
	list_display 		= ['nombre', 'activo']
	list_filter			= ['nombre']
	search_fields		= ['nombre']

class CategoriaAdmin(admin.ModelAdmin):
	list_display 		= ['nombre', 'activo']
	list_filter			= ['nombre']
	search_fields		= ['nombre']

admin.site.register(Marca, MarcaAdmin)
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Sucursal)

