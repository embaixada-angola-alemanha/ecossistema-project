# PROMPTS COMPLETAS — ECOSSISTEMA DIGITAL v2.0

Total: 63 task prompts + 20 sprint prompts

---


## T0.1: Docker Compose + Infra Repo

- Sprint: 0 | Fase: Infra | Repo: ecossistema-infra | 12h
- Descrição: Criar ecossistema-infra com docker-compose.yml: PostgreSQL 16, Redis 7, Keycloak, nginx, MinIO, MailHog. Configurar volumes, networks, healthchecks.
- Critérios:
  - docker-compose up funcional
  - Todos os serviços healthy
  - Keycloak realm 'ecossistema' criado
  - nginx routing configurado
  - README com instruções

**Prompt:**
```
Concluí a tarefa T0.1 (Docker Compose + Infra Repo). Repositório: ecossistema-infra. Sprint: 0. Horas: [X]h. Artefactos: [lista]. Actualiza o project_state.json.
```


## T0.2: Commons Maven Multi-Module

- Sprint: 0 | Fase: Infra | Repo: ecossistema-commons | 12h
- Descrição: Criar ecossistema-commons: parent POM + 6 módulos (security, dto, i18n, util, audit, notification). Java 21, Spring Boot 3.4 parent.
- Critérios:
  - Maven build sem erros
  - Módulo security com JWT filter
  - Módulo dto com BaseEntity, BaseDTO
  - Módulo i18n com 4 locales
  - Testes compilam e passam

**Prompt:**
```
Concluí a tarefa T0.2 (Commons Maven Multi-Module). Repositório: ecossistema-commons. Sprint: 0. Horas: [X]h. Artefactos: [lista]. Actualiza o project_state.json.
```


## T0.3: GitHub Repos + CI/CD

- Sprint: 0 | Fase: Infra | Repo: todos | 8h
- Descrição: Criar 12 repositórios GitHub. Configurar branch protection (main, develop). GitHub Actions workflows para build, test, Docker image push.
- Critérios:
  - 12 repos criados
  - Branch protection activa
  - CI workflow funcional
  - Docker build automático
  - Conventional commits enforced

**Prompt:**
```
Concluí a tarefa T0.3 (GitHub Repos + CI/CD). Repositório: todos. Sprint: 0. Horas: [X]h. Artefactos: [lista]. Actualiza o project_state.json.
```


## T0.4: ADRs + Documentação Base

- Sprint: 0 | Fase: Infra | Repo: ecossistema-docs | 8h
- Descrição: Criar ecossistema-docs com ADR-001 (Arquitectura), ADR-002 (Multi-Repo), ADR-003 (Auth/Keycloak), ADR-004 (PostgreSQL), ADR-005 (i18n). LaTeX templates.
- Critérios:
  - 5 ADRs escritos
  - Template LaTeX configurado
  - README com índice
  - Diagramas C4 básicos
  - Glossário técnico

**Prompt:**
```
Concluí a tarefa T0.4 (ADRs + Documentação Base). Repositório: ecossistema-docs. Sprint: 0. Horas: [X]h. Artefactos: [lista]. Actualiza o project_state.json.
```


## T1.1: SGC Scaffold + Flyway V1

- Sprint: 1 | Fase: SGC-BE | Repo: ecossistema-sgc-backend | 14h
- Descrição: Spring Boot 3.4 scaffold com Flyway. Migração V1: cidadaos, documentos, utilizadores, roles, audit_log. Base entities com JPA auditing.
- Critérios:
  - Spring Boot arranca sem erros
  - Flyway V1 executada com sucesso
  - BaseEntity com createdAt, updatedAt, createdBy
  - Perfis dev/staging/prod
  - Health endpoint /actuator/health

**Prompt:**
```
Concluí a tarefa T1.1 (SGC Scaffold + Flyway V1). Repositório: ecossistema-sgc-backend. Sprint: 1. Horas: [X]h. Artefactos: [lista]. Actualiza o project_state.json.
```


## T1.2: Citizen Management CRUD

- Sprint: 1 | Fase: SGC-BE | Repo: ecossistema-sgc-backend | 14h
- Descrição: Módulo Gestão de Cidadãos: CidadaoEntity, CidadaoRepository, CidadaoService, CidadaoController. CRUD completo com paginação, filtros, DTOs.
- Critérios:
  - POST/GET/PUT/DELETE /api/v1/cidadaos
  - Paginação com Specification
  - DTOs request/response separados
  - Validação com Jakarta Validation
  - Testes unitários >80% cobertura

**Prompt:**
```
Concluí a tarefa T1.2 (Citizen Management CRUD). Repositório: ecossistema-sgc-backend. Sprint: 1. Horas: [X]h. Artefactos: [lista]. Actualiza o project_state.json.
```


## T1.3: Keycloak Auth + RBAC

- Sprint: 1 | Fase: SGC-BE | Repo: ecossistema-sgc-backend | 12h
- Descrição: Integração Keycloak: realm config, 6 roles (ADMIN, CONSUL, OFFICER, CITIZEN, EDITOR, VIEWER), JWT validation, Spring Security config, method-level security.
- Critérios:
  - Login via Keycloak funcional
  - 6 roles definidas no realm
  - @PreAuthorize em controllers
  - JWT refresh token flow
  - Testes de autorização

**Prompt:**
```
Concluí a tarefa T1.3 (Keycloak Auth + RBAC). Repositório: ecossistema-sgc-backend. Sprint: 1. Horas: [X]h. Artefactos: [lista]. Actualiza o project_state.json.
```


## T2.1: Visa Processing Module

- Sprint: 2 | Fase: SGC-BE | Repo: ecossistema-sgc-backend | 16h
- Descrição: Módulo Vistos: VisaApplication entity, lifecycle (SUBMITTED→REVIEWING→APPROVED/REJECTED→ISSUED), fee calculator, document checklist, status tracking API.
- Critérios:
  - CRUD completo para aplicações de visto
  - State machine com transições validadas
  - Fee calculator por nacionalidade
  - Checklist de documentos por tipo de visto
  - Status tracking endpoint

