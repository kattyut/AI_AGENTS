# /qa.enrich.jira

## Uso

/qa.enrich.jira QA-123

o

/qa.enrich.jira QA-123 <contenido historia>

---

## Comportamiento

1. Validar input:

- Si hay issue_key:
  → obtener historia desde Jira

- Si hay contenido adicional:
  → usarlo como base

---

2. Ejecutar agente:

- Validar historia
- Completar QA
- Generar Gherkin

---

3. Validar calidad:

- Si NO cumple:
  → detener ejecución
  → mostrar errores

- Si cumple:
  → continuar

---

4. Publicar en Jira:

→ usar jira.update_ticket

---

5. (Opcional)

Si el estado es "To refine":
→ mover a "Pending refinement validation"

---

## Resultado esperado

- Historia lista para QA
- Criterios completos
- Gherkin generado
- Ticket actualizado

---

## Error handling

Si falta issue_key:

→ pedirlo al usuario

Si falla Jira:

→ mostrar error claro