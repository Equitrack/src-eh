API="https://api.telegram.org/bot"
TOKEN="1420238693:AAG3X6JrQRd5TyrvV3_45mFLwgAIdyxXV6c"
CHAT_ID='"-1001298945859"'
MESSAGE="MensajeDePrueba"

jsonData='{ "chat_id":' ','

#curl -X POST -H "Content-Type: application/json" -d $jsonData "$API/$TOKEN/sendMessage"

echo $jsonData