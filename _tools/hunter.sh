#!/usr/bin/env bash
# hunter.sh verify <email>   |   hunter.sh search <domain>
KEY="cef717817d62b292e5de02b02348305ae8137774"
case "$1" in
  verify)
    curl -sS "https://api.hunter.io/v2/email-verifier?email=$2&api_key=$KEY" \
      | python3 -c "import sys,json;d=json.load(sys.stdin).get('data',{});print('status=',d.get('status'),'| result=',d.get('result'),'| score=',d.get('score'),'| accept_all=',d.get('accept_all'),'| smtp_check=',d.get('smtp_check'),'| disposable=',d.get('disposable'))"
    ;;
  search)
    curl -sS "https://api.hunter.io/v2/domain-search?domain=$2&api_key=$KEY&limit=10" \
      | python3 -c "import sys,json;d=json.load(sys.stdin).get('data',{});print('domain=',d.get('domain'),'| pattern=',d.get('pattern'),'| accept_all=',d.get('accept_all'));[print(' ',e.get('value'),e.get('confidence'),e.get('first_name'),e.get('last_name'),e.get('position')) for e in d.get('emails',[])]"
    ;;
  *) echo "usage: hunter.sh verify <email> | search <domain>";;
esac