**Prompt:**
```
Concluí a tarefa T2.1 (Visa Processing Module). Repositório: ecossistema-sgc-backend. Sprint: 2. Horas: [X]h. Artefactos: [lista]. Actualiza o project_state.json.
```


## T2.2: Appointment System

- Sprint: 2 | Fase: SGC-BE | Repo: ecossistema-sgc-backend | 12h
- Descrição: Sistema de Agendamento: AppointmentEntity, calendar slots, conflict detection, confirmation emails via commons-notification, recurring availability rules.
- Critérios:
  - Booking endpoint funcional
  - Detecção de conflitos
  - Email de confirmação
  - Cancelamento e reagendamento
  - Slots configuráveis por tipo de serviço

**Prompt:**
```
Concluí a tarefa T2.2 (Appointment System). Repositório: ecossistema-sgc-backend. Sprint: 2. Horas: [X]h. Artefactos: [lista]. Actualiza o project_state.json.
```


## T2.3: OpenAPI Docs + Tests

- Sprint: 2 | Fase: SGC-BE | Repo: ecossistema-sgc-backend | 12h
- Descrição: Swagger/OpenAPI 3.0 config, integration tests com Testcontainers (PostgreSQL), API contract tests, test coverage report.
- Critérios:
  - Swagger UI em /swagger-ui
  - OpenAPI spec exportável
  - Integration tests com Testcontainers
  - Cobertura global >80%
  - API contract tests

**Prompt:**
```
Concluí a tarefa T2.3 (OpenAPI Docs + Tests). Repositório: ecossistema-sgc-backend. Sprint: 2. Horas: [X]h. Artefactos: [lista]. Actualiza o project_state.json.
```


## T3.1: Document Management + MinIO

- Sprint: 3 | Fase: SGC-BE | Repo: ecossistema-sgc-backend | 14h
- Descrição: Módulo Documentos: upload/download via MinIO, metadata tracking, versioning, virus scan placeholder, thumbnail generation, access control per document.
- Critérios:
  - Upload multipart funcional
  - MinIO integration testada
  - Metadata (tipo, cidadao, processo)
  - Download com access control
  - Versioning de documentos

**Prompt:**
```
Concluí a tarefa T3.1 (Document Management + MinIO). Repositório: ecossistema-sgc-backend. Sprint: 3. Horas: [X]h. Artefactos: [lista]. Actualiza o project_state.json.
```


## T3.2: Civil Registry Module

- Sprint: 3 | Fase: SGC-BE | Repo: ecossistema-sgc-backend | 12h
- Descrição: Módulo Registos Civis: nascimentos, casamentos, óbitos. Workflow de verificação multi-party, geração de certificados PDF, integração com cidadão.
- Critérios:
  - CRUD para 3 tipos de registo
  - Workflow de verificação
  - Geração de PDF
  - Ligação com entidade Cidadão
  - Audit trail completo

**Prompt:**
```
Concluí a tarefa T3.2 (Civil Registry Module). Repositório: ecossistema-sgc-backend. Sprint: 3. Horas: [X]h. Artefactos: [lista]. Actualiza o project_state.json.
```


## T3.3: Notarial Services Module

- Sprint: 3 | Fase: SGC-BE | Repo: ecossistema-sgc-backend | 14h
- Descrição: Módulo Notariado: procurações, legalizações, apostilas, cópias certificadas. Payment tracking, request workflow, certificate generation.
- Critérios:
  - 4 tipos de serviço notarial
  - Workflow de pedido→aprovação→emissão
  - Fee tracking
  - Geração de certificado
  - Integração com agendamento

**Prompt:**
```
Concluí a tarefa T3.3 (Notarial Services Module). Repositório: ecossistema-sgc-backend. Sprint: 3. Horas: [X]h. Artefactos: [lista]. Actualiza o project_state.json.
```


## T4.1: Workflow Engine

- Sprint: 4 | Fase: SGC-BE | Repo: ecossistema-sgc-backend | 14h
- Descrição: Motor de Workflow genérico: state machine configurável, transições validadas, eventos, listeners, histórico de transições, aplicável a todos os módulos.
- Critérios:
  - State machine genérica
  - Transições com validação
  - Event listeners
  - Histórico persistido
  - Aplicado a vistos e registos civis

**Prompt:**
```
Concluí a tarefa T4.1 (Workflow Engine). Repositório: ecossistema-sgc-backend. Sprint: 4. Horas: [X]h. Artefactos: [lista]. Actualiza o project_state.json.
```


## T4.2: Notification Service

- Sprint: 4 | Fase: SGC-BE | Repo: ecossistema-sgc-backend | 12h
- Descrição: Serviço de notificações: email (SMTP via commons-notification), templates Thymeleaf, async processing via RabbitMQ, notification preferences per citizen.
- Critérios:
  - Email sending funcional
  - Templates para cada evento
  - Async via RabbitMQ
  - Preferências de notificação
  - Log de notificações enviadas

**Prompt:**
```
Concluí a tarefa T4.2 (Notification Service). Repositório: ecossistema-sgc-backend. Sprint: 4. Horas: [X]h. Artefactos: [lista]. Actualiza o project_state.json.
```


## T4.3: Audit + Reporting Module

- Sprint: 4 | Fase: SGC-BE | Repo: ecossistema-sgc-backend | 10h
- Descrição: Audit trail completo com Hibernate Envers ou custom. Relatórios: vistos processados, cidadãos registados, receitas. Export CSV/PDF.
- Critérios:
  - Audit trail em todas as entidades
  - Dashboard de métricas API
  - Export CSV
  - Export PDF (JasperReports)
  - Filtros por período/tipo

**Prompt:**
```
Concluí a tarefa T4.3 (Audit + Reporting Module). Repositório: ecossistema-sgc-backend. Sprint: 4. Horas: [X]h. Artefactos: [lista]. Actualiza o project_state.json.
```


## T4.4: API Security Hardening

