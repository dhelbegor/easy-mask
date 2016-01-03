from django import template


register = template.Library()


class PhoneRegex():
    @register.filter(name='phone')
    def PhoneMask(PHONE):
        """ Return (00) 0000-0000 or (00) 00000-0000 """
        try:
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
        except ValueError:
            print('error in the counting of numeric characters')


class CpfRegex():
    @register.filter(name='cpf')
    def CpfMask(CPF):
        """ Return 000.000.000-00 """
        a = CPF[0:3]
        b = CPF[3:6]
        c = CPF[6:9]
        d = CPF[9:11]
        return a + '.' + b + '.' + c + '-' + d


class RgRegex():
    @register.filter(name='rg')
    def RgMask(RG):
        """ Return 00.000.000-0 or 0.000.000 or 0.000.000-00 """
        pass


class CnpjRegex():
    @register.filter(name='cnpj')
    def CnpjMask(CNPJ):
        """ Return 00.000.000/0000-00 """
        a = CNPJ[0:2]
        b = CNPJ[2:5]
        c = CNPJ[5:8]
        d = CNPJ[8:12]
        e = CNPJ[12:14]
        return a + '.' + b + '.' + c + '/' + d + '-' + e


class CepRegex():
    @register.filter(name='cep')
    def CepMask(CEP):
        """ Return 00000-000 """
        a = CEP[0:5]
        b = CEP[5:8]
        return a + '-' + b


class NcmRegex():
    @register.filter(name='ncm')
    def NcmMask(NCM):
        """ Return 0000.00.00 """
        a = NCM[0:4]
        b = NCM[4:6]
        c = NCM[6:8]
        return a + '.' + b + '.' + c
