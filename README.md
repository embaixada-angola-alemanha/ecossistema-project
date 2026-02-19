# Ecossistema Digital — Embaixada de Angola na Alemanha

> Plataforma digital completa para a Embaixada da Republica de Angola na Republica Federal da Alemanha. 4 sistemas, 13 repositorios, 115.000+ linhas de codigo.

## Visao Geral

O **Ecossistema Digital** e uma plataforma integrada que digitaliza todos os servicos consulares, comunicacao institucional, gestao de noticias e gestao de projectos da Embaixada de Angola em Berlim.

| Metrica | Valor |
|---------|-------|
| Estado | **CONCLUIDO** (100%) |
| Tarefas | 71/71 |
| Sprints | 20/20 |
| Horas | 888h |
| Repositorios | 13 |
| Commits | 126 |
| Ficheiros | 1.172 |
| Linhas de codigo | 115.795 |
| Dominio | `embaixada-angola.site` |

## 4 Sistemas

### SGC — Sistema de Gestao Consular
O sistema principal para gestao de servicos consulares: registo de cidadaos, processamento de vistos, agendamentos, registo civil (nascimento/casamento/obito) e servicos notariais. Inclui motor de workflow, notificacoes por email, auditoria completa e geracao de certificados PDF.

### SI — Sitio Institucional
Website institucional multilingue (PT/EN/DE) com gestao de paginas, eventos, menus e contactos. Workflow editorial completo (Rascunho → Revisao → Publicado → Arquivado).

### WN — Welwitschia Noticias
Portal de noticias com artigos, categorias, tags, autores e gestao de media. Workflow editorial, newsletter e feed RSS. Conteudo migrado do WordPress anterior (botschaftangola.de).

### GPJ — Gestao de Projectos
Sistema de gestao de projectos com quadro Kanban, grafico Gantt, burndown/velocity charts, registo de tempo e gestao de bloqueios. Usado para monitorar o proprio desenvolvimento do ecossistema.

## Stack Tecnologico

```
Backend:     Java 21 + Spring Boot 3.4
Frontend:    Angular 18 + Angular Material
Mobile:      React Native 0.76+
Database:    PostgreSQL 16
Cache:       Redis 7
Auth:        Keycloak 26 (SSO + JWT)
Storage:     MinIO (S3-compatible)
Messaging:   RabbitMQ
Monitoring:  Prometheus + Grafana + Loki
Deploy:      Docker Compose (Strato VPS)
CI/CD:       GitHub Actions
```

## Repositorios

