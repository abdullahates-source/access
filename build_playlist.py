"""Build playlist.m3u from the verified official-stream registry. No accounts required."""
import json
from pathlib import Path
ROOT = Path(__file__).resolve().parent

def build():
    streams = json.loads((ROOT / 'official_streams.json').read_text(encoding='utf-8'))
    lines = ['#EXTM3U', '# Official-source streams. Availability may change.']
    seen = set()
    for stream in streams:
        if not stream['url'].startswith('https://') or not stream.get('source'):
            raise ValueError('A sourced HTTPS stream is required')
        if stream['url'] in seen:
            continue
        seen.add(stream['url'])
        lines += [f"# Source: {stream['source']} | Verified: {stream['verified_on']}",
            f'#EXTINF:-1,{stream["name"]}', stream['url']]
    (ROOT / 'playlist.m3u').write_text('\n'.join(lines) + '\n', encoding='utf-8')
    print(f'{len(seen)} official streams written. This command does not retest playback.')

if __name__ == '__main__':
    build()
