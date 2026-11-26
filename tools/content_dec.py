"""Carrousels du 6 au 25 décembre 2026 (20 posts). Ajoute les entrées à tools/posts_carrousel.json.
Usage : python3 tools/content_dec.py  puis  node tools/carrousel.js <slugs>
Contenu tiré des fiches 3, 6, 25-30 du site et des fiches de lecture de la bibliographie 2026. Rien n'est publié."""
import json, os

HERE = os.path.dirname(__file__)
POOL = ['s7', 's9', 's10', 's11', 's12', 's13', 's15', 's16']
TAGS = "#concourscpe #cpe2027 #prepaconcours #conseillerprincipaldeducation #viescolaire"


def styles(cover, i):
    mid, prev, k = [], cover, i * 3 + 1
    for n in range(6):
        while True:
            s = POOL[k % len(POOL)]; k += 1
            if s != prev and not (n == 5 and s == cover):
                break
        mid.append(s); prev = s
    return [cover] + mid + [cover]


def cover(kicker, title, note, sticker, size=None):
    d = dict(kind="cover", kicker=kicker, title=title, note=note, sticker=sticker)
    if size: d["size"] = size
    return d


def L(kicker, title, lines, numbered=False):
    return dict(kind="list", kicker=kicker, title=title, numbered=numbered, small=True, lines=lines)


def S(kicker, title, lines):
    return dict(kind="scene", kicker=kicker, title=title, lines=lines)


def Q(title, options):
    return dict(kind="quiz", kicker="LA QUESTION", title=title, options=options)


def A(letter, title, lines):
    return dict(kind="answer", kicker="LA RÉPONSE", letter=letter, title=title, lines=lines)


def cta(lines):
    return dict(kind="cta", title="Prep'CPE", lines=lines, url="prep-cpe.netlify.app", note="Lien en bio")


def fiche_cta(n, audio=True):
    return cta([f"La fiche {n} complète, avec quiz,", "situation de jury et audio, gratuite"] if audio
               else [f"La fiche {n} complète, avec quiz", "et situation de jury, gratuite"])


GEN = ["Fiches, quiz et audios", "gratuits, tous concours"]

P = []


def add(date, slug, fiche, cov, slides, caption, tags):
    i = len(P)
    P.append(dict(slug=f"{date}-{slug}", date=date, fiche=fiche, style=cov, styles=styles(cov, i),
                  slides=slides, caption=caption + "\n\n" + TAGS + " " + tags, title=slug))


# 6 déc : bilan
add("2026-12-06", "bilan-semaine", None, "s10", [
    cover("BILAN DE LA SEMAINE", "6 réflexes à retenir", "Du 30 novembre au 5 décembre", "Bilan", 100),
    L("À RETENIR · 1/2", "Cette semaine", [
        "Sécurité : le chef d'établissement en est responsable, le CPE l'organise (surveillance, AED, zones à risque).",
        "Orientation : le conseil de classe donne un avis, le chef d'établissement décide, la famille peut faire appel.",
        "Parents : membres de la communauté éducative, informés aussi quand tout va bien."]),
    L("À RETENIR · 2/2", "Cette semaine", [
        "Santé : le CPE repère, écoute, oriente. Il n'est pas thérapeute. En urgence : le 15, ou le 3114.",
        "Médiation par les pairs : pour les conflits entre égaux, jamais pour le harcèlement.",
        "Vie associative : le budget de l'association n'est pas celui de l'EPLE."]),
    Q("Un élève se confie et évoque un danger pour lui. Que fait le CPE ?",
      ["Il promet de garder le secret", "Il transmet immédiatement", "Il interroge d'abord les camarades de classe"]),
    A("B", "Transmettre sans délai", [
        "Écouter sans enquêter, noter les mots de l'élève.",
        "Informer le chef d'établissement : information préoccupante à la CRIP ou signalement au procureur.",
        "Jamais de promesse de secret."]),
    S("LE MINI-DÉFI", "60 secondes", [
        "Choisis une des fiches de la semaine et explique-la à voix haute, comme devant un jury.",
        "Chronomètre-toi, puis relis la fiche pour vérifier."]),
    L("LE RÔLE DU CPE", "Le fil rouge de la semaine", [
        "Organiser, repérer, orienter, informer : le CPE ne travaille jamais seul.",
        "Chaque fiche relie une règle de droit à un geste professionnel.",
        "Au jury : cite la règle, puis dis ce que tu ferais."]),
    cta(GEN)],
    "Bilan de la semaine : 6 réflexes à retenir (sécurité, orientation, parents, santé, médiation, vie associative), un mini-quiz sur la conduite à tenir quand un élève se confie, puis un mini-défi du dimanche. Explique à voix haute, en 60 secondes, une des fiches de la semaine, comme devant un jury. Le fil rouge : le CPE organise, repère, oriente et informe, jamais seul. Toutes celles et ceux qui préparent le concours, enregistrez ce post pour vos révisions. As-tu réussi ton minuteur ? Dis-le en commentaire. Lien en bio.",
    "#bilan #defi #quiz")

# 7 déc : fiche 25
add("2026-12-07", "adolescent", 25, "s9", [
    cover("ADOLESCENCE · FICHE 25", "Connaître l'adolescent", "Comprendre avant de réagir", "Ados", 100),
    L("UNE PÉRIODE DE TRANSFORMATIONS", "Quatre dimensions", [
        "Physique : la puberté.",
        "Psychique : identité, autonomie, rapport à l'autorité.",
        "Cognitive : pensée abstraite, hypothèses.",
        "Sociale : poids du groupe de pairs. De 11-12 ans à plus de 18 ans."]),
    L("LES BESOINS", "Ce dont il a besoin", [
        "Être reconnu et appartenir à un groupe.",
        "S'affirmer et tester les limites : la transgression fait partie du processus.",
        "Être protégé : l'adulte pose des limites qui contiennent sans humilier."]),
    L("REPÈRES THÉORIQUES", "Quatre auteurs", [
        "Erikson : identité contre confusion des rôles.",
        "Winnicott : un environnement qui tient et survit aux attaques.",
        "Dolto : le complexe du homard, la carapace perdue.",
        "Marcelli : l'autorité repose sur la confiance, non sur la force."]),
    L("À MANIER AVEC PRUDENCE", "Le cerveau", [
        "Le cortex préfrontal (contrôle, anticipation) mûrit jusqu'à environ 25 ans.",
        "Le système émotionnel est très actif : sensibilité à la récompense et au regard des pairs.",
        "Les neurosciences n'expliquent pas tout (Gentaz, 2022). Il y a des adolescences, pas « un » adolescent."]),
    L("LA DÉMARCHE", "L'entretien éducatif", [
        "Préparer, puis accueillir : cadre, confidentialité et ses limites.",
        "Faire parler : questions ouvertes, reformulation.",
        "Distinguer l'acte et la personne, chercher le sens.",
        "Conclure par un engagement concret et une date de suivi."], True),
    L("LE RÔLE DU CPE", "Et le CPE dans tout ça ?", [
        "Conduire des entretiens adaptés, accompagner le parcours (C5).",
        "Poser un cadre ferme et bienveillant, protéger (CC6) ; connaître les élèves (CC3).",
        "S'appuyer sur le besoin d'autonomie : délégués, médiateurs, MDL (C6).",
        "Piège : psychologiser à l'excès. Relais : infirmier, PsyEN, maison des adolescents."]),
    fiche_cta(25, False)],
    "Connaître l'adolescent : un passage obligé des écrits comme des oraux. Quatre dimensions de l'adolescence (physique, psychique, cognitive, sociale), les besoins à reconnaître, des repères théoriques (Erikson, Winnicott, Dolto, Marcelli), les limites des neurosciences et la démarche d'un entretien éducatif. Le rôle du CPE : mener l'entretien (C5), poser un cadre ferme et bienveillant (CC6), connaître les élèves (CC3). Piège classique : psychologiser à l'excès, le CPE n'est pas thérapeute. Toutes celles et ceux qui préparent le concours, enregistrez ce post pour vos révisions. Tout est dans la fiche 25 de Prep'CPE, avec le quiz et une situation de jury. Quel auteur t'aide le plus à comprendre les adolescents ? Dis-le en commentaire. Lien en bio.",
    "#adolescence #entretieneducatif")

