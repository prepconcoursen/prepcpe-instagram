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
