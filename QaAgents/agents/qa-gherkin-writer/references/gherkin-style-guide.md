# Guia de Estilo Gherkin

## Estrutura base

```gherkin
@p1 @regression
Feature: Nome da funcionalidade
  Como <persona>
  Quero <objetivo>
  Para <benefício>

  Background:
    Given <contexto comum>

  Scenario: Caminho principal
    Given <estado inicial>
    When <ação>
    Then <resultado esperado>
```

## Exemplo com variação

```gherkin
@p0
Scenario Outline: Login com múltiplos perfis
  Given que o usuário está na tela de login
  When ele informa usuário "<usuario>" e senha "<senha>"
  Then o sistema deve exibir "<resultado>"

  Examples:
    | usuario | senha   | resultado               |
    | admin   | 123456  | Dashboard administrativo |
    | guest   | guest12 | Acesso restrito          |
```

## Checklist de qualidade

- Cenário é compreensível por pessoas não técnicas.
- Resultado esperado é objetivo e verificável.
- Linguagem de domínio está consistente.
- Tags de execução/prioridade estão presentes.
