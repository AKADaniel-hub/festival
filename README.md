# festival

adicionei o path dos dias ao urls.py, nao estaava a funcionar por o dias.html nao estar criado

criei o palcos view


concerto view.py corrigi o `concerto =` com erro de syntax
adicionei os imports ao mesmo


criei o template para os dias.hmtl

a pagina foi retornada vazia 

alterei o dias.py views e o dia.html e foi apresentada a informaçao correta 

mas nao dava paraclicar nos concertos adicionei href {% url 'concerto' concerto.id %} aambos

deu erro 404 no concerto/id por nao ter os imports necessarios 