- Sprint: 4 | Fase: SGC-BE | Repo: ecossistema-sgc-backend | 4h
- Descrição: Rate limiting (Bucket4j), CORS config, CSRF protection, input sanitisation, SQL injection prevention review, security headers.
- Critérios:
  - Rate limiting activo
  - CORS configurado
  - Headers de segurança
  - Input sanitisation
  - Security scan sem criticals

**Prompt:**
```
Concluí a tarefa T4.4 (API Security Hardening). Repositório: ecossistema-sgc-backend. Sprint: 4. Horas: [X]h. Artefactos: [lista]. Actualiza o project_state.json.
```


## T5.1: Angular Scaffold + Auth UI

- Sprint: 5 | Fase: SGC-FE | Repo: ecossistema-sgc-frontend | 16h
- Descrição: Angular 18 scaffold: routing, lazy loading, Keycloak adapter, auth guards, HTTP interceptor (JWT), role-based UI rendering.
- Critérios:
  - Angular app funcional
  - Login via Keycloak
  - Guards em rotas protegidas
  - Interceptor JWT automático
  - Menu adapta-se ao role

**Prompt:**
```
Concluí a tarefa T5.1 (Angular Scaffold + Auth UI). Repositório: ecossistema-sgc-frontend. Sprint: 5. Horas: [X]h. Artefactos: [lista]. Actualiza o project_state.json.
```


## T5.2: Citizen Dashboard UI

- Sprint: 5 | Fase: SGC-FE | Repo: ecossistema-sgc-frontend | 14h
- Descrição: Dashboard de Cidadãos: listagem com paginação, pesquisa avançada, criação/edição com formulários reactivos, detalhe com tabs (dados, documentos, processos).
- Critérios:
  - Listagem paginada
  - Pesquisa com filtros
  - Formulário create/edit
  - Página de detalhe com tabs
  - Validação client-side

**Prompt:**
```
Concluí a tarefa T5.2 (Citizen Dashboard UI). Repositório: ecossistema-sgc-frontend. Sprint: 5. Horas: [X]h. Artefactos: [lista]. Actualiza o project_state.json.
```


## T5.3: Visa Application Forms

- Sprint: 5 | Fase: SGC-FE | Repo: ecossistema-sgc-frontend | 10h
- Descrição: Formulários de visto multi-step: dados pessoais → tipo de visto → documentos → pagamento → confirmação. Stepper visual, save draft, document upload.
- Critérios:
  - Stepper de 5 passos
  - Upload de documentos
  - Save draft
  - Validação por step
  - Confirmação com resumo

**Prompt:**
```
Concluí a tarefa T5.3 (Visa Application Forms). Repositório: ecossistema-sgc-frontend. Sprint: 5. Horas: [X]h. Artefactos: [lista]. Actualiza o project_state.json.
```


## T6.1: Appointment Calendar UI

- Sprint: 6 | Fase: SGC-FE | Repo: ecossistema-sgc-frontend | 14h
- Descrição: Calendário de agendamentos: vista semanal/mensal, drag-and-drop, slot selection, booking confirmation, cancellation flow.
- Critérios:
  - Vista semanal e mensal
  - Seleção de slot disponível
  - Confirmação de booking
  - Cancelamento/reagendamento
  - Integração com backend

**Prompt:**
```
Concluí a tarefa T6.1 (Appointment Calendar UI). Repositório: ecossistema-sgc-frontend. Sprint: 6. Horas: [X]h. Artefactos: [lista]. Actualiza o project_state.json.
```


## T6.2: Document Management UI

- Sprint: 6 | Fase: SGC-FE | Repo: ecossistema-sgc-frontend | 12h
- Descrição: Gestão de Documentos: upload drag-and-drop, preview (PDF/imagem), metadata editing, version history, download, access control indicators.
- Critérios:
  - Upload drag-and-drop
  - Preview inline
  - Metadata editing
  - Version history
  - Download funcional

**Prompt:**
```
Concluí a tarefa T6.2 (Document Management UI). Repositório: ecossistema-sgc-frontend. Sprint: 6. Horas: [X]h. Artefactos: [lista]. Actualiza o project_state.json.
```


## T6.3: Reports Dashboard

- Sprint: 6 | Fase: SGC-FE | Repo: ecossistema-sgc-frontend | 14h
- Descrição: Dashboard de relatórios: gráficos (Chart.js/ngx-charts) para vistos, cidadãos, receitas. Filtros temporais, export CSV/PDF, KPI cards.
- Critérios:
  - Gráficos interactivos
  - KPI cards no topo
  - Filtros por período
  - Export CSV e PDF
  - Responsive design

**Prompt:**
```
Concluí a tarefa T6.3 (Reports Dashboard). Repositório: ecossistema-sgc-frontend. Sprint: 6. Horas: [X]h. Artefactos: [lista]. Actualiza o project_state.json.
```


## T7.1: Civil Registry + Notarial UI

- Sprint: 7 | Fase: SGC-FE | Repo: ecossistema-sgc-frontend | 14h
- Descrição: UI para Registos Civis (nascimentos, casamentos, óbitos) e Serviços Notariais. Formulários, listagens, workflow visual.
- Critérios:
  - Formulários para 3 tipos de registo
  - Formulários para 4 serviços notariais
  - Visualização de workflow
  - Geração/download de certificados
  - Integração com cidadão

**Prompt:**
```
Concluí a tarefa T7.1 (Civil Registry + Notarial UI). Repositório: ecossistema-sgc-frontend. Sprint: 7. Horas: [X]h. Artefactos: [lista]. Actualiza o project_state.json.
```


## T7.2: Workflow Admin Panel

- Sprint: 7 | Fase: SGC-FE | Repo: ecossistema-sgc-frontend | 12h
- Descrição: Painel de administração de workflows: visualização do pipeline, approve/reject actions, bulk operations, queue management.
- Critérios:
  - Pipeline visual
  - Acções approve/reject
  - Bulk operations
  - Fila de pendentes
  - Filtros e pesquisa

