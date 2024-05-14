# Observer

O padrão Observer é um padrão de projeto comportamental que define uma dependência um-para-muitos entre objetos, de modo que quando um objeto muda de estado, todos os seus dependentes são notificados e atualizados automaticamente.

## Problema

Quando temos objetos que precisam ser notificados sobre mudanças de estado de outro objeto, sem que o objeto observado tenha que conhecer diretamente seus observadores, é necessário um mecanismo eficiente para isso.

## Solução

O Observer resolve esse problema definindo uma relação entre um objeto observado (Subject) e vários objetos observadores (Observers), permitindo que os observadores sejam notificados automaticamente quando o estado do objeto observado muda.

## Exemplo

No exemplo fornecido, temos a classe `Subject` que mantém uma lista de observadores e notifica-os quando há mudanças de estado. `EmailNotifier` e `SMSNotifier` são observadores concretos que implementam o método `update()` para reagir às notificações.
