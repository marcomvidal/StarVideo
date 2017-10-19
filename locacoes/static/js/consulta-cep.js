(function() {
    $('#cep').blur(function() {
        consultaCEP();
    });

    function consultaCEP() {
        var cep = $.trim($('#cep').val()),
        messageClass = 'm-notice',
        messageElement = $('#cep').closest('.group').find('.message');

        if (cep != '') {
            messageElement.addClass(messageClass).text('Pesquisando endereço...');
            $.getJSON("https://viacep.com.br/ws/"+ $("#cep").val() +"/json/?callback=?", function(dados) {
                if (!("erro" in dados)) {
                    // Atualiza os campos com os valores da consulta.
                    $("#endereco").val(dados.logradouro).addClass('ng-dirty');;
                    $("#cidade").val(dados.localidade).addClass('ng-dirty');
                    $("#uf").val(dados.uf).addClass('ng-dirty');
                    $('#numero').val('').focus();
                    messageElement.removeClass(messageClass).text('');
                } else {
                    messageElement.removeClass(messageClass).text('Endereço não encontrado');
                }
            });
        }
    }

})();