# Factory Method

O padrão Factory Method é um padrão de projeto criacional que define uma interface para criar objetos em uma superclasse, mas permite que subclasses alterem o tipo de objetos que serão criados.

## Problema

Quando temos uma hierarquia de classes e desejamos criar objetos dessas classes, precisamos decidir qual classe concreta instanciar. Isso pode levar à violação do princípio do Open/Closed do SOLID, pois precisamos modificar o código da superclasse sempre que uma nova classe concreta for adicionada.

## Solução

O Factory Method resolve esse problema definindo um método na superclasse para criar objetos, mas deixando que as subclasses escolham qual classe concreta instanciar.

## Exemplo

No exemplo fornecido, temos a classe abstrata `Carro` que define o método `dirigir()`. As subclasses concretas `CarroSedan` e `CarroHatch` implementam esse método. A classe abstrata `FabricaCarros` define o método abstrato `fabricar_carro()`, enquanto `FabricaCarroSedan` e `FabricaCarroHatch` são subclasses concretas que implementam esse método para criar instâncias de `CarroSedan` e `CarroHatch`, respectivamente.
