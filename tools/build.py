#!/usr/bin/env python3
"""Generates the static Cablons site into /home/claude/cablons-site."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from circuit import circuit

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
CAL = "https://calendly.com/shaun-wakefield-cablons"
SITE = "https://www.cablons.com"

NAV = [
    ("vciso.html", "Fractional CISO"),
    ("penetration-testing.html", "Pen testing"),
    ("grc-consultancy.html", "GRC"),
    ("msp-partners.html", "For MSPs"),
    ("insights.html", "Insights"),
    ("about.html", "About"),
    ("contact.html", "Contact"),
]

ARROW = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M13 6l6 6-6 6"/></svg>'

def head(title, desc, path):
    url = SITE + "/" + ("" if path == "index.html" else path)
    return f"""<!doctype html>
<html lang="en-GB">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{url}">
<meta property="og:type" content="website">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{SITE}/assets/og-image.png">
<meta name="twitter:card" content="summary">
<meta name="theme-color" content="#070b14">
<link rel="icon" href="assets/favicon.png" type="image/png" sizes="32x32">
<link rel="apple-touch-icon" href="assets/apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Manrope:wght@300;400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="styles.css">
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "ProfessionalService",
  "name": "Cablons Cyber Limited",
  "url": "{SITE}/",
  "logo": "{SITE}/assets/logo.svg",
  "email": "sales@cablons.com",
  "address": {{"@type": "PostalAddress", "streetAddress": "36 The Oval", "addressLocality": "Bingley", "addressRegion": "West Yorkshire", "postalCode": "BD16 4RQ", "addressCountry": "GB"}},
  "areaServed": "United Kingdom",
  "description": "{desc}"
}}
</script>
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<header class="site-header">
  <div class="wrap">
    <a class="brand" href="index.html" aria-label="Cablons Cyber home"><img src="assets/logo.svg" alt="Cablons Cyber"></a>
    <button class="nav-toggle" aria-expanded="false" aria-controls="nav">Menu</button>
    <nav class="nav" id="nav" aria-label="Main">
{nav_links(path)}
      <a class="btn btn-gold" href="{CAL}">Book a call</a>
    </nav>
  </div>
</header>
<main id="main">
"""

def nav_links(path):
    return "\n".join(
        f'      <a href="{href}"{" aria-current=\"page\"" if href == path else ""}>{label}</a>'
        for href, label in NAV)

FOOT = f"""
</main>
<footer class="site-footer">
  <div class="wrap">
    <div class="cols">
      <div>
        <a class="brand" href="index.html"><img src="assets/logo.svg" alt="Cablons Cyber"></a>
        <p>Independent cyber security consultancy based in West Yorkshire, working with organisations across the UK.</p>
      </div>
      <div>
        <h4>Services</h4>
        <ul>
          <li><a href="vciso.html">Fractional CISO</a></li>
          <li><a href="penetration-testing.html">Penetration testing</a></li>
          <li><a href="grc-consultancy.html">GRC and compliance</a></li>
          <li><a href="msp-partners.html">Partnering with MSPs</a></li>
          <li><a href="insights.html">Insights</a></li>
        </ul>
      </div>
      <div>
        <h4>Contact</h4>
        <ul>
          <li><a href="mailto:sales@cablons.com">sales@cablons.com</a></li>
          <li><a href="{CAL}">Book a free consultation</a></li>
          <li>36 The Oval, Bingley<br>West Yorkshire, BD16 4RQ</li>
        </ul>
      </div>
    </div>
    <div class="legal">
      <span>&copy; 2026 Cablons Cyber Limited. Registered in England and Wales, company number 15090311.</span>
      <span><a href="privacy.html">Privacy</a></span>
    </div>
  </div>
</footer>
<script>
  (function () {{
    var t = document.querySelector('.nav-toggle'), n = document.getElementById('nav');
    if (t) t.addEventListener('click', function () {{
      var open = n.classList.toggle('open');
      t.setAttribute('aria-expanded', open ? 'true' : 'false');
    }});
    var arts = document.querySelectorAll('.art');
    if ('IntersectionObserver' in window) {{
      var io = new IntersectionObserver(function (es) {{
        es.forEach(function (e) {{ if (e.isIntersecting) {{ e.target.classList.add('draw'); io.unobserve(e.target); }} }});
      }}, {{ threshold: 0.2 }});
      arts.forEach(function (a) {{ io.observe(a); }});
    }} else {{
      arts.forEach(function (a) {{ a.classList.add('draw'); }});
    }}
  }})();
</script>
</body>
</html>
"""

def hero(kicker_unused, h1, lead, actions, small=False, seed=7, pos="right"):
    """pos: right, left, top or bottom. small keeps a compact hero for utility pages."""
    cls = "hero art-" + pos + (" hero-small" if small else "")
    wide = pos in ("top", "bottom")
    art = circuit(seed=seed, traces=36 if small else 55, width=1400 if wide else 900, height=520 if wide else 620)
    return f"""
<section class="{cls}">
  <div class="art">{art}</div>
  <div class="wrap">
    <div class="hero-copy">
      <h1>{h1}</h1>
      <p class="lead">{lead}</p>
      {('<div class="actions">' + actions + '</div>') if actions else ''}
    </div>
  </div>
