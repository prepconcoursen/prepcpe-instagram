# Routine Prep'CPE Instagram (publication quotidienne)

Compte : @prep_concours_cpe (IG id 17841441275723815). Jeton Page injecté par le proxy réseau (secret « Authorization » pour graph.facebook.com) : ne jamais le chercher ni l'afficher.

## Chaque jour
1. Ouvrir `lot-XX/LEGENDES.md` du lot en cours (le calendrier donne la date de chaque Reel). Prendre le Reel daté d'aujourd'hui (Europe/Paris).
2. Vérifier `PUBLISHED.log` (racine du dépôt) : si la date y figure déjà, ne rien publier.
3. Publier : `tools/publish_reel.sh lot-XX NN "<légende copiée de LEGENDES.md>"`.
4. Ajouter une ligne `AAAA-MM-JJ lot-XX NN <permalien>` à `PUBLISHED.log`, commit, push sur main.
5. Annoncer le titre du Reel et le permalien dans la réponse finale (notification à Tanguy).

## Chaque dimanche : préparer la semaine suivante
Si moins de 8 Reels restent à publier : créer le lot suivant (`lot-03`, etc.) de 7 Reels, un par jour, avec le même moteur (`tools/` : content.py, render.js, music.py, build.py ; voir lot-02 pour le format). Contenu issu des fiches du site https://prep-cpe.netlify.app, en alternant quiz, notion, méthode, repères, situation de jury, bilan ; styles s1 à s4 en alternance ; une musique lofi différente par Reel. Ne rien affirmer que les fiches ne disent pas. Générer vidéos + `LEGENDES.md` (même format que lot-02), pousser sur main.
Lot 3 : build avec LOUD=-28 (musique discrète).
Musiques ambiantes : music3.py + LOUD=-30 (lot 3).

Règle de légende (demande de Tanguy, 2026-10-29) : chaque légende se termine par une question qui invite à répondre en commentaire (avant « Lien en bio. »). Pour les nouveaux lots, respecter cette règle.

Règle de cohérence (échange avec Tanguy, 2026-10-30) : un thème par semaine, puis le thème suivant dans l'ordre des fiches, avec des formats variés (quiz, notion ou auteur, repère, situation de jury, fiche, bilan le dimanche). Les quiz de la semaine portent sur les fiches du thème, le bilan les récapitule. Pas de saut aléatoire d'une fiche à l'autre, mais pas de monotonie non plus.

Rappels d'inscription (demande de Tanguy, 2026-10-30) : en plus de la série, deux Reels `rappels/` sont publiés par des tâches planifiées dédiées le 18 novembre (J-7) et le 24 novembre (J-1) 2026 à 12 h, via `VIDEO_URL=<raw rappels/...> tools/publish_reel.sh x x "<légende>"`. Ne pas les inclure dans le calendrier quotidien.

Calendrier du lot 2 avancé d'un jour (demande de Tanguy, 2026-10-30) : le Reel 2 (Bourdieu) est publié le soir du 30 octobre à 17h49 (publication manuelle par Claude), puis un Reel par jour : le 31 octobre = Reel 3, etc. jusqu'au 11 novembre = Reel 14. Un Reel est considéré comme publié s'il figure dans PUBLISHED.log (lot et numéro) : ne jamais republier un Reel déjà au journal.

Lot 4 (2026-10-30) : 7 Reels du 12 au 18 novembre (fiche 8, discriminations), générés avec tools/content_lot04.py et la palette musicale élargie tools/music4.py (styles lofi, ambient, piano, pluck, pulse ; demande de Tanguy : varier davantage la musique d'un Reel à l'autre). Pour les prochains lots, utiliser music4.py et alterner les styles.

Musique du lot 2 refaite (2026-10-30, demande de Tanguy : varier davantage d'un Reel à l'autre) : Reels 3 à 14 remixés avec tools/remix_lot02.py (palette music4.py), vidéos muettes inchangées. Les Reels 1 et 2 étaient déjà publiés.
