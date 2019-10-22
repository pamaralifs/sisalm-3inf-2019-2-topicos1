from django.contrib import admin
from .models import Produto


# Register your models here.
#admin.site.register(Produto)  antes

#Classe para exibir foto com a ferramenta Admin
class ProdutoAdmin(admin.ModelAdmin): 
   list_display = ['nome','foto_tag','data_cadastro','preco','qtd_estoque','total'] #Para mostrar foto na página de listagem
   readonly_fields = ['foto_tag'] #Para mostrar foto na página do produto
   #fields = ['nome','foto_tag']
   #fields = ['nome','descricao'] #Original
   #list_filter = ['nome', 'descricao','qtd_estoque']
   search_fields = ['nome']
   ordering = ['-data_cadastro','nome'] #Lista order by, com "-" é DESC ou DESCENDING
   #Ou criar o método aqui
   #def total(self, obj):
   #   return obj.preco * obj.qtd_estoque
   list_per_page = 1  #O valor default é 100 itens por página
   #list_max_show_all O valor padrão mostrar tudo é 200

admin.site.register(Produto, ProdutoAdmin)  #Registro dos dois modelos no admin