</section>
"""

def cta(h="Not sure where to start?", p="A 30-minute call is usually enough to work out whether a test, a gap analysis or ongoing support is the right next step.", seed=21):
    return f"""
<section class="cta">
  <div class="art">{circuit(seed=seed, traces=34)}</div>
  <div class="wrap">
    <div>
      <h2>{h}</h2>
      <p>{p}</p>
    </div>
    <div class="actions">
      <a class="btn btn-gold" href="{CAL}">Book a free consultation</a>
      <a class="btn btn-ghost" href="contact.html">Send an enquiry</a>
    </div>
  </div>
</section>
"""

def ledger(rows):
    out = ['<div class="ledger">']
    for title, body, href in rows:
        tag = "a" if href else "div"
        h = f' href="{href}"' if href else ""
        go = f'<span class="go" aria-hidden="true">{ARROW}</span>' if href else "<span></span>"
        out.append(f'<{tag} class="ledger-row"{h}><h3>{title}</h3><p>{body}</p>{go}</{tag}>')
    out.append("</div>")
    return "\n".join(out)

pages = {}

pages["index.html"] = ("Fractional CISO, penetration testing and GRC consultancy | Cablons Cyber",
"Independent UK cyber security consultancy offering fractional CISO services, penetration testing and ISO 27001 and GRC consultancy. Based in West Yorkshire.",
hero(None, "Consultants who have run the blue team, not just tested it.",
     "Cablons Cyber is an independent consultancy whose people have defended networks, tested them and audited them. We give you fractional CISO leadership without the full-time cost, test your defences, and close the gaps auditors and customers care about.",
     f'<a class="btn btn-gold" href="{CAL}">Book a free consultation</a><a class="btn btn-ghost" href="#services">See what we do</a>') + f"""

<section class="section on-bone" id="services">
  <div class="wrap">
    <div class="section-head">
      <h2>Three things, done properly.</h2>
      <p class="muted">Most clients arrive with one of three problems: nobody senior owns security, a customer or regulator wants evidence, or they want to know how exposed they are. Each service answers one of those.</p>
    </div>
    {ledger([
      ("Fractional CISO", "A named senior security lead for a few days a month. Strategy, risk, board reporting, supplier and customer due diligence, and someone accountable for the roadmap.", "vciso.html"),
      ("Penetration testing", "Infrastructure, web application, cloud and social engineering testing, scoped to your actual risk and reported in language the board can act on.", "penetration-testing.html"),
      ("GRC and compliance", "ISO 27001 gap analysis and implementation, Cyber Essentials, NIST CSF and PCI DSS readiness, policies and internal audit.", "grc-consultancy.html"),
    ])}
  </div>
</section>

<section class="section on-void">
  <div class="wrap statement">
    <div>
      <h2>Senior people on every engagement.</h2>
      <p class="cred">CISSP and ISO 27001 Lead Auditor certified. Backgrounds in ISP blue teams, penetration testing, audit and governance.</p>
      <p class="muted">Larger firms sell the engagement with a principal and deliver it with whoever is free. We do not. The consultant you speak to on the first call scopes the work, does the work and presents the findings. Our people have sat on the receiving end of a findings report on a Friday afternoon, so the reports we write are the ones we wished we had been sent: what an auditor will accept, what a board will ask and what an engineering team can realistically fix this quarter.</p>
      <ul class="checks">
        <li>Fixed-price scoping with no surprises on the invoice</li>
        <li>Reports written for two audiences: an executive summary and a technical appendix</li>
        <li>Free retest of remediated findings within 60 days</li>
        <li>UK-based, insured, and happy to sign your NDA before the first conversation</li>
      </ul>
    </div>
    <div class="panel">
      <h3>Who we work with</h3>
      <dl>
        <dt>SMEs and scale-ups</dt>
        <dd>Typically 20 to 500 staff, often being asked for ISO 27001 or a pen test report by a larger customer.</dd>
        <dt>Regulated and supply-chain businesses</dt>
        <dd>Firms handling payment data, health data or working under public sector and defence supply-chain requirements.</dd>
        <dt>IT and MSP partners</dt>
        <dd>Managed service providers who want to add fractional CISO, testing or compliance work to their own offer. <a href="msp-partners.html">How partnering works</a>.</dd>
      </dl>
    </div>
  </div>
</section>

<section class="section on-bone">
  <div class="wrap">
    <div class="section-head">
      <h2>Clear scope, clear findings, clear next steps.</h2>
      <p class="muted">Every engagement runs the same way, whether it is a two-day test or a nine-month certification programme.</p>
    </div>
    <div class="process">
      <div class="step"><h3>Scoping call</h3><p>Thirty minutes to understand what you need evidence of, what is in scope and what is off limits. You get a fixed quote within two working days.</p></div>
      <div class="step"><h3>Delivery</h3><p>Testing or assessment work runs to an agreed window, with a named contact and daily check-ins. Critical findings are raised the day they are found.</p></div>
      <div class="step"><h3>Reporting</h3><p>A risk-ranked findings list with reproduction steps, business impact and practical remediation. Presented live, not just emailed.</p></div>
      <div class="step"><h3>Retest and support</h3><p>Fixes are verified and the report updated so you have clean evidence for customers, auditors and insurers.</p></div>
    </div>
  </div>
