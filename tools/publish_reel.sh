#!/bin/bash
# usage: publish_reel.sh LOT NN "LÉGENDE"   (ex: publish_reel.sh lot-02 01 "texte")
# Publie lot-XX/prepcpe_NN.mp4 en Reel via l'API Graph (jeton injecté par le proxy réseau).
IG=17841441275723815; API=https://graph.facebook.com/v26.0
URL="${VIDEO_URL:-https://raw.githubusercontent.com/prepconcoursen/prepcpe-instagram/main/$1/prepcpe_$2.mp4}"
j() { python3 -c "import sys,json;d=json.load(sys.stdin);print(d.get('id') or d)"; }
CID=$(curl -sS -X POST "$API/$IG/media" --data-urlencode "media_type=REELS" --data-urlencode "video_url=$URL" --data-urlencode "share_to_feed=true" --data-urlencode "caption=$3" | j)
echo "container $CID" >&2
for i in $(seq 1 60); do s=$(curl -sS "$API/$CID?fields=status_code" | python3 -c "import sys,json;print(json.load(sys.stdin).get('status_code'))"); [ "$s" = FINISHED ] && break; [ "$s" = ERROR ] && { echo "ERROR container" >&2; exit 1; }; sleep 5; done
[ "$s" = FINISHED ] || { echo "timeout: $s" >&2; exit 1; }
MID=$(curl -sS -X POST "$API/$IG/media_publish" --data-urlencode "creation_id=$CID" | j)
echo "media $MID"
curl -sS "$API/$MID?fields=permalink"; echo
