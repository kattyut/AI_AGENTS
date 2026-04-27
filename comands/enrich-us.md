# Command: /enrich-us

## Description
Refine and improve a user story without introducing new or invented information.

## Agent
enrich-us-agent

## Input
A user story or raw requirement text.

## Strict Rules

- Do NOT invent missing information
- Do NOT create acceptance criteria if none exist
- Do NOT assume technical details that are not present
- Only clarify, structure, and improve what already exists

## Process

1. Validate input:
   - If no user story is provided → return error
   - If content is too vague → highlight missing information

2. Analyze the content:
   - Identify ambiguity
   - Identify missing structure (actor, action, benefit)

3. Improve the user story:
   - Rewrite using standard format if possible:
     As a [actor], I want [action], so that [benefit]
   - If any part is missing → keep it empty and report it

4. Acceptance Criteria:
   - If they exist → rewrite in Given / When / Then format
   - If they do NOT exist → DO NOT generate them
   - Instead → add a warning

5. Technical clarity:
   - Do NOT invent endpoints, fields, or architecture
   - If missing → list as "Missing Technical Details"

## Output

### User Story (Refined)
...

### Acceptance Criteria
- (only if provided, improved)

### Issues Detected
- Missing actor / action / benefit
- Ambiguity found
- Missing acceptance criteria

### Missing Information
- Technical details not defined
- Acceptance criteria not provided

### Improvements Applied
- Clarified wording
- Removed ambiguity
- Structured format
