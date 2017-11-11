(function() {
    // Permutador de máscaras
    function inputHandler(masks, max, event) {
        var c = event.target;
        var v = c.value.replace(/\D/g, '');
        var m = c.value.length > max ? 1 : 0;
        VMasker(c).unMask();
        VMasker(c).maskPattern(masks[m]);
        c.value = VMasker.toPattern(v, masks[m]);
      }
      
      // CPF
      VMasker(document.querySelector("#cpf")).maskPattern("999.999.999-99");
      
      // RG
      VMasker(document.querySelector("#rg")).maskPattern("99.999.999-9");

      // CEP
      VMasker(document.querySelector("#cep")).maskPattern("99999-999");

      // Telefone
      var telMask = ['9999-99999', '99999-9999'];
      var tel = document.querySelector('#telefone');
      VMasker(tel).maskPattern(telMask[0]);
      tel.addEventListener('input', inputHandler.bind(undefined, telMask, 9), false);
})();