# 8 déc : fiche 26
add("2026-12-08", "espaces-temps", 26, "s12", [
    cover("VIE SCOLAIRE · FICHE 26", "Espaces et temps", "Là où l'éducation se joue hors de la classe", "Hors classe", 100),
    L("LE PRINCIPE", "Tous les moments hors classe", [
        "Entrées et sorties, interclasses, récréations, études, pause méridienne, internat, abords.",
        "Ces temps ont une valeur éducative : ils ne se réduisent pas à la surveillance (IH2EF)."]),
    L("LES TEMPS SENSIBLES", "Où agir ?", [
        "Entrées et sorties : sécurité, ponctualité, régime de sortie.",
        "Interclasses : circulation organisée, présence adulte aux croisements.",
        "Récréations : zones différenciées, cour aménagée avec les élèves.",
        "Pause méridienne : passage par niveaux, clubs, CDI ouvert."]),
    L("LA DEMI-PENSION", "Qui fait quoi ?", [
        "La collectivité (département ou région) : organisation et tarifs.",
        "L'EPLE : fonctionnement et cadre éducatif.",
        "Un moment de socialisation et d'éducation à l'alimentation (loi EGalim), parfois de tensions : bruit, attente."]),
    L("L'INTERNAT", "Points de vigilance", [
        "Projet éducatif annexé au projet d'établissement ; règlement adopté par le CA.",
        "Encadrement de nuit par des AED, protocoles d'urgence.",
        "Santé, sommeil, PAI. Vie collective : intimité, prévention du harcèlement, écrans le soir."]),
    S("SITUATION DE JURY", "Au self, 25 minutes d'attente", [
        "Bruit, incidents, les 3e passent devant les 6e.",
        "Diagnostic : flux, avis des agents, des AED, du CVC.",
        "Passage par niveau, activités pendant l'attente, AED dans la file.",
        "Aménagements avec le secrétaire général et la collectivité."]),
    L("LE RÔLE DU CPE", "Et le CPE dans tout ça ?", [
        "Organiser l'espace scolaire et le temps (M5) : externat, demi-pension, internat.",
        "Améliorer les conditions de vie des élèves (C1) ; construire l'emploi du temps des AED (C4).",
        "Porter le projet d'internat (C3).",
        "Piège : oublier la collectivité pour les bâtiments et la restauration."]),
    fiche_cta(26)],
    "Espaces et temps scolaires : tout ce qui se joue en dehors de la classe. Entrées, interclasses, récréations, pause méridienne, demi-pension (qui fait quoi entre la collectivité et l'EPLE), internat (projet, règlement, encadrement de nuit), et une situation de jury : l'attente au self. Le rôle du CPE : organiser l'espace et le temps (M5), améliorer les conditions de vie (C1), construire l'emploi du temps des AED (C4), porter le projet d'internat (C3). Piège classique : réduire ces temps à de la surveillance. Toutes celles et ceux qui préparent le concours, enregistrez ce post pour vos révisions. Tout est dans la fiche 26 de Prep'CPE, avec le quiz et une situation de jury. Dans ton établissement, quel moment hors classe aimerais-tu réaménager en premier ? Dis-le en commentaire. Lien en bio.",
    "#viescolaire #internat #demipension")

# 9 déc : fiche 27
add("2026-12-09", "equipe-vie-scolaire", 27, "s11", [
    cover("MANAGEMENT · FICHE 27", "Animer l'équipe", "AED, service civique, projet de service", "Équipe", 100),
    L("QUI EST QUI", "L'équipe de vie scolaire", [
        "Un ou plusieurs CPE, des assistants d'éducation, parfois des assistants pédagogiques et des volontaires du service civique.",
        "Le CPE organise et anime. Le chef d'établissement recrute les AED et signe leurs contrats, après délibération du CA."]),
    L("LES AED", "Leur statut", [
        "Contrats de droit public de trois ans maximum, renouvelables jusqu'à six ans.",
        "CDI possible après six ans (décret du 9 août 2022).",
        "Missions : surveillance, assiduité, aide aux devoirs, projets, encadrement à l'internat."]),
    L("LE SERVICE CIVIQUE", "Le piège fréquent", [
        "Volontaires de 16 à 25 ans, pour des missions d'intérêt général.",
        "Jamais en substitution d'un emploi.",
        "Pas de surveillance seul, pas de remplacement d'un AED."]),
    L("LES LEVIERS", "Animer, concrètement", [
        "Clarifier et organiser : protocoles écrits, emploi du temps selon les flux.",
        "Former : accueil, tutorat, posture, harcèlement, laïcité, premiers secours.",
        "Réunir et responsabiliser : réunion hebdomadaire courte, AED référents d'un niveau ou d'un projet.",
        "Reconnaître et évaluer : entretiens individuels, bilan du projet de service."]),
    L("LA DÉMARCHE", "Accueillir un nouvel AED", [
        "Entretien d'accueil et livret : protocoles, règlement, sécurité.",
        "Tutorat par un AED expérimenté.",
        "Formation : logiciel, posture, neutralité, signalement.",
        "Point à un mois, puis entretiens réguliers."], True),
    L("LE RÔLE DU CPE", "Et le CPE dans tout ça ?", [
        "Animer l'équipe (M7), construire emplois du temps, protocoles et projet de service (C4).",
        "Coopérer au sein d'une équipe (CC10) ; former et se former (CC14).",
        "Piège : se présenter comme le supérieur hiérarchique statutaire. C'est le chef d'établissement."]),
    fiche_cta(27)],
    "Animer l'équipe de vie scolaire : une question de management très fréquente à l'oral. Qui compose l'équipe, le statut des AED (contrats de trois ans, six ans maximum, CDI possible ensuite), le piège du service civique (jamais en substitution d'un emploi), les leviers d'animation et la démarche pour accueillir un nouvel AED. Le rôle du CPE : animer l'équipe (M7), construire emplois du temps, protocoles et projet de service (C4), coopérer (CC10), former (CC14). Piège classique : se dire supérieur hiérarchique, c'est le chef d'établissement. Toutes celles et ceux qui préparent le concours, enregistrez ce post pour vos révisions. Tout est dans la fiche 27 de Prep'CPE, avec le quiz et une situation de jury. Quel est le premier conseil que tu donnerais à un nouvel AED ? Dis-le en commentaire. Lien en bio.",
    "#aed #management #equipe")