**Prompt:**
```
Concluí a tarefa T7.2 (Workflow Admin Panel). Repositório: ecossistema-sgc-frontend. Sprint: 7. Horas: [X]h. Artefactos: [lista]. Actualiza o project_state.json.
```


## T7.3: User Management Admin

- Sprint: 7 | Fase: SGC-FE | Repo: ecossistema-sgc-frontend | 14h
- Descrição: Gestão de utilizadores: CRUD de staff, atribuição de roles, activity log, session management, password policies.
- Critérios:
  - CRUD de utilizadores
  - Atribuição de roles
  - Activity log
  - Session management
  - Integração Keycloak admin

**Prompt:**
```
Concluí a tarefa T7.3 (User Management Admin). Repositório: ecossistema-sgc-frontend. Sprint: 7. Horas: [X]h. Artefactos: [lista]. Actualiza o project_state.json.
```


## T8.1: i18n (PT/DE/EN/CZ)

- Sprint: 8 | Fase: SGC-FE | Repo: ecossistema-sgc-frontend | 12h
- Descrição: Internacionalização completa: 4 idiomas (Português, Alemão, Inglês, Checo), language switcher, locale-aware date/number formatting, RTL-ready.
- Critérios:
  - 4 ficheiros de tradução completos
  - Language switcher no header
  - Formatação de datas/números
  - Persistência da preferência
  - Nenhum texto hardcoded

**Prompt:**
```
Concluí a tarefa T8.1 (i18n (PT/DE/EN/CZ)). Repositório: ecossistema-sgc-frontend. Sprint: 8. Horas: [X]h. Artefactos: [lista]. Actualiza o project_state.json.
```


## T8.2: Accessibility (WCAG 2.1 AA)

- Sprint: 8 | Fase: SGC-FE | Repo: ecossistema-sgc-frontend | 10h
- Descrição: Acessibilidade: ARIA labels, keyboard navigation, colour contrast (4.5:1), skip links, focus management, screen reader testing.
- Critérios:
  - ARIA labels em todos os componentes
  - Navegação por teclado
  - Contraste ≥4.5:1
  - Skip links
  - Lighthouse accessibility >90

**Prompt:**
```
Concluí a tarefa T8.2 (Accessibility (WCAG 2.1 AA)). Repositório: ecossistema-sgc-frontend. Sprint: 8. Horas: [X]h. Artefactos: [lista]. Actualiza o project_state.json.
```


## T8.3: SGC E2E Testing

- Sprint: 8 | Fase: SGC-FE | Repo: ecossistema-sgc-frontend | 10h
- Descrição: Testes E2E com Cypress: fluxo cidadão→visto→agendamento→documento. Happy paths e error paths. CI integration.
- Critérios:
  - 10+ cenários E2E
  - Happy paths cobertos
  - Error paths cobertos
  - Screenshots em falha
  - CI integration

**Prompt:**
```
Concluí a tarefa T8.3 (SGC E2E Testing). Repositório: ecossistema-sgc-frontend. Sprint: 8. Horas: [X]h. Artefactos: [lista]. Actualiza o project_state.json.
```


## T8.4: SGC Integration Testing

- Sprint: 8 | Fase: SGC-FE | Repo: ecossistema-sgc-backend | 8h
- Descrição: Testes de integração backend completos: Testcontainers, API contract tests, workflow integration, notification delivery verification.
- Critérios:
  - Testcontainers para PostgreSQL + Redis
  - API contract tests
  - Workflow end-to-end
  - Notification delivery test
  - Cobertura global >80%

**Prompt:**
```
Concluí a tarefa T8.4 (SGC Integration Testing). Repositório: ecossistema-sgc-backend. Sprint: 8. Horas: [X]h. Artefactos: [lista]. Actualiza o project_state.json.
```


## T9.1: SI Backend + CMS API

- Sprint: 9 | Fase: SI | Repo: ecossistema-si-backend | 14h
- Descrição: Scaffold SI backend: CMS API para páginas, menus, media. Multilingual content model (cada conteúdo em 4 idiomas). SEO metadata per page.
- Critérios:
  - Spring Boot scaffold funcional
  - CMS API (pages, menus, media)
  - Modelo multilingual
  - SEO metadata por página
  - Flyway migrations

**Prompt:**
```
Concluí a tarefa T9.1 (SI Backend + CMS API). Repositório: ecossistema-si-backend. Sprint: 9. Horas: [X]h. Artefactos: [lista]. Actualiza o project_state.json.
```


## T9.2: SI Content Management

- Sprint: 9 | Fase: SI | Repo: ecossistema-si-backend | 12h
- Descrição: Gestão de conteúdo: editorial workflow (draft→review→published), versioning, scheduling, content templates, media library integration with MinIO.
- Critérios:
  - Workflow editorial
  - Versioning de conteúdo
  - Scheduling de publicação
  - Media library
  - API de templates

**Prompt:**
```
Concluí a tarefa T9.2 (SI Content Management). Repositório: ecossistema-si-backend. Sprint: 9. Horas: [X]h. Artefactos: [lista]. Actualiza o project_state.json.
```


## T9.3: SI Institutional Pages API

- Sprint: 9 | Fase: SI | Repo: ecossistema-si-backend | 14h
- Descrição: APIs para: Embaixadora, Sobre Angola (Presidente, poderes, geografia, história, demografia, economia), relações bilaterais, eventos, contactos.
- Critérios:
  - API para Ambassador page
  - API para About Angola (8 subsecções)
  - API para bilateral relations
  - API para events/protocol
  - API para contactos

**Prompt:**
```
Concluí a tarefa T9.3 (SI Institutional Pages API). Repositório: ecossistema-si-backend. Sprint: 9. Horas: [X]h. Artefactos: [lista]. Actualiza o project_state.json.
```


## T10.1: SI Angular Frontend Scaffold

- Sprint: 10 | Fase: SI | Repo: ecossistema-si-frontend | 14h
- Descrição: Angular 18 public website: responsive design, navigation, footer, Angola branding, lazy loading, SSR preparation.
- Critérios:
  - Angular app funcional
  - Navigation menu
  - Footer com contactos
  - Branding Angola
  - Responsive (mobile-first)

