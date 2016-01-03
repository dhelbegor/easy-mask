#easy-mask

Um simples pacote para uso de máscaras no django [demo]

##Instalação

    pip install easy-mask
    
    
##Configuração

Adicione o pacote ao [__INSTALLED_APPS__](https://docs.djangoproject.com/en/1.9/ref/settings/#installed-apps)

para usar o mesmo basta adicionar {% load easy_mask %} no inicio de template/html .

##exemplo de uso

    {% for data in personal %}
      <tr>
        <td>{{ data.cpf | cpf }}</td>
        <td>{{ data.phone | phone }}</td>
        <td>{{ data.cnpj | cnpj }}</td>
        <td>{{ data.cep | cep }}</td>
      </tr>
    {% endfor %}

##observação

As máscaras existentes são

- phone
- cnpj
- cpf
- cep

Gostaria de ver alguma máscara que ainda não existe no projeto? então abra uma issue __[aqui]__, e deixe na descrição um exemplo de como seria essa máscara :D .

[aqui]:https://github.com/dhelbegor/easy-mask/issues
[demo]:https://easy-mask.herokuapp.com