# 10 déc : fiche 28
add("2026-12-10", "numerique-ecrans-ia", 28, "s16", [
    cover("NUMÉRIQUE · FICHE 28", "Écrans et IA", "Téléphone, réseaux, cyberharcèlement", "Numérique", 100),
    L("LE CADRE", "Téléphone et IA", [
        "Téléphone interdit à l'école et au collège depuis la loi du 3 août 2018 (sauf usages pédagogiques et élèves en situation de handicap).",
        "Au lycée : les modalités passent par le règlement intérieur (vérifier le texte à jour).",
        "IA : cadre d'usage du 14 juin 2025, usage autonome des élèves à partir de la 4e, sous conditions. Un usage non autorisé en évaluation peut être une fraude."]),
    L("CYBERHARCÈLEMENT", "Une forme de harcèlement", [
        "Délit de harcèlement scolaire (loi du 2 mars 2022, art. 222-33-2-3 du Code pénal).",
        "Il prolonge souvent le harcèlement de l'établissement.",
        "L'établissement agit dès qu'il y a un lien avec la scolarité."]),
    L("LES RÉFLEXES", "Que faire ?", [
        "Protéger la victime, conserver les preuves.",
        "3018 : écoute et signalement accéléré aux plateformes. Pharos : contenus illicites.",
        "Plainte possible ; sanction si lien avec la scolarité.",
        "Images intimes ou chantage : signalement immédiat au procureur."]),
    L("ATTENTION", "Ce qu'on ne fait pas", [
        "Fouiller un téléphone : seul un officier de police judiciaire le peut.",
        "Faire circuler des images intimes, même pour prouver.",
        "Mener l'enquête à la place de la police.",
        "Réduire l'éducation au numérique à l'interdiction."]),
    L("DONNÉES ET MÉDIAS", "RGPD et EMI", [
        "Le RGPD s'applique : ENT, logiciel de vie scolaire, photos, listes.",
        "Droit à l'image : autorisation des représentants légaux.",
        "Éducation aux médias avec le professeur documentaliste et le CLEMI.",
        "Le CVL est consulté sur la charte du numérique."]),
    L("LE RÔLE DU CPE", "Et le CPE dans tout ça ?", [
        "Utiliser l'ENT et le logiciel de vie scolaire, éduquer aux usages (CC9).",
        "Faire appliquer les règles et traiter le cyberharcèlement (C2) ; protéger les données, signaler (CC6).",
        "Inscrire l'éducation au numérique dans le projet et le CESCE (C3)."]),
    fiche_cta(28, False)],
    "Numérique, écrans, réseaux sociaux, IA : un sujet d'actualité très probable aux écrits comme aux oraux. Le cadre du téléphone portable, le cadre d'usage de l'IA du 14 juin 2025, le cyberharcèlement (délit de harcèlement scolaire), les bons réflexes (3018, Pharos, preuves, plainte), ce qu'on ne fait jamais (fouiller un téléphone, faire circuler des images intimes) et les données personnelles. Le rôle du CPE : utiliser et expliquer l'ENT (CC9), faire appliquer les règles (C2), protéger les données et signaler (CC6), inscrire le numérique dans le projet (C3). Toutes celles et ceux qui préparent le concours, enregistrez ce post pour vos révisions. Tout est dans la fiche 28 de Prep'CPE, avec le quiz et une situation de jury. Dans ton établissement, comment est appliquée la règle sur le téléphone portable ? Dis-le en commentaire. Lien en bio.",
    "#numerique #cyberharcelement #ia")

# 11 déc : fiche 29
add("2026-12-11", "partenariats", 29, "s7", [
    cover("PARTENAIRES · FICHE 29", "Partenariats", "Nommer, cadrer, coordonner", "Réseau", 100),
    L("LE PRINCIPE", "Un partenariat, c'est", [
        "Un objectif commun, des rôles distincts, une formalisation par convention.",
        "L'école garde la responsabilité éducative et pédagogique ; le partenaire apporte une expertise.",
        "Convention autorisée par le CA, signée par le chef d'établissement."]),
    L("LA CARTE · 1/2", "Collectivités, sécurité, justice", [
        "Département (collèges), Région (lycées), commune : bâtiments, restauration, transports.",
        "Police, gendarmerie, référent sécurité-école, équipe mobile de sécurité : prévention et infractions.",
        "Procureur, PJJ, juge des enfants : signalements, éducation au droit."]),
    L("LA CARTE · 2/2", "Social, santé, insertion", [
        "ASE et CRIP, CAF, CCAS : informations préoccupantes, aides, soutien parental.",
        "Maison des adolescents, CMP, centres de santé sexuelle : prévention et soins.",
        "CIO, ONISEP, mission locale, MLDS : orientation, raccrochage.",
        "Ligue de l'enseignement, CEMÉA, Francas : formation des délégués."]),
    L("INTERVENANTS EXTÉRIEURS", "Les règles", [
        "Association éducative agréée, ou sans agrément : autorisation du chef d'établissement après information des autorités académiques (art. D. 551-6).",
        "Sous la responsabilité de l'établissement, en présence d'un personnel.",
        "Contenu préparé, conforme à la neutralité et à la laïcité."]),
    L("LA DÉMARCHE", "Construire un partenariat", [
        "Partir d'un besoin identifié dans le diagnostic.",
        "Identifier le partenaire compétent, co-construire objectifs, public, calendrier.",
        "Formaliser par convention, préparer élèves et enseignants.",
        "Évaluer avec le partenaire et ajuster."], True),
    L("LE RÔLE DU CPE", "Et le CPE dans tout ça ?", [
        "Identifier, solliciter et coordonner les partenaires (CC13) ; inscrire les partenariats dans le projet et le CESCE (C3).",
        "Respecter agrément, convention, CA (CC2) ; articuler avec le territoire (M1).",
        "Piège : citer « des partenaires » sans les nommer ni dire leur rôle."]),
    fiche_cta(29, False)],
    "Partenariats : le jury attend des partenaires précis, avec leur rôle et le cadre de leur intervention. Le principe (objectif commun, rôles distincts, convention autorisée par le CA), la carte des partenaires (collectivités, sécurité, justice, protection de l'enfance, santé, orientation, éducation populaire), les règles pour les intervenants extérieurs et la démarche pour construire un partenariat. Le rôle du CPE : coordonner (CC13), inscrire dans le projet (C3), respecter le cadre (CC2). Piège classique : citer des partenaires sans les nommer. Toutes celles et ceux qui préparent le concours, enregistrez ce post pour vos révisions. Tout est dans la fiche 29 de Prep'CPE, avec le quiz et une situation de jury. Quel partenaire de ton territoire connais-tu le moins bien ? Dis-le en commentaire. Lien en bio.",
    "#partenariats #territoire")

# 12 déc : fiche 30
add("2026-12-12", "eco-delegues", 30, "s13", [
    cover("ÉCOLOGIE · FICHE 30", "Éco-délégués", "Transition écologique et démarche E3D", "E3D", 100),
    L("LE CADRE", "Ce que disent les textes", [
        "Loi Climat et résilience du 22 août 2021 : éducation à l'environnement et au développement durable tout au long de la scolarité (art. L. 312-19).",
        "Circulaire du 27 août 2019 : au moins un éco-délégué par classe, au moins deux au CVC et au CVL, un référent EDD par établissement."]),
    L("LA DÉMARCHE E3D", "Un établissement engagé", [
        "Un projet qui associe enseignements, vie scolaire, gestion de l'établissement et partenaires.",
        "Labellisation académique à trois niveaux : engagement, approfondissement, expertise.",
        "Lien avec les 17 objectifs de développement durable de l'ONU."]),
    L("DES ACTIONS", "Ce que ça donne", [
        "Cours renaturées, potager, aires éducatives.",
        "Gaspillage alimentaire au self (loi EGalim).",
        "Tri et réduction des déchets, énergie, mobilités douces."]),
    L("UN ÉQUILIBRE", "Éduquer, pas militer", [
        "Passer des petits gestes à la compréhension des enjeux et à l'engagement.",
        "Sans culpabiliser ni militer : neutralité du service public.",
        "Piège : réduire l'EDD aux gestes individuels."]),
    L("LA DÉMARCHE", "Faire vivre les éco-délégués", [
        "Élire, puis former : enjeux, conduite de projet.",
        "Diagnostiquer : déchets, énergie, self, biodiversité.",
        "Choisir deux ou trois projets réalistes, avec budget et adulte référent.",
        "Présenter au CESCE et au CA, évaluer, valoriser."], True),
    L("LE RÔLE DU CPE", "Et le CPE dans tout ça ?", [
        "Organiser l'élection et la formation des éco-délégués (C6) ; porter la démarche E3D via le CESCE (C3).",
        "Agir sur les espaces : cour, self, déchets (C1) ; mobiliser collectivité et associations (CC13).",
        "Si les éco-délégués se découragent : expliquer un refus, chercher une alternative, redonner du pouvoir d'agir."]),
    fiche_cta(30)],
    "Transition écologique et éco-délégués : un sujet émergent des écrits, et un classique des oraux. Le cadre (loi Climat et résilience, circulaire du 27 août 2019), la démarche E3D et ses trois niveaux de label, des actions concrètes, l'équilibre entre éduquer et militer, et la démarche pour faire vivre les éco-délégués. Le rôle du CPE : élection et formation des éco-délégués (C6), démarche E3D via le CESCE (C3), actions sur les espaces (C1), collectivité et associations (CC13). Piège classique : réduire l'EDD aux petits gestes. Toutes celles et ceux qui préparent le concours, enregistrez ce post pour vos révisions. Tout est dans la fiche 30 de Prep'CPE, avec le quiz et une situation de jury. Quel projet écologique réaliste proposerais-tu à des éco-délégués ? Dis-le en commentaire. Lien en bio.",
    "#ecodelegues #developpementdurable")

