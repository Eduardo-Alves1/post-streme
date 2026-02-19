# QaAgents

Coleção de agentes (skills) para uso no **CODEX CLI** com foco em **Qualidade de Software (QA)**.

## Objetivo

Estes agentes foram criados para:

- analisar o código-fonte do projeto;
- gerar plano de testes baseado em risco;
- produzir casos de teste detalhados;
- escrever cenários em formato **Step by Step** e **Gherkin**.

## Estrutura

```text
QaAgents/
  agents/
    qa-test-strategist/
      SKILL.md
      references/
        test-plan-template.md
    qa-test-designer/
      SKILL.md
      references/
        test-cases-template.md
    qa-gherkin-writer/
      SKILL.md
      references/
        gherkin-style-guide.md
  templates/
    test-plan.md
    test-cases-step-by-step.md
    test-cases-gherkin.feature
```

## Como usar no CODEX CLI

1. Copie a pasta `QaAgents/agents/*` para o diretório de skills do Codex:
   - Linux/macOS: `$CODEX_HOME/skills/`
2. Em uma sessão, peça explicitamente o uso do agente desejado (ex.: `use qa-test-strategist`).
3. Informe contexto do repositório, objetivo da validação e escopo funcional.

## Fluxo recomendado

1. **qa-test-strategist**: analisa o código e gera plano de testes.
2. **qa-test-designer**: detalha casos de teste step by step.
3. **qa-gherkin-writer**: converte/refina cenários em Gherkin.

## Templates prontos

Os templates em `templates/` podem ser usados diretamente para padronizar entregas de QA.

## Como ver tudo completo

Para visualizar o pacote completo no terminal:

```bash
find QaAgents -maxdepth 4 -type f | sort
```

Para validar rapidamente se todos os agentes têm `name` e `description` no frontmatter:

```bash
python - <<'PY'
from pathlib import Path
import re
for skill in Path('QaAgents/agents').glob('*/SKILL.md'):
    txt = skill.read_text(encoding='utf-8')
    ok = bool(re.search(r'^---\n(?s:.*?)\n---\n', txt)) and 'name:' in txt and 'description:' in txt
    print(f"{skill}: {'OK' if ok else 'FAIL'}")
PY
```

Se quiser usar imediatamente no Codex CLI, copie a pasta `QaAgents/agents/*` para `$CODEX_HOME/skills/`.
