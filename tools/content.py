"""Contenu des 14 Reels du lot 2 (30 octobre au 12 novembre 2026).

Chaque post : date, type, style graphique (s1 bleu, s2 clair, s3 sombre, s4 crème),
paramètres de musique, diapositives et légende. Les textes viennent des fiches Prep'CPE.
"""
import json

CTA = {"kind": "cta", "title": "Prep'CPE", "lines": ["Fiches, quiz et audios", "gratuits, tous concours"], "url": "prep-cpe.netlify.app", "note": "Lien en bio"}


def cta(fiche=None):
    c = dict(CTA)
    if fiche:
        c["lines"] = [f"La fiche {fiche} complète, avec quiz", "et audio, gratuite"]
    return c


H = "#concourscpe #cpe2027 #prepaconcours #conseillerprincipaldeducation #viescolaire"

POSTS = [
    dict(n=1, date="2026-10-30", day="Vendredi 30 octobre", kind="Quiz", fiche=1, style="s1",
         music=dict(bpm=76, root=57, prog="maj_a", seed=11, lead=True),
         slides=[
             dict(kind="cover", kicker="QUIZ CPE · FICHE 1", title="Teste-toi en 20 secondes", note="Une question, une réponse, une explication"),
             dict(kind="quiz", kicker="LA QUESTION", title="Quel texte fixe aujourd'hui les missions du CPE ?",
                  options=["Le décret de 1970", "La circulaire n° 2015-139 du 10 août 2015", "La loi d'orientation de 1989"]),
             dict(kind="answer", kicker="LA RÉPONSE", letter="B", title="La circulaire du 10 août 2015",
                  lines=["Elle fixe 3 domaines et 7 missions, numérotées M1 à M7.", "Le décret de 1970 a, lui, créé le corps des CPE."]),
             cta(1)],
         caption="Quiz CPE : quel texte fixe aujourd'hui les missions du CPE ? A, B ou C ? Réponds en commentaire, puis fais glisser pour la réponse. La fiche 1 de Prep'CPE détaille les 7 missions et les 8 compétences du référentiel. Lien en bio.\n\n" + H + " #quiz"),
    dict(n=2, date="2026-10-31", day="Samedi 31 octobre", kind="Notion", fiche=31, style="s2",
         music=dict(bpm=70, root=62, prog="min_a", seed=22, lead=True),
         slides=[
             dict(kind="cover", kicker="UNE NOTION, UN AUTEUR", title="Bourdieu et la reproduction sociale"),
             dict(kind="list", kicker="L'IDÉE EN UNE PHRASE", title="L'école transforme les inégalités sociales en inégalités scolaires",
                  lines=["Le levier : le capital culturel hérité de la famille."], numbered=False),
             dict(kind="list", kicker="LES OUVRAGES À CITER", title="Deux titres",
                  lines=["Les Héritiers (1964)", "La Reproduction (1970), avec Jean-Claude Passeron"], numbered=False),
             dict(kind="list", kicker="DANS UNE COPIE", title="À quoi ça sert ?",
                  lines=["Problématiser l'égalité des chances.", "Nuancer avec Boudon (stratégies individuelles) ou Dubet (expérience scolaire)."], numbered=False),
             cta(31)],
         caption="Une notion, un auteur : Bourdieu et la reproduction sociale. L'école transforme les inégalités sociales en inégalités scolaires, par le capital culturel. Pour problématiser l'égalité des chances dans une copie, puis nuancer avec Boudon ou Dubet. Tous les auteurs et notions clés sont dans la fiche 31 de Prep'CPE. Et toi, tu cites plutôt Bourdieu, Boudon ou Dubet dans tes copies ? Dis-le en commentaire. Lien en bio.\n\n" + H + " #sciencesdeleducation #bourdieu"),
    dict(n=3, date="2026-11-01", day="Dimanche 1er novembre", kind="Méthode", fiche=31, style="s3",
         music=dict(bpm=68, root=52, prog="maj_b", seed=33, lead=False),
         slides=[
             dict(kind="cover", kicker="MÉTHODE", title="Comment citer un auteur dans une copie ?"),
             dict(kind="list", kicker="LA RÈGLE", title="Une référence, c'est 3 éléments",
                  lines=["L'auteur.", "Son idée, en une phrase.", "Ce qu'elle change dans un EPLE."]),
             dict(kind="list", kicker="UN EXEMPLE", title="Hannah Arendt",
                  lines=["L'autorité est un pouvoir reconnu comme légitime, sans force ni persuasion.", "Le CPE fonde son autorité sur la légitimité du cadre qu'il doit rendre explicite aux élèves."], numbered=False),
             dict(kind="list", kicker="À ÉVITER", title="Les deux pièges",
                  lines=["Un catalogue de noms sans lien avec l'argument.", "Oublier les auteurs de la bibliographie officielle 2027."]),
             cta(31)],
         caption="Comment citer un auteur dans une copie ? Une référence, c'est trois éléments : l'auteur, son idée en une phrase, et ce qu'elle change dans un EPLE. Exemple avec Arendt et l'autorité. Évite le catalogue de noms. Toutes les notions clés sont dans la fiche 31. Lien en bio.\n\n" + H + " #methode #sciencesdeleducation"),
    dict(n=4, date="2026-11-02", day="Lundi 2 novembre", kind="Fiche", fiche=1, style="s1",
         music=dict(bpm=78, root=59, prog="maj_c", seed=44, lead=True),
         slides=[
             dict(kind="cover", kicker="FICHE 1", title="Les missions du CPE : 7 missions, 3 domaines"),
             dict(kind="list", kicker="DOMAINE 1 · LA POLITIQUE ÉDUCATIVE", title="M1 et M2",
                  lines=["M1 : participer à la politique éducative de l'établissement", "M2 : contribuer à une citoyenneté active"], tags=["M1", "M2"]),
             dict(kind="list", kicker="DOMAINE 2 · LE SUIVI DES ÉLÈVES", title="M3 et M4",
                  lines=["M3 : suivi pédagogique et éducatif, individuel et collectif", "M4 : relations de confiance avec les familles"], tags=["M3", "M4"]),
             dict(kind="list", kicker="DOMAINE 3 · LA VIE SCOLAIRE", title="M5, M6 et M7",
                  lines=["M5 : espace scolaire et gestion du temps", "M6 : qualité du climat scolaire", "M7 : animer l'équipe de vie scolaire"], tags=["M5", "M6", "M7"]),
             dict(kind="list", kicker="LE TEXTE À CITER", title="Circulaire n° 2015-139 du 10 août 2015",
                  lines=["Le CPE est un cadre éducatif : ni adjoint du chef d'établissement, ni enseignant."], numbered=False),
             cta(1)],
         caption="Les missions du CPE en 30 secondes : 3 domaines, 7 missions (M1 à M7), fixées par la circulaire n° 2015-139 du 10 août 2015. Enregistre ce post pour tes révisions. La fiche 1 complète, avec les compétences du référentiel, est sur Prep'CPE. Quelle mission te pose le plus de difficultés, de M1 à M7 ? Dis-le en commentaire. Lien en bio.\n\n" + H + " #missions #circulaire2015"),
    dict(n=5, date="2026-11-03", day="Mardi 3 novembre", kind="Repères", fiche=1, style="s4",
         music=dict(bpm=72, root=55, prog="min_b", seed=55, lead=True),
         slides=[
             dict(kind="cover", kicker="REPÈRES DATÉS", title="Du surveillant général au CPE, en 4 dates"),
             dict(kind="timeline", kicker="L'HISTOIRE DU MÉTIER", title="Quatre dates à retenir",
                  items=[("1847", "Le surveillant général, le « surgé », dans les lycées"),
                         ("1970", "Décret du 12 août 1970 : création du corps des CPE"),
                         ("2013", "Référentiel de compétences du 1er juillet 2013"),
                         ("2015", "Circulaire n° 2015-139 du 10 août 2015")]),
             dict(kind="list", kicker="CE QU'IL FAUT RETENIR", title="De la surveillance à l'éducation",
                  lines=["Le CPE devient un conseiller, puis un acteur de la politique éducative de l'établissement."], numbered=False),
             dict(kind="list", kicker="À LIRE", title="Christine Focquenoy",
                  lines=["Le passage du surveillant général au CPE et le « mythe du surgé » (bibliographie 2027)."], numbered=False),
             cta(1)],
         caption="Du surveillant général au CPE en 4 dates : 1847, 1970, 2013, 2015. À connaître pour l'oral et pour les copies sur le métier. Le détail est dans la fiche 1 de Prep'CPE. Laquelle de ces dates te manquait ? Dis-le en commentaire. Lien en bio.\n\n" + H + " #histoire #metier"),
    dict(n=6, date="2026-11-04", day="Mercredi 4 novembre", kind="Quiz", fiche=16, style="s2",
         music=dict(bpm=74, root=60, prog="maj_a", seed=66, lead=True),
         slides=[
             dict(kind="cover", kicker="QUIZ CPE · FICHE 16", title="Punition ou sanction ?", note="Une question, une réponse"),
             dict(kind="quiz", kicker="LA QUESTION", title="Qui peut prononcer une punition scolaire ?",
                  options=["Seulement le chef d'établissement", "Tout personnel de l'établissement", "Seulement le conseil de discipline"]),
             dict(kind="answer", kicker="LA RÉPONSE", letter="B", title="Tout personnel",
                  lines=["Professeurs, personnels de direction, d'éducation et de surveillance.", "Les sanctions, elles, relèvent du chef d'établissement ou du conseil de discipline."]),
             cta(16)],
         caption="Quiz CPE : qui peut prononcer une punition scolaire ? A, B ou C ? Réponds en commentaire. Punitions et sanctions, l'échelle de l'article R. 511-13 et la procédure sont dans la fiche 16 de Prep'CPE. Lien en bio.\n\n" + H + " #quiz #sanctions"),
    dict(n=7, date="2026-11-05", day="Jeudi 5 novembre", kind="Fiche", fiche=14, style="s3",
         music=dict(bpm=80, root=57, prog="min_a", seed=77, lead=True),
         slides=[
             dict(kind="cover", kicker="HARCÈLEMENT · FICHE 14", title="Le programme pHARe en 5 piliers"),
             dict(kind="list", kicker="LES 5 PILIERS", title="pHARe, c'est :",
                  lines=["Sensibiliser dès le plus jeune âge", "Constituer une communauté protectrice : équipe ressource, élèves ambassadeurs",
                         "Agir efficacement, avec la préoccupation partagée", "Associer les parents et les partenaires", "Mobiliser les instances : CVC, CVL, CESCE"], small=True),
             dict(kind="list", kicker="LES DEUX ERREURS À NE PAS FAIRE", title="À retenir pour le jury",
                  lines=["Pas de médiation entre la victime et l'auteur.", "Procédure disciplinaire obligatoire (décret du 16 août 2023)."], numbered=False),
             cta(14)],
         caption="Le programme pHARe en 5 piliers : sensibiliser, constituer une communauté protectrice, agir efficacement, associer les parents, mobiliser les instances. Et deux points à retenir pour le jury : pas de médiation entre victime et auteur, procédure disciplinaire obligatoire. Fiche 14 sur Prep'CPE. Lequel des 5 piliers te semble le plus difficile à mettre en œuvre dans un établissement ? Réponds en commentaire. Lien en bio.\n\n" + H + " #harcelement #phare #climatscolaire"),
    dict(n=8, date="2026-11-06", day="Vendredi 6 novembre", kind="Situation de jury", fiche=14, style="s1",
         music=dict(bpm=72, root=53, prog="maj_b", seed=88, lead=False),
         slides=[
             dict(kind="cover", kicker="SITUATION DE JURY", title="Que faites-vous ?"),
             dict(kind="scene", kicker="LA SITUATION", title="Un lundi matin",
                  lines=["La mère d'une élève de 5e appelle la vie scolaire.", "Sa fille refuse de venir au collège : des photos moqueuses d'elle circulent depuis une semaine sur un groupe Snapchat de la classe."]),
             dict(kind="list", kicker="VOS PREMIERS RÉFLEXES", title="Protéger d'abord",
                  lines=["Accueillir la parole, sans promettre le secret absolu.", "Protéger : surveillance renforcée, adulte référent.", "Informer le chef d'établissement et tracer chaque étape."]),
             dict(kind="list", kicker="ENSUITE", title="Traiter la situation",
                  lines=["Évaluer avec l'équipe ressource.", "Recevoir les familles, séparément.", "Faire cesser, sanctionner, signaler.", "Suivre la victime dans la durée."], small=True),
             cta(14)],
         caption="Situation de jury : un lundi matin, la mère d'une élève de 5e vous appelle. Sa fille refuse de venir au collège, des photos moqueuses circulent sur un groupe Snapchat de la classe. Que faites-vous ? Les 10 étapes de la démarche sont dans la fiche 14 de Prep'CPE. Dis-moi en commentaire ta première action. Lien en bio.\n\n" + H + " #harcelement #cyberharcelement #oral"),
    dict(n=9, date="2026-11-07", day="Samedi 7 novembre", kind="Notion", fiche=31, style="s4",
         music=dict(bpm=69, root=50, prog="min_b", seed=99, lead=True),
         slides=[
             dict(kind="cover", kicker="UNE NOTION, UN AUTEUR", title="Charlot et le rapport au savoir"),
             dict(kind="list", kicker="L'IDÉE", title="La relation de l'élève au fait d'apprendre",
                  lines=["Elle explique des réussites « paradoxales ».", "Auteur : Bernard Charlot et l'équipe ESCOL."], numbered=False),
             dict(kind="list", kicker="À RELIER", title="Le décrochage et le rapport à l'école",
                  lines=["Dubet et Martuccelli : l'expérience scolaire, entre intégration, stratégie et subjectivation."], numbered=False),
             dict(kind="list", kicker="LA MÉTHODE", title="Définir avant d'argumenter",
                  lines=["Une notion bien définie en introduction structure toute la copie."], numbered=False),
             cta(31)],
         caption="Une notion, un auteur : le rapport au savoir de Bernard Charlot. La relation de l'élève au fait d'apprendre, qui explique des réussites « paradoxales ». À relier à la sociologie de l'expérience de Dubet et Martuccelli. Les auteurs et notions clés sont dans la fiche 31 de Prep'CPE. Et toi, quel auteur te parle le plus pour le décrochage ? Dis-le en commentaire. Lien en bio.\n\n" + H + " #sciencesdeleducation #charlot"),
    dict(n=10, date="2026-11-08", day="Dimanche 8 novembre", kind="Bilan", fiche=None, style="s2",
         music=dict(bpm=66, root=64, prog="maj_c", seed=101, lead=True),
         slides=[
             dict(kind="cover", kicker="BILAN DE LA SEMAINE", title="5 choses à retenir"),
             dict(kind="list", kicker="À RETENIR", title="Cette semaine",
                  lines=["Les missions M1 à M7 viennent de la circulaire de 2015.", "Une punition n'est pas une sanction.", "Harcèlement : répétition, domination, isolement.",
                         "Jamais de médiation entre victime et auteur.", "Une référence : auteur, idée, usage en EPLE."], small=True),
             dict(kind="scene", kicker="LE MINI-DÉFI", title="30 secondes",
                  lines=["Explique à voix haute la différence entre punition et sanction.", "Si tu bloques, la fiche 16 t'attend."]),
             cta()],
         caption="Bilan de la semaine : 5 choses à retenir, puis un mini-défi. Explique à voix haute, en 30 secondes, la différence entre punition et sanction. Dis-moi en commentaire si tu as réussi. Toutes les fiches sont sur Prep'CPE. Lien en bio.\n\n" + H + " #bilan #defi"),
    dict(n=11, date="2026-11-09", day="Lundi 9 novembre", kind="Fiche", fiche=16, style="s1",
         music=dict(bpm=77, root=58, prog="maj_a", seed=111, lead=True),
         slides=[
             dict(kind="cover", kicker="FICHE 16", title="Punitions et sanctions : ne plus les confondre"),
             dict(kind="compare", kicker="LA DIFFÉRENCE", title="Punition ou sanction ?",
                  left=("PUNITION", ["Manquement mineur", "Tout personnel peut en prononcer", "Pas de recours devant le juge", "Non inscrite au dossier"]),
                  right=("SANCTION", ["Atteinte aux personnes ou aux biens, manquement grave", "Chef d'établissement ou conseil de discipline", "Recours possible", "Inscrite au dossier"])),
             dict(kind="list", kicker="L'ÉCHELLE · ART. R. 511-13", title="6 sanctions, liste limitative",
                  lines=["Avertissement", "Blâme", "Mesure de responsabilisation (20 h max)", "Exclusion temporaire de la classe (8 jours max)", "Exclusion temporaire de l'établissement (8 jours max)", "Exclusion définitive"], small=True),
             dict(kind="list", kicker="TOUTE SANCTION RESPECTE", title="6 principes",
                  lines=["Légalité", "Contradictoire", "Proportionnalité", "Individualisation", "« Non bis in idem »", "Motivation"], small=True),
             cta(16)],
         caption="Punitions et sanctions : ne plus les confondre. Qui décide, quels faits, quels recours, et l'échelle des 6 sanctions de l'article R. 511-13. Enregistre ce post pour tes révisions : c'est un classique des écrits et de l'oral. Fiche 16 complète sur Prep'CPE. Qu'est-ce qui te pose le plus de difficultés : l'échelle des sanctions ou la procédure ? Réponds en commentaire. Lien en bio.\n\n" + H + " #sanctions #reglementinterieur #climatscolaire"),
    dict(n=12, date="2026-11-10", day="Mardi 10 novembre", kind="Texte du jour", fiche=7, style="s3",
         music=dict(bpm=71, root=55, prog="min_a", seed=121, lead=True),
         slides=[
             dict(kind="cover", kicker="TEXTE DU JOUR", title="La loi du 15 mars 2004"),
             dict(kind="list", kicker="CE QU'ELLE INTERDIT", title="Les signes ostensibles",
                  lines=["Dans les écoles, collèges et lycées publics, les élèves ne portent pas de signes ou tenues par lesquels ils manifestent ostensiblement une appartenance religieuse.", "Code de l'éducation, art. L. 141-5-1."], numbered=False),
             dict(kind="list", kicker="AVANT TOUTE PROCÉDURE DISCIPLINAIRE", title="Le dialogue est obligatoire",
                  lines=["Un dialogue avec l'élève et sa famille, avant toute sanction."], numbered=False),
             dict(kind="list", kicker="À SAVOIR", title="Note de service du 31 août 2023",
                  lines=["L'abaya et le qamis relèvent de cette interdiction.", "Validé par le Conseil d'État le 7 septembre 2023."], numbered=False),
             cta(7)],
         caption="Le texte du jour : la loi du 15 mars 2004 sur les signes religieux ostensibles (art. L. 141-5-1 du Code de l'éducation). Avant toute procédure disciplinaire, un dialogue avec l'élève et sa famille est obligatoire. Tous les textes et situations de la laïcité sont dans la fiche 7 de Prep'CPE. Quelle situation de laïcité te paraît la plus délicate à gérer ? Dis-le en commentaire. Lien en bio.\n\n" + H + " #laicite #loi2004"),
    dict(n=13, date="2026-11-11", day="Mercredi 11 novembre", kind="Quiz", fiche=7, style="s4",
         music=dict(bpm=75, root=61, prog="maj_b", seed=131, lead=True),
         slides=[
             dict(kind="cover", kicker="QUIZ CPE · FICHE 7", title="Laïcité : le bon réflexe", note="Une question, une réponse"),
             dict(kind="quiz", kicker="LA QUESTION", title="Un élève porte un signe religieux ostensible. Que prévoit la loi de 2004 avant toute procédure disciplinaire ?",
                  options=["Une exclusion immédiate", "Un dialogue avec l'élève et sa famille", "Rien : la procédure commence tout de suite"]),
             dict(kind="answer", kicker="LA RÉPONSE", letter="B", title="Un dialogue d'abord",
                  lines=["Le chef d'établissement, le CPE et l'équipe formée expliquent la loi.", "En cas de refus persistant, la procédure disciplinaire peut s'engager."]),
             cta(7)],
         caption="Quiz CPE : un élève porte un signe religieux ostensible. Que prévoit la loi de 2004 avant toute procédure disciplinaire ? A, B ou C ? Réponds en commentaire. La fiche 7 de Prep'CPE détaille les situations fréquentes et les réponses. Lien en bio.\n\n" + H + " #quiz #laicite"),
    dict(n=14, date="2026-11-12", day="Jeudi 12 novembre", kind="Fiche", fiche=7, style="s2",
         music=dict(bpm=73, root=56, prog="min_b", seed=141, lead=True),
         slides=[
             dict(kind="cover", kicker="FICHE 7", title="Valeurs de la République et laïcité"),
             dict(kind="compare", kicker="DEUX RÉGIMES À DISTINGUER", title="Personnels et élèves",
                  left=("LES PERSONNELS", ["Neutralité stricte", "Tous statuts : AED, AESH, contractuels, stagiaires", "Aucun signe religieux"]),
                  right=("LES ÉLÈVES", ["Liberté de conscience", "Mais pas de signe ostensible (loi de 2004)", "Dialogue avant toute procédure"])),
             dict(kind="list", kicker="LES TEXTES À CONNAÎTRE", title="Trois repères",
                  lines=["Loi du 9 décembre 1905", "Loi du 15 mars 2004", "Charte de la laïcité à l'École (2013, 15 articles)"]),
             dict(kind="list", kicker="LE RÔLE DU CPE", title="Faire vivre les valeurs",
                  lines=["Expliquer le sens de la laïcité aux élèves et aux familles.", "Organiser la journée du 9 décembre."], numbered=False),
             cta(7)],
         caption="Valeurs de la République et laïcité : deux régimes à distinguer. Les personnels sont soumis à une stricte neutralité, les élèves ont la liberté de conscience mais pas de signe ostensible. Les textes, les situations fréquentes et les réponses sont dans la fiche 7 de Prep'CPE. Quelle est ta question sur la laïcité qui revient le plus souvent à l'oral ? Pose-la en commentaire. Lien en bio.\n\n" + H + " #laicite #valeursdelarepublique"),
]

if __name__ == "__main__":
    json.dump(POSTS, open("posts.json", "w"), ensure_ascii=False, indent=1)
    print(len(POSTS), "posts")
