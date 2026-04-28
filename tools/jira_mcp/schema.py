# tools/jira_mcp/schema.py

jira_tools = [
    {
        "name": "jira.get_ticket",
        "description": "Obtiene un ticket de Jira por issue_key",
        "input_schema": {
            "type": "object",
            "properties": {
                "issue_key": {
                    "type": "string",
                    "description": "Clave del ticket, ej: QA-123"
                }
            },
            "required": ["issue_key"]
        }
    },
    {
        "name": "jira.update_ticket",
        "description": "Actualiza la descripción del ticket en Jira",
        "input_schema": {
            "type": "object",
            "properties": {
                "issue_key": {"type": "string"},
                "content": {"type": "string"}
            },
            "required": ["issue_key", "content"]
        }
    },
    {
        "name": "jira.transition_ticket",
        "description": "Cambia el estado del ticket en Jira",
        "input_schema": {
            "type": "object",
            "properties": {
                "issue_key": {"type": "string"},
                "transition_id": {"type": "string"}
            },
            "required": ["issue_key", "transition_id"]
        }
    }
]