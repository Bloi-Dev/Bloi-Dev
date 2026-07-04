from pathlib import Path
import json
import urllib.request

USERNAME = "BLoiChessMobile"
API_URL = f"https://api.chess.com/pub/player/{USERNAME}/stats"

output_path = Path("assets/chess-card.svg")
output_path.parent.mkdir(exist_ok=True)

with urllib.request.urlopen(API_URL) as response:
    data = json.loads(response.read().decode())

def rating(mode):
    return data.get(mode, {}).get("last", {}).get("rating", "N/A")

rapid = rating("chess_rapid")
blitz = rating("chess_blitz")
bullet = rating("chess_bullet")
daily = rating("chess_daily")

svg = f"""<svg width="500" height="220" xmlns="http://www.w3.org/2000/svg">
  <rect width="500" height="220" rx="20" fill="#1f1f1f"/>
  <text x="30" y="50" font-size="28" fill="white" font-family="Arial">♟️ Chess.com</text>
  <text x="30" y="85" font-size="20" fill="#81B64C" font-family="Arial">@{USERNAME}</text>

  <text x="30" y="130" font-size="18" fill="white" font-family="Arial">Rapid: {rapid}</text>
  <text x="250" y="130" font-size="18" fill="white" font-family="Arial">Blitz: {blitz}</text>

  <text x="30" y="165" font-size="18" fill="white" font-family="Arial">Bullet: {bullet}</text>
  <text x="250" y="165" font-size="18" fill="white" font-family="Arial">Daily: {daily}</text>

  <text x="30" y="200" font-size="14" fill="#aaaaaa" font-family="Arial">Updated automatically with GitHub Actions</text>
</svg>
"""

output_path.write_text(svg, encoding="utf-8")
