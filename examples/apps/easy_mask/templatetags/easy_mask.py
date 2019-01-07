from django import template



register = template.Library()

@register.filter(name='phone')
def phone_mask(item, mask="({}) {}-{}"):
    """ return (00) 00000-0000 or (00) 0000-0000  """
    if item and len(item) >=11:
        return mask.format(
            item[0:2],
            item[2:7],
            item[7:11]
        )
    elif item:
        return mask.format(
            item[0:2],
            item[2:6],
            item[6:10]
        )

@register.filter(name='cpf')
def cpf_mask(item, mask="{}.{}.{}-{}"):
    """ return 000.000.000-00 """
    if item:
        return mask.format(
            item[0:3],
            item[3:6],
            item[6:9],
            item[9:11]
        )
    else:
        return None

@register.filter(name='rg')
def rg_mask(item, mask="{}.{}.{}-{}", other_mask="{}.{}.{}"):
    """
    return 00.000.000-0 or 0.000.000
    in this case I was have to create another mask to work with in both objects
    """
    if item and len(item) >=8:
        return mask.format(
            item[0:2],
            item[2:5],
            item[5:8],
            item[8:9]
        )
    else:
        return other_mask.format(
            item[0:1],
            item[1:4],
            item[4:7]
        )

@register.filter(name='cnpj')
def cnpj_mask(item, mask="{}.{}.{}/{}-{}"):
    """ return 00.000.000/0000-00 """
    if item:
        return mask.format(
            item[0:2],
            item[2:5],
            item[5:8],
            item[8:12],
            item[12:14]
        )
    else:
        return None

@register.filter(name='cep')
def cep_mask(item, mask="{}-{}"):
    """ Return 00000-000 """
    if item:
        return mask.format(
            item[0:5],
            item[5:8]
    )
    else:
        return None

@register.filter(name='ncm')
def ncm_mask(item, mask="{}.{}.{}"):
    """ Return 0000.00.00 """
    if item:
        return mask.format(
            item[:4],
            item[4:6],
            item[6:8]
        )
    else:
        return None

@register.filter(name='isbn')
def isbn_mask(item, mask="{}-{}-{}-{}-{}", other_mask="{}-{}-{}-{}"):
    """ Return 0-000-00000-0 or 000-00-000-0000-0 """
    if item and len(item) >=13:
        return mask.format(
            item[0:3],
            item[3:5],
            item[5:8],
            item[8:12],
            item[12:13]
        )
    else:
        return other_mask.format(
            item[0:1],
            item[1:4],
            item[4:9],
            item[9:10]
        )
