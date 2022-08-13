(function(win,doc) {
  'use strict';

  // Verificar se o usuario quer apagar ou nao
  if(doc.querySelector('.btnDel')){
    let btnDel = doc.querySelectorAll('.btnDel');
    for(let i=0; i < btnDel.length; i++){
      btnDel[i].addEventListener('click', function(event){
        if(confirm('Deseja apagar este dado ?')){
          return true;
        }
        else {
          event.preventDefault();
        }
      });
    }
  }
})(window, document);