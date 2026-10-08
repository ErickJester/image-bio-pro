# Registro de errores

Cada error que aparezca durante el proyecto: qué pasó, por qué y cómo se resolvió.

## Plantilla

```markdown
### AAAA-MM-DD — Descripción corta

- **Dónde:** archivo, comando o paso
- **Mensaje:** el texto del error
- **Causa:**
- **Solución:**
- **Lo que aprendí:**
```

## Errores

### 2026-10-07 — PowerShell no deja activar el entorno virtual

- **Dónde:** al ejecutar `.venv\Scripts\Activate.ps1` (módulo 1, paso 2).
- **Mensaje:** `File ...\.venv\Scripts\Activate.ps1 cannot be loaded because running scripts is disabled on this system.` (`PSSecurityException`, `UnauthorizedAccess`).
- **Causa:** Windows trae PowerShell con la política de ejecución en `Restricted`, que bloquea todos los scripts `.ps1`. `Activate.ps1` es un script, así que no se pudo ejecutar.
- **Solución:** ejecutar una sola vez `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned` y responder que sí.
  - `-Scope CurrentUser`: el cambio aplica solo a mi usuario y no requiere permisos de administrador.
  - `RemoteSigned`: permite los scripts creados en la computadora; los descargados de internet solo corren si vienen firmados.
- **Lo que aprendí:** es normal en cualquier Windows nuevo. En la capacitación o en otra computadora va a volver a pasar la primera vez, y se resuelve igual.
