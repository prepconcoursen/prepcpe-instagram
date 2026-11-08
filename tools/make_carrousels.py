"""Exporte les carrousels (ex-Reels) vers posts_carrousel.json : un dossier posts/auto/<date> par jour.
Calendrier : lot 2 n°8-14 = 5-11 nov ; lot 4 = 12-18 nov ; lot 3 (10 posts) = 19-28 nov ; rappels J-7 (18 nov) et J-1 (24 nov)."""
import json, re, datetime, sys, os
sys.path.insert(0, os.path.dirname(__file__))
import content, content_lot03, content_lot04
from content import cta

def clean(c):
    c = re.sub(r"\bReel\b", "post", c)
    return c

out = []
d0 = datetime.date(2026, 11, 5)
for p in content.POSTS:
    if p['n'] >= 8:
        d = d0 + datetime.timedelta(days=p['n'] - 8)
        out.append((d, p))
for p in content_lot04.POSTS:
    out.append((datetime.date.fromisoformat(p['date']), p))
d = datetime.date(2026, 11, 19)
for p in content_lot03.POSTS:
    out.append((d, p)); d += datetime.timedelta(days=1)
res = []
for d, p in out:
    res.append(dict(slug=d.isoformat(), date=d.isoformat(), fiche=p.get('fiche'), style=p['style'], slides=p['slides'], caption=clean(p['caption']), title=p.get('day', '') + ' ' + p.get('kind', '')))
L = open(os.path.join(os.path.dirname(__file__), '..', 'rappels', 'LEGENDES.md'), encoding='utf-8').read()
def cap(t):
    m = re.search(r"## " + t + r"\n\n(.*?\n)\n(#concours[^\n]*)", L, re.S)
    return m.group(1).strip() + "\n\n" + m.group(2)
res += [
 dict(slug="2026-11-18-rappel-j7", date="2026-11-18", time="12:00", fiche=None, style="s2", title="Rappel J-7", caption=cap("J-7"), slides=[
  dict(kind="cover", kicker="INSCRIPTION · J-7", title="Plus qu'une semaine pour t'inscrire", note="Concours de CPE 2027"),
  dict(kind="list", kicker="LA DATE À RETENIR", title="Clôture des inscriptions", lines=["Mercredi 25 novembre 2026, à 12 h (heure de Paris)", "Sur Cyclades"], numbered=False),
  dict(kind="list", kicker="À FAIRE CETTE SEMAINE", title="Ne laisse pas passer la date", lines=["Inscris-toi sur Cyclades dès cette semaine.", "Externe, interne ou 3e concours : choisis le tien."], numbered=True),
  cta()]),
 dict(slug="2026-11-24-rappel-j1", date="2026-11-24", time="12:00", fiche=None, style="s1", title="Rappel J-1", caption=cap("J-1"), slides=[
  dict(kind="cover", kicker="INSCRIPTION · J-1", title="Les inscriptions ferment demain", note="Mercredi 25 novembre, 12 h"),
  dict(kind="list", kicker="DERNIÈRE LIGNE DROITE", title="Inscris-toi aujourd'hui", lines=["Clôture : mercredi 25 novembre 2026, 12 h (heure de Paris)", "Sur Cyclades", "Ne prends pas le risque d'attendre la dernière heure"], numbered=False),
  dict(kind="list", kicker="TU PEUX Y ARRIVER", title="Et on t'accompagne", lines=["Prep'CPE est gratuit pour t'accompagner jusqu'au jour J."], numbered=False),
  cta()])]
json.dump(res, open(os.path.join(os.path.dirname(__file__), 'posts_carrousel.json'), 'w'), ensure_ascii=False, indent=1)
print(len(res), 'carrousels', res[0]['slug'], '->', res[-1]['slug'])