**Prompt:**
```
Concluí a tarefa T10.1 (SI Angular Frontend Scaffold). Repositório: ecossistema-si-frontend. Sprint: 10. Horas: [X]h. Artefactos: [lista]. Actualiza o project_state.json.
```


## T10.2: SI Public Pages

- Sprint: 10 | Fase: SI | Repo: ecossistema-si-frontend | 14h
- Descrição: Páginas públicas: Homepage, Embaixadora, Sobre Angola, Sector Consular (info), Informações Úteis, Contactos, Eventos.
- Critérios:
  - Homepage com hero + highlights
  - Página da Embaixadora
  - 8 páginas Sobre Angola
  - Consular info pages
  - Página de contactos com mapa

**Prompt:**
```
Concluí a tarefa T10.2 (SI Public Pages). Repositório: ecossistema-si-frontend. Sprint: 10. Horas: [X]h. Artefactos: [lista]. Actualiza o project_state.json.
```


## T10.3: SI SEO + Structured Data

- Sprint: 10 | Fase: SI | Repo: ecossistema-si-frontend | 12h
- Descrição: SEO: meta tags, Schema.org structured data, hreflang tags (4 idiomas), sitemap.xml, robots.txt, Open Graph tags, Twitter Cards.
- Critérios:
  - Meta tags dinâmicos
  - Schema.org GovernmentOrganization
  - hreflang para 4 idiomas
  - Sitemap.xml automático
  - Lighthouse SEO >90

**Prompt:**
```
Concluí a tarefa T10.3 (SI SEO + Structured Data). Repositório: ecossistema-si-frontend. Sprint: 10. Horas: [X]h. Artefactos: [lista]. Actualiza o project_state.json.
```


## T11.1: WN Backend + Article API

- Sprint: 11 | Fase: WN | Repo: ecossistema-wn-backend | 14h
- Descrição: Scaffold WN backend: Article entity, CRUD API, categories, tags, author profiles, featured articles, pagination, search.
- Critérios:
  - Spring Boot scaffold funcional
  - Article CRUD API
  - Categories e Tags
  - Author profiles
  - Search endpoint

**Prompt:**
```
Concluí a tarefa T11.1 (WN Backend + Article API). Repositório: ecossistema-wn-backend. Sprint: 11. Horas: [X]h. Artefactos: [lista]. Actualiza o project_state.json.
```


## T11.2: WN Editorial Workflow

- Sprint: 11 | Fase: WN | Repo: ecossistema-wn-backend | 12h
- Descrição: Workflow editorial: draft→submitted→review→published. Scheduling, versioning, comments internos, role-based (editor/journalist/reviewer).
- Critérios:
  - Workflow editorial completo
  - Scheduling de publicação
  - Versioning
  - Comentários internos
  - Roles editor/journalist

**Prompt:**
```
Concluí a tarefa T11.2 (WN Editorial Workflow). Repositório: ecossistema-wn-backend. Sprint: 11. Horas: [X]h. Artefactos: [lista]. Actualiza o project_state.json.
```


## T11.3: WN Media + RSS

- Sprint: 11 | Fase: WN | Repo: ecossistema-wn-backend | 14h
- Descrição: Media management (MinIO), image resizing, RSS/Atom feed generation, newsletter subscription API, article sharing endpoints.
- Critérios:
  - Media upload + resizing
  - RSS feed funcional
  - Atom feed funcional
  - Newsletter subscription
  - Share endpoints (social)

**Prompt:**
```
Concluí a tarefa T11.3 (WN Media + RSS). Repositório: ecossistema-wn-backend. Sprint: 11. Horas: [X]h. Artefactos: [lista]. Actualiza o project_state.json.
```


## T12.1: WN Angular Frontend

- Sprint: 12 | Fase: WN | Repo: ecossistema-wn-frontend | 14h
- Descrição: Angular news portal: homepage with featured/latest, article page, category pages, responsive, branding Welwitschia.
- Critérios:
  - Homepage com featured + latest
  - Artigo page com social share
  - Category pages
  - Responsive design
  - Branding Welwitschia

**Prompt:**
```
Concluí a tarefa T12.1 (WN Angular Frontend). Repositório: ecossistema-wn-frontend. Sprint: 12. Horas: [X]h. Artefactos: [lista]. Actualiza o project_state.json.
```


## T12.2: WN Archive + Search

- Sprint: 12 | Fase: WN | Repo: ecossistema-wn-frontend | 14h
- Descrição: Arquivo de notícias com filtros (data, categoria, tag), pesquisa full-text, paginação infinita, breadcrumbs, related articles.
- Critérios:
  - Archive com filtros
  - Pesquisa full-text
  - Paginação infinita
  - Breadcrumbs
  - Artigos relacionados

**Prompt:**
```
Concluí a tarefa T12.2 (WN Archive + Search). Repositório: ecossistema-wn-frontend. Sprint: 12. Horas: [X]h. Artefactos: [lista]. Actualiza o project_state.json.
```


## T12.3: WN Newsletter + Social

- Sprint: 12 | Fase: WN | Repo: ecossistema-wn-frontend | 12h
- Descrição: Newsletter subscription form, email template, social media integration (Open Graph, Twitter Cards), share buttons, feed widget for SI.
- Critérios:
  - Subscription form
  - Email template
  - Social meta tags
  - Share buttons
  - Feed widget exportável

**Prompt:**
```
Concluí a tarefa T12.3 (WN Newsletter + Social). Repositório: ecossistema-wn-frontend. Sprint: 12. Horas: [X]h. Artefactos: [lista]. Actualiza o project_state.json.
```


## T13.1: GPJ Backend + Sprint/Task API

- Sprint: 13 | Fase: GPJ | Repo: ecossistema-gpj-backend | 14h
- Descrição: Scaffold GPJ backend: Sprint, Task, TimeLog entities. CRUD APIs, state machine, dependency tracking, capacity planning.
- Critérios:
  - Spring Boot scaffold
  - Sprint/Task CRUD
  - State machine per task
  - Dependency tracking
  - Capacity planning API

