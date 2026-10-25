"""Build a TV+ channel catalog and an M3U from independently verified official streams.
Run: python build_playlist.py
No TV+ account, token, cookie, DRM license, or private API is used.
"""
import html
import json
import re
import unicodedata
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SOURCE = 'https://tvplus.com.tr/destek/sss/tvplus-kanallari'

def normalize(name):
    name = name.translate(str.maketrans({'ı':'i','İ':'I','ü':'u','Ü':'U','ö':'o','Ö':'O','ş':'s','Ş':'S','ç':'c','Ç':'C','ğ':'g','Ğ':'G','î':'i','Î':'I'}))
    return re.sub(r'[^a-z0-9]', '', unicodedata.normalize('NFKD', name).lower())

def build():
    with urllib.request.urlopen(SOURCE, timeout=30) as response:
        page = response.read().decode('utf-8')
    streams = json.loads((ROOT / 'official_streams.json').read_text(encoding='utf-8'))
    by_name = {normalize(s['name']): s for s in streams}
    channels = []
    for row in re.findall(r'<tr\b[^>]*>(.*?)</tr>', page, re.S):
        cells = re.findall(r'<td\b[^>]*>(.*?)</td>', row, re.S)
        if len(cells) != 3:
            continue
        number = re.sub('<[^>]+>', '', cells[0]).strip()
        link = re.search(r'href="([^"]+)"', cells[2])
        name = html.unescape(re.sub('<[^>]+>', '', cells[2])).strip()
        if not number.isdigit() or not link or not name:
            continue
        stream = by_name.get(normalize(name))
        channels.append({'number': int(number), 'name': name,
            'tvplus_page': 'https://tvplus.com.tr' + html.unescape(link.group(1)),
            'm3u_available': stream is not None,
            'official_stream': stream['url'] if stream else None,
            'status': 'verified_official_stream' if stream else 'no_verified_direct_stream'})
    if not channels:
        raise RuntimeError('No channel rows found; inspect the source before replacing outputs.')
    channels.sort(key=lambda c: c['number'])
    (ROOT / 'tvplus_channels.json').write_text(json.dumps({'source': SOURCE, 'channels': channels}, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    numbers = {normalize(c['name']): c['number'] for c in channels}
    lines = ['#EXTM3U', '# Independent official streams; TV+ catalog is metadata only.']
    for s in sorted(streams, key=lambda s: numbers.get(normalize(s['name']), 9999)):
        if not s['url'].startswith('https://') or not s.get('source'):
            raise ValueError('Only sourced HTTPS streams are accepted.')
        number = numbers.get(normalize(s['name']))
        attr = f' tvg-chno="{number}"' if number is not None else ''
        lines += [f"# Source: {s['source']} | Verified: {s['verified_on']}",
            f'#EXTINF:-1 group-title="{s["group"]}"{attr},{s["name"]}', s['url']]
    (ROOT / 'playlist.m3u').write_text('\n'.join(lines) + '\n', encoding='utf-8')
    print(f'Catalog: {len(channels)} channels; M3U: {len(streams)} official streams; matched: {sum(c["m3u_available"] for c in channels)}')

if __name__ == '__main__':
    build()
