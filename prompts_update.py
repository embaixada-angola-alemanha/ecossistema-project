#!/usr/bin/env python3
"""
═══════════════════════════════════════════════════════════════
  GESTOR DE PROJECTO — ECOSSISTEMA DIGITAL v2.0
  Embaixada de Angola na Alemanha
  
  Multi-Repo | Spring Boot 3.4 | Angular 18 | React Native
  PostgreSQL 16 | Keycloak | 68 tarefas | 20 sprints | 820h
═══════════════════════════════════════════════════════════════
"""

import json, sys, os, argparse
from datetime import datetime, timezone

STATE_FILE = "project_state.json"

# ─── COLOURS ───
class C:
    R = "\033[0m"
    B = "\033[1m"
    RED = "\033[91m"
    GRN = "\033[92m"
    YLW = "\033[93m"
    BLU = "\033[94m"
    MAG = "\033[95m"
    CYN = "\033[96m"
    DIM = "\033[2m"

PHASE_COLOURS = {
    "Infra": C.BLU, "SGC-BE": C.RED, "SGC-FE": C.YLW, "SI": C.GRN,
    "WN": C.MAG, "GPJ": C.CYN, "Integração": C.YLW, "Mobile": C.BLU,
    "Testes": C.DIM, "Go-Live": C.GRN,
}

