# Sito PODS APS

Sito di **PODS, Piemonte Orientale Digitale e Solidale** (associazione-pods.it).

È un sito statico: HTML, CSS e un po' di JavaScript, senza database e senza framework. Non c'è nulla da installare per pubblicarlo.

## Come è fatto

| File | A cosa serve |
|---|---|
| `index.html` | La pagina. **È generata** da `build.py`, non modificarla a mano |
| `build.py` | Contiene tutti i testi del sito e la struttura della pagina |
| `style.css` | Grafica, colori, layout (desktop e mobile) |
| `app.js` | Menu mobile, blocchi "Leggi di più", animazioni di comparsa |
| `sprite.svg`, `vb.json` | Le macchie colorate del logo |
| `favicon.png`, `og.png` | Icona del browser e anteprima quando il link viene condiviso (LinkedIn, WhatsApp, Facebook) |
| `og-src.html` | Sorgente da cui è stata ricavata `og.png` |
| `archivo-*.woff2` | Font Archivo (licenza SIL OFL) |

## Come cambiare un testo

1. Apri `build.py` e cerca il testo da cambiare (Ctrl+F).
2. Modificalo mantenendo le virgolette e i tag HTML intorno.
3. Dal terminale, nella cartella del progetto: `python3 build.py` (serve Python 3, nessuna libreria extra). Rigenera `index.html`.
4. Controlla in locale: `python3 -m http.server 8000` e apri http://localhost:8000
5. Salva su Git: `git add -A && git commit -m "Descrizione della modifica" && git push`

Se la cartella è collegata a Vercel, il push pubblica il sito da solo in circa un minuto.

## Pubblicazione

Il sito è ospitato su **Vercel**. Impostazioni del progetto:

- Framework preset: **Other**
- Build command: *(vuoto)*
- Output directory: *(vuoto, si pubblica la radice del repository)*
- Branch di produzione: `main`

Ogni push su `main` va online. Ogni push su un altro branch crea un'anteprima con un indirizzo provvisorio, utile per controllare prima di pubblicare.

## Passaggio di consegne

Da compilare a cura dell'associazione, in modo che il sito non dipenda da una sola persona.

| Cosa | Dove si trova | Chi lo amministra |
|---|---|---|
| Repository del codice | GitHub: *da compilare* | *almeno due persone* |
| Hosting | Vercel: *team / account da compilare* | *almeno due persone* |
| Dominio associazione-pods.it | Registrar: *da compilare* | *intestato all'associazione* |
| Casella info@associazione-pods.it | *da compilare* | *da compilare* |

Regola pratica: repository, hosting e dominio devono essere intestati all'associazione (non a un account personale) e avere almeno due amministratori.

## Contenuti istituzionali

I testi derivano dalla brochure istituzionale, dall'atto costitutivo e dallo statuto. Se cambiano denominazione, sede o recapiti, vanno aggiornati in `build.py` (sezione footer e contatti).