</section>

<section class="section on-navy">
  <div class="wrap">
    <div class="section-head">
      <h2>Where clients usually begin.</h2>
    </div>
    <div class="starts">
      <div class="start">
        <h3>Nobody owns security</h3>
        <p>A fractional CISO retainer gives you a named senior owner for a few days a month: risk register, roadmap, supplier questionnaires and board reporting.</p>
        <a href="vciso.html">About the fractional CISO service</a>
      </div>
      <div class="start">
        <h3>A customer wants ISO 27001</h3>
        <p>A gap analysis against ISO 27001:2022 tells you exactly how far you are from certification and what it will take. Usually two to four weeks.</p>
        <a href="grc-consultancy.html">About the gap analysis</a>
      </div>
      <div class="start">
        <h3>Insurance or a tender needs a pen test</h3>
        <p>An external infrastructure and web application test, scoped to the systems that matter and reported in a format underwriters and procurement teams recognise.</p>
        <a href="penetration-testing.html">About penetration testing</a>
      </div>
    </div>
  </div>
</section>

<section class="section on-bone">
  <div class="wrap statement">
    <div>
      <h2>Run an MSP? Add senior security without the hire.</h2>
      <p class="muted">Your clients are starting to ask for a CISO, a pen test or ISO 27001, and the honest answer is that it is not what your team does. We work behind the scenes or alongside you as a named partner, so you keep the relationship and add the service.</p>
      <a class="btn btn-dark" href="msp-partners.html">Partnering with MSPs</a>
    </div>
    <div class="panel">
      <h3>What partners typically ask for</h3>
      <dl>
        <dt>Fractional CISO for their clients</dt><dd>Delivered under your brand or ours, with you as the technical delivery partner.</dd>
        <dt>Independent penetration testing</dt><dd>Separation between the people who run the environment and the people who test it, which auditors and insurers increasingly expect.</dd>
        <dt>Compliance programmes</dt><dd>ISO 27001 and Cyber Essentials for clients you already manage, with your engineers doing the hands-on remediation.</dd>
      </dl>
    </div>
  </div>
</section>

{cta()}
""")

pages["penetration-testing.html"] = ("Penetration testing services UK | Cablons Cyber",
"Infrastructure, web application, cloud and social engineering penetration testing for UK businesses, with executive and technical reporting and a free retest.",
hero(None, "Find out what an attacker would find, before they do.",
     "Manual, consultant-led testing scoped to your real exposure. Not a vulnerability scan with a cover sheet.",
     f'<a class="btn btn-gold" href="{CAL}">Scope a test</a>', seed=11, pos="top") + f"""

<section class="section on-bone">
  <div class="wrap">
    <div class="section-head"><h2>What we test</h2></div>
    {ledger([
      ("External infrastructure", "Everything you expose to the internet: perimeter, VPN, mail, remote access and exposed services. The test most insurers and tenders ask for.", None),
      ("Internal infrastructure", "What a compromised laptop or a malicious insider could reach. Active Directory, segmentation, credential hygiene and lateral movement paths.", None),
      ("Web and API applications", "Authenticated and unauthenticated testing against OWASP Top 10 and the application's own business logic, including the flaws scanners cannot see.", None),
      ("Cloud configuration review", "Microsoft 365, Azure and AWS reviews against vendor benchmarks and CIS controls. Identity, conditional access, logging and storage exposure.", None),
      ("Social engineering", "Phishing, vishing and pretext campaigns that measure how your people and processes respond, with results used for training rather than blame.", None),
      ("Cyber Essentials Plus", "Testing and the assessment itself delivered through our certification body partner, with the remediation support to pass first time.", None),
    ])}
  </div>
</section>

<section class="section on-void">
  <div class="wrap statement">
    <div>
      <h2>A report two audiences can use.</h2>
      <p class="muted">Every report has an executive summary a non-technical director can read in five minutes, and a technical section an engineer can work through without needing to call us. Each finding carries a severity rating, evidence, reproduction steps, business impact and a specific remediation, ranked so the team knows what to fix first.</p>
      <p class="muted">We present findings live, walk through anything contested, and provide a remediation tracker. Fixed findings are retested free within 60 days and the report reissued, so the evidence you hand to a customer or auditor reflects the current state rather than the one on test day.</p>
    </div>
    <div class="panel">
      <h3>How we work</h3>
      <dl>
        <dt>Scoping</dt><dd>Written scope and rules of engagement agreed before any testing. Fixed price per engagement.</dd>
        <dt>Method</dt><dd>Manual testing led by experienced consultants, supported by tooling where it adds coverage. Methodology aligned to OWASP, PTES and NIST SP 800-115.</dd>
        <dt>Safety</dt><dd>Agreed test windows, no denial-of-service, named emergency contact and a daily status note.</dd>
        <dt>Timing</dt><dd>Most engagements run two to ten days, with reports delivered within five working days of completion.</dd>
      </dl>
    </div>
  </div>
</section>

