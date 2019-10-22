from django.db import models
from django.utils import timezone

from django.utils.safestring import mark_safe #para exibir foto e usar mark_safe() na string
#da imagem, caso contrário, terá um código html escapado em vez da thumbnail no django-admin

def subdiretorio_foto_produto(instance, filename):
    #Upload do arquivo para MEDIA_ROOT/produto/<id>/<filename>
    return 'fotos/produto/{0}/{1}'.format(instance.id, filename)

class Produto(models.Model):
    TIPO_CHOICES = (
        ("Material de consumo","Material de consumo"),
        ("Material permanente","Material permanente")
    )
    #id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=50,null=False,verbose_name="Nome",unique=True)
    descricao = models.TextField(verbose_name="Descrição")
    preco = models.DecimalField(max_digits=9,decimal_places=2,verbose_name="Preço")
    qtd_estoque = models.IntegerField(verbose_name="Estoque",help_text="Informe a quantidade atual")
    tipo = models.CharField(max_length=20,choices=TIPO_CHOICES,default="Material de consumo",
           verbose_name="Tipo")
    data_cadastro = models.DateTimeField(default=timezone.now,verbose_name="Data criação")
    foto = models.ImageField(upload_to=subdiretorio_foto_produto,null=True,default=None,
           verbose_name="Foto")
    
    def __str__(self):
        return self.nome

    def foto_tag(self):  #método para poder exibir a foto
        if self.foto:
            return mark_safe('<img src="%s" style="width: 45px; height:45px;" />' % self.foto.url)
        else:
            return 'Foto não encontrada'
    foto_tag.short_description = 'Foto do produto'
    
    def total(self):
         return self.preco * self.qtd_estoque
    total.short_description = 'Valor total estoque'