# 13 déc : fiche 3
add("2026-12-13", "systeme-educatif", 3, "s15", [
    cover("SYSTÈME ÉDUCATIF · FICHE 3", "Qui fait quoi ?", "Organisation, acteurs et pilotage", "Repères", 100),
    L("LE PRINCIPE", "Centralisé, déconcentré", [
        "L'éducation est « la première priorité nationale » (art. L. 111-1).",
        "L'État fixe les programmes, recrute et paie les personnels.",
        "Les académies mettent en œuvre. Les collectivités construisent et entretiennent les bâtiments."]),
    L("LES NIVEAUX", "Qui décide quoi ?", [
        "Commune : écoles. Département : collèges. Région : lycées.",
        "IA-DASEN : affectation des élèves, moyens des collèges.",
        "Recteur : mise en œuvre de la politique nationale, projet académique.",
        "EPLE : autonomie, projet d'établissement, règlement intérieur, budget."]),
    L("LES INSPECTEURS", "Qui évalue qui ?", [
        "IA-IPR : professeurs du second degré.",
        "IA-IPR « Établissements et vie scolaire » (EVS) : CPE et chefs d'établissement.",
        "IEN : premier degré et voie professionnelle."]),
    L("LES TEXTES", "Cinq lois à situer", [
        "1989 : l'élève au centre. 2005 : socle commun.",
        "2013 : refondation, école inclusive.",
        "2019 : instruction obligatoire dès 3 ans, formation obligatoire jusqu'à 18 ans.",
        "2022 : lutte contre le harcèlement scolaire."]),
    L("LE PILOTAGE", "Des projets emboîtés", [
        "Projet académique, puis projet d'établissement (adopté par le CA pour trois à cinq ans), contrat d'objectifs.",
        "Chaque établissement est évalué tous les cinq ans : autoévaluation, puis évaluation externe.",
        "Circulaire de rentrée 2026 : « instruire et protéger »."]),
    L("LE RÔLE DU CPE", "Et le CPE dans tout ça ?", [
        "Inscrire la vie scolaire dans les priorités nationales et académiques (M1).",
        "Connaître les textes et les interlocuteurs (CC2) ; s'appuyer sur les indicateurs pour le volet éducatif (C3).",
        "Participer à l'autoévaluation (CC11). Piège : citer des chiffres sans vérifier l'édition la plus récente des Repères et références statistiques."]),
    fiche_cta(3)],
    "Le système éducatif : organisation, acteurs, pilotage. Qui décide quoi (État, académie, département, région, commune, EPLE), qui évalue les CPE (l'IA-IPR EVS), cinq lois à situer de 1989 à 2022, le pilotage par projets emboîtés et l'évaluation des établissements tous les cinq ans. Le rôle du CPE : inscrire la vie scolaire dans les priorités nationales et académiques (M1), connaître le cadre (CC2), bâtir le volet éducatif (C3), participer à l'autoévaluation (CC11). Toutes celles et ceux qui préparent le concours, enregistrez ce post pour vos révisions. Tout est dans la fiche 3 de Prep'CPE, avec le quiz et une situation de jury. Sais-tu qui est l'inspecteur ou l'inspectrice EVS de ton académie ? Dis-le en commentaire. Lien en bio.",
    "#systemeeducatif #politiqueeducative")

# 14 déc : fiche 6
add("2026-12-14", "travail-en-equipe", 6, "s12", [
    cover("ÉQUIPE · FICHE 6", "Jamais seul", "Travailler avec toute l'équipe", "Ensemble", 100),
    L("LE POSITIONNEMENT", "Sous l'autorité du chef", [
        "Le CPE est sous l'autorité du chef d'établissement et membre de l'équipe de direction élargie sur les questions éducatives. Il n'est pas adjoint.",
        "Chacun dans son champ : la pédagogie aux professeurs, la santé à l'infirmier, le social à l'assistant de service social, l'orientation au PsyEN."]),
    L("AU QUOTIDIEN", "Avec qui, pour quoi ?", [
        "Chef d'établissement : rencontre hebdomadaire, remontée des incidents.",
        "Professeur principal : suivi, conseil de classe, entretiens conjoints.",
        "PsyEN : orientation, mal-être, décrochage.",
        "Infirmier et ASS : conduites à risque, absentéisme, informations préoccupantes."]),
    L("INFORMATIONS", "Que partager ?", [
        "Secret professionnel et discrétion encadrent les échanges.",
        "Secret partagé : seulement l'information strictement nécessaire, entre professionnels concernés, dans l'intérêt de l'élève.",
        "Rien de confidentiel en conseil de classe ni en salle des professeurs."]),
    L("LES CADRES", "Où travailler ensemble ?", [
        "Équipe de direction, équipe pédagogique de classe.",
        "GPDS (prévention du décrochage), cellule de veille.",
        "Équipe de suivi de la scolarisation pour les PPS, équipe ressource pHARe."]),
    S("SITUATION DE JURY", "Une collègue te reproche de « toujours prendre le parti des élèves »", [
        "Ne pas répondre à chaud ni en public.",
        "Rappeler les rôles : l'exclusion de cours est une punition du professeur, entendre l'élève relève du suivi éducatif.",
        "Soutenir l'autorité du professeur, proposer un protocole d'exclusion partagé."]),
    L("LE RÔLE DU CPE", "Et le CPE dans tout ça ?", [
        "Coopérer au sein d'une équipe (CC10), contribuer à l'action de la communauté éducative (CC11).",
        "Participer aux conseils de classe et aux projets (C8).",
        "Piège : se présenter comme le supérieur des professeurs ou le « chef de la discipline »."]),
    fiche_cta(6)],
    "Travailler en équipe : le jury vérifie qu'on ne travaille jamais seul. Le positionnement du CPE (sous l'autorité du chef d'établissement, membre de l'équipe de direction élargie), les partenaires du quotidien, ce qu'on peut partager (secret professionnel, secret partagé), les cadres de travail collectif, et une situation de jury : une collègue reproche de toujours prendre le parti des élèves. Le rôle du CPE : coopérer (CC10), contribuer à la communauté éducative (CC11), participer aux conseils de classe (C8). Piège classique : se présenter comme le chef de la discipline. Toutes celles et ceux qui préparent le concours, enregistrez ce post pour vos révisions. Tout est dans la fiche 6 de Prep'CPE, avec le quiz et une situation de jury. Quelle collaboration t'a le plus appris sur le travail d'équipe ? Dis-le en commentaire. Lien en bio.",
    "#equipe #cooperation")

