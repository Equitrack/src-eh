API="https://api.telegram.org/bot"
TOKEN="1420238693:AAG3X6JrQRd5TyrvV3_45mFLwgAIdyxXV6c"
CHAT_ID="-1001298945859"
MESSAGE="MensajeDePrueba"

jsonData='{"chat_id":''"'$CHAT_ID'"','"text"':'"'$MESSAGE'"','"disable_notification":true}';

curl -X POST -H '"'"Content-Type: application/json"'"' -d "'"$jsonData"'" "$API/$TOKEN/sendMessage"
