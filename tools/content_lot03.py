"""Lot 3 : 10 Reels « démarrage » sans date, publiables d'un coup (textes issus des fiches Prep'CPE)."""
import json
from content import cta, H

M = lambda bpm, root, prog, seed, lead=True: dict(bpm=bpm, root=root, prog=prog, seed=seed, lead=lead)
COVER_Q = lambda f, t: dict(kind="cover", kicker=f"QUIZ CPE · FICHE {f}", title=t, note="Une question, une réponse")

def quiz(n, f, style, music, title, options, letter, rtitle, rlines, caption, tags):
    return dict(n=n, kind="Quiz", fiche=f, style=style, music=music, slides=[
        COVER_Q(f, "Teste-toi en 20 secondes"),
        dict(kind="quiz", kicker="LA QUESTION", title=title, options=options),
        dict(kind="answer", kicker="LA RÉPONSE", letter=letter, title=rtitle, lines=rlines),
        cta(f)], caption=caption + "\n\n" + H + " #quiz " + tags)

POSTS = [
    dict(n=1, kind="Parcours", fiche=None, style="s1", music=dict(**{'bpm': 84, 'root': 57, 'prog': 'maj_a', 'kick': 'half', 'hats': 1, 'arp': 8, 'bass': 'root', 'dens': 0.6, 'seed': 201}),
         slides=[dict(kind="cover", kicker="RÉVISIONS CPE", title="Par où commencer ses révisions ?"),
                 dict(kind="list", kicker="LES 4 PREMIÈRES FICHES", title="Pose les bases",
                      lines=["Fiche 1 : le statut et les missions du CPE", "Fiche 2 : le référentiel de compétences", "Fiche 4 : l'EPLE et ses instances", "Fiche 7 : valeurs de la République et laïcité"], numbered=True),
                 dict(kind="list", kicker="ENSUITE", title="Une fiche, un quiz, un audio",
                      lines=["Lis la fiche.", "Teste-toi avec le quiz.", "Réécoute l'audio dans les transports."]),
                 cta()],
         caption="Par où commencer ses révisions pour le concours de CPE ? Les 4 premières fiches : le statut et les missions, le référentiel de compétences, l'EPLE et ses instances, les valeurs de la République et la laïcité. Chaque fiche a son quiz et son audio sur Prep'CPE, gratuit. Lien en bio.\n\n" + H + " #revisions"),
    quiz(2, 4, "s2", dict(**{'bpm': 72, 'root': 62, 'prog': 'min_a', 'kick': 'none', 'hats': 0, 'arp': 8, 'bass': 'root', 'dens': 0.5, 'keys': True, 'seed': 202}), "Combien de membres compte le CA d'un lycée ?", ["24", "30", "14"], "B", "30 membres",
         ["30 membres en lycée et en collège de plus de 600 élèves ou avec SEGPA.", "24 dans les autres collèges et en EREA."],
         "Quiz CPE : combien de membres compte le conseil d'administration d'un lycée ? A, B ou C ? Réponds en commentaire. La composition du CA et les autres instances de l'EPLE sont dans la fiche 4 de Prep'CPE. Lien en bio.", "#eple #ca"),
    quiz(3, 5, "s3", dict(**{'bpm': 78, 'root': 52, 'prog': 'maj_b', 'kick': 'broken', 'hats': 1, 'arp': 0, 'bass': 'sync', 'keys': True, 'seed': 203}), "Pour quelle durée le projet d'établissement est-il adopté ?", ["Trois à cinq ans", "Un an", "Dix ans"], "A", "Trois à cinq ans",
         ["Il est adopté par le conseil d'administration.", "Il fixe les objectifs de l'établissement, et le CPE y a toute sa part."],
         "Quiz CPE : pour quelle durée le projet d'établissement est-il adopté ? A, B ou C ? Réponds en commentaire. Tout sur le projet d'établissement dans la fiche 5 de Prep'CPE. Lien en bio.", "#projetdetablissement"),
    dict(n=4, kind="Fiche", fiche=13, style="s4", music=dict(**{'bpm': 90, 'root': 59, 'prog': 'maj_c', 'kick': 'half', 'hats': 2, 'arp': 16, 'bass': 'sync', 'dens': 0.5, 'seed': 204}),
         slides=[dict(kind="cover", kicker="CLIMAT SCOLAIRE · FICHE 13", title="Les 7 facteurs d'un bon climat scolaire"),
                 dict(kind="list", kicker="LES 7 FACTEURS DU MINISTÈRE", title="Pour agir sur le climat scolaire",
                      lines=["Une stratégie d'équipe", "Une justice scolaire", "La prévention des violences", "Une pédagogie et une coopération", "La coéducation", "Les partenariats", "La qualité de vie"], small=True),
                 dict(kind="list", kicker="LE RÔLE DU CPE", title="Mission M6",
                      lines=["Contribuer à la qualité du climat scolaire : c'est l'une des 7 missions du CPE."], numbered=False),
                 cta(13)],
         caption="Les 7 facteurs d'un bon climat scolaire retenus par le ministère : stratégie d'équipe, justice scolaire, prévention des violences, pédagogie et coopération, coéducation, partenariats, qualité de vie. Un grand classique des écrits et de l'oral. Fiche 13 sur Prep'CPE. Lien en bio.\n\n" + H + " #climatscolaire"),
    quiz(5, 19, "s1", dict(**{'bpm': 70, 'root': 60, 'prog': 'maj_a', 'kick': 'none', 'hats': 0, 'arp': 4, 'bass': 'off', 'dens': 0.9, 'start': 1, 'seed': 205}), "À partir de quel seuil d'absences non justifiées faut-il engager un dialogue avec la famille ?",
         ["Deux demi-journées dans le trimestre", "Dix demi-journées dans l'année", "Quatre demi-journées dans le mois"], "C", "Quatre demi-journées dans le mois",
         ["Le chef d'établissement engage le dialogue et réunit l'équipe éducative.", "Article L. 131-8 du Code de l'éducation."],
         "Quiz CPE : à partir de quel seuil d'absences non justifiées le chef d'établissement doit-il engager un dialogue avec la famille ? A, B ou C ? Réponds en commentaire. Absentéisme et assiduité : fiche 19 de Prep'CPE. Lien en bio.", "#absenteisme #assiduite"),
    quiz(6, 8, "s2", dict(**{'bpm': 80, 'root': 55, 'prog': 'min_b', 'kick': 'half', 'hats': 1, 'arp': 8, 'bass': 'root', 'dens': 0.45, 'seed': 206}), "Qui peut être saisi par toute personne victime de discrimination ?",
         ["Le médiateur académique", "Le Défenseur des droits", "Le CDEN"], "B", "Le Défenseur des droits",
         ["L'article 225-1 du Code pénal liste les critères de discrimination prohibés."],
         "Quiz CPE : qui peut être saisi par toute personne victime de discrimination ? A, B ou C ? Réponds en commentaire. Discriminations et égalité : fiche 8 de Prep'CPE. Lien en bio.", "#discriminations #egalite"),
    quiz(7, 2, "s3", dict(**{'bpm': 88, 'root': 57, 'prog': 'min_a', 'kick': 'four', 'hats': 1, 'arp': 8, 'bass': 'sync', 'dens': 0.55, 'seed': 207}), "Combien de compétences communes à tous les professeurs et personnels d'éducation compte le référentiel ?",
         ["8", "10", "14"], "C", "14 compétences communes",
         ["CC1 à CC14 sont communes.", "C1 à C8 sont spécifiques aux CPE."],
         "Quiz CPE : combien de compétences communes à tous les professeurs et personnels d'éducation compte le référentiel ? A, B ou C ? Réponds en commentaire. Le référentiel de compétences est détaillé dans la fiche 2 de Prep'CPE. Lien en bio.", "#referentiel"),
    dict(n=8, kind="Fiche", fiche=17, style="s4", music=dict(**{'bpm': 66, 'root': 56, 'prog': 'min_b', 'kick': 'none', 'hats': 1, 'arp': 0, 'bass': 'root', 'keys': True, 'seed': 208}),
         slides=[dict(kind="cover", kicker="FICHE 17", title="Commission éducative ou conseil de discipline ?"),
                 dict(kind="compare", kicker="LA DIFFÉRENCE", title="Deux instances, deux logiques",
                      left=("COMMISSION ÉDUCATIVE", ["Instance éducative (R. 511-19-1)", "Aucune sanction", "Procédure souple, dialogue", "Faire comprendre, prévenir la récidive"]),
                      right=("CONSEIL DE DISCIPLINE", ["Instance disciplinaire", "Toutes sanctions, dont l'exclusion définitive", "Procédure contradictoire", "Sanctionner un manquement grave"])),
                 dict(kind="list", kicker="À RETENIR", title="La commission n'est pas l'antichambre du conseil",
                      lines=["Elle cherche une réponse éducative personnalisée.", "Elle compte au moins un professeur et un parent."], numbered=False),
                 cta(17)],
         caption="Commission éducative ou conseil de discipline ? L'une cherche une réponse éducative personnalisée sans prononcer de sanction, l'autre sanctionne un manquement grave. La commission n'est pas l'antichambre du conseil de discipline. Fiche 17 sur Prep'CPE. Lien en bio.\n\n" + H + " #sanctions #justicescolaire"),
    dict(n=9, kind="Fiche", fiche=20, style="s1", music=dict(**{'bpm': 76, 'root': 64, 'prog': 'maj_c', 'kick': 'half', 'hats': 0, 'arp': 16, 'bass': 'off', 'dens': 0.35, 'start': 1, 'seed': 209}),
         slides=[dict(kind="cover", kicker="DÉCROCHAGE · FICHE 20", title="Décrochage scolaire : les repères à connaître"),
                 dict(kind="list", kicker="L'OBLIGATION DE FORMATION", title="De 16 à 18 ans",
                      lines=["Loi du 26 juillet 2019, en vigueur depuis la rentrée 2020.", "Études, apprentissage, emploi, service civique ou accompagnement.", "Les missions locales contrôlent son respect."], numbered=False),
                 dict(kind="list", kicker="DANS L'ÉTABLISSEMENT", title="Le GPDS",
                      lines=["Groupe de prévention du décrochage scolaire.", "Piloté par le chef d'établissement, avec un référent décrochage.", "Le CPE y repère les signaux faibles."], numbered=False),
                 dict(kind="list", kicker="UN CHIFFRE", title="Sortants précoces",
                      lines=["7,6 % des 18-24 ans en France en 2023 (objectif européen : 9 % en 2030)."], numbered=False),
                 cta(20)],
         caption="Décrochage scolaire, les repères à connaître : l'obligation de formation de 16 à 18 ans (loi du 26 juillet 2019), le GPDS dans l'établissement, et 7,6 % de sortants précoces en France en 2023. Un thème majeur des écrits. Fiche 20 sur Prep'CPE. Lien en bio.\n\n" + H + " #decrochage"),
    dict(n=10, kind="Fiche", fiche=10, style="s3", music=dict(**{'bpm': 92, 'root': 61, 'prog': 'maj_b', 'kick': 'broken', 'hats': 2, 'arp': 8, 'bass': 'sync', 'dens': 0.5, 'seed': 210}),
         slides=[dict(kind="cover", kicker="INSTANCES ÉLÈVES · FICHE 10", title="CVC ou CVL : ne plus les confondre"),
                 dict(kind="compare", kicker="COMPARATIF", title="Collège et lycée",
                      left=("CVC · COLLÈGE", ["Composition fixée par le CA", "Réunions : au moins 3 par an", "Rôle de proposition"]),
                      right=("CVL · LYCÉE", ["20 membres : 10 lycéens, 10 adultes", "Mandat de deux ans, élection directe", "Consultation obligatoire"])),
                 dict(kind="list", kicker="LE RÔLE DU CPE", title="Faire vivre les instances",
                      lines=["Organiser les élections.", "Former et accompagner les élus.", "Inscrire leurs projets dans le projet d'établissement."]),
                 cta(10)],
         caption="CVC ou CVL, ne plus les confondre : au collège, une composition fixée par le CA et un rôle de proposition ; au lycée, 20 membres dont 10 lycéens élus pour deux ans et une consultation obligatoire. Fiche 10 sur Prep'CPE. Lien en bio.\n\n" + H + " #cvl #cvc #participation"),
]

if __name__ == "__main__":
    json.dump(POSTS, open("posts.json", "w"), ensure_ascii=False, indent=1)
    print(len(POSTS), "posts")