**Prompt:**
```
Concluí a tarefa T13.1 (GPJ Backend + Sprint/Task API). Repositório: ecossistema-gpj-backend. Sprint: 13. Horas: [X]h. Artefactos: [lista]. Actualiza o project_state.json.
```


## T13.2: GPJ Progress Tracking API

- Sprint: 13 | Fase: GPJ | Repo: ecossistema-gpj-backend | 12h
- Descrição: APIs de tracking: burndown data, velocity metrics, blocker management, milestone tracking, automated status notifications, report generation.
- Critérios:
  - Burndown data API
  - Velocity metrics
  - Blocker CRUD
  - Milestone tracking
  - Report generation endpoint

**Prompt:**
```
Concluí a tarefa T13.2 (GPJ Progress Tracking API). Repositório: ecossistema-gpj-backend. Sprint: 13. Horas: [X]h. Artefactos: [lista]. Actualiza o project_state.json.
```


## T13.3: GPJ Angular Dashboard

- Sprint: 13 | Fase: GPJ | Repo: ecossistema-gpj-frontend | 14h
- Descrição: Dashboard Angular: sprint board (kanban), Gantt chart, burndown chart, task detail, time logging, milestone timeline.
- Critérios:
  - Sprint board (kanban)
  - Gantt chart
  - Burndown chart
  - Task detail modal
  - Time logging

**Prompt:**
```
Concluí a tarefa T13.3 (GPJ Angular Dashboard). Repositório: ecossistema-gpj-frontend. Sprint: 13. Horas: [X]h. Artefactos: [lista]. Actualiza o project_state.json.
```


## T14.1: Angular Shared Libraries Final

- Sprint: 14 | Fase: Integração | Repo: ecossistema-sgc-frontend | 12h
- Descrição: Finalizar @ecossistema/ui-kit, @ecossistema/auth, @ecossistema/i18n, @ecossistema/api-client, @ecossistema/core. Publish como npm packages internos.
- Critérios:
  - 5 packages publicados
  - Documentação Compodoc
  - Storybook ou demos
  - Versionamento semântico
  - Consumidos por SGC/SI/WN/GPJ

**Prompt:**
```
Concluí a tarefa T14.1 (Angular Shared Libraries Final). Repositório: ecossistema-sgc-frontend. Sprint: 14. Horas: [X]h. Artefactos: [lista]. Actualiza o project_state.json.
```


## T14.2: OpenAPI Client Generation

- Sprint: 14 | Fase: Integração | Repo: ecossistema-docs | 10h
- Descrição: OpenAPI Generator para criar TypeScript clients para todos os 4 backends. Publish como @ecossistema/api-client. CI auto-generation.
- Critérios:
  - Clients para 4 backends
  - TypeScript types gerados
  - CI auto-regeneration
  - Versionamento alinhado
  - Consumido por frontends e mobile

**Prompt:**
```
Concluí a tarefa T14.2 (OpenAPI Client Generation). Repositório: ecossistema-docs. Sprint: 14. Horas: [X]h. Artefactos: [lista]. Actualiza o project_state.json.
```


## T14.3: Cross-System Integration

- Sprint: 14 | Fase: Integração | Repo: todos | 18h
- Descrição: Integração entre sistemas: SI consome dados SGC (consular info), WN publica notícias do SGC, GPJ monitora todos. Event-driven via RabbitMQ.
- Critérios:
  - SI↔SGC: consular data feed
  - WN↔SGC: news from activities
  - GPJ↔ALL: monitoring
  - RabbitMQ events
  - Integration tests E2E

**Prompt:**
```
Concluí a tarefa T14.3 (Cross-System Integration). Repositório: todos. Sprint: 14. Horas: [X]h. Artefactos: [lista]. Actualiza o project_state.json.
```


## T15.1: React Native Scaffold + Auth

- Sprint: 15 | Fase: Mobile | Repo: ecossistema-mobile | 16h
- Descrição: React Native 0.76+ scaffold: navigation (React Navigation), Keycloak auth (AppAuth), secure token storage, biometric auth option.
- Critérios:
  - React Native app funcional (iOS+Android)
  - Login via Keycloak
  - Secure token storage
  - Biometric auth option
  - Navigation structure

**Prompt:**
```
Concluí a tarefa T15.1 (React Native Scaffold + Auth). Repositório: ecossistema-mobile. Sprint: 15. Horas: [X]h. Artefactos: [lista]. Actualiza o project_state.json.
```


## T15.2: Mobile: Profile + Documents

- Sprint: 15 | Fase: Mobile | Repo: ecossistema-mobile | 12h
- Descrição: Ecrãs de perfil de cidadão, lista de documentos, status de processos, download de certificados, upload de documentos com câmara.
- Critérios:
  - Profile screen
  - Documents list
  - Process status tracking
  - Certificate download
  - Camera upload

**Prompt:**
```
Concluí a tarefa T15.2 (Mobile: Profile + Documents). Repositório: ecossistema-mobile. Sprint: 15. Horas: [X]h. Artefactos: [lista]. Actualiza o project_state.json.
```


## T15.3: Mobile: Visa + Tracking

- Sprint: 15 | Fase: Mobile | Repo: ecossistema-mobile | 12h
- Descrição: Fluxo de aplicação de visto mobile, status tracking com timeline visual, push notifications para mudanças de estado.
- Critérios:
  - Visa application flow (simplified)
  - Status tracking timeline
  - Push notifications
  - Offline draft saving
  - Deep linking

**Prompt:**
```
Concluí a tarefa T15.3 (Mobile: Visa + Tracking). Repositório: ecossistema-mobile. Sprint: 15. Horas: [X]h. Artefactos: [lista]. Actualiza o project_state.json.
```


## T16.1: Mobile: Appointments

- Sprint: 16 | Fase: Mobile | Repo: ecossistema-mobile | 14h
- Descrição: Booking de agendamentos mobile: calendar view, slot selection, confirmation, reminder notifications, QR code for check-in.
- Critérios:
  - Calendar com slots disponíveis
  - Booking flow
  - Confirmation screen
  - Reminder push notifications
  - QR code check-in

