#!/bin/bash
# usage: publish_carrousel.sh SLUG   (ex. 2026-11-05 ou 2026-11-18-rappel-j7)
# Publie posts/auto/SLUG (images 01.jpg... + LEGENDE.md) en carrousel Instagram, sans musique. Affiche le permalien.
set -e
cd "$(dirname "$0")/.."
SLUG="$1"; DIR="posts/auto/$SLUG"
[ -d "$DIR" ] || { echo "dossier introuvable: $DIR" >&2; exit 1; }
BRANCH="${BRANCH:-claude/project-thread-ezz2z0}"
CAP="$(cat "$DIR/LEGENDE.md")"
IMGS=$(cd "$DIR" && ls [0-9][0-9].jpg)
BASE="https://raw.githubusercontent.com/prepconcoursen/prepcpe-instagram/$BRANCH/$DIR" bash tools/pub.sh carousel "$CAP" $IMGS