<section class="section on-bone faq">
  <div class="wrap">
    <div class="section-head"><h2>Questions we get asked</h2></div>
    <details><summary>How often should we test?</summary><p>Annually at minimum, plus after any significant change such as a new application release, a cloud migration or a merger. Many clients move to a six-monthly cycle once a customer or insurer asks for it.</p></details>
    <details><summary>Is this the same as a vulnerability scan?</summary><p>No. A scan automates known-signature checks and produces a long list with many false positives. A penetration test is a consultant actively trying to chain weaknesses together and demonstrate real impact, with the noise removed. We offer managed scanning as a supplement, not as a substitute.</p></details>
    <details><summary>Will testing disrupt our systems?</summary><p>We agree a window, avoid anything destructive, and stop and call you if something unexpected happens. Production testing is routine, but we can test a staging environment where that makes sense.</p></details>
    <details><summary>Can you test our supplier's product?</summary><p>Only with the supplier's written authorisation. We can help you request it and define scope, which is common for SaaS due diligence.</p></details>
  </div>
</section>

{cta("Need a test scoped quickly?", "Tell us what you expose and who is asking for the report. We will come back with a fixed quote within two working days.", seed=31)}
""")

pages["grc-consultancy.html"] = ("ISO 27001, Cyber Essentials and GRC consultancy | Cablons Cyber",
"ISO 27001 gap analysis and implementation, Cyber Essentials, NIST CSF and PCI DSS readiness, policy writing and internal audit from an ISO 27001 Lead Auditor.",
hero(None, "Get certified, stay certified, and keep the paperwork proportionate.",
     "Practical GRC consultancy from an ISO 27001 Lead Auditor who has implemented management systems as well as audited them.",
     f'<a class="btn btn-gold" href="{CAL}">Discuss a gap analysis</a>', seed=13, pos="bottom") + f"""

<section class="section on-bone">
  <div class="wrap">
    <div class="section-head"><h2>Compliance work we take on</h2></div>
    {ledger([
      ("ISO 27001 gap analysis", "A structured review against ISO 27001:2022 and Annex A, producing a clause-by-clause gap report, a prioritised plan and a realistic estimate of the time and cost to certification.", None),
      ("ISO 27001 implementation", "Risk assessment, Statement of Applicability, policy set, control implementation support and internal audit, taking you through to Stage 1 and Stage 2 with your chosen certification body.", None),
      ("Readiness assessments", "Assessments against NIST CSF 2.0, PCI DSS v4, Cyber Essentials and sector frameworks, with a scored baseline and a roadmap your leadership can fund.", None),
      ("Policies and procedures", "A policy set written for your organisation rather than downloaded from a template library, short enough that people read it and specific enough that auditors accept it.", None),
      ("Supplier and customer assurance", "Help answering security questionnaires, running supplier due diligence, and building the evidence pack that shortens every future enterprise sales cycle.", None),
      ("Internal audit and ongoing support", "Annual internal audit, management review facilitation and surveillance audit preparation on a light retainer, so certification does not lapse the year after you get it.", None),
    ])}
  </div>
</section>

<section class="section on-void">
  <div class="wrap statement">
    <div>
      <h2>Controls that fit the business, not the other way round.</h2>
      <p class="muted">A management system that only exists to pass an audit will be ignored by week three. We start from how the business actually operates, keep documentation to what the standard requires and the business will use, and build evidence collection into existing processes rather than adding a parallel one.</p>
      <p class="muted">Because our consultants audit as well as implement, we know where certification bodies push and where they do not. That keeps scope tight and avoids gold-plating controls nobody has asked for.</p>
      <p class="cred">A certificate you can keep with a day a month of effort, not one that needs a consultant on site every quarter.</p>
    </div>
    <div class="panel">
      <h3>Typical timelines</h3>
      <dl>
        <dt>Gap analysis</dt><dd>Two to four weeks, including interviews, document review and a presented report.</dd>
        <dt>ISO 27001 from a standing start</dt><dd>Four to nine months to Stage 2 for most SMEs, depending on how much is already in place.</dd>
        <dt>Cyber Essentials</dt><dd>Two to six weeks including remediation. Plus adds a short testing window.</dd>
        <dt>Ongoing support</dt><dd>One to two days a month covers internal audit, management review and surveillance prep.</dd>
      </dl>
    </div>
  </div>
</section>

{cta("Being asked for ISO 27001?", "A gap analysis tells you exactly how far away you are and what it will cost. Book a call and we will scope it with you.", seed=37)}
""")

pages["vciso.html"] = ("Fractional CISO services | Cablons Cyber",
"Fractional CISO services for UK SMEs and MSP clients: security strategy, risk management, board reporting and customer due diligence on a monthly retainer.",
hero(None, "Senior security leadership, a few days a month.",
     "A named, accountable security lead for organisations that need one but cannot justify a full-time hire.",
     f'<a class="btn btn-gold" href="{CAL}">Talk about a retainer</a>', seed=17, pos="left") + f"""

