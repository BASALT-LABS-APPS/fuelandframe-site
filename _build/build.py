import re, pathlib
ROOT = pathlib.Path(__file__).resolve().parent.parent
STUDIO = ROOT.parent / "basaltlabsapps-site"  # the studio site, checked out beside this one
BETA = "https://testflight.apple.com/join/wJWjfs3D"

def page(path, title, desc, current, body):
    nav = [("/#features", "Features", "features"), ("/plans/", "Plans", "plans"), ("/coaches/", "For coaches", "coaches"), ("/faq/", "FAQ", "faq")]
    cur = ' aria-current="page"'
    links = "\n      ".join(f'<a href="{h}"{cur if k == current else ""}>{t}</a>' for h, t, k in nav)
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="/img/today.jpg">
<meta name="theme-color" content="#F1EFEA" media="(prefers-color-scheme: light)">
<meta name="theme-color" content="#1A1E19" media="(prefers-color-scheme: dark)">
<link rel="icon" href="/favicon.png">
<link rel="apple-touch-icon" href="/img/icon.png">
<link rel="stylesheet" href="/styles.css">
</head>
<body>

<header class="site">
  <div class="wrap">
    <a class="brand" href="/"><img src="/img/icon.png" alt="">Fuel &amp; Frame</a>
    <nav>
      {links}
      <a class="btn" href="{BETA}">Join the beta</a>
    </nav>
  </div>
</header>

{body}

<footer class="site">
  <div class="wrap">
    <span>© 2026 BASALT LABS LLC</span>
    <span><a href="/support/">Support</a><a href="/privacy/">Privacy Policy</a><a href="/terms/">Terms of Use</a><a href="mailto:hello@basaltlabsapps.com">Contact</a><a href="https://www.basaltlabsapps.com">BASALT LABS</a></span>
  </div>
</footer>

</body>
</html>
"""
    out = ROOT / path
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(html)

def phone(img, alt):
    return f'<img class="phone" src="/img/{img}.jpg" alt="{alt}" loading="lazy">'

def feature(eyebrow, title, text, bullets, shots, flip=False, dot=None):
    lis = "\n          ".join(f"<li>{b}</li>" for b in bullets)
    style = f' style="--dot: var(--{dot})"' if dot else ""
    return f"""  <section>
    <div class="wrap feature{' flip' if flip else ''}">
      <div class="feature-text"{style}>
        <div class="eyebrow">{eyebrow}</div>
        <h2>{title}</h2>
        <p class="sub">{text}</p>
        <ul>
          {lis}
        </ul>
      </div>
      <div class="feature-shots">
        {"".join(shots)}
      </div>
    </div>
  </section>
