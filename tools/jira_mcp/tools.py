# tools/jira_mcp/tools.py

from .client import jira_request


def get_ticket(issue_key: str) -> dict:
    """
    Obtiene información relevante del ticket
    """
    data = jira_request("GET", f"/issue/{issue_key}")

    return {
        "id": data.get("id"),
        "key": data.get("key"),
        "summary": data["fields"].get("summary"),
        "description": data["fields"].get("description"),
        "status": data["fields"]["status"]["name"]
    }


def update_ticket(issue_key: str, content: str) -> dict:
    """
    Actualiza la descripción del ticket
    """
    jira_request("PUT", f"/issue/{issue_key}", {
        "fields": {
            "description": content
        }
    })

    return {
        "status": "updated",
        "issue_key": issue_key
    }


def transition_ticket(issue_key: str, transition_id: str) -> dict:
    """
    Mueve el ticket de estado en Jira
    (debes mapear transition_id según tu workflow)
    """
    jira_request("POST", f"/issue/{issue_key}/transitions", {
        "transition": {
            "id": transition_id
        }
    })

    return {
        "status": "transitioned",
        "issue_key": issue_key,
        "transition_id": transition_id
    }


def format_for_jira(markdown_content: str) -> str:
    """
    Placeholder para adaptar markdown a formato Jira si lo necesitas.
    Actualmente devuelve el contenido tal cual.
    """
    return markdown_content