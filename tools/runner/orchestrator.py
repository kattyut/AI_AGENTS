# runner/orchestrator.py

from runner.loader import load_markdown
from runner.llm import run_llm
from runner.parser import parse_command

from tools.jira_mcp.tools import (
    get_ticket,
    update_ticket,
    format_for_jira
)


def build_prompt(agent_md, prompt_md, command_md, context):
    return f"""
{agent_md}

{command_md}

{prompt_md}

--- CONTEXT ---
{context}
"""


def run(command_input: str):
    parsed = parse_command(command_input)

    if parsed["command"] != "/qa.enrich.jira":
        raise Exception("Comando no soportado")

    issue_key = parsed["issue_key"]

    if not issue_key:
        raise Exception("Debe proporcionar issue_key")

    # 1. Obtener ticket
    ticket = get_ticket(issue_key)

    context = f"""
Issue: {ticket['key']}
Summary: {ticket['summary']}
Description: {ticket['description']}
Status: {ticket['status']}
"""

    # 2. Cargar markdowns
    agent_md = load_markdown("agents/jira-qa-agent.md")
    prompt_md = load_markdown("prompts/qa-enrich-jira.prompt.md")
    command_md = load_markdown("commands/qa.enrich.jira.md")

    # 3. Construir prompt final
    full_prompt = build_prompt(agent_md, prompt_md, command_md, context)

    # 4. Ejecutar LLM
    result = run_llm(full_prompt)

    print("\n--- RESULTADO ---\n")
    print(result)

    # 5. Validar si es publicable
    if "❌" in result:
        print("\nNo se publica en Jira por errores.\n")
        return

    # 6. Formatear y subir
    jira_content = format_for_jira(result)

    update_ticket(issue_key, jira_content)

    print(f"\nTicket {issue_key} actualizado correctamente.\n")