**Prompt:**
```
Concluí a tarefa T16.1 (Mobile: Appointments). Repositório: ecossistema-mobile. Sprint: 16. Horas: [X]h. Artefactos: [lista]. Actualiza o project_state.json.
```


## T16.2: Mobile: Push + Offline

- Sprint: 16 | Fase: Mobile | Repo: ecossistema-mobile | 14h
- Descrição: Push notifications (Firebase), offline data caching (AsyncStorage), sync queue para operações offline, i18n mobile (4 idiomas).
- Critérios:
  - Push notifications (FCM)
  - Offline data cache
  - Sync queue funcional
  - 4 idiomas
  - OTA updates (CodePush)

**Prompt:**
```
Concluí a tarefa T16.2 (Mobile: Push + Offline). Repositório: ecossistema-mobile. Sprint: 16. Horas: [X]h. Artefactos: [lista]. Actualiza o project_state.json.
```


## T16.3: Mobile: E2E Testing

- Sprint: 16 | Fase: Mobile | Repo: ecossistema-mobile | 12h
- Descrição: Testes E2E mobile (Detox ou Appium): fluxos críticos (auth→profile→visa→appointment), screenshot testing, CI integration.
- Critérios:
  - Detox/Appium configurado
  - 5+ cenários E2E
  - Auth→visa→appointment flow
  - Screenshot testing
  - CI integration

**Prompt:**
```
Concluí a tarefa T16.3 (Mobile: E2E Testing). Repositório: ecossistema-mobile. Sprint: 16. Horas: [X]h. Artefactos: [lista]. Actualiza o project_state.json.
```


## T17.1: Full E2E Test Suite

- Sprint: 17 | Fase: Testes | Repo: todos | 14h
- Descrição: Suite completa de testes E2E (Cypress): SGC admin flows, SI public pages, WN editorial flow, cross-system integration scenarios.
- Critérios:
  - 30+ cenários E2E
  - SGC admin flows
  - SI public navigation
  - WN editorial flow
  - Cross-system scenarios

**Prompt:**
```
Concluí a tarefa T17.1 (Full E2E Test Suite). Repositório: todos. Sprint: 17. Horas: [X]h. Artefactos: [lista]. Actualiza o project_state.json.
```


## T17.2: Security Audit

- Sprint: 17 | Fase: Testes | Repo: todos | 14h
- Descrição: Auditoria de segurança: OWASP ZAP scan, dependency vulnerability check (Trivy), Keycloak config review, GDPR compliance check, penetration testing.
- Critérios:
  - OWASP ZAP scan limpo
  - Trivy scan sem criticals
  - Keycloak config reviewed
  - GDPR checklist completo
  - Penetration test report

**Prompt:**
```
Concluí a tarefa T17.2 (Security Audit). Repositório: todos. Sprint: 17. Horas: [X]h. Artefactos: [lista]. Actualiza o project_state.json.
```


## T17.3: Performance + Load Testing

- Sprint: 17 | Fase: Testes | Repo: todos | 12h
- Descrição: Performance: JMeter load tests, Lighthouse scores, database query optimization, caching strategy validation, CDN configuration.
- Critérios:
  - JMeter: 100 concurrent users
  - Lighthouse Performance >80
  - Slow queries optimized
  - Redis caching validated
  - Response time <3s p95

**Prompt:**
```
Concluí a tarefa T17.3 (Performance + Load Testing). Repositório: todos. Sprint: 17. Horas: [X]h. Artefactos: [lista]. Actualiza o project_state.json.
```


## T18.1: UAT com Equipa Embaixada

- Sprint: 18 | Fase: Testes | Repo: todos | 14h
- Descrição: User Acceptance Testing com staff da embaixada: cenários reais, feedback collection, usability assessment, training needs identification.
- Critérios:
  - Cenários UAT definidos
  - Sessões com staff
  - Feedback documentado
  - Issues priorizados
  - Training needs identified

**Prompt:**
```
Concluí a tarefa T18.1 (UAT com Equipa Embaixada). Repositório: todos. Sprint: 18. Horas: [X]h. Artefactos: [lista]. Actualiza o project_state.json.
```


## T18.2: Bug Fixing + Polish

- Sprint: 18 | Fase: Testes | Repo: todos | 14h
- Descrição: Correcção de bugs UAT, polish visual, edge cases, error handling improvements, loading states, empty states, responsive fixes.
- Critérios:
  - Todos os bugs UAT critical corrigidos
  - Polish visual completo
  - Error handling robusto
  - Loading/empty states
  - Responsive verificado

**Prompt:**
```
Concluí a tarefa T18.2 (Bug Fixing + Polish). Repositório: todos. Sprint: 18. Horas: [X]h. Artefactos: [lista]. Actualiza o project_state.json.
```


## T18.3: Technical Documentation

- Sprint: 18 | Fase: Testes | Repo: ecossistema-docs | 12h
- Descrição: Documentação técnica final: LaTeX document completo, API docs, deployment guide, runbook, architecture diagrams, data dictionary.
- Critérios:
  - LaTeX doc completo
  - API docs actualizados
  - Deployment guide
  - Runbook para operações
  - Data dictionary

**Prompt:**
```
Concluí a tarefa T18.3 (Technical Documentation). Repositório: ecossistema-docs. Sprint: 18. Horas: [X]h. Artefactos: [lista]. Actualiza o project_state.json.
```


## T19.1: Production Kubernetes Deploy

- Sprint: 19 | Fase: Go-Live | Repo: ecossistema-infra | 14h
- Descrição: Deploy produção: Kubernetes manifests, Helm charts, SSL certificates, DNS config, monitoring (Prometheus+Grafana), log aggregation (Loki), backup automation.
- Critérios:
  - Kubernetes cluster configurado
  - Helm charts para 4 backends
  - SSL/TLS configurado
  - Monitoring operacional
  - Backup automático diário

