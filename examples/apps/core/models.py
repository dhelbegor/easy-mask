from django.db.models import Model, CharField
from django.utils.translation import ugettext_lazy as _



class PersonalData(Model):
    first_name    = CharField(_("nome"), max_length=100)
    last_name     = CharField(_("sobrenome"), max_length=100)   
    phone         = CharField(_("telefone"), max_length=10)
    cell          = CharField(_("celular"), max_length=11)
    cpf           = CharField(_("cpf"), max_length=11)
    cnpj          = CharField(_("cnpj"), max_length=14)
    cep           = CharField(_("cep"), max_length=8)
    ncm           = CharField(_("ncm"), max_length=8)
    isbn          = CharField(_("isbn"), max_length=13)

    class Meta:
        ordering = ['first_name']
        verbose_name = 'dado pessoal'
        verbose_name_plural = 'dados pessoais'

    def __str__(self):
        return self.first_name + ' ' + self.last_name

    full_name = property(__str__)
