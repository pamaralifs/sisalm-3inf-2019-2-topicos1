# Arquivo criado para implementar filtro na view listview
from django.forms import ModelForm
from fornecedor.models import Fornecedor


class FornecedorMeuFormFiltro(ModelForm):
    class Meta:
        model = Fornecedor
        fields = ['nome']