<section class="section on-bone">
  <div class="wrap split">
    <div class="prose">
      <h2>Ownership, not just advice.</h2>
      <p>Plenty of firms will send a consultant to write a strategy document. A fractional CISO engagement is different: we take ownership of the security programme, sit in your leadership meetings, answer to your board and your customers, and are measured on whether risk actually goes down.</p>
      <ul class="checks-bone">
        <li>Security strategy and a costed 12 to 24 month roadmap</li>
        <li>Risk register ownership and quarterly board reporting</li>
        <li>Customer security questionnaires and enterprise due diligence calls</li>
        <li>Supplier risk management and contract security clauses</li>
        <li>Incident response planning, tabletop exercises and first call when something goes wrong</li>
        <li>Oversight of your MSP, SOC and other security suppliers</li>
        <li>Security input to product, cloud and architecture decisions</li>
      </ul>
    </div>
    <div class="panel">
      <h3>Engagement options</h3>
      <dl>
        <dt>Advisory</dt><dd>Two days a month. Strategy, risk and board reporting, with ad hoc calls in between.</dd>
        <dt>Embedded</dt><dd>Four to six days a month. Everything in Advisory plus hands-on programme delivery and supplier management.</dd>
        <dt>Project</dt><dd>Fixed-term cover for a specific outcome: a certification, an audit, an incident or a leadership gap while you recruit.</dd>
      </dl>
      <p class="muted" style="margin-top:1.2rem">All options are monthly rolling with 30 days' notice. We will tell you if you have outgrown us.</p>
    </div>
  </div>
</section>

<section class="section on-navy">
  <div class="wrap">
    <div class="section-head"><h2>Signs you need one.</h2></div>
    <div class="starts">
      <div class="start"><h3>Enterprise customers are asking questions</h3><p>You are losing weeks on security questionnaires and nobody internally can speak to the answers with authority.</p></div>
      <div class="start"><h3>Security sits with IT by default</h3><p>Your IT lead or MSP is doing their best, but nobody owns risk, policy or the conversation with the board.</p></div>
      <div class="start"><h3>You are growing into regulation</h3><p>Payment data, health data, public sector contracts or a supply-chain requirement have arrived and the compliance load is now real.</p></div>
    </div>
  </div>
</section>

{cta("Want to talk it through?", "A first call costs nothing and usually ends with a clear view of whether a retainer, a project or a one-off assessment fits best.", seed=41)}
""")

pages["about.html"] = ("About Cablons Cyber | Independent UK cyber security consultancy",
"Cablons Cyber Limited is an independent cyber security and GRC consultancy in Bingley, West Yorkshire, with CISSP and ISO 27001 Lead Auditor certified consultants from blue team, testing and audit backgrounds.",
hero(None, "Independent, consultant-led, based in West Yorkshire.",
     "Cablons Cyber was founded to give smaller organisations the quality of security advice that is normally reserved for enterprises that can afford a full-time CISO.",
     "", seed=19, pos="bottom") + f"""

<section class="section on-bone">
  <div class="wrap split">
    <div class="prose">
      <h2>Who we are</h2>
      <p>Cablons Cyber Limited is a UK registered consultancy based in Bingley, working with clients across England and further afield by remote delivery. We are deliberately small, and every engagement is led by a senior consultant rather than handed down. Our consultants hold CISSP and ISO 27001 Lead Auditor certifications and have come to consultancy from the defending side: the founder spent a decade on the blue team at an ISP, running first-line security and then the network team, before fifteen years in penetration testing, ISO 27001 audit and implementation, and advisory work. We hire and partner with people who have the same mix of hands-on and governance experience.</p>
      <h2>How we think about security</h2>
      <p>Security is a business function. The point of a penetration test is not a long list of findings; it is a shorter list of things that would actually hurt, fixed. The point of ISO 27001 is not the certificate; it is a business that can show a customer, an insurer or a regulator how it manages risk, and keep doing so after the auditor leaves.</p>
      <p class="pull">We scope tightly, write in plain English, rank by business impact rather than CVSS alone, and tell clients when they are about to spend money on something that will not reduce risk.</p>
      <h2>What you can expect</h2>
      <ul class="checks-bone">
        <li>The consultant who scopes the work does the work</li>
        <li>Fixed prices agreed up front</li>
        <li>Professional indemnity and cyber insurance in place</li>
        <li>NDA signed before any sensitive conversation</li>
        <li>Honest advice, including when the answer is that you do not need us</li>
      </ul>
    </div>
    <div class="panel">
      <h3>Company details</h3>
      <dl>
        <dt>Registered name</dt><dd>Cablons Cyber Limited</dd>
        <dt>Company number</dt><dd>15090311, registered in England and Wales</dd>
        <dt>Registered office</dt><dd>36 The Oval, Bingley, West Yorkshire, BD16 4RQ</dd>
        <dt>Consultant credentials</dt><dd>CISSP, ISO/IEC 27001 Lead Auditor</dd>
        <dt>Coverage</dt><dd>UK wide, on site across the North of England, remote elsewhere</dd>
      </dl>
    </div>
  </div>
</section>

{cta(seed=43)}
""")

pages["contact.html"] = ("Contact Cablons Cyber | Book a free consultation",
"Get in touch with Cablons Cyber for fractional CISO services, penetration testing or ISO 27001 and GRC consultancy, or to talk about partnering as an MSP. Book a free 30-minute consultation or send an enquiry.",
hero(None, "Let's talk about what you need.",
     "Book a call directly, or send a short enquiry and we will reply within one working day.",
     f'<a class="btn btn-gold" href="{CAL}">Book a free 30-minute call</a>', seed=23, pos="left") + f"""

