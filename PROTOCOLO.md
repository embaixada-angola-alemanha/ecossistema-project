# PROTOCOLO DE ACTUALIZAÇÃO — ECOSSISTEMA DIGITAL v2.0

## Arquitectura: Multi-Repo (12 repositórios) | Stack: Spring Boot 3.4 + Angular 18 + React Native + PostgreSQL 16 + Keycloak

---

## 1. VISÃO GERAL

Este protocolo define exactamente como o Claude actualiza o estado do projecto após cada tarefa e cada sprint. O ficheiro `project_state.json` é a **fonte única de verdade**.

**Mudanças face à v1.0:**
- De monorepo para **12 repositórios independentes**
- MySQL → **PostgreSQL 16**
- Auth custom → **Keycloak SSO**
- Liquibase → **Flyway**
- 61 tarefas → **68 tarefas**
- Sem mobile → **React Native** (Sprints 15-16)
- Sem GPJ → **GPJ incluído** (Sprint 13)
- Shared libraries: **commons-*** (Maven) + **@ecossistema/*** (Angular npm)

---

## 2. FICHEIROS DO SISTEMA

| Ficheiro | Função |
|----------|--------|
| `project_state.json` | Estado do projecto (fonte única de verdade) |
| `PROTOCOLO.md` | Este documento — regras de actualização |
| `prompts_update.py` | Motor de prompts e actualizações CLI |

---

## 3. FASES E REPOSITÓRIOS

| Fase | Sprints | Repositório(s) Principal(is) | Horas |
|------|---------|-------------------------------|-------|
| Infraestrutura | S0 | ecossistema-infra, commons, docs | 40h |
| SGC Backend | S1–S4 | ecossistema-sgc-backend | 160h |
| SGC Frontend | S5–S8 | ecossistema-sgc-frontend | 160h |
| Sítio Institucional | S9–S10 | ecossistema-si-backend, si-frontend | 80h |
| Welwitschia Notícias | S11–S12 | ecossistema-wn-backend, wn-frontend | 80h |
| GPJ + Integração | S13–S14 | ecossistema-gpj-*, todos | 80h |
| React Native Mobile | S15–S16 | ecossistema-mobile | 80h |
| Testes & QA | S17–S18 | todos | 80h |
| Go-Live | S19 | ecossistema-infra, docs | 40h |
| **Buffer** | **23-30 Nov** | — | **20h** |
| **TOTAL** | | | **820h** |

---

## 4. PROTOCOLO: TAREFA CONCLUÍDA (7 passos obrigatórios)

Quando o utilizador reporta conclusão de uma tarefa, o Claude **DEVE** executar:

### Passo 1: Ler estado
```
Ler project_state.json
```

### Passo 2: Actualizar tarefa
```json
{
  "estado": "CONCLUIDA",
  "progresso_pct": 100,
  "horas_consumidas": <valor reportado>,
  "data_conclusao": "<ISO timestamp>",
  "artefactos": [<lista de ficheiros/repos>],
  "notas": "<resumo do trabalho + desvios>"
}
```

### Passo 3: Recalcular sprint
```
sprint.horas_consumidas = soma(tarefas do sprint.horas_consumidas)
sprint.progresso_pct = (tarefas concluídas / total tarefas do sprint) * 100
sprint.estado = "EM_PROGRESSO" se alguma concluída, "CONCLUIDO" se todas
```

### Passo 4: Recalcular projecto
```
projecto.horas_consumidas = soma(todas as tarefas.horas_consumidas)
projecto.tarefas_concluidas = count(tarefas com estado CONCLUIDA)
projecto.progresso_pct = (tarefas_concluidas / 68) * 100
projecto.estado = "EM_PROGRESSO" ou "CONCLUIDO"
```

### Passo 5: Adicionar ao histórico
```json
{
  "data": "<ISO timestamp>",
  "evento": "TAREFA_CONCLUIDA",
  "detalhe": "<task_id>: <nome> | <horas>h | Sprint <N> | Repo: <repo>"
}
```

### Passo 6: Mensagem ao cliente
```json
{
  "id": <next_id>,
  "data": "<ISO timestamp>",
  "de": "sistema",
  "texto": "✅ Tarefa <ID> concluída: <Nome>\n\nFase: <Fase> | Sprint <N> | <X>h | Repo: <repo>\nProgresso global: <X>% | Tarefas: <N>/68\n\nArtefactos:\n• <item1>\n• <item2>",
  "tipo": "tarefa_concluida"
}
```

### Passo 7: Gravar e reportar
```
Gravar project_state.json
Reportar: "<task_id> concluída. Sprint <N>: <X>%. Próxima: <next_task_id> (<nome>)"
```

---

## 5. PROTOCOLO: SPRINT CONCLUÍDO (passos adicionais)

Quando a **última tarefa** de um sprint é concluída:

### Passo A: Sprint Review
```json
{
  "id": <next_id>,
  "data": "<ISO timestamp>",
  "de": "sistema",
  "texto": "🏁 SPRINT <N> CONCLUÍDO: <título>\n\n<Review: 3-5 frases>\n\n📊 Métricas:\n• Tarefas: <N>/<N> concluídas\n• Horas: <X>h de <X>h planeadas\n• Eficiência: <X>%\n• Progresso global: <X>%\n\n➡️ Próximo: Sprint <N+1> (<data>→<data>)\n• <Tarefa 1>\n• <Tarefa 2>\n• <Tarefa 3>",
  "tipo": "sprint_concluido"
}
```

### Passo B: Actualizar sprint
```json
{
  "estado": "CONCLUIDO",
  "progresso_pct": 100
}
```

---

## 6. ESTADOS

### Tarefas
| Estado | Significado |
|--------|-------------|
| `PENDENTE` | Não iniciada |
| `EM_PROGRESSO` | Em desenvolvimento |
| `CONCLUIDA` | Finalizada e verificada |
| `BLOQUEADA` | Impedida por dependência |

### Sprints
| Estado | Significado |
|--------|-------------|
| `PENDENTE` | Não iniciado |
| `EM_PROGRESSO` | Pelo menos 1 tarefa em curso |
| `CONCLUIDO` | Todas as tarefas concluídas |

---

## 7. COMANDOS DO SCRIPT

```bash
python3 prompts_update.py --status           # Estado actual
python3 prompts_update.py --list             # Lista todas as tarefas
python3 prompts_update.py --next             # Próxima tarefa pendente
python3 prompts_update.py --task T0.1        # Prompt de conclusão
python3 prompts_update.py --sprint 0         # Prompt de review
python3 prompts_update.py --execute-task T0.1  # Marca tarefa concluída
python3 prompts_update.py --export           # Exporta todas as prompts
python3 prompts_update.py --burndown         # Dados de burndown
python3 prompts_update.py --repos            # Estado por repositório
```

---

## 8. EXEMPLO COMPLETO

**Utilizador:** "Concluí a T0.1. Criei o ecossistema-infra com Docker Compose (PostgreSQL, Redis, Keycloak, nginx, MinIO, MailHog). Demorei 10h."

**Claude executa passos 1-7 e reporta:**

> ✅ T0.1 concluída. Sprint 0: 25% (1/4). Progresso global: 1.5% (1/68).
> Próxima: T0.2 — Commons Maven Multi-Module (ecossistema-commons, 12h)