"""

# ---------- Home ----------
home = f"""<main>
  <div class="wrap hero">
    <div>
      <div class="eyebrow">For iPhone and Apple Watch</div>
      <h1>Food, training and progress. One calm app.</h1>
      <p class="lead">Fuel &amp; Frame turns what you eat and how you train into clear next steps — on your own, or with a real coach when you want one.</p>
      <div class="rings" aria-label="Your three daily goals">
        <span class="ring-chip"><i style="background: var(--carbs)"></i>Fuel</span>
        <span class="ring-chip"><i style="background: var(--accent)"></i>Train</span>
        <span class="ring-chip"><i style="background: var(--fiber)"></i>Hydrate</span>
      </div>
      <div class="actions">
        <a class="btn" href="{BETA}">Join the beta on TestFlight</a>
        <a class="btn ghost" href="/plans/">See plans</a>
      </div>
      <p class="muted note">Coming soon to the App Store. Requires iOS 27 and, for the watch app, watchOS 27.</p>
    </div>
    <div class="phones">
      {phone("workoutpicture", "The workout player: one exercise at a time with its demo and sets")}
      {phone("today", "My Day: your goals, your week and today's nutrition")}
    </div>
  </div>

  <div id="features"></div>
{feature("My Day", "Your whole day, at a glance.",
  "Three daily goals — Fuel, Train and Hydrate — show how today is going. Hit all three for a perfect day and keep your streak alive.",
  ["Cards for nutrition, water, training, steps, sleep, weight and fasting, in the order you choose",
   "A weekly look back and a gentle nudge when a goal is nearly there",
   "Your reason for starting, shown on the days you need it most"],
  [phone("why", "My Day with a coach note, your why and then and now")], dot="carbs")}
{feature("Nutrition", "Log food in seconds.",
  "Search millions of foods, scan a barcode or just type what you ate. Your targets adjust to your real progress, not a guess.",
  ["Daily macros with protein, carbs, fat and fibre",
   "A weekly check-in that adjusts your targets from your weight trend",
   "Calorie cycling: more carbs on strength days, fewer on rest days",
   "Water, coffee and drinks, with caffeine and alcohol insights",
   "Your own recipes, or a meal plan from your coach"],
  [phone("nutrition", "Nutrition summary with daily macros"), phone("logfood", "Log food: search, type what you ate or scan")], flip=True, dot="calories")}
{feature("Training", "Train with purpose.",
  "Follow a program or build your own workouts. The player shows one exercise at a time, with a demo video, your last numbers and a rest timer.",
  ["Strength, supersets, circuits and timed work like walks or planks",
   "Clear signs when you're ready to go up in weight",
   "Strength trends and a balance check across muscle groups",
   "A body map and how-to videos to get your form right"],
  [phone("fitness", "Fitness: today's workout"), phone("summary", "A finished workout: sets, heart rate and how it felt")], dot="accent")}
{feature("Intermittent fasting", "Know what your body is doing.",
  "Start a fast with one tap. The live ring shows where you are, from digesting to the metabolic switch, and logging a meal ends it for you.",
  ["Common plans like 16:8 and 18:6, or your own",
   "Plain-language stages, checked against their sources",
   "Fasting shows up on My Day while it's running"],
  [phone("fasting", "A fast in progress, with its stages")], flip=True, dot="fat")}
{feature("Progress", "See what's working.",
  "Weight, body composition, sleep, water and steps come together in clear charts — straight from Apple Health, without logging twice.",
  ["Charts by week, month, year or all time",
   "Then and now: last month's recap and your lifts over time",
   "Two-week experiments to find out what really helps you"],
  [phone("progress", "Progress charts")], dot="fiber")}
{feature("Friends", "Better together, on your terms.",
  "Add friends by username, cheer each other on and start seven-day challenges. You choose exactly what they can see.",
  ["Workouts, streaks and perfect weeks in a private friends feed",
   "Seven-day challenges with a friendly leaderboard",
   "An invite card for Apple Wallet with your QR code"],
  [phone("community", "The friends feed")], flip=True, dot="gold")}

{feature("Make it yours", "Seven themes, light and dark.",
  "From quiet Sage &amp; Stone to always-dark Midnight &amp; Gold. Set a schedule to change the theme by day of the week, or at sunset.",
  ["Follows your iPhone's Text Size",
   "Readable with Increase Contrast and Reduce Transparency",
   "Your theme follows your account to every device"],
  [phone("appearance", "Appearance: choose a theme")], dot="fat")}
  <section>
    <div class="wrap">
      <div class="eyebrow">Every screen</div>
      <h2>On your wrist and on the big screen.</h2>
      <p class="sub">Log sets, rest and water from Apple Watch, with your heart rate during workouts. On iPad, wide screens get two columns.</p>
      <div class="devices" style="margin-top: 32px">
        <img class="ipad" src="/img/ipad-today.jpg" alt="My Day on iPad, in two columns" loading="lazy">
        <div class="watches">
          <img class="watch" src="/img/watch-today.png" alt="Today on Apple Watch" loading="lazy">
          <img class="watch" src="/img/watch-set.png" alt="Logging a set on Apple Watch" loading="lazy">
        </div>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap grid2">
      <div class="card">
        <div class="dot" style="background: var(--accent)"></div>
        <h3>A coach when you want one</h3>
        <p class="sub">Start on your own with targets calculated for you. Upgrade any time to a real coach who builds your meal plan and program, reviews your check-ins and messages you directly.</p>
        <a href="/plans/">Compare plans →</a>
      </div>
      <div class="card">
        <div class="dot" style="background: var(--gold)"></div>
        <h3>Your data stays yours</h3>
        <p class="sub">No ads, no tracking and no selling of data. Apple Health data is never used for marketing, and private things like glucose readings stay on your iPhone.</p>
        <a href="/privacy/">Read the privacy policy →</a>
      </div>
    </div>
  </section>

  <section class="tight">
    <div class="wrap">
      <div class="band accent">
        <h2>Try it before everyone else.</h2>
        <p class="sub">Fuel &amp; Frame is in public beta on TestFlight. Install it on your iPhone and tell us what you think.</p>
        <div class="actions"><a class="btn" href="{BETA}">Join the beta</a></div>
      </div>
    </div>
  </section>