def load():
    with open(STATE_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save(state):
    with open(STATE_FILE, "w", encoding="utf-8") as f:
        json.dump(state, f, ensure_ascii=False, indent=2)

def now_iso():
    return datetime.now(timezone.utc).isoformat()

def get_task(state, tid):
    for t in state["tarefas"]:
        if t["id"] == tid:
            return t
    return None

def sprint_tasks(state, sid):
    return [t for t in state["tarefas"] if t["sprint"] == sid]

def next_task(state):
    for t in state["tarefas"]:
        if t["estado"] == "PENDENTE":
            return t
    return None

def next_msg_id(state):
    if not state["mensagens_cliente"]:
        return 1
    return max(m["id"] for m in state["mensagens_cliente"]) + 1

# ─── STATUS ───
def cmd_status(state):
    p = state["projecto"]
    done = p["tarefas_concluidas"]
    total = p["total_tarefas"]
    hrs_done = p["horas_consumidas"]
    hrs_plan = p["horas_totais_planeadas"]
    pct = p["progresso_pct"]

    bar_len = 40
    filled = int(bar_len * pct / 100)
    bar = f"{'█' * filled}{'░' * (bar_len - filled)}"

    print(f"\n{C.B}{'═' * 60}{C.R}")
    print(f"{C.B}{C.BLU}  ECOSSISTEMA DIGITAL v2.0 — Estado do Projecto{C.R}")
    print(f"{C.B}{'═' * 60}{C.R}")
    print(f"  Arquitectura: {C.B}Multi-Repo (12 repositórios){C.R}")
    print(f"  Stack:        {C.B}Spring Boot 3.4 + Angular 18 + React Native{C.R}")
    print(f"  Database:     {C.B}PostgreSQL 16 + Redis 7{C.R}")
    print(f"  Auth:         {C.B}Keycloak + JWT{C.R}")
    print(f"  Estado:       {C.B}{p['estado']}{C.R}")
    print(f"  Prazo:        {C.B}{p['data_fim_prevista']}{C.R}")
    print(f"\n  {C.B}Progresso:{C.R} [{bar}] {pct:.1f}%")
    print(f"  Tarefas:   {C.GRN}{done}{C.R}/{total}")
    print(f"  Horas:     {hrs_done:.0f}/{hrs_plan:.0f}h")
    print()

    # Sprint summary
    print(f"  {C.B}Sprints:{C.R}")
    for s in state["sprints"]:
        sid = s["id"]
        icon = "✅" if s["estado"] == "CONCLUIDO" else "🔄" if s["estado"] == "EM_PROGRESSO" else "⬜"
        tasks = sprint_tasks(state, sid)
        done_t = sum(1 for t in tasks if t["estado"] == "CONCLUIDA")
        colour = PHASE_COLOURS.get(s["fase"], "")
        print(f"    {icon} S{sid:02d} {colour}{s['titulo']:<35}{C.R} {done_t}/{len(tasks)} tarefas  {s['progresso_pct']:.0f}%")

    # Next task
    nt = next_task(state)
    if nt:
        print(f"\n  {C.B}Próxima tarefa:{C.R} {C.YLW}{nt['id']}{C.R} — {nt['nome']} ({nt['horas_planeadas']}h)")
        print(f"    Repo: {nt.get('repo', '?')} | Sprint {nt['sprint']}")
    print(f"\n{C.B}{'═' * 60}{C.R}\n")

# ─── LIST ───
def cmd_list(state):
    print(f"\n{C.B}{'═' * 80}{C.R}")
    print(f"{C.B}  LISTA DE TAREFAS — 68 tarefas, 20 sprints{C.R}")
    print(f"{C.B}{'═' * 80}{C.R}")
    
    current_sprint = -1
    for t in state["tarefas"]:
        if t["sprint"] != current_sprint:
            current_sprint = t["sprint"]
            s = state["sprints"][current_sprint]
            print(f"\n  {C.B}Sprint {current_sprint}: {s['titulo']}{C.R} ({s['fase']}) — {s['data_inicio']} → {s['data_fim']}")
            print(f"  {'─' * 76}")

        icon = "✅" if t["estado"] == "CONCLUIDA" else "🔄" if t["estado"] == "EM_PROGRESSO" else "⬜" if t["estado"] == "PENDENTE" else "🚫"
        colour = PHASE_COLOURS.get(t["fase"], "")
        repo = t.get("repo", "?")
        print(f"    {icon} {C.B}{t['id']:6s}{C.R} {colour}{t['nome']:<40}{C.R} {t['horas_planeadas']:3.0f}h  [{repo}]")
    print()

# ─── TASK PROMPT ───
def cmd_task(state, tid):
    t = get_task(state, tid)
    if not t:
        print(f"{C.RED}Tarefa {tid} não encontrada.{C.R}")
        return

    desc = t.get("descricao", "Implementar conforme especificação")
    criterios = t.get("criterios", [])
    repo = t.get("repo", "?")

    print(f"\n{C.B}{'═' * 70}{C.R}")
    print(f"{C.B}{C.BLU}  PROMPT DE CONCLUSÃO — {tid}: {t['nome']}{C.R}")
    print(f"{C.B}{'═' * 70}{C.R}")
    print(f"""
{C.B}Copiar e colar ao Claude quando concluir:{C.R}

───────────────────────────────────────────────────────
Concluí a tarefa {tid} ({t['nome']}).

Repositório: {repo}
Sprint: {t['sprint']} ({state['sprints'][t['sprint']]['titulo']})
Fase: {t['fase']}
Horas planeadas: {t['horas_planeadas']}h
Horas consumidas: [PREENCHER]h

Descrição: {desc}

Critérios de aceitação cumpridos:
""")
    for c in criterios:
        print(f"  ✅ {c}")
    print(f"""
Artefactos entregues:
  • [PREENCHER]

Notas: [PREENCHER]

Actualiza o project_state.json conforme o PROTOCOLO.md.
───────────────────────────────────────────────────────
""")

# ─── SPRINT PROMPT ───
def cmd_sprint(state, sid):
    s = state["sprints"][sid]
    tasks = sprint_tasks(state, sid)
    print(f"\n{C.B}{'═' * 70}{C.R}")
    print(f"{C.B}{C.MAG}  PROMPT DE SPRINT REVIEW — Sprint {sid}: {s['titulo']}{C.R}")
    print(f"{C.B}{'═' * 70}{C.R}")
    print(f"\n  Fase: {s['fase']} | {s['data_inicio']} → {s['data_fim']} | {s['horas_planeadas']}h")
    print(f"\n  Tarefas:")
    for t in tasks:
        icon = "✅" if t["estado"] == "CONCLUIDA" else "⬜"
        print(f"    {icon} {t['id']}: {t['nome']} ({t['horas_planeadas']}h) [{t.get('repo','?')}]")
    print()

# ─── EXECUTE TASK ───
def cmd_execute_task(state, tid, hours=None, artefactos=None, notas=None):
    t = get_task(state, tid)
    if not t:
        print(f"{C.RED}Tarefa {tid} não encontrada.{C.R}")
        return

    # Update task
    t["estado"] = "CONCLUIDA"
    t["progresso_pct"] = 100
    t["horas_consumidas"] = hours if hours else t["horas_planeadas"]
    t["data_conclusao"] = now_iso()
    t["artefactos"] = artefactos if artefactos else ["Conforme especificação"]
    t["notas"] = notas if notas else f"Concluída em {t['horas_consumidas']}h"

    # Recalculate sprint
    sid = t["sprint"]
    s = state["sprints"][sid]
    tasks = sprint_tasks(state, sid)
    done_tasks = [tt for tt in tasks if tt["estado"] == "CONCLUIDA"]
    s["horas_consumidas"] = sum(tt["horas_consumidas"] for tt in tasks)
    s["progresso_pct"] = (len(done_tasks) / len(tasks)) * 100
    sprint_complete = len(done_tasks) == len(tasks)
    if sprint_complete:
        s["estado"] = "CONCLUIDO"
    elif len(done_tasks) > 0:
        s["estado"] = "EM_PROGRESSO"

    # Recalculate project
    p = state["projecto"]
    all_done = [tt for tt in state["tarefas"] if tt["estado"] == "CONCLUIDA"]
    p["horas_consumidas"] = sum(tt["horas_consumidas"] for tt in state["tarefas"])
    p["tarefas_concluidas"] = len(all_done)
    p["progresso_pct"] = (len(all_done) / p["total_tarefas"]) * 100
    p["estado"] = "CONCLUIDO" if len(all_done) == p["total_tarefas"] else "EM_PROGRESSO"

    # History
    state["historico"].append({
        "data": now_iso(),
        "evento": "TAREFA_CONCLUIDA",
        "detalhe": f"{tid}: {t['nome']} | {t['horas_consumidas']}h | Sprint {sid} | Repo: {t.get('repo', '?')}"
    })

    # Client message
    msg = f"✅ Tarefa {tid} concluída: {t['nome']}\n\nFase: {t['fase']} | Sprint {sid} | {t['horas_consumidas']}h | Repo: {t.get('repo', '?')}\nProgresso global: {p['progresso_pct']:.1f}% | Tarefas: {p['tarefas_concluidas']}/{p['total_tarefas']}"
    state["mensagens_cliente"].append({
        "id": next_msg_id(state),
        "data": now_iso(),
        "de": "sistema",
        "texto": msg,
        "tipo": "tarefa_concluida"
    })

    # Sprint complete message
    if sprint_complete:
        state["historico"].append({
            "data": now_iso(),
            "evento": "SPRINT_CONCLUIDO",
            "detalhe": f"Sprint {sid}: {s['titulo']} | {s['horas_consumidas']}h"
        })
        
        next_sprint = state["sprints"][sid + 1] if sid + 1 < len(state["sprints"]) else None
        next_tasks = sprint_tasks(state, sid + 1) if next_sprint else []
        next_info = ""
        if next_sprint:
            next_info = f"\n\n➡️ Próximo: Sprint {sid+1} — {next_sprint['titulo']} ({next_sprint['data_inicio']}→{next_sprint['data_fim']})"
            for nt in next_tasks[:4]:
                next_info += f"\n  • {nt['id']}: {nt['nome']} ({nt['horas_planeadas']}h)"

        sprint_msg = f"🏁 SPRINT {sid} CONCLUÍDO: {s['titulo']}\n\n📊 Métricas:\n• Tarefas: {len(done_tasks)}/{len(tasks)}\n• Horas: {s['horas_consumidas']:.0f}h de {s['horas_planeadas']}h planeadas\n• Progresso global: {p['progresso_pct']:.1f}%{next_info}"
        state["mensagens_cliente"].append({
            "id": next_msg_id(state),
            "data": now_iso(),
            "de": "sistema",
            "texto": sprint_msg,
            "tipo": "sprint_concluido"
        })

    save(state)

    print(f"\n  {C.GRN}✅ {tid} concluída.{C.R} Sprint {sid}: {s['progresso_pct']:.0f}%. Global: {p['progresso_pct']:.1f}% ({p['tarefas_concluidas']}/{p['total_tarefas']})")
    if sprint_complete:
        print(f"  {C.MAG}🏁 Sprint {sid} CONCLUÍDO!{C.R}")
    nt = next_task(state)
    if nt:
        print(f"  Próxima: {C.YLW}{nt['id']}{C.R} — {nt['nome']} ({nt['horas_planeadas']}h) [{nt.get('repo','?')}]")
    print()

# ─── NEXT ───
def cmd_next(state):
    nt = next_task(state)
    if nt:
        print(f"\n  {C.B}Próxima tarefa:{C.R} {C.YLW}{nt['id']}{C.R} — {nt['nome']}")
        print(f"  Sprint: {nt['sprint']} | Fase: {nt['fase']} | Repo: {nt.get('repo','?')} | {nt['horas_planeadas']}h")
        print(f"  Descrição: {nt.get('descricao', '—')}")
        criterios = nt.get("criterios", [])
        if criterios:
            print(f"  Critérios:")
            for c in criterios:
                print(f"    • {c}")
        print()
    else:
        print(f"\n  {C.GRN}🎉 Todas as tarefas concluídas!{C.R}\n")

# ─── BURNDOWN ───
def cmd_burndown(state):
    print(f"\n{C.B}  BURNDOWN — Horas restantes por sprint{C.R}")
    print(f"  {'─' * 60}")
    remaining = state["projecto"]["horas_totais_planeadas"]
    for s in state["sprints"]:
        tasks = sprint_tasks(state, s["id"])
        consumed = sum(t["horas_consumidas"] for t in tasks)
        remaining -= consumed
        bar_len = int(remaining / state["projecto"]["horas_totais_planeadas"] * 50)
        bar = "█" * bar_len
        icon = "✅" if s["estado"] == "CONCLUIDO" else "🔄" if s["estado"] == "EM_PROGRESSO" else "⬜"
        print(f"  {icon} S{s['id']:02d} {bar:<50s} {remaining:.0f}h")
    print()

# ─── REPOS ───
def cmd_repos(state):
    print(f"\n{C.B}  ESTADO POR REPOSITÓRIO{C.R}")
    print(f"  {'─' * 60}")
    repos = {}
    for t in state["tarefas"]:
        repo = t.get("repo", "?")
        if repo not in repos:
            repos[repo] = {"total": 0, "done": 0, "hours_plan": 0, "hours_done": 0}
        repos[repo]["total"] += 1
        repos[repo]["hours_plan"] += t["horas_planeadas"]
        repos[repo]["hours_done"] += t["horas_consumidas"]
        if t["estado"] == "CONCLUIDA":
            repos[repo]["done"] += 1

    for repo, data in sorted(repos.items()):
        pct = (data["done"] / data["total"] * 100) if data["total"] > 0 else 0
        print(f"  {C.B}{repo:<35}{C.R} {data['done']}/{data['total']} tarefas  {pct:.0f}%  ({data['hours_done']:.0f}/{data['hours_plan']:.0f}h)")
    print()

# ─── EXPORT ───
def cmd_export(state):
    lines = ["# PROMPTS COMPLETAS — ECOSSISTEMA DIGITAL v2.0\n"]
    lines.append(f"Total: {len(state['tarefas'])} task prompts + {len(state['sprints'])} sprint prompts\n\n---\n")
    
    for t in state["tarefas"]:
        lines.append(f"\n## {t['id']}: {t['nome']}\n")
        lines.append(f"- Sprint: {t['sprint']} | Fase: {t['fase']} | Repo: {t.get('repo','?')} | {t['horas_planeadas']}h")
        lines.append(f"- Descrição: {t.get('descricao', '—')}")
        criterios = t.get("criterios", [])
        if criterios:
            lines.append("- Critérios:")
            for c in criterios:
                lines.append(f"  - {c}")
        lines.append(f"\n**Prompt:**\n```\nConcluí a tarefa {t['id']} ({t['nome']}). Repositório: {t.get('repo','?')}. Sprint: {t['sprint']}. Horas: [X]h. Artefactos: [lista]. Actualiza o project_state.json.\n```\n")

    for s in state["sprints"]:
        lines.append(f"\n## Sprint {s['id']}: {s['titulo']}\n")
        tasks = sprint_tasks(state, s["id"])
        for t in tasks:
            lines.append(f"  - {t['id']}: {t['nome']} ({t['horas_planeadas']}h)")
        lines.append("")

    output = "prompts_completas_v2.md"
    with open(output, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    print(f"\n  {C.GRN}✅ Exportado para {output}{C.R} ({len(lines)} linhas)\n")

# ─── MAIN ───
def main():
    parser = argparse.ArgumentParser(description="Gestor de Projecto — Ecossistema Digital v2.0")
    parser.add_argument("--status", action="store_true", help="Estado actual do projecto")
    parser.add_argument("--list", action="store_true", help="Lista todas as tarefas")
    parser.add_argument("--next", action="store_true", help="Próxima tarefa pendente")
    parser.add_argument("--task", type=str, help="Prompt de conclusão para tarefa (ex: T0.1)")
    parser.add_argument("--sprint", type=int, help="Prompt de review para sprint (ex: 0)")
    parser.add_argument("--execute-task", type=str, dest="execute_task", help="Marca tarefa como concluída")
    parser.add_argument("--hours", type=float, help="Horas consumidas (com --execute-task)")
    parser.add_argument("--export", action="store_true", help="Exporta todas as prompts")
    parser.add_argument("--burndown", action="store_true", help="Dados de burndown")
    parser.add_argument("--repos", action="store_true", help="Estado por repositório")

    args = parser.parse_args()
    
    if not os.path.exists(STATE_FILE):
        print(f"{C.RED}Erro: {STATE_FILE} não encontrado.{C.R}")
        sys.exit(1)

    state = load()

    if args.status:
        cmd_status(state)
    elif args.list:
        cmd_list(state)
    elif args.next:
        cmd_next(state)
    elif args.task:
        cmd_task(state, args.task)
    elif args.sprint is not None:
        cmd_sprint(state, args.sprint)
    elif args.execute_task:
        cmd_execute_task(state, args.execute_task, hours=args.hours)
    elif args.export:
        cmd_export(state)
    elif args.burndown:
        cmd_burndown(state)
    elif args.repos:
        cmd_repos(state)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
