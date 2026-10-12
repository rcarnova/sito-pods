#!/usr/bin/env python3
"""Genera index.html del sito PODS (testi dalla brochure istituzionale)."""
import json

VB = json.load(open('vb.json'))
SPR = 'sprite.svg'


def blob(name, cls='', extra=''):
    x, y, w, h = VB[name]
    return (f'<svg class="blob {name} {cls}" viewBox="{x} {y} {w} {h}" aria-hidden="true" focusable="false"{extra}>'
            f'<use href="{SPR}#b-{name}"/></svg>')


def letters(cls, full=False, extra=''):
    vb = '121 1028 1270 336' if full else '121 1028 962 336'
    return (f'<svg class="{cls}" viewBox="{vb}" aria-hidden="true" focusable="false"{extra}>'
            f'<use href="{SPR}#p-letters"/></svg>')


ICON_AI = '''<svg class="ico" viewBox="0 0 64 64" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M32 12a14 14 0 0 0-8 25.5c1.6 1.2 2.4 2.8 2.4 4.5v1.5h11.2V42c0-1.7.8-3.3 2.4-4.5A14 14 0 0 0 32 12Z"/><path d="M27 47h10M28.5 51.5h7"/><path d="M32 3v4M12 9l3 3M52 9l-3 3M4 26h4M56 26h4"/><path d="M26.5 31l3-9 3 9M27.5 28h4M36 22v9"/></svg>'''

ICON_PEOPLE = '''<svg class="ico" viewBox="0 0 64 64" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="14" cy="14" r="4.5"/><circle cx="32" cy="11" r="4.5"/><circle cx="50" cy="14" r="4.5"/><path d="M7 24h14v16h-3v18h-3.5V44h-1V58H10V40H7z"/><path d="M25 21h14v18h-3v19h-3.5V43h-1v15H28V39h-3z"/><path d="M43 24h14v16h-3v18h-3.5V44h-1V58H46V40h-3z"/></svg>'''

ICON_CHAT = '''<svg class="ico" viewBox="0 0 64 64" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M8 12h28a4 4 0 0 1 4 4v14a4 4 0 0 1-4 4H20l-8 7v-7H8a4 4 0 0 1-4-4V16a4 4 0 0 1 4-4Z"/><path d="M26 30h30a4 4 0 0 1 4 4v14a4 4 0 0 1-4 4h-4v7l-8-7H26a4 4 0 0 1-4-4V34a4 4 0 0 1 4-4Z"/><circle cx="14" cy="23" r="1.4"/><circle cx="22" cy="23" r="1.4"/><circle cx="30" cy="23" r="1.4"/><circle cx="34" cy="41" r="1.4"/><circle cx="42" cy="41" r="1.4"/><circle cx="50" cy="41" r="1.4"/></svg>'''

PROVS = [  # nome, colore, lunghezza barra (decorativa)
    ('Biella', 'brown', 22),
    ('Verbano-Cusio-Ossola', 'sky', 50),
    ('Asti', 'green', 72),
    ('Alessandria', 'blue', 58),
    ('Novara', 'purple', 30),
    ('Vercelli', 'yellow', 40),
]
prov_html = '\n'.join(
    f'''          <li class="prov" style="--c:var(--{c});--len:{ln}%;--i:{i}">
            <span class="bar" aria-hidden="true"></span>
            <span class="tag">{n}</span>
            {blob(c, 'pb')}
          </li>''' for i, (n, c, ln) in enumerate(PROVS))

VBARS = [('brown', 38), ('sky', 56), ('green', 100), ('blue', 82), ('purple', 44), ('yellow', 70)]
vbars_html = ''.join(f'<i style="--c:var(--{c});--h:{h}%;--i:{i}"></i>' for i, (c, h) in enumerate(VBARS))

