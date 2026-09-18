# nft-floor-watcher

I got tired of manually reloading OpenSea tabs to check floor prices, and I didn't want to use a bloated commercial Discord bot. This is a dead-simple script that polls OpenSea and pings a Discord or Telegram webhook when a floor price drops below your target.

It saves its last-seen state in a local JSON file so it won't spam you with duplicate notifications for the same price level.

## Installation

Requires Python 3.10+.

```cmd
pip install -r requirements.txt
```

## Usage

You need an OpenSea API key (set as `OPENSEA_API_KEY` environment variable).

```cmd
set OPENSEA_API_KEY=your_key_here

python watcher.py --slug pudgypenguins --target 12.5 --discord-webhook https://discord.com/api/webhooks/...
```

Options:

* `--slug`: The OpenSea collection slug (from the URL).
* `--target`: Notify only if the floor goes below this value (in ETH).
* `--interval`: Polling interval in seconds (default is 300).
* `--discord-webhook`: URL of your Discord webhook channel.
* `--telegram-token` / `--telegram-chat`: For Telegram notifications instead of Discord.

To run it in the background on Windows, you can use a simple batch file or run it inside a terminal window.

<!-- last-checked: 2026-09-18 -->