</main>"""
page("index.html", "Fuel & Frame — food, training and progress in one calm app",
     "Fuel & Frame for iPhone and Apple Watch: log food in seconds, train with purpose and see what's working — on your own or with a real coach.",
     "", home)

# ---------- Plans ----------
plans = [
    ("App Access", "On your own", "14.99", False, ["Food, water, drinks and fasting", "Targets calculated for you", "Your own workouts and recipes", "Goals, streaks, insights and friends", "Apple Health and Apple Watch"]),
    ("Nutrition", "Coached", "24.99", False, ["Everything in App Access", "A custom meal plan and recipes from your coach", "A meal plan change every 2 weeks on request"]),
    ("Nutrition + Training", "Coached", "39.99", True, ["Everything in Nutrition", "A custom training program from your coach", "A program refresh every 4 weeks on request"]),
    ("Full Coaching", "Coached", "89.99", False, ["Everything in Nutrition + Training", "Message your coach directly", "Weekly check-in review", "Feedback on your logs", "A program adjusted as you progress"]),
]
cards = "\n".join(f"""      <div class="card plan{' featured' if feat else ''}">
        <span class="tag">{tag}{' · Popular' if feat else ''}</span>
        <h3 style="margin-top:6px">{name}</h3>
        <p class="price">${price}<small> / month</small></p>
        <ul>{"".join(f"<li>{b}</li>" for b in bullets)}</ul>
      </div>""" for name, tag, price, feat, bullets in plans)
rows = [
    ("Food, water, drinks and fasting tracking", [1,1,1,1]),
    ("Targets calculated for you, adjusted weekly", [1,1,1,1]),
    ("Your own workouts and recipes", [1,1,1,1]),
    ("Goals, streaks, insights and friends", [1,1,1,1]),
    ("Apple Health and Apple Watch", [1,1,1,1]),
    ("Custom meal plan from your coach", [0,1,1,1]),
    ("Custom training program from your coach", [0,0,1,1]),
    ("Plan change requests", [0,1,1,1]),
    ("Message your coach", [0,0,0,1]),
    ("Weekly check-in review and feedback on logs", [0,0,0,1]),
]
trs = "\n".join("        <tr><td>" + label + "</td>" + "".join('<td class="yes">✓</td>' if v else '<td class="no">—</td>' for v in vals) + "</tr>" for label, vals in rows)
plans_body = f"""<main>
  <section>
    <div class="wrap">
      <div class="eyebrow">Plans</div>
      <h1>Start on your own. Add a coach any time.</h1>
      <p class="lead">Every plan includes the full app. Coached plans add a real coach who builds your plan around you.</p>
      <div class="plans" style="margin-top: 36px">
{cards}
      </div>
      <p class="muted" style="margin-top: 18px">Prices in US dollars; they vary by country and are shown in the app before you subscribe. Yearly plans are available in the app. Subscriptions are billed through your Apple Account and renew until you cancel in Settings.</p>
    </div>
  </section>
  <section class="tight">
    <div class="wrap">
      <h2>Compare plans</h2>
      <div class="card scroll-x" style="margin-top: 18px">
        <table class="compare">
          <thead><tr><th></th><th>App Access</th><th>Nutrition</th><th>Nutrition + Training</th><th>Full Coaching</th></tr></thead>
          <tbody>
{trs}
          </tbody>
        </table>
      </div>
    </div>
  </section>
  <section class="tight">
    <div class="wrap">
      <div class="band">
        <h2>Not sure which plan?</h2>
        <p class="sub">Join the beta and try the app first. You can change your plan from the app at any time; upgrades start straight away and downgrades at your next renewal, and your history always stays.</p>
        <div class="actions"><a class="btn" href="{BETA}">Join the beta</a><a class="btn ghost" href="/faq/">Read the FAQ</a></div>
      </div>
    </div>
  </section>