<section class="section on-bone">
  <div class="wrap split">
    <div>
      <h2>Send an enquiry</h2>
      <form class="form" action="https://formspree.io/f/REPLACE_WITH_FORM_ID" method="POST">
        <div class="row">
          <div><label for="name">Name</label><input id="name" name="name" type="text" required autocomplete="name"></div>
          <div><label for="company">Company</label><input id="company" name="company" type="text" autocomplete="organization"></div>
        </div>
        <div class="row">
          <div><label for="email">Email</label><input id="email" name="email" type="email" required autocomplete="email"></div>
          <div><label for="phone">Phone (optional)</label><input id="phone" name="phone" type="tel" autocomplete="tel"></div>
        </div>
        <div>
          <label for="interest">What do you need?</label>
          <select id="interest" name="interest">
            <option>Fractional CISO</option>
            <option>Penetration testing</option>
            <option>ISO 27001 or other compliance</option>
            <option>I run an MSP and want to partner</option>
            <option>Not sure yet</option>
          </select>
        </div>
        <div><label for="message">Message</label><textarea id="message" name="message" required></textarea></div>
        <div class="hp" aria-hidden="true"><label>Leave blank<input name="_gotcha" tabindex="-1" autocomplete="off"></label></div>
        <input type="hidden" name="_subject" value="Website enquiry from cablons.com">
        <div>
          <button class="btn btn-dark" type="submit">Send enquiry</button>
          <p style="margin-top:.8rem"><small>We use your details only to respond to your enquiry. See our <a href="privacy.html">privacy notice</a>.</small></p>
        </div>
      </form>
    </div>
    <div class="panel">
      <h3>Other ways to reach us</h3>
      <dl>
        <dt>Email</dt><dd><a href="mailto:sales@cablons.com">sales@cablons.com</a></dd>
        <dt>Book directly</dt><dd><a href="{CAL}">Choose a time on our calendar</a></dd>
        <dt>Office</dt><dd>36 The Oval, Bingley, West Yorkshire, BD16 4RQ</dd>
        <dt>Hours</dt><dd>Monday to Friday, 9am to 5.30pm. Incident support for retained clients is available outside these hours.</dd>
      </dl>
    </div>
  </div>
</section>
""")


pages["msp-partners.html"] = ("Partnering with MSPs | Cablons Cyber",
"Cablons Cyber partners with managed service providers to add fractional CISO, penetration testing and ISO 27001 services to their offer, white-labelled or co-branded.",
hero(None, "Add a security practice to your MSP without building one.",
     "We partner with managed service providers who want to offer fractional CISO, independent testing and compliance work to the clients they already look after.",
     f'<a class="btn btn-gold" href="contact.html">Talk about partnering</a>', seed=47, pos="left") + f"""

<section class="section on-bone">
  <div class="wrap split">
    <div class="prose">
      <h2>Why MSPs come to us</h2>
      <p>The clients you manage are being asked questions you did not sign up to answer. A larger customer wants ISO 27001. An insurer wants a penetration test from someone other than the firm that runs the network. A board wants a security strategy and a name against it. Hiring a CISO to serve a handful of clients does not add up, and sending the work to a large consultancy means they meet your client without you.</p>
      <p>We fill that gap. Our consultants have run service desks and network teams, so we understand how an MSP works and where the margin is. We do the senior security work; you keep the client, the infrastructure and the remediation.</p>
      <h2>How the arrangement works</h2>
      <p>Most partners start with one client and one engagement, usually a fractional CISO retainer or a gap analysis, and grow from there. We can work under your brand with your engineers as the delivery team, or appear as a named partner on your proposals. Either way we agree in writing that we do not sell managed services, so there is no risk of us competing for the account.</p>
      <p>Referral and resale terms are simple and agreed up front, and we are happy to join your sales calls when a client wants to meet the people doing the work.</p>
      <h2>What we bring</h2>
      <ul class="checks-bone">
        <li>Fractional CISO engagements for your clients, with you as the technical partner</li>
        <li>Independent penetration testing with the separation auditors and insurers want to see</li>
        <li>ISO 27001, Cyber Essentials and sector readiness programmes your engineers help deliver</li>
        <li>A second opinion on your own security posture and the questionnaires your clients send you</li>
        <li>Supplier due diligence on the vendors you resell</li>
      </ul>
    </div>
    <div class="panel">
      <h3>A typical first engagement</h3>
      <dl>
        <dt>Week one</dt><dd>Introduction call with you, then a scoping call with the client. Fixed proposal issued under whichever brand you prefer.</dd>
        <dt>Weeks two to four</dt><dd>Gap analysis or first month of fractional CISO cover. Your engineers are copied on anything technical.</dd>
        <dt>Month two onwards</dt><dd>Remediation handed to your team, with us owning the governance, the reporting and the conversation with the client's leadership.</dd>
      </dl>
      <p class="muted" style="margin-top:1.2rem">Partners are generally UK MSPs with between 10 and 100 staff and clients in the 20 to 500 seat range.</p>
    </div>
  </div>
