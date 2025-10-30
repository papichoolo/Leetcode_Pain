Here’s the clean start-to-finish run sequence for both backend (FastAPI) and frontend (Next.js + shadcn/ui) on Windows PowerShell.

## 1) Backend: FastAPI + Firestore

Open a new PowerShell window and run:

- 
- 
- 
- 

Notes:

- If Firestore auth complains locally, point ADC to your service account:
    
    - 
    - 
    - 
    - 
    
    then rerun uvicorn.
- CORS is already wide open in [main.py](vscode-file://vscode-app/c:/Users/utfu/AppData/Local/Programs/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-browser/workbench/workbench.html), so the Next.js app can call it.

## 2) Frontend: Next.js + shadcn/ui

Open another PowerShell window and run:

- 
- 
- 
- 

Open [http://localhost:3000](vscode-file://vscode-app/c:/Users/utfu/AppData/Local/Programs/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-browser/workbench/workbench.html) in your browser.

Flow:

- Visit /login and sign in (email/password or Google).
- If you’re a new user, you’ll be sent to /setup to select Branch + Roles.
- After setup you’ll land on /dashboard; Students tab fetches from the backend.

## Quick tips

- Changed .env.local? Stop the dev server and start it again so Next.js reloads variables.
- If you want to bypass Firebase entirely for quick backend-only tests:
    
    - 
    - 
    - 
    - 
    
    Then hit the backend directly; the frontend still expects real Firebase.