# 15 déc : Delahaye-Véran
add("2026-12-15", "biblio-delahaye-veran", None, "s10", [
    cover("BIBLIOGRAPHIE 2026", "Le CPE", "Delahaye et Véran, 4e éd. 2026", "Lire", 130),
    L("L'OUVRAGE", "De la vie scolaire à la politique éducative", [
        "Ouvrage collectif dirigé par Jean-Paul Delahaye (ancien directeur général de l'enseignement scolaire) et Véran (Berger-Levrault, 4e éd. 2026).",
        "Thèse : séparé de l'enseignement à l'origine, le CPE est devenu un cadre éducatif polyvalent, dans une éducation partagée."]),
    L("L'HISTOIRE", "Du surveillant général au CPE", [
        "1819 : le surveillant général, d'abord tourné vers la surveillance.",
        "1970 : le statut de CPE, avec une mission d'éducation.",
        "Depuis 1857, les tentatives d'élargir le service des professeurs aux tâches éducatives ont échoué.",
        "La circulaire de 1982 a été remplacée en 2015."]),
    L("LA TENDANCE", "Une éducation partagée", [
        "D'une division du travail entre enseignants et CPE vers une éducation partagée.",
        "La qualité de la vie scolaire conditionne l'enseignement.",
        "Le CPE : conseiller du chef d'établissement, animateur d'une politique éducative concertée."]),
    L("LA POSTURE", "Autorité et dignité", [
        "Tenir ensemble l'autorité des adultes et l'égale dignité de tous.",
        "Expliquer ce qui est négociable et ce qui ne l'est pas.",
        "Considérer les parents comme de vrais partenaires."]),
    L("À L'ÉCRIT ET À L'ORAL", "Comment l'utiliser ?", [
        "Sujets : identité et missions du CPE, place dans l'équipe, autorité et discipline, absentéisme.",
        "En ouverture : la séparation historique entre enseigner et éduquer, puis l'éducation partagée.",
        "Nuance : ne pas réduire le CPE à la discipline, et vérifier les textes cités, certains sont dépassés."]),
    L("LE RÔLE DU CPE", "Pour le jury", [
        "Question probable : quelle différence entre un surveillant général et un CPE ?",
        "Phrase pour l'oral : « Héritier du surveillant général, le CPE est devenu un éducateur polyvalent engagé dans une éducation partagée. »",
        "Pièges : citer des textes abrogés, opposer professeurs et CPE."]),
    cta(GEN)],
    "Une lecture de la bibliographie 2026 : Le CPE, de la vie scolaire à la politique éducative, de Jean-Paul Delahaye et Véran (4e édition, 2026). Du surveillant général de 1819 au statut de CPE de 1970, la tendance vers une éducation partagée avec les professeurs, la posture qui tient ensemble autorité des adultes et égale dignité de tous, et comment mobiliser l'ouvrage à l'écrit et à l'oral. Le rôle du CPE : cadre éducatif polyvalent, conseiller du chef d'établissement. Dates et textes à confirmer dans le livre avant de les citer en copie. Toutes celles et ceux qui préparent le concours, enregistrez ce post pour vos révisions. As-tu déjà lu cet ouvrage en entier ? Dis-le en commentaire. Lien en bio.",
    "#bibliographie2026 #delahaye #lecture")

# 16 déc : Debarbieux
add("2026-12-16", "biblio-debarbieux", None, "s9", [
    cover("BIBLIOGRAPHIE 2026", "L'impasse de la punition", "Éric Debarbieux (dir.), 2e éd. 2022", "Lire", 100),
    L("LE CONSTAT", "La punition, massive", [
        "Dans l'enquête citée par l'ouvrage, deux tiers des collégiens disent avoir déjà été punis, un quart plus de quatre fois.",
        "Elle nourrit le sentiment d'injustice et ne suffit pas à éduquer.",
        "Toute alternative est vite soupçonnée de laxisme."]),
    L("CINQ PISTES", "Les alternatives", [
        "Coopérative : conseil d'élèves, règlement coconstruit.",
        "Positive : cadre ferme et bienveillant, conséquences logiques.",
        "Compétences psychosociales : décider, communiquer, coopérer, gérer sa colère.",
        "Restaurative : réparer les dommages et rétablir le lien."]),
    L("LE FIL COMMUN", "Du contrôle à la responsabilisation", [
        "Passer du contrôle par la peur à la responsabilisation, à la réparation et au lien.",
        "Sans renoncer au cadre : alternative ne veut pas dire absence de limites.",
        "Les compétences psychosociales demandent de la durée : au moins dix heures par an, sur plusieurs années."]),
    L("DISCIPLINE POSITIVE", "Naturelle ou logique ?", [
        "Conséquence naturelle : la suite directe de l'acte.",
        "Conséquence logique : en rapport avec l'acte, annoncée, respectueuse.",
        "Chercher des solutions avec l'élève plutôt que punir."]),
    L("ATTENTION", "Les limites", [
        "Médiation ou restauration ne conviennent pas au harcèlement.",
        "C'est un plaidoyer : l'effet dépend de la mise en œuvre et de l'adhésion des équipes.",
        "Préciser la source des chiffres d'enquête avant de les citer."]),
    L("LE RÔLE DU CPE", "Pour le jury", [
        "Revoir avec l'équipe l'échelle des punitions et sanctions, une réponse graduée (C2, M6).",
        "Mesures de responsabilisation et de réparation, commission éducative.",
        "Question probable : « Vous supprimez les punitions ? » Réponse : non, un cadre ferme, une réponse graduée."]),
    cta(GEN)],
    "Une lecture de la bibliographie 2026 : L'impasse de la punition à l'école, sous la direction d'Éric Debarbieux (2e édition, 2022). Le constat (une punition massive et vécue comme injuste), cinq alternatives (discipline coopérative, discipline positive, compétences psychosociales, approche de Palo Alto, communication non violente et justice restaurative), le fil commun de la responsabilisation, et les limites à garder en tête. Le rôle du CPE : repenser punitions et sanctions, règlement intérieur et commission éducative, en réponse graduée. Chiffres à vérifier dans le livre avant de les citer. Toutes celles et ceux qui préparent le concours, enregistrez ce post pour vos révisions. Quelle alternative à la punition te paraît la plus réaliste dans un établissement ? Dis-le en commentaire. Lien en bio.",
    "#bibliographie2026 #debarbieux #discipline")

# 17 déc : Bidar-Meirieu
add("2026-12-17", "biblio-bidar-meirieu", None, "s16", [
    cover("BIBLIOGRAPHIE 2026", "Grandir en humanité", "Bidar et Meirieu, Autrement, 2022", "Lire", 100),
    L("L'OUVRAGE", "Un dialogue par lettres", [
        "Un philosophe, Abdennour Bidar, et un pédagogue, Philippe Meirieu.",
        "Une question : comment aider chacun, élève comme adulte, à devenir pleinement humain ?",
        "Constat : individualisme, repli identitaire, institutions qui ne font plus autorité d'elles-mêmes."]),
    L("LE CAP", "Grandir en humanité", [
        "L'école ne se réduit pas à instruire : elle aide à se développer tout entier (pensée, sensibilité, engagement).",
        "Accepter l'altérité sous trois formes : la nature, autrui, soi-même.",
        "Devenir sujet plutôt que se conformer."]),
    L("LA MÉTHODE", "De l'imposé au proposé", [
        "Passer de la contrainte à la libération des initiatives.",
        "Apprendre par la confrontation : débat, recherche et projet collectifs (conflit sociocognitif).",
        "Avec un adulte exigeant, qui tient le cadre."]),
    L("LE COLLECTIF", "Les équipes, moteur du changement", [
        "Les équipes changent l'école si la hiérarchie leur reconnaît de l'autonomie et les accompagne.",
        "La liberté pédagogique se construit à plusieurs.",
        "L'État fixe les objectifs, accompagne, vérifie."]),
    L("REPÈRES", "À savoir citer", [
        "Korczak : l'enfant est à la fois inachevé et complet.",
        "Pestalozzi : tête, cœur et mains.",
        "Claparède : la révolution copernicienne de l'école, l'enfant au centre.",
        "Droits de l'enfant : être protégé, mais aussi s'exprimer et s'associer."]),
    L("LE RÔLE DU CPE", "Pour le jury", [
        "Former les délégués et leur confier de vrais projets (C6) ; installer médiation et tutorat.",
        "Associer la vie scolaire au projet éducatif (CC10) ; organiser des débats réglés en heure de vie de classe.",
        "Piège : c'est un essai, pas un guide pratique. Ne pas opposer autorité et liberté."]),
    cta(GEN)],
    "Une lecture de la bibliographie 2026 : Grandir en humanité, dialogue entre Abdennour Bidar et Philippe Meirieu (Autrement, 2022). Le cap (aider chacun à devenir pleinement humain), la méthode (de l'imposé au proposé, la confrontation comme moteur d'apprentissage), le rôle des équipes, et des repères à citer (Korczak, Pestalozzi, Claparède). Le rôle du CPE : former les délégués, confier de vrais projets, associer la vie scolaire au projet éducatif. Formules et attributions à vérifier dans le livre avant de les citer. Toutes celles et ceux qui préparent le concours, enregistrez ce post pour vos révisions. Quelle phrase de ce livre pourrais-tu glisser dans une copie ? Dis-le en commentaire. Lien en bio.",
    "#bibliographie2026 #bidar #meirieu")