</section>

{cta("Want to talk partnership?", "Tell us about your client base and what they are asking for. The first conversation is informal and takes half an hour.", seed=53)}
""")

ARTICLE_SLUG = "assessing-the-business-ending-event.html"

pages["insights.html"] = ("Insights | Cablons Cyber",
"Articles from Cablons Cyber on risk assessment, security leadership and getting the fundamentals right.",
hero(None, "Insights", "Occasional writing on risk, leadership and the parts of security that decide whether a business survives.", "", seed=59, pos="right") + f"""
<section class="section on-bone">
  <div class="wrap">
    {ledger([
      ("Assess your firm for the business-ending event", "If your security meetings are spent arguing over DLP products, you are probably missing the one scenario that matters. How to build a risk assessment around what would actually close the business.", ARTICLE_SLUG),
    ])}
  </div>
</section>
""")

pages[ARTICLE_SLUG] = ("Assess your firm for the business-ending event | Cablons Cyber",
"Most security programmes are built around controls rather than consequences. A guide to assessing the one or two events that would end the business, and building the risk assessment from there.",
hero(None, "Assess your firm for the business-ending event.",
     "If your security meetings are spent arguing over DLP products, you are probably missing the one scenario that matters.", "", seed=61, pos="top") + """
<section class="section on-bone">
  <div class="wrap prose">
    <p class="muted">Cablons Cyber. November 2026. About eight minutes.</p>

    <p>Sit in enough security steering meetings and you notice a pattern. The agenda is a list of products. Which data loss prevention tool to buy. Whether the email filter should be swapped for the one the reseller is pushing this quarter. Whether the endpoint agent needs upgrading to the tier with the dashboard. Each of these is a reasonable question, and each will eat an hour. What rarely appears on the agenda is the question that should have come first: what is the event that ends this company, and how well are we placed to survive it?</p>

    <p>That is not a rhetorical question. For most mid-sized firms there are one or two scenarios that would be fatal within weeks, and a long tail of incidents that would be expensive, embarrassing and survivable. A security programme that treats these as the same thing, as a list of controls to be bought and ticked, is spending its budget in proportion to vendor marketing rather than in proportion to risk.</p>

    <h2>The controls-first trap</h2>
    <p>The DLP argument is a good example because it feels like serious security work. Data leaving the business is a real risk, the products are complex, and the evaluation generates a satisfying amount of activity. But ask what happens to the company if a spreadsheet of customer names leaks. In most cases the answer is an uncomfortable conversation with the ICO, some customer churn, a bruised reputation and a bad quarter. Painful, but the firm is still trading a year later.</p>

    <p>Now ask what happens if the firm is ransomwared on a Thursday night and the attackers have had domain admin for a fortnight. Not the headline version where files are encrypted and a note appears. The operational version. The warehouse management system is gone and the backups were on the same domain. Nobody can pick, pack or raise a delivery note. The building management system that runs the cold store was reachable from the corporate network, and when it failed the compressors stopped and the stock is now unsellable. The finance system is encrypted, so you cannot invoice, and the bank cannot see why you have stopped paying the loan covenant. Your biggest customer has a clause allowing termination after seven days of non-supply, and on day five their procurement team starts calling your competitor.</p>

    <p>Each of those consequences is survivable on its own. Together, arriving in the same week, they are how companies close. And the control that would have made the difference was not a DLP product. It was knowing that the cold store depended on the corporate network, that the backups could be reached from the domain, and that the customer contract had a seven-day clause.</p>

    <h2>Start from the consequence, not the threat</h2>
    <p>The standard risk assessment template starts from assets and threats. List the servers, list the things that could go wrong with them, score each one. This produces a long register in which everything is medium and the two things that would actually close the business are buried somewhere in the middle, scored the same as a lost laptop.</p>

    <p>The better approach, and the one we use in fractional CISO engagements, is to start from the other end. Get the leadership team in a room for half a day and ask them to describe, in plain terms, the events that would end the business. Not the IT events, the business events. We cannot fulfil orders for three weeks. We cannot invoice for a month. We lose the regulated status that lets us trade. The stock in the warehouse is destroyed. The product we ship is found to be unsafe. Our largest customer leaves. Most firms land on between three and six of these, and they can usually say roughly how long they could survive each one before cash or contracts ran out.</p>

    <p>Only then do you work backwards to the technology. For each business-ending event, what are the systems, suppliers, people and physical dependencies that could cause it? That is where the cold store controller, the single warehouse system, the backups on the same domain and the one person who knows the ERP all surface. They surface because you traced them from a consequence the board already cares about, rather than from a scan result nobody outside IT can interpret.</p>

    <h2>What a useful assessment looks like</h2>
    <p>A risk assessment built this way has a few properties that the template version does not. It is short, because it is organised around a handful of scenarios rather than hundreds of assets. It includes operational technology, because the fridges, the conveyors, the door controllers and the building management system turn out to sit on the path to at least one fatal outcome in most physical businesses, and they are almost always missing from an IT-led register. It includes suppliers and contracts, because a termination clause or a single-source logistics provider is as much a dependency as a server. And it produces a tolerable downtime figure for each scenario, agreed by the people who run the business rather than guessed by IT, which is the number every recovery decision should be measured against.</p>

    <p>It also changes the conversation about spend. When the board can see that the warehouse system has no tested recovery and the cold store is on the flat network, the DLP evaluation stops looking urgent. Segmenting the operational network, moving backups to an immutable store that domain admin cannot touch, testing a full restore of the warehouse system and reading the customer contracts are not glamorous. They are cheaper than most product purchases. And they are the difference between an incident and an obituary.</p>

    <h2>Questions to ask this month</h2>
    <p>If you want to test whether your current assessment is doing its job, these are the questions we put to new clients in the first week.</p>
    <ul>
      <li>Name the three events that would close the business. Does the risk register mention them in those terms?</li>
      <li>For each, how long could you survive it? Who agreed that number?</li>
      <li>Which systems, suppliers, contracts and physical plant sit on the path to each one? When were they last reviewed together rather than separately?</li>
      <li>Can someone with domain admin reach the backups, the building management system or the warehouse controllers?</li>
      <li>When did you last restore the system you most depend on, from scratch, and time it?</li>
      <li>Does your cyber insurance cover business interruption and stock loss from a cyber event, or just the forensics and the lawyers?</li>
    </ul>

    <p>If the answers are uncomfortable, that is the assessment working. Fix those before you go back to the DLP shortlist. The shortlist will still be there.</p>

    <p class="pull">Security is not a list of products. It is knowing which week would be your last, and making sure it never arrives.</p>

    <p class="muted">Cablons Cyber provides fractional CISO services, penetration testing and ISO 27001 consultancy to UK businesses and MSP partners. If you would like help running this kind of assessment, <a href="contact.html">get in touch</a>.</p>
  </div>