### Infraestrutura & Shared
| Repositorio | Descricao |
|-------------|-----------|
| **ecossistema-project** | Estado do projecto, protocolo e gestao (este repo) |
| [ecossistema-infra](https://github.com/embaixada-angola-alemanha/ecossistema-infra) | Docker Compose, Nginx, Keycloak, deploy scripts, migracao WordPress |
| [ecossistema-commons](https://github.com/embaixada-angola-alemanha/ecossistema-commons) | Bibliotecas Java partilhadas: security, dto, i18n, audit, notification |
| [ecossistema-docs](https://github.com/embaixada-angola-alemanha/ecossistema-docs) | Documentacao, guias de utilizador, runbook, go-live |

### SGC — Sistema de Gestao Consular
| Repositorio | Descricao |
|-------------|-----------|
| [ecossistema-sgc-backend](https://github.com/embaixada-angola-alemanha/ecossistema-sgc-backend) | API REST — cidadaos, vistos, agendamentos, registo civil, notarial |
| [ecossistema-sgc-frontend](https://github.com/embaixada-angola-alemanha/ecossistema-sgc-frontend) | Painel Angular — gestao consular completa |

### SI — Sitio Institucional
| Repositorio | Descricao |
|-------------|-----------|
| [ecossistema-si-backend](https://github.com/embaixada-angola-alemanha/ecossistema-si-backend) | API REST — paginas, eventos, menus, contactos (multilingue) |
| [ecossistema-si-frontend](https://github.com/embaixada-angola-alemanha/ecossistema-si-frontend) | Website publico Angular — sitio institucional |

### WN — Welwitschia Noticias
| Repositorio | Descricao |
|-------------|-----------|
| [ecossistema-wn-backend](https://github.com/embaixada-angola-alemanha/ecossistema-wn-backend) | API REST — artigos, categorias, tags, media, newsletter |
| [ecossistema-wn-frontend](https://github.com/embaixada-angola-alemanha/ecossistema-wn-frontend) | Portal de noticias Angular |

### GPJ — Gestao de Projectos
| Repositorio | Descricao |
|-------------|-----------|
| [ecossistema-gpj-backend](https://github.com/embaixada-angola-alemanha/ecossistema-gpj-backend) | API REST — sprints, tarefas, milestones, time logging |
| [ecossistema-gpj-frontend](https://github.com/embaixada-angola-alemanha/ecossistema-gpj-frontend) | Painel Angular — Kanban, Gantt, burndown charts |

### Mobile
| Repositorio | Descricao |
|-------------|-----------|
| [ecossistema-mobile](https://github.com/embaixada-angola-alemanha/ecossistema-mobile) | App React Native (iOS + Android) para cidadaos |

## Arquitectura

```
                         embaixada-angola.site
                                |
                              Nginx
                         (reverse proxy + TLS)
                                |
        ┌───────────┬───────────┼───────────┬───────────┐
        |           |           |           |           |
   sgc.~site   si.~site    wn.~site    gpj.~site   app.~site
        |           |           |           |           |
   SGC Backend  SI Backend  WN Backend  GPJ Backend   Mobile
   (port 8081)  (port 8082) (port 8083) (port 8084)   (RN)
        |           |           |           |
        └───────────┴─────┬─────┴───────────┘
                          |
              ┌───────────┼───────────┐
              |           |           |
         PostgreSQL    Keycloak     MinIO
           (5432)       (8080)     (9000)
              |           |
           Redis      RabbitMQ
           (6379)      (5672)
              |
     Prometheus + Grafana + Loki
```

## Infraestrutura de Producao

- **Servidor:** Strato VPS (6 vCPU, 24 GB RAM, 360 GB SSD)
- **Dominio:** `embaixada-angola.site` (12 subdominios)
- **Containers:** 18 servicos Docker Compose
- **TLS:** Let's Encrypt via Certbot (renovacao automatica)
- **Backups:** pg_dump diario automatizado
- **Monitoring:** Prometheus + Grafana dashboards + Loki log aggregation

## Roles (RBAC via Keycloak)

| Role | SGC | SI | WN | GPJ |
|------|-----|----|----|-----|
| ADMIN | Gestao total | Gestao total | Gestao total | Gestao total |
| CONSUL | Aprovacoes, relatorios | — | — | — |
| OFFICER | Operacoes diarias | — | — | — |
| REGISTRAR | Registo civil | — | — | — |
| NOTARY | Servicos notariais | — | — | — |
| CITIZEN | Self-service (portal/app) | — | — | — |
| EDITOR | — | Conteudo editorial | Conteudo editorial | — |
| JOURNALIST | — | — | Criacao de artigos | — |
| PROJECT_MANAGER | — | — | — | Sprints e tarefas |

## Ficheiros neste Repositorio

| Ficheiro | Descricao |
|----------|-----------|
| `project_state.json` | Estado completo do projecto — sprints, tarefas, horas, historico |
| `PROTOCOLO.md` | Protocolo de actualizacao em 7 passos |
| `prompts_completas_v2.md` | Templates de prompts para todas as tarefas |
| `prompts_update.py` | CLI helper para consultar estado/tarefas/prompts |

## Sprints

| Sprint | Titulo | Fase | Horas |
|--------|--------|------|-------|
| S0 | Infraestrutura & Fundacao | Infra | 40h |
| S1 | GPJ Sistema Completo | GPJ | 48h |
| S2 | SGC Backend Core I | SGC-BE | 40h |
| S3 | SGC Backend Core II | SGC-BE | 40h |
| S4 | SGC Backend Avancado I | SGC-BE | 40h |
| S5 | SGC Backend Avancado II | SGC-BE | 40h |
| S6 | SGC Frontend Core I | SGC-FE | 50h |
| S7 | SGC Frontend Core II | SGC-FE | 40h |
| S8 | SGC Frontend Avancado I | SGC-FE | 40h |
| S9 | SGC Frontend Avancado II + Testes | SGC-FE | 56h |
| S10 | Sitio Institucional Backend | SI | 40h |
| S11 | Sitio Institucional Frontend | SI | 50h |
| S12 | Welwitschia Noticias Backend | WN | 40h |
| S13 | Welwitschia Noticias Frontend | WN | 50h |
| S14 | Shared Libraries & Integracao | Integracao | 40h |
| S15 | React Native Mobile I | Mobile | 40h |
| S16 | React Native Mobile II | Mobile | 40h |
| S17 | Testes & Seguranca | Testes | 40h |
| S18 | UAT & Documentacao | Testes | 40h |
| S19 | Go-Live & Formacao | Go-Live | 32h |

## Licenca

Propriedade da Embaixada da Republica de Angola na Republica Federal da Alemanha.
