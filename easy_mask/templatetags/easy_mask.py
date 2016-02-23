from django import template
from .utils import empty_phone, empty_cpf, empty_rg, empty_cnpj, empty_cep, empty_ncm, empty_isbn



register = template.Library()

@register.filter(name='phone')
def phone_mask(PHONE, empty="", placeholder=empty_phone):
    """ Return (00) 00000-0000 or (00) 0000-0000  """
    try:
        if PHONE is not empty:
            if len(PHONE) >=11:
                a = PHONE[0:2]
                b = PHONE[2:7]
                c = PHONE[7:11]
                return '(' + a + ')' + ' ' + b + '-' + c
            else:
                a = PHONE[0:2]
                b = PHONE[2:6]
                c = PHONE[6:10]
                return '(' + a + ')' + ' ' + b + '-' + c
        else:
            return placeholder
    except ValueError:
        pass



@register.filter(name='cpf')
def cpf_mask(CPF, empty="", placeholder=empty_cpf):
    """ Return 000.000.000-00 """
    if CPF is not empty:
        a = CPF[0:3]
        b = CPF[3:6]
        c = CPF[6:9]
        d = CPF[9:11]
        return a + '.' + b + '.' + c + '-' + d
    else:
        return placeholder
            


@register.filter(name='rg')
def rg_mask(RG, empty="", placeholder=empty_rg):
    """ Return 00.000.000-0 or 0.000.000 """
    try:
        if RG is not empty:
            if len(RG) >=7:
                a = RG[0:2]
                b = RG[2:5]
                c = RG[5:8]
                d = RG[8:9]
                return a + '.' + b + '.' + c + '-' + d
            else:
                a = RG[0:1]
                b = RG[1:4]
                c = RG[4:7]
                return a + '.' + b + '.' + c
        else:
            return placeholder
    except ValueError:
        pass



@register.filter(name='cnpj')
def cnpj_mask(CNPJ, empty="", placeholder=empty_cnpj):
    """ Return 00.000.000/0000-00 """
    if CNPJ is not empty:
        a = CNPJ[0:2]
        b = CNPJ[2:5]
        c = CNPJ[5:8]
        d = CNPJ[8:12]
        e = CNPJ[12:14]
        return a + '.' + b + '.' + c + '/' + d + '-' + e
    else:
        return placeholder



@register.filter(name='cep')
def cep_mask(CEP, empty="", placeholder=empty_cep):
    """ Return 00000-000 """
    if CEP is not empty:
        a = CEP[0:5]
        b = CEP[5:8]
        return a + '-' + b
    else:
        return placeholder



@register.filter(name='ncm')
def ncm_mask(NCM, empty="", placeholder=empty_ncm):
    """ Return 0000.00.00 """
    if NCM is not empty:
        a = NCM[0:4]
        b = NCM[4:6]
        c = NCM[6:8]
        return a + '.' + b + '.' + c
    else:
        return placeholder



@register.filter(name='isbn')
def isbn_mask(ISBN, empty="", placeholder=empty_isbn):
    """ Return 0-000-00000-0 or 000-00-000-0000-0 """
    try:
        if ISBN is not empty:
            if len(ISBN) >=13:
                a = ISBN[0:3]
                b = ISBN[3:5]
                c = ISBN[5:8]
                d = ISBN[8:12]
                e = ISBN[12:13]
                return a + '-' + b + '-' + c + '-' + d + "-" + e
            else:
                a = ISBN[0:1]
                b = ISBN[1:4]
                c = ISBN[4:9]
                d = ISBN[9:10]
                return a + '-' + b + '-' + c + "-" + d
        else:
            return placeholder
    except ValueError:
        pass