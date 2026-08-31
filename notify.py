import httpx

def send_discord(url: str, collection: str, floor: float, target: float, link: str):
    payload = {
        "embeds": [{
            "title": f"🚨 Floor Alert: {collection}",
            "description": f"Floor price has dropped to **{floor} ETH** (target: {target} ETH).",
            "url": link,
            "color": 15158332
        }]
    }
    # print(f"sending payload: {payload}")
    response = httpx.post(url, json=payload, timeout=10.0)
    response.raise_for_status()

def send_telegram(token: str, chat_id: str, collection: str, floor: float, target: float, link: str):
    # TODO: tg MarkdownV2 is picky about escaping dots, HTML is safer here
    text = f"<b>🚨 Floor Alert: {collection}</b>\nFloor price is now <b>{floor} ETH</b> (target: {target} ETH).\n<a href='{link}'>View on OpenSea</a>"
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": text,
        "parse_mode": "HTML"
    }
    response = httpx.post(url, json=payload, timeout=10.0)
    response.raise_for_status()