# 18 déc : Duru-Bellat et Dubet
add("2026-12-18", "biblio-duru-bellat-dubet", None, "s11", [
    cover("BIBLIOGRAPHIE 2026", "Sauver la démocratie ?", "Duru-Bellat et Dubet, Seuil, 2020", "Lire", 100),
    L("LA THÈSE", "Trois promesses tenues à moitié", [
        "Plus de justice, plus de compétences et de croissance, plus de confiance dans la démocratie.",
        "Bilan nuancé : favorable aux vainqueurs de la compétition scolaire, moins aux vaincus.",
        "L'égalité des chances ne suffit pas."]),
    L("DÉMOCRATISER ?", "La distillation continue", [
        "L'accès s'est ouvert : de 2,4 % de bacheliers en 1900 à 80 % en 2020 (chiffres de l'ouvrage).",
        "Mais les élèves sont triés au fil du parcours : filières, options.",
        "L'origine sociale pèse toujours."]),
    L("L'ÉCOLE N'EST PAS NEUTRE", "Ce que fait l'établissement", [
        "Attentes et biais d'évaluation des enseignants.",
        "Composition des classes et des établissements.",
        "Orientation et stratégies des familles.",
        "Selon son organisation, l'école réduit ou aggrave les inégalités."]),
    L("UNE ÉPREUVE PERSONNELLE", "L'échec, vécu seul", [
        "Dans l'école de masse, l'échec est vécu comme un échec individuel.",
        "Perte d'estime de soi, désengagement, attitudes anti-scolaires.",
        "La méritocratie fait du diplôme le reflet de la valeur des personnes."]),
    L("NUANCER", "Ne pas conclure trop vite", [
        "Ne pas dire que la massification a échoué : les inégalités ont aussi reculé.",
        "L'école ne peut pas, seule, « sauver » la démocratie.",
        "Chiffres de la fin des années 2010 : préciser source et date."]),
    L("LE RÔLE DU CPE", "Pour le jury", [
        "Accompagner l'orientation pour éviter l'orientation par l'échec ; repérer le décrochage.",
        "Faire vivre les instances d'élèves (C6) ; veiller aux biais dans les décisions de sanction (C2).",
        "Associer les familles éloignées de l'école (CC12)."]),
    cta(GEN)],
    "Une lecture de la bibliographie 2026 : L'école peut-elle sauver la démocratie ?, de Marie Duru-Bellat et François Dubet (Seuil, 2020). Les trois promesses de la massification et leur bilan nuancé, la distillation continue, ce que l'établissement fait (ou défait) aux inégalités, l'échec vécu comme épreuve personnelle, et les nuances à garder à l'écrit. Le rôle du CPE : accompagner l'orientation, repérer le décrochage, faire vivre les instances d'élèves, veiller aux biais dans les sanctions, associer les familles éloignées. Chiffres à vérifier dans le livre avant de les citer. Toutes celles et ceux qui préparent le concours, enregistrez ce post pour vos révisions. Selon toi, où l'établissement peut-il le plus réduire les inégalités ? Dis-le en commentaire. Lien en bio.",
    "#bibliographie2026 #dubet #inegalites")

# 19 déc : Jellab-Marsollier
add("2026-12-19", "biblio-jellab-marsollier", None, "s13", [
    cover("BIBLIOGRAPHIE 2026", "Bienveillance", "Jellab et Marsollier (dir.), 2018", "Lire", 120),
    L("L'OUVRAGE", "Une école humaine et exigeante", [
        "Ouvrage collectif sous la direction d'Aziz Jellab et Christophe Marsollier (Berger-Levrault, 2018).",
        "Thèse : la bienveillance n'est ni du laxisme ni un effet de mode, c'est une posture éthique et professionnelle qui s'apprend."]),
    L("LE PARADOXE", "Bienveillance ou exigence ?", [
        "Depuis 2012, le bien-être est reconnu comme facteur de climat et de réussite.",
        "Mais la bienveillance passe pour du laxisme.",
        "Elle est un « care » au service du pouvoir d'agir : elle protège les élèves vulnérables sans réduire l'exigence."]),
    L("TROIS CONDITIONS", "Une école bienveillante", [
        "Prendre conscience du pouvoir de l'école sur le devenir des élèves.",
        "Être attentif au rapport au savoir.",
        "Soigner l'évaluation."], True),
    L("JUSTICE", "Des règles et sanctions justes", [
        "30 % des collégiens disent ne pas être traités avec justice par leurs professeurs, contre 19 % dans l'OCDE (chiffres de l'ouvrage).",
        "Règles et sanctions doivent être justes et expliquées.",
        "Une contrainte n'est pas forcément injuste."]),
    L("ATTENTION", "Les limites", [
        "Ne pas réduire la bienveillance à la gentillesse.",
        "La critique d'une injonction managériale existe.",
        "Les expériences citées (Motiv'action, Spark, classes bien-être) sont rapportées par leurs porteurs : pas des preuves générales."]),
    L("LE RÔLE DU CPE", "Pour le jury", [
        "Expliquer chaque sanction et la relier au règlement (C2) ; mettre des mots sur une situation vécue comme injuste.",
        "Proposer un référent à un élève en risque de décrochage ; former les équipes (CC10, M6).",
        "Question probable : que répondre à un enseignant qui y voit du laxisme ?"]),
    cta(GEN)],
    "Une lecture de la bibliographie 2026 : Bienveillance et bien-être à l'école, sous la direction d'Aziz Jellab et Christophe Marsollier (Berger-Levrault, 2018). Une posture éthique et professionnelle qui s'apprend, trois conditions d'une école bienveillante, la justice des règles et des sanctions, et les limites à connaître (pas de gentillesse molle, expériences rapportées par leurs porteurs). Le rôle du CPE : expliquer chaque sanction, proposer un référent à un élève fragile, former les équipes. Chiffres à vérifier dans le livre avant de les citer. Toutes celles et ceux qui préparent le concours, enregistrez ce post pour vos révisions. Que répondrais-tu à un collègue qui voit de l'angélisme dans la bienveillance ? Dis-le en commentaire. Lien en bio.",
    "#bibliographie2026 #bienveillance #climatscolaire")

# 20 déc : quiz bilan
add("2026-12-20", "quiz-bilan", None, "s7", [
    cover("QUIZ DU DIMANCHE", "3 questions, 3 fiches", "Teste ta semaine", "Quiz", 100),
    Q("Qui recrute les assistants d'éducation et signe leurs contrats ?",
      ["Le conseiller principal d'éducation", "Le chef d'établissement", "Le recteur d'académie"]),
    A("B", "Le chef d'établissement", [
        "Après délibération du CA (fiche 27).",
        "Le CPE, lui, organise et anime l'équipe de vie scolaire (M7)."]),
    Q("Combien d'éco-délégués, au moins, siègent au CVC ou au CVL ?", ["1", "2", "5"]),
    A("B", "Au moins deux", [
        "Circulaire du 27 août 2019 : un éco-délégué par classe, deux au CVC et au CVL (fiche 30).",
        "Le CPE organise leur élection et leur formation (C6)."]),
    Q("Quelle collectivité a la charge des lycées ?", ["Le département", "La région", "La commune"]),
    A("B", "La région", [
        "Département : collèges. Commune : écoles (fiche 3).",
        "Le CPE s'adresse à la collectivité pour les bâtiments et la restauration."]),
    cta(GEN)],
    "Quiz du dimanche : trois questions pour tester ta semaine (qui recrute les assistants d'éducation, combien d'éco-délégués au CVC et au CVL, quelle collectivité a la charge des lycées). Chaque réponse est reliée à une mission du CPE : animer l'équipe (M7), organiser la participation (C6), dialoguer avec la collectivité. Combien de bonnes réponses ? Dis-le en commentaire. Les fiches 27, 30 et 3 sont sur Prep'CPE. Lien en bio.",
    "#quiz #bilan")