**Prompt:**
```
Concluí a tarefa T19.1 (Production Kubernetes Deploy). Repositório: ecossistema-infra. Sprint: 19. Horas: [X]h. Artefactos: [lista]. Actualiza o project_state.json.
```


## T19.2: WordPress Data Migration

- Sprint: 19 | Fase: Go-Live | Repo: ecossistema-infra | 12h
- Descrição: Migração de dados do WordPress actual: conteúdo de páginas, imagens, contactos. Script de migração, validação, URL redirects.
- Critérios:
  - Script de migração completo
  - Conteúdo migrado e validado
  - Imagens transferidas para MinIO
  - URL redirects configurados
  - Zero data loss verificado

**Prompt:**
```
Concluí a tarefa T19.2 (WordPress Data Migration). Repositório: ecossistema-infra. Sprint: 19. Horas: [X]h. Artefactos: [lista]. Actualiza o project_state.json.
```


## T19.3: Staff Training + Go-Live

- Sprint: 19 | Fase: Go-Live | Repo: ecossistema-docs | 14h
- Descrição: Formação do pessoal da embaixada: sessões hands-on, user guides (PDF), video tutorials, support channel setup, go-live checklist, DNS cutover.
- Critérios:
  - Sessões de formação realizadas
  - User guides PDF entregues
  - Video tutorials gravados
  - Support channel operacional
  - DNS cutover executado

**Prompt:**
```
Concluí a tarefa T19.3 (Staff Training + Go-Live). Repositório: ecossistema-docs. Sprint: 19. Horas: [X]h. Artefactos: [lista]. Actualiza o project_state.json.
```


## Sprint 0: Infraestrutura & Fundação

  - T0.1: Docker Compose + Infra Repo (12h)
  - T0.2: Commons Maven Multi-Module (12h)
  - T0.3: GitHub Repos + CI/CD (8h)
  - T0.4: ADRs + Documentação Base (8h)


## Sprint 1: SGC Backend Core I

  - T1.1: SGC Scaffold + Flyway V1 (14h)
  - T1.2: Citizen Management CRUD (14h)
  - T1.3: Keycloak Auth + RBAC (12h)


## Sprint 2: SGC Backend Core II

  - T2.1: Visa Processing Module (16h)
  - T2.2: Appointment System (12h)
  - T2.3: OpenAPI Docs + Tests (12h)


## Sprint 3: SGC Backend Avançado I

  - T3.1: Document Management + MinIO (14h)
  - T3.2: Civil Registry Module (12h)
  - T3.3: Notarial Services Module (14h)


## Sprint 4: SGC Backend Avançado II

  - T4.1: Workflow Engine (14h)
  - T4.2: Notification Service (12h)
  - T4.3: Audit + Reporting Module (10h)
  - T4.4: API Security Hardening (4h)


## Sprint 5: SGC Frontend Core I

  - T5.1: Angular Scaffold + Auth UI (16h)
  - T5.2: Citizen Dashboard UI (14h)
  - T5.3: Visa Application Forms (10h)


## Sprint 6: SGC Frontend Core II

  - T6.1: Appointment Calendar UI (14h)
  - T6.2: Document Management UI (12h)
  - T6.3: Reports Dashboard (14h)


## Sprint 7: SGC Frontend Avançado I

  - T7.1: Civil Registry + Notarial UI (14h)
  - T7.2: Workflow Admin Panel (12h)
  - T7.3: User Management Admin (14h)


## Sprint 8: SGC Frontend Avançado II + Testes

  - T8.1: i18n (PT/DE/EN/CZ) (12h)
  - T8.2: Accessibility (WCAG 2.1 AA) (10h)
  - T8.3: SGC E2E Testing (10h)
  - T8.4: SGC Integration Testing (8h)


## Sprint 9: Sítio Institucional Backend

  - T9.1: SI Backend + CMS API (14h)
  - T9.2: SI Content Management (12h)
  - T9.3: SI Institutional Pages API (14h)


## Sprint 10: Sítio Institucional Frontend

  - T10.1: SI Angular Frontend Scaffold (14h)
  - T10.2: SI Public Pages (14h)
  - T10.3: SI SEO + Structured Data (12h)


## Sprint 11: Welwitschia Notícias Backend

  - T11.1: WN Backend + Article API (14h)
  - T11.2: WN Editorial Workflow (12h)
  - T11.3: WN Media + RSS (14h)


## Sprint 12: Welwitschia Notícias Frontend

  - T12.1: WN Angular Frontend (14h)
  - T12.2: WN Archive + Search (14h)
  - T12.3: WN Newsletter + Social (12h)


## Sprint 13: GPJ Sistema & Integração I

  - T13.1: GPJ Backend + Sprint/Task API (14h)
  - T13.2: GPJ Progress Tracking API (12h)
  - T13.3: GPJ Angular Dashboard (14h)


## Sprint 14: Shared Libraries & Integração II

  - T14.1: Angular Shared Libraries Final (12h)
  - T14.2: OpenAPI Client Generation (10h)
  - T14.3: Cross-System Integration (18h)


## Sprint 15: React Native Mobile I

  - T15.1: React Native Scaffold + Auth (16h)
  - T15.2: Mobile: Profile + Documents (12h)
  - T15.3: Mobile: Visa + Tracking (12h)


## Sprint 16: React Native Mobile II

  - T16.1: Mobile: Appointments (14h)
  - T16.2: Mobile: Push + Offline (14h)
  - T16.3: Mobile: E2E Testing (12h)


## Sprint 17: Testes & Segurança

  - T17.1: Full E2E Test Suite (14h)
  - T17.2: Security Audit (14h)
  - T17.3: Performance + Load Testing (12h)


## Sprint 18: UAT & Documentação

  - T18.1: UAT com Equipa Embaixada (14h)
  - T18.2: Bug Fixing + Polish (14h)
  - T18.3: Technical Documentation (12h)


## Sprint 19: Go-Live & Formação

  - T19.1: Production Kubernetes Deploy (14h)
  - T19.2: WordPress Data Migration (12h)
  - T19.3: Staff Training + Go-Live (14h)