</section>
""")

pages["privacy.html"] = ("Privacy notice | Cablons Cyber",
"How Cablons Cyber Limited collects and uses personal data through this website and in the course of its services.",
hero(None, "Privacy notice", "Last reviewed October 2026.", "", small=True, seed=29, pos="right") + """
<section class="section on-bone">
  <div class="wrap prose">
    <h2>Who we are</h2>
    <p>Cablons Cyber Limited (company number 15090311) is the data controller for personal data collected through this website. Our registered office is 36 The Oval, Bingley, West Yorkshire, BD16 4RQ. You can contact us about data protection at <a href="mailto:sales@cablons.com">sales@cablons.com</a>.</p>
    <h2>What we collect and why</h2>
    <p>When you submit the contact form or email us, we collect your name, email address, and any company, phone number or message details you provide. We use this to respond to your enquiry and, where you become a client, to deliver and administer our services. The lawful basis is our legitimate interest in responding to enquiries and, for clients, performance of a contract.</p>
    <p>When you book a call through our scheduling link, your details are processed by Calendly under its own privacy notice. When you submit the contact form, the submission is relayed by our form provider, which processes it on our behalf.</p>
    <p>This website is hosted as static files. The hosting provider may record standard server logs, including IP address and browser type, for security and operational purposes. We do not run analytics or advertising trackers and we do not set cookies for our own purposes.</p>
    <h2>Sharing and retention</h2>
    <p>We do not sell personal data. We share it only with the service providers named above and where required by law. Enquiry data is kept for 12 months from the last contact unless you become a client, in which case it is kept for the duration of the engagement and for six years afterwards to meet legal and insurance obligations.</p>
    <h2>Your rights</h2>
    <p>Under UK GDPR you have the right to access, correct or erase your personal data, to object to or restrict its processing, and to data portability. To exercise any of these rights, email <a href="mailto:sales@cablons.com">sales@cablons.com</a>. You also have the right to complain to the Information Commissioner's Office at <a href="https://ico.org.uk" rel="noopener">ico.org.uk</a>.</p>
    <h2>Changes</h2>
    <p>We will update this notice if our practices change and show the review date at the top of the page.</p>
  </div>
</section>
""")

pages["404.html"] = ("Page not found | Cablons Cyber", "The page you were looking for does not exist.",
hero(None, "That page does not exist.", "The link may be out of date. Everything on the site is reachable from the menu.",
     '<a class="btn btn-gold" href="index.html">Back to the home page</a><a class="btn btn-ghost" href="contact.html">Contact us</a>', seed=5, pos="right"))

os.makedirs(os.path.join(OUT, "assets"), exist_ok=True)
for path, (title, desc, body) in pages.items():
    with open(os.path.join(OUT, path), "w") as f:
        f.write(head(title, desc, path) + body + FOOT)

urls = [p for p in pages if p != "404.html"]
with open(os.path.join(OUT, "sitemap.xml"), "w") as f:
    f.write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n')
    for u in urls:
        f.write(f"  <url><loc>{SITE}/{'' if u == 'index.html' else u}</loc></url>\n")
    f.write("</urlset>\n")
with open(os.path.join(OUT, "robots.txt"), "w") as f:
    f.write(f"User-agent: *\nAllow: /\nSitemap: {SITE}/sitemap.xml\n")
with open(os.path.join(OUT, "CNAME"), "w") as f:
    f.write("www.cablons.com\n")
open(os.path.join(OUT, ".nojekyll"), "w").close()
print("built", list(pages))