</main>"""
page("plans/index.html", "Plans — Fuel & Frame", "Fuel & Frame plans: App Access on your own, or coached Nutrition, Nutrition + Training and Full Coaching.", "plans", plans_body)

# ---------- Coaches ----------
coach_cards = [
    ("Your clients at a glance", "See who needs you today — missed check-ins, quiet weeks and milestones — and approve new clients when they sign up.", "accent"),
    ("Programs and workouts", "Build programs with supersets, circuits and timed work, assign them in a tap and see every session your clients log.", "fiber"),
    ("Meal plans and recipes", "Write meal plans and recipes your clients can log in one tap, and set their targets or let the app calculate them.", "calories"),
    ("Check-ins and feedback", "Review weekly check-ins, comment on logs and adjust targets and programs as your clients progress.", "carbs"),
    ("Messages", "Message clients directly, with quick replies for the things you say every week.", "fat"),
    ("Milestone notes", "Record a short voice note that plays when a client reaches a milestone you set.", "gold"),
]
cc = "\n".join(f"""      <div class="card"><div class="dot" style="background: var(--{c})"></div><h3>{t}</h3><p class="sub">{d}</p></div>""" for t, d, c in coach_cards)
coaches_body = f"""<main>
  <section>
    <div class="wrap feature">
      <div class="feature-text">
        <div class="eyebrow">For coaches</div>
        <h1>Coach your clients where they already log.</h1>
        <p class="lead">Your clients track food, training and progress in Fuel &amp; Frame. You see it all, build their plans and keep in touch — in the same app.</p>
        <div class="actions"><a class="btn" href="mailto:hello@basaltlabsapps.com?subject=Coaching%20with%20Fuel%20%26%20Frame">Coach with Fuel &amp; Frame</a></div>
      </div>
      <div class="feature-shots">{phone("messages", "Messages between a client and their coach")}</div>
    </div>
  </section>
  <section class="tight">
    <div class="wrap grid3">
{cc}
    </div>
  </section>
  <section class="tight">
    <div class="wrap">
      <div class="band">
        <h2>Interested?</h2>
        <p class="sub">Tell us a little about how you coach and how many clients you work with, and we'll be in touch.</p>
        <div class="actions"><a class="btn" href="mailto:hello@basaltlabsapps.com?subject=Coaching%20with%20Fuel%20%26%20Frame">Email hello@basaltlabsapps.com</a></div>
      </div>
    </div>
  </section>
</main>"""
page("coaches/index.html", "For coaches — Fuel & Frame", "Coach your clients in Fuel & Frame: programs, meal plans, check-ins and messages, where your clients already log.", "coaches", coaches_body)

# ---------- FAQ ----------
faqs = [
    ("Is Fuel &amp; Frame on the App Store?", f'Not yet — it\'s in public beta. <a href="{BETA}">Join the beta on TestFlight</a> to try it now; the App Store release is coming soon.'),
    ("How do I join the beta?", f'Open <a href="{BETA}">the TestFlight link</a> on your iPhone, install TestFlight if you don\'t have it, then tap Accept and Install. You can send feedback from inside TestFlight or the app.'),
    ("Which devices does it work on?", "iPhone with iOS 27 or later, and Apple Watch with watchOS 27 for the watch app. It also runs on iPad, where wide screens get two columns."),
    ("Do I need a coach?", 'No. App Access is the full app on your own, with targets calculated for you. You can add a coach later — see <a href="/plans/">plans</a>.'),
    ("How much does it cost?", 'App Access is $14.99 a month; coached plans start at $24.99. See <a href="/plans/">plans</a> for everything each one includes.'),
    ("Does it work with Apple Health?", "Yes. Weight, body composition, sleep, steps, workouts and heart rate come in from Apple Health, and what you log can be saved back to it. You choose what to share."),
    ("Does it work offline?", "Yes. Everything you log is saved on your iPhone and sent as soon as you're back online."),
    ("Is my data private?", 'Yes. There are no ads and no tracking, and we never sell your data. Glucose readings never leave your iPhone. Read the <a href="/privacy/">privacy policy</a>.'),
    ("How do I cancel?", "Subscriptions are billed by Apple. On your iPhone, go to Settings → your name → Subscriptions → Fuel &amp; Frame. Your history stays in your account."),
    ("How do I delete my account?", 'In the app, go to Profile → Delete Account. If you can\'t sign in, email <a href="mailto:privacy@basaltlabsapps.com">privacy@basaltlabsapps.com</a>.'),
]
fq = "\n".join("      <details><summary>" + q + "</summary><p>" + a + "</p></details>" for q, a in faqs)
faq_body = f"""<main class="wrap doc">
  <div class="eyebrow">FAQ</div>
  <h1>Questions and answers</h1>
  <div class="callout">Try Fuel &amp; Frame now: <a href="{BETA}">join the public beta on TestFlight</a>.</div>
{fq}
  <p class="muted" style="margin-top: 28px">Something else? See <a href="/support/">support</a> or email <a href="mailto:support@basaltlabsapps.com">support@basaltlabsapps.com</a>.</p>
