"""Small Streamlit UI that talks to the API.

This file is intentionally simple so students can focus on structure.
"""

from __future__ import annotations

import streamlit as st
import requests
import sys
import os

# Ajouter le répertoire parent au path pour les imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from todo_app.config import settings
from todo_app.logger import logger

API_BASE = settings.api_host


def get_todos():
    resp = requests.get(f"{API_BASE}/todos")
    resp.raise_for_status()
    return resp.json()


def create_todo(title: str, description: str | None):
    payload = {"title": title, "description": description}
    resp = requests.post(f"{API_BASE}/todos", json=payload)
    resp.raise_for_status()
    return resp.json()


def main() -> None:
    st.title("Todo List — Best Practices Demo")

    with st.form("create"):
        title = st.text_input("Titre")
        description = st.text_area("Description")
        submitted = st.form_submit_button("Créer")
        if submitted and title:
            try:
                create_todo(title, description)
                st.success("Todo créé")
            except Exception as exc:  # pragma: no cover - surface errors to user
                logger.exception("Erreur lors de la création de todo")
                st.error(f"Impossible de créer le todo: {exc}")

    try:
        todos = get_todos()
    except Exception as exc:
        st.error("Impossible de récupérer les todos — vérifiez que l'API tourne")
        logger.exception("Erreur récup todos")
        return

    for t in todos:
        st.checkbox(t["title"], value=t["completed"])  # affichage minimal


if __name__ == "__main__":
    main()