# 21 déc : Petiot-Visioli
add("2026-12-21", "biblio-petiot-visioli", None, "s15", [
    cover("BIBLIOGRAPHIE 2026", "Les émotions", "Petiot et Visioli, De Boeck, 2022", "Lire", 120),
    L("L'OUVRAGE", "Une école des émotions", [
        "Oriane Petiot et Jérôme Visioli (De Boeck, 2022).",
        "L'élève n'est pas seulement un apprenant : le rapport au savoir a une dimension affective.",
        "Longtemps vues comme perturbatrices, les émotions sont une ressource pour l'engagement et une finalité de l'école."]),
    L("COMPRENDRE", "Qu'est-ce qu'une émotion ?", [
        "Une réaction soudaine et spontanée à un événement précis, à distinguer de l'humeur, du stress ou du bien-être.",
        "Cinq composantes : réactions physiologiques, comportements expressifs, évaluations cognitives, sentiments subjectifs, tendances à l'action."]),
    L("L'ENJEU", "Plus de la moitié du temps éveillé", [
        "Enfants et adolescents passent plus de 50 % de leur temps éveillé à l'école.",
        "Les émotions nourrissent attention et mémorisation.",
        "Il faut éviter les « chagrins d'école » (Pennac)."]),
    L("INTELLIGENCE ÉMOTIONNELLE", "Quatre dimensions", [
        "Conscience de soi.",
        "Maîtrise de soi.",
        "Conscience sociale : empathie, gestion des conflits.",
        "Aptitudes sociales de communication."], True),
    L("ÉVALUER, EXIGER", "À visage humain", [
        "L'évaluation est vécue comme un jugement sur soi.",
        "Évaluation formative ou par capitalisation : la note ne peut plus régresser.",
        "La bienveillance ne s'oppose pas à l'autorité.",
        "Les adultes aussi ont des émotions : travail émotionnel, risque d'épuisement."]),
    L("LE RÔLE DU CPE", "Pour le jury", [
        "Écouter et aider à nommer les émotions lors d'un conflit ; développer les compétences psychosociales (conseils d'élèves, médiation).",
        "Soutenir les AED et les collègues après une agression : temps de parole (CC10, M6).",
        "Limite : l'ouvrage vise surtout les enseignants, la vie scolaire y est peu présente."]),
    cta(GEN)],
    "Une lecture de la bibliographie 2026 : Les émotions en contexte scolaire, d'Oriane Petiot et Jérôme Visioli (De Boeck, 2022). Ce qu'est une émotion (cinq composantes), pourquoi l'enjeu est majeur (plus de 50 % du temps éveillé à l'école), les quatre dimensions de l'intelligence émotionnelle, l'évaluation à visage humain et les émotions des adultes. Le rôle du CPE : aider à nommer les émotions, développer les compétences psychosociales, soutenir les équipes après un événement difficile. Chiffres à vérifier dans le livre avant de les citer. Toutes celles et ceux qui préparent le concours, enregistrez ce post pour vos révisions. Comment accueillerais-tu la colère d'un élève après une sanction ? Dis-le en commentaire. Lien en bio.",
    "#bibliographie2026 #emotions #competencespsychosociales")

# 22 déc : Galand
add("2026-12-22", "biblio-galand", None, "s12", [
    cover("BIBLIOGRAPHIE 2026", "Harcèlement : mythes", "Benoît Galand, Retz, 2021", "Lire", 100),
    L("L'OUVRAGE", "Dix idées reçues, confrontées à la recherche", [
        "Définition : un déséquilibre de pouvoir, très peu de réciprocité, dans une dynamique de groupe où les témoins comptent.",
        "Ampleur : selon les études, 10 à 30 % des élèves sont ou ont été victimes de harcèlement ou de cyberharcèlement."]),
    L("IDÉES REÇUES · 1/2", "Faux !", [
        "« C'est un conflit entre deux élèves » : non, il y a déséquilibre et groupe.",
        "« Les filles sont plus touchées » : non, même proportion de victimes.",
        "« C'est un phénomène d'adolescence » : la proportion baisse au cours de la scolarité obligatoire."]),
    L("IDÉES REÇUES · 2/2", "Faux aussi !", [
        "« Ça forge le caractère » : non, détresse et risques pour la santé.",
        "« Les harceleurs sont des jeunes en souffrance » : rarement, ils gagnent pouvoir et statut dans le groupe.",
        "« C'est lié à l'origine sociale ou ethnique » : peu, voire pas du tout."]),
    L("CYBERHARCÈLEMENT", "Un prolongement", [
        "Moins répandu que le harcèlement en face-à-face, aux causes et conséquences proches.",
        "Possible 24 heures sur 24.",
        "Prévenir seulement le cyber n'a guère de sens."]),
    L("CE QUI MARCHE", "Et ce qui ne marche pas", [
        "Repérage, recadrage ferme et immédiat de l'auteur, prévention collective associant les familles.",
        "L'absence de réaction aggrave le harcèlement.",
        "Pas de protocole unique appliqué automatiquement."]),
    L("LE RÔLE DU CPE", "Pour le jury", [
        "Repérer avec les AED, protéger la victime, recadrer et sanctionner de façon éducative, mobiliser les témoins, informer les familles (C2, M6, CC10, CC12).",
        "Piège : proposer une médiation à une victime de harcèlement."]),
    fiche_cta(14, False)],
    "Une lecture de la bibliographie 2026 : Le harcèlement à l'école. Mythes et réalités, de Benoît Galand (Retz, 2021). Une définition claire (déséquilibre de pouvoir, dynamique de groupe), six idées reçues démontées, le cyberharcèlement comme prolongement, et ce que la recherche valide : repérage, recadrage ferme, action collective. Le rôle du CPE : repérer, protéger la victime, recadrer l'auteur, mobiliser les témoins, informer les familles. Piège classique : proposer une médiation à une victime. Pourcentages et résultats à vérifier dans le livre avant de les citer. Toutes celles et ceux qui préparent le concours, enregistrez ce post pour vos révisions. Le point de départ pratique est dans la fiche 14 de Prep'CPE. Quelle idée reçue entends-tu le plus souvent en salle des professeurs ? Dis-le en commentaire. Lien en bio.",
    "#bibliographie2026 #galand #harcelement")