</main>"""
page("faq/index.html", "FAQ — Fuel & Frame", "Questions and answers about Fuel & Frame: the beta, devices, plans, Apple Health, privacy and your account.", "faq", faq_body)

# ---------- Support and privacy: the same content as the studio site ----------
def main_of(p):
    html = (STUDIO / p).read_text()
    return re.search(r"<main.*?</main>", html, re.S).group(0)
support = main_of("fuel-and-frame/support/index.html").replace('<main class="doc">', '<main class="wrap doc">')
support = support.replace("</main>", f"""  <h2>Beta</h2>
  <h3>How do I join the beta?</h3>
  <p>Open <a href="{BETA}">the TestFlight link</a> on your iPhone and tap Accept and Install.</p>

  <h2>Contact</h2>
  <div class="card">
    <ul class="contact-list">
      <li><span>Help with the app</span><a href="mailto:support@basaltlabsapps.com">support@basaltlabsapps.com</a></li>
      <li><span>Privacy</span><a href="mailto:privacy@basaltlabsapps.com">privacy@basaltlabsapps.com</a></li>
      <li><span>Everything else</span><a href="mailto:hello@basaltlabsapps.com">hello@basaltlabsapps.com</a></li>
    </ul>
  </div>
</main>""")
page("support/index.html", "Support — Fuel & Frame", "Help with Fuel & Frame: account, subscriptions, Apple Health and Apple Watch.", "", support)
privacy = main_of("fuel-and-frame/privacy/index.html")
privacy = re.sub(r'<main class="([^"]*)"', lambda m: f'<main class="{m.group(1) if "wrap" in m.group(1) else "wrap " + m.group(1)}"', privacy, count=1)
privacy = privacy.replace('href="/fuel-and-frame/', 'href="/')
page("privacy/index.html", "Privacy Policy — Fuel & Frame", "The Fuel & Frame privacy policy.", "", privacy)

# ---------- Terms of Use and Community Rules: also from the studio site ----------
def doc(p):
    body = main_of(p).replace('<main class="doc">', '<main class="wrap doc">')
    return body.replace('href="/fuel-and-frame/', 'href="/')
page("terms/index.html", "Terms of Use — Fuel & Frame", "The Fuel & Frame terms of use, including subscriptions and community rules.", "", doc("fuel-and-frame/terms/index.html"))
page("community/index.html", "Community Rules — Fuel & Frame", "What's allowed in Fuel & Frame's friends features, and how reports are handled.", "", doc("fuel-and-frame/community/index.html"))

# Old /fuel-and-frame/ links (the app and the App Store listing) forward here.
def forward(old, new):
    out = ROOT / old / "index.html"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Fuel &amp; Frame</title>
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="canonical" href="https://www.basaltlabsapps.com{new}">
<meta http-equiv="refresh" content="0; url={new}">
<meta name="robots" content="noindex">
</head>
<body>
<p>This page has moved. <a href="{new}">Continue to Fuel &amp; Frame</a>.</p>
</body>
</html>
""")
forward("fuel-and-frame/terms", "/terms/")
forward("fuel-and-frame/community", "/community/")

# ---------- 404 ----------
page("404.html", "Page not found — Fuel & Frame", "This page doesn't exist.", "", """<main class="wrap doc">
  <h1>Page not found</h1>
  <p class="sub">This page doesn't exist. <a href="/">Back to Fuel &amp; Frame</a>.</p>
</main>""")
print("built")
