# tools/jira_mcp/client.py

import os
import requests
from requests.auth import HTTPBasicAuth

JIRA_URL = os.getenv("JIRA_URL")          # ej: https://tu-dominio.atlassian.net
JIRA_EMAIL = os.getenv("JIRA_EMAIL")
JIRA_TOKEN = os.getenv("JIRA_TOKEN")

DEFAULT_HEADERS = {
    "Accept": "application/json",
    "Content-Type": "application/json"
}


class JiraClientError(Exception):
    pass


def jira_request(method: str, endpoint: str, data: dict | None = None, params: dict | None = None):
    if not JIRA_URL or not JIRA_EMAIL or not JIRA_TOKEN:
        raise JiraClientError("Faltan variables de entorno: JIRA_URL, JIRA_EMAIL, JIRA_TOKEN")

    url = f"{JIRA_URL}/rest/api/3{endpoint}"

    response = requests.request(
        method=method,
        url=url,
        json=data,
        params=params,
        headers=DEFAULT_HEADERS,
        auth=HTTPBasicAuth(JIRA_EMAIL, JIRA_TOKEN),
        timeout=30
    )

    if not response.ok:
        raise JiraClientError(
            f"Error Jira [{response.status_code}] {response.text}"
        )

    if response.text:
        return response.json()
    return {}