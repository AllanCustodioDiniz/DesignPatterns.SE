# Adapter

O padrão Adapter é um padrão de projeto estrutural que permite que objetos com interfaces incompatíveis trabalhem juntos, envolvendo um adaptador que faz a interface do objeto existente funcionar com o sistema.

## Problema

Quando temos uma classe com uma interface incompatível com o sistema que desejamos integrar, precisamos de um mecanismo para adaptar a interface do objeto existente para que ele possa ser usado pelo sistema sem alterações.

## Solução

O Adapter resolve esse problema fornecendo um adaptador que converte a interface de um objeto existente para uma interface esperada pelo sistema, permitindo a colaboração entre objetos com interfaces incompatíveis.

## Exemplo

No exemplo fornecido, temos a classe `TomadaDeTresPinos` com uma interface de três pinos e a classe `TomadaDeDoisPinos` com uma interface de dois pinos. O `Adaptador` permite que `TomadaDeDoisPinos` seja usado como se fosse `TomadaDeTresPinos` através do método `ligar_na_tomada_de_tres_pinos()`.