HTML = f'''<!doctype html>
<html lang="it">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="format-detection" content="telephone=no, date=no, address=no">
<title>PODS | Piemonte Orientale Digitale e Solidale</title>
<meta name="description" content="PODS è una rete di professionisti che mette a disposizione pro bono la propria competenza per scuole, università, enti pubblici, imprese e Terzo Settore del Piemonte Orientale.">
<meta property="og:title" content="PODS | Piemonte Orientale Digitale e Solidale">
<meta property="og:description" content="Competenze, contenuti e progetti dal mondo del digitale, restituiti al territorio del Piemonte Orientale.">
<meta property="og:type" content="website">
<meta property="og:url" content="https://associazione-pods.it">
<meta property="og:locale" content="it_IT">
<meta property="og:image" content="https://associazione-pods.it/og.png">
<meta property="og:image:width" content="600">
<meta property="og:image:height" content="315">
<meta property="og:image:alt" content="PODS, Piemonte Orientale Digitale e Solidale">
<meta property="og:site_name" content="PODS">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#ffffff">
<link rel="canonical" href="https://associazione-pods.it/">
<link rel="icon" type="image/png" href="favicon.png">
<link rel="preload" href="archivo-700.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="archivo-400.woff2" as="font" type="font/woff2" crossorigin>
<script>document.documentElement.className+=' js'</script>
<link rel="stylesheet" href="style.css">
</head>
<body id="top">
<a class="skip" href="#main">Vai al contenuto</a>

<header class="site-header">
  <div class="hdr">
    <a class="brand" href="#top" aria-label="PODS, torna in alto">{letters('brand-logo')}</a>
    <button class="menu-btn" type="button" aria-expanded="false" aria-controls="nav"><span class="sr">Menu</span><i></i><i></i></button>
    <nav class="nav" id="nav" aria-label="Principale">
      <a href="#cose">Cos’è PODS</a>
      <a href="#iniziative">Iniziative</a>
      <a href="#territorio">Territorio</a>
      <a href="#chi-siamo">Chi siamo</a>
      <a href="#visione">Visione</a>
      <a href="#formazione">Formazione</a>
      <a class="nav-cta" href="#contatti">Contatti</a>
    </nav>
  </div>
</header>

<main id="main">

<!-- HERO -->
<section class="hero" aria-labelledby="h1">
  <div class="hero-art">
    {blob('purple', 'h-purple')}
    {blob('sky', 'h-sky')}
    {blob('yellow', 'h-yellow')}
    <h1 id="h1" class="hero-logo"><span class="sr">PODS, Piemonte Orientale Digitale e Solidale</span>{letters('hero-wordmark', full=True)}</h1>
  </div>
  <div class="hero-foot">
    <p class="hero-lead">Competenze, contenuti e progetti dal mondo del digitale, restituiti al territorio del Piemonte Orientale.</p>
    <p class="hero-cta"><a class="btn btn-ink" href="#cose">Scopri PODS</a><a class="btn btn-line" href="#contatti">Scrivici</a></p>
  </div>
</section>

<!-- COS'E' PODS -->
<section class="cose" id="cose" aria-labelledby="h-cose">
  <div class="cose-a">
    <h2 id="h-cose" class="display" data-rv>Cos’è PODS?</h2>
    <p class="cose-sub" data-rv>Un contenitore no profit di competenze, contenuti e progetti dal mondo del digitale, della tecnologia e della consulenza.</p>
    {blob('brown', 'c-brown')}
    {blob('sky', 'c-sky')}
  </div>
  <div class="cose-b">
    <p class="statement" data-rv>Una rete di <mark class="hl hl-y" style="--d:.2s">professionisti</mark> che <mark class="hl hl-y" style="--d:.45s">mette a disposizione</mark> pro bono la propria competenza per <mark class="hl hl-s" style="--d:.7s">supportare</mark> il mondo della <mark class="hl hl-p" style="--d:.95s">scuola</mark>, l’<mark class="hl hl-g" style="--d:1.15s">accademia</mark>, i <mark class="hl hl-b" style="--d:1.35s">soggetti pubblici, privati</mark> e <mark class="hl hl-y" style="--d:1.6s">del terzo settore.</mark></p>
  </div>
</section>

<section class="band" aria-label="Come operiamo">
  <p class="band-text" data-rv>Attraverso <strong>progetti di formazione</strong> per la consapevolezza digitale, percorsi <strong>educativi co-progettati</strong> per l’animazione digitale, il mentoring e il networking sui territori del <em>Piemonte Orientale</em>.</p>
  {letters('ghost')}
</section>

<!-- INIZIATIVE -->
<section class="ini" id="iniziative" aria-labelledby="h-ini">
  <div class="ini-head">
    <div class="ini-copy">
      <h2 id="h-ini" class="display" data-rv>Le iniziative in partenza</h2>
      <p class="kicker" data-rv>Progetti concreti per le scuole, la cittadinanza, la comunità universitaria.</p>
    </div>
    <div class="ini-art" aria-hidden="true">{blob('sky', 'i-sky')}{blob('yellow', 'i-yellow')}{blob('brown', 'i-brown')}{blob('green', 'i-green')}</div>
  </div>
  <div class="cards">
    <article class="card card-y" data-rv>
      <header><h3>Intelligenti,<br>non artificiali</h3>{ICON_AI}</header>
      <p data-more>Con il programma <strong>“Intelligenti, non artificiali”</strong> avviamo nelle scuole superiori percorsi di approfondimento e sfide pratiche d’istituto per <strong>educare all’uso etico delle tecnologie intelligenti.</strong> Gli <em>studenti utilizzeranno la tecnologia come acceleratore</em> per elaborare risposte a problemi reali posti dalle imprese, mentre i <em>docenti valuteranno la tenuta logica</em> del ragionamento.</p>
    </article>
    <article class="card card-p" data-rv>
      <header><h3>Mentoring<br>&amp; Coaching</h3>{ICON_PEOPLE}</header>
      <p data-more>In collaborazione con alcune <strong>associazioni universitarie</strong>, stiamo progettando un <strong>programma pro bono di mentoring</strong> e affiancamento per gli studenti universitari, dedicato allo sviluppo delle competenze trasversali e all’orientamento professionale.</p>
    </article>
    <article class="card card-b" data-rv>
      <header><h3>Branding e<br>ascolto pubblico</h3>{ICON_CHAT}</header>
      <p data-more>Per il <strong>Dipartimento DIGSPES di UPO</strong> co-progettiamo il <strong>“Corso di Formazione in Branding e ascolto pubblico”</strong> ad Alessandria, che combinerà laboratori urbani, seminari diffusi e lo sviluppo di applicazioni ad uso della collettività.</p>
    </article>
  </div>
</section>

<!-- IDENTITA' E MISSIONE TERRITORIALE -->
<section class="ident" id="territorio" aria-labelledby="h-ident">
  <div class="wrap">
    <h2 id="h-ident" class="display" data-rv>Identità e missione territoriale</h2>
  </div>
  <div class="panel" data-rv>
    <ul class="provs" aria-label="Province in cui operiamo">
{prov_html}
    </ul>
    <p class="panel-text">L’Associazione Piemonte Orientale Digitale e Solidale (PODS) nasce nel 2026 da un network di professionisti, manager, ricercatori e docenti già attivi nel territorio nelle province di <strong>Alessandria, Asti, Biella, Novara, Vercelli e del Verbano-Cusio-Ossola.</strong></p>
  </div>
</section>

<section class="mozione" aria-label="La nostra mozione ideale">
  {blob('purple', 'm-purple')}
  {blob('sky', 'm-sky')}
  {blob('yellow', 'm-yellow')}
  <div class="wrap">
    <p class="moz-box" data-rv>La nostra mozione ideale nasce dalla restituzione di competenze alla collettività, mettendo a disposizione tempo ed esperienze pro bono per generare utilità sociale, promuovere la cultura delle competenze, il networking sul territorio.</p>
  </div>
</section>

<section class="stake" aria-label="Il nostro rapporto con il territorio">
  <div class="stake-a">
    <p data-rv data-more>Collaborando con i tanti <strong>stakeholder pubblici, privati e del terzo settore</strong> già attivi sul territorio, ci proponiamo di <strong>contribuire alla cultura dell’innovazione e alla diffusione di consapevolezza e cittadinanza digitali</strong>: leve concrete di inclusione sociale ed educativa per affrontare le sfide <em>(il declino demografico, il mismatch tra opportunità lavorative e talenti, il disallineamento tra percorsi formativi e mondo del lavoro, i legami fragili fra gli ecosistemi)</em> di queste terre comprese fra Torino, Milano e Genova.</p>
  </div>
  <div class="stake-b" aria-hidden="true">
    {blob('green', 's-green')}
    {blob('blue', 's-blue')}
  </div>
</section>

<!-- CHI SIAMO -->
<section class="chi" id="chi-siamo" aria-labelledby="h-chi">
  <div class="chi-a">
    <h2 id="h-chi" class="display" data-rv>Chi siamo&nbsp;<span class="star" aria-hidden="true">*</span></h2>
    <p class="kicker" data-rv>Persone, professionalità e territori in rete.</p>
  </div>
  <div class="chi-b" aria-hidden="true">
    <div class="chi-dark">{blob('brown', 'x-brown')}{blob('sky', 'x-sky')}{blob('purple', 'x-purple')}</div>
    <div class="chi-purple"></div>
  </div>
</section>

<section class="rete" aria-label="La nostra rete">
  {blob('yellow', 'r-yellow')}
  <div class="rete-a">
    <p class="rete-lead" data-rv>La nostra rete riunisce <mark class="hl hl-y" style="--d:.3s">circa cento soci e volontari</mark> attivi nelle diverse province del Piemonte Orientale.</p>
    <div class="rete-deco" aria-hidden="true"><span class="rd-dark"></span><span class="rd-purple"></span></div>
  </div>
  <div class="rete-b">
    <div class="rete-txt" data-more>
    <p data-rv>La base associativa integra competenze multidisciplinari spaziando dai ricercatori accademici ai docenti, dai tecnologi ai dirigenti d’azienda, dagli esperti di formazione a comunicatori, giornalisti e consulenti d’impresa.</p>
    <p data-rv>La forza del nostro gruppo risiede in una spiccata sinergia <strong>intergenerazionale, che affianca giovani laureati a professionisti senior</strong>, in uno scambio continuo che favorisce la trasmissione tra l’<strong>energia dei profili emergenti e l’esperienza operativa</strong> maturata nei centri tecnologici e nelle realtà industriali italiane e multinazionali.</p>
    <p data-rv><strong>Le iniziative che co-progettiamo con i nostri interlocutori</strong> sono il risultato di una elaborazione interna delle nostre complessità territoriali, anagrafiche e di ruoli professionali: è una garanzia di concretezza, coerenza metodologica e appropriatezza del codice di comunicazione.</p>
    </div>
  </div>
</section>

<!-- VISIONE -->
<section class="vis" id="visione" aria-labelledby="h-vis">
  <div class="vis-head">
    <div class="vis-copy">
      <h2 id="h-vis" class="display" data-rv>La nostra visione</h2>
      <p class="kicker" data-rv>Sull’ecosistema locale dell’innovazione e la cooperazione con gli stakeholder.</p>
    </div>
    <div class="vbars" aria-hidden="true" data-rv>{vbars_html}</div>
  </div>
  <div class="vis-body">
    <p class="vis-lead" data-rv>Sosteniamo una visione antropocentrica dell’innovazione, in cui la tecnologia rimane uno strumento al servizio della persona.</p>
    <div class="vis-cols" data-more>
      <p data-rv>Consideriamo il Piemonte Orientale come un ecosistema unico e integrato, capace di valorizzare le proprie filiere produttive e scientifiche in un quadro macroregionale.</p>
      <p data-rv><strong>Contribuiamo a connettere la ricerca accademica e la formazione al tessuto economico e sociale, per ridurre le disuguaglianze e generare opportunità per il territorio.</strong></p>
      <p data-rv>Il nostro metodo di lavoro parte <strong>dall’ascolto</strong> attento dei contesti e dalla <strong>co-progettazione</strong> degli interventi insieme alle comunità locali e agli interlocutori privati. Impieghiamo strumenti quali il <strong>mentoring</strong> e il <strong>coaching</strong>, i <strong>laboratori partecipati di progettazione</strong>, le simulazioni di risoluzione di sfide complesse (envisioning, studi di futuro, group coaching).</p>
      <p data-rv>Ci poniamo come antenna territoriale di ecosistemi nazionali ed internazionali attivi nel mondo della formazione, del supporto all’innovazione, della cittadinanza digitale.</p>
    </div>
  </div>
</section>

<!-- FORMAZIONE -->
<section class="form" id="formazione" aria-labelledby="h-form">
  <div class="form-head">
    <h2 id="h-form" class="display" data-rv>La formazione per la tecnologia:</h2>
    <p class="kicker" data-rv>Intelligenza artificiale, consapevolezza e cittadinanza digitale al servizio della comunità.</p>
  </div>
  <div class="form-body">
    <div class="stripes" aria-hidden="true"><i></i><i></i><i></i><i></i></div>
    <div class="form-text">
      <p class="form-lead" data-rv>Mettiamo a disposizione del territorio percorsi formativi co-progettati con le scuole e soggetti pubblici e privati: questo metodo ci permette di calibrare ogni intervento didattico sui bisogni concreti degli studenti, dei docenti e dei contesti operativi.</p>
      <div class="form-cols" data-more>
        <p data-rv>Riteniamo che la <strong>tecnologia e i sistemi digitali debbano mantenere una funzione esclusivamente strumentale</strong> e di mero supporto all’umano, affinché gli studenti e i cittadini sappiano <strong>trasformare l’innovazione in una piena cittadinanza digitale attiva</strong>, un’opportunità concreta di crescita e di employability.</p>
        <p data-rv><strong>Educhiamo all’autonomia di giudizio, all’analisi rigorosa delle fonti</strong> e al contrasto della delega cognitiva agli strumenti come l’Intelligenza Artificiale. Affianchiamo le comunità <strong>educanti con la presenza dei nostri soci esperti per garantire continuità didattica</strong> e accompagnamento di metodo, per integrare l’apprendimento tecnico con <strong>la riflessione etica e sociale.</strong></p>
      </div>
    </div>
    <div class="bar-r" aria-hidden="true"></div>
  </div>
</section>

<!-- CONTATTI -->
<section class="contact" id="contatti" aria-labelledby="h-contact">
  <div class="contact-art" aria-hidden="true">{blob('brown', 'k-brown')}{blob('sky', 'k-sky')}{blob('purple', 'k-purple')}{blob('yellow', 'k-yellow')}{blob('green', 'k-green')}</div>
  <div class="contact-copy">
    <h2 id="h-contact" class="display" data-rv>Collabora con PODS</h2>
    <p data-rv>Se rappresenti una scuola, un’università, un ente pubblico, un’impresa o un ente del Terzo Settore e vuoi capire come possiamo lavorare insieme, scrivici.</p>
    <p data-rv><a class="btn btn-white" href="mailto:info@associazione-pods.it">info@associazione-pods.it</a></p>
  </div>
</section>

</main>

<footer class="site-footer">
  <div class="foot">
    <div class="foot-logo">{letters('foot-wordmark', full=True)}<span class="sr">PODS, Piemonte Orientale Digitale e Solidale</span></div>
    <address>
      <p>Piemonte Orientale Digitale e Solidale APS ETS, PODS</p>
      <p>Sede legale: via Gaudenzio Ferrari 17, 13100 Vercelli</p>
      <p>Codice fiscale 94047260024</p>
      <p>Iscritta al RUNTS dal 9 ottobre 2026, repertorio n. 182788, sezione Associazioni di promozione sociale</p>
      <p><a href="mailto:info@associazione-pods.it">info@associazione-pods.it</a></p>
    </address>
    <p class="copy">© 2026 PODS</p>
  </div>
</footer>

<script src="app.js" defer></script>
</body>
</html>
'''
open('index.html', 'w', encoding='utf-8').write(HTML)
print(len(HTML.encode()))
