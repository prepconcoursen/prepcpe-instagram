#!/bin/bash
# usage: pub.sh single IMG CAPTION | pub.sh carousel CAPTION IMG...
IG=17841441275723815; API=https://graph.facebook.com/v26.0
BASE=https://raw.githubusercontent.com/prepconcoursen/prepcpe-instagram/main/lot-01
j() { python3 -c "import sys,json;d=json.load(sys.stdin);print(d.get('id') or d)"; }
wait_ready() { for i in $(seq 1 20); do s=$(curl -sS "$API/$1?fields=status_code" | python3 -c "import sys,json;print(json.load(sys.stdin).get('status_code'))"); [ "$s" = FINISHED ] && return 0; sleep 3; done; echo "not ready: $s" >&2; return 1; }
if [ "$1" = single ]; then
  CID=$(curl -sS -X POST "$API/$IG/media" --data-urlencode "image_url=$BASE/$2" --data-urlencode "caption=$3" | j)
else
  CAP="$2"; shift 2; IDS=""
  for f in "$@"; do c=$(curl -sS -X POST "$API/$IG/media" --data-urlencode "image_url=$BASE/$f" --data-urlencode "is_carousel_item=true" | j); wait_ready $c || exit 1; IDS="$IDS,$c"; done
  CID=$(curl -sS -X POST "$API/$IG/media" --data-urlencode "media_type=CAROUSEL" --data-urlencode "children=${IDS#,}" --data-urlencode "caption=$CAP" | j)
fi
echo "container $CID" >&2
wait_ready $CID || exit 1
MID=$(curl -sS -X POST "$API/$IG/media_publish" --data-urlencode "creation_id=$CID" | j)
echo "media $MID"
curl -sS "$API/$MID?fields=permalink"; echo