# 23 déc : Haeberli
add("2026-12-23", "biblio-haeberli", None, "s9", [
    cover("BIBLIOGRAPHIE 2026", "La participation", "Haeberli, Pagoni et Maulini (dir.), 2017", "Lire", 110),
    L("L'OUVRAGE", "Effet de mode ou nécessité ?", [
        "Ouvrage collectif dirigé par Philippe Haeberli, Maria Pagoni et Olivier Maulini (L'Harmattan, 2017).",
        "Thèse : faire participer les élèves est une nécessité, mais la participation scolaire fonctionne mal : l'écart est grand entre valeurs affichées et pratiques."]),
    L("DEUX MODÈLES", "Simulacre ou affranchissement", [
        "Maintenir l'ordre par des simulacres de représentation.",
        "Ou offrir une implication citoyenne authentique.",
        "Dans les lycées enquêtés, la méfiance domine : la parole des élèves, sollicitée, n'est pas écoutée."]),
    L("CE QUE DISENT LES ÉLÈVES", "Consultés, pas aux commandes", [
        "La participation est jugée peu utile, parfois « complètement toc ».",
        "Ils ne réclament pas le pouvoir, seulement d'être consultés sur ce qui les concerne.",
        "Une minorité s'engage, souvent par intérêt (projet d'études)."]),
    L("LES DÉLÉGUÉS", "Représenter, ça a un coût", [
        "Aucune démocratie sans délégation : tous participent, certains représentent.",
        "Les délégués se sentent peu écoutés au conseil de classe et craignent un coût à s'exprimer.",
        "Enquête auprès de 668 collégiens : punitions non réglementaires, près d'un tiers évoquent un sentiment d'humiliation."]),
    L("NUANCER", "Les limites", [
        "Enquêtes anciennes (lycées enquêtés entre 1999 et 2004) et limitées.",
        "La participation ne se décrète pas, même chez les adultes.",
        "Ne pas attendre des élèves plus que des adultes."]),
    L("LE RÔLE DU CPE", "Pour le jury", [
        "Donner aux délégués un rôle précis, un retour sur les suites données, une protection contre tout coût à s'exprimer (C6).",
        "Veiller aux règles justes et légales (C2) ; connaître les élèves et leurs attentes (CC3).",
        "Liens : fiches 9, 10, 11, 12 et 16."]),
    cta(GEN)],
    "Une lecture de la bibliographie 2026 : La participation des élèves, effet de mode ou nécessité ?, sous la direction de Philippe Haeberli, Maria Pagoni et Olivier Maulini (L'Harmattan, 2017). Une nécessité qui fonctionne mal, deux modèles (simulacre ou affranchissement), ce que disent les élèves (être consultés, vraiment), la place des délégués et les limites des enquêtes citées. Le rôle du CPE : donner aux délégués un rôle précis, un retour sur les suites données et une protection. Enquêtes et chiffres à vérifier dans le livre avant de les citer. Toutes celles et ceux qui préparent le concours, enregistrez ce post pour vos révisions. Que ferais-tu pour qu'un délégué se sente vraiment écouté ? Dis-le en commentaire. Lien en bio.",
    "#bibliographie2026 #participation #delegues")

# 24 déc : vacances
add("2026-12-24", "reviser-vacances", None, "s10", [
    cover("VACANCES DE NOËL", "Bonnes fêtes", "Et un plan pour réviser sans t'épuiser", "Vacances", 120),
    L("D'ABORD", "Souffler", [
        "Le repos fait partie de la préparation : dors, marche, retrouve tes proches.",
        "Mieux vaut un créneau court et régulier qu'un marathon.",
        "Une fiche bien relue vaut mieux que cinq survolées."]),
    L("EXEMPLE DE SEMAINE", "Quatre rendez-vous", [
        "Une fiche relue, puis redite à voix haute.",
        "Un quiz de dix questions pour repérer les trous.",
        "Une situation de jury chronométrée.",
        "Une carte mentale de la semaine."], True),
    L("À L'ÉCRIT", "Un sujet par semaine", [
        "Choisis une notion : autorité, climat scolaire, participation, inégalités.",
        "Rédige l'introduction : définition, problématique, annonce du plan.",
        "Appuie-toi sur un auteur : son idée, et ce qu'elle change dans un EPLE."]),
    L("À L'ORAL", "Entraîne ta voix", [
        "Explique une fiche en deux minutes, à voix haute.",
        "Enregistre-toi, puis réécoute.",
        "Pour une situation de jury : règle de droit, geste professionnel, partenaires."]),
    L("PENSE AU TERRAIN", "Observe ton quotidien", [
        "Une récréation, un self, une heure de permanence : qu'est-ce qui s'y joue ?",
        "Note ce qu'un CPE ferait, et avec quelle compétence.",
        "Chaque observation nourrit tes copies."]),
    L("LE RÔLE DU CPE", "Le métier que tu prépares", [
        "Le CPE organise la vie scolaire, protège, écoute, fait participer, coopère.",
        "À chaque fiche : une règle de droit, un geste professionnel, un partenaire.",
        "Tu ne mémorises pas des listes : tu te prépares à agir."]),
    cta(GEN)],
    "Bonnes fêtes à toutes celles et ceux qui préparent le concours. Pendant les vacances, souffle d'abord : le repos fait partie de la préparation. Puis un petit plan pour réviser sans t'épuiser : une fiche redite à voix haute, un quiz, une situation de jury chronométrée, une carte mentale. À l'écrit, un sujet par semaine (définition, problématique, un auteur). À l'oral, entraîne ta voix. Et reste attentif ou attentive au terrain : chaque observation nourrit tes copies. Le CPE que tu prépares à devenir organise, protège, écoute, fait participer, coopère. Quel est ton rendez-vous de révision pendant les vacances ? Dis-le en commentaire. Lien en bio.",
    "#vacances #methode #bonnesfetes")

# 25 déc : Noël, 10 notions
add("2026-12-25", "noel-10-notions", 31, "s11", [
    cover("JOYEUX NOËL · FICHE 31", "10 notions en une phrase", "Un cadeau de révision", "Noël", 100),
    L("NOTIONS 1 ET 2", "Autorité, sanction éducative", [
        "Autorité : pouvoir reconnu comme légitime, qui obtient l'obéissance sans force ni persuasion (Arendt, Marcelli, Prairat).",
        "Sanction éducative : réponse à un manquement qui vise un acte, la réparation et la réintégration (Prairat)."]),
    L("NOTIONS 3 ET 4", "Bienveillance, climat scolaire", [
        "Bienveillance : attention portée à l'élève et à ses besoins, compatible avec l'exigence (Jellab et Marsollier).",
        "Climat scolaire : qualité de vie et de relations perçue dans l'établissement (Debarbieux, Cohen)."]),
    L("NOTIONS 5 ET 6", "Harcèlement, décrochage", [
        "Harcèlement : violence répétée, intentionnelle, avec déséquilibre des forces (Olweus, Galand, Catheline).",
        "Décrochage : processus de désengagement aboutissant à une sortie sans diplôme (Bernard et Michaut)."]),
    L("NOTIONS 7 ET 8", "Égalité des chances, inclusion", [
        "Égalité des chances : égalité d'accès aux positions selon le mérite, critiquée car elle légitime les inégalités (Dubet, Duru-Bellat).",
        "Inclusion : l'école s'adapte à chaque élève, contre l'intégration où l'élève s'adapte (Ebersold, Garnier et al.)."]),
    L("NOTIONS 9 ET 10", "Coéducation, participation", [
        "Coéducation : partage de la responsabilité éducative entre école et familles (Auduc, Périer).",
        "Participation : prise de part réelle des élèves aux décisions qui les concernent (Bozec, Haeberli et al., Condette)."]),
    L("LE RÔLE DU CPE", "Relier à la fonction", [
        "Chaque notion renvoie à une mission : autorité et sanction (C2), climat (M6), participation (C6), coéducation (CC12).",
        "En introduction : définir, problématiser. À l'oral : une définition, puis un exemple de terrain.",
        "Joyeux Noël à toutes celles et ceux qui préparent le concours."]),
    cta(["La fiche 31 complète, avec quiz,", "situation de jury et audio, gratuite"])],
    "Joyeux Noël ! Un petit cadeau de révision : dix notions à définir en une phrase, avec les auteurs à associer (autorité, sanction éducative, bienveillance, climat scolaire, harcèlement, décrochage, égalité des chances, inclusion, coéducation, participation). Une définition bien posée en introduction structure toute la copie, et à l'oral elle ouvre sur un exemple de terrain. Le rôle du CPE : chaque notion renvoie à une mission (C2, M6, C6, CC12). Toutes celles et ceux qui préparent le concours, enregistrez ce post pour vos révisions. Tout est dans la fiche 31 de Prep'CPE, avec le quiz et une situation de jury. Quelle notion as-tu le plus de mal à définir ? Dis-le en commentaire. Lien en bio.",
    "#noel #notions #sciencesdeleducation")

if __name__ == "__main__":
    path = os.path.join(HERE, "posts_carrousel.json")
    cur = [p for p in json.load(open(path, encoding="utf-8")) if not p["slug"].startswith(("2026-12-06", "2026-12-07", "2026-12-08", "2026-12-09", "2026-12-1", "2026-12-2"))]
    json.dump(cur + P, open(path, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(len(P), "posts ajoutés ;", P[0]["slug"], "->", P[-1]["slug"])
    for p in P:
        assert len(p["slides"]) == 8, p["slug"]
        assert p["styles"][0] == p["style"]
