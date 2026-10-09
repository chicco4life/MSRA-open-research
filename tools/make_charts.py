#!/usr/bin/env python3
"""Draw the charts in the main README from every project's sources/sources.csv.

Run from the repository folder after adding or changing a project:
    python3 tools/make_charts.py
It rewrites the SVG files in assets/charts/. No extra packages needed.
"""
import csv, html, pathlib, re

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT = ROOT / 'assets' / 'charts'
BLUE, BLUE_2, BLUE_3, BLUE_4 = '#1F59A7', '#5F8BC8', '#A9C1E3', '#DCE6F4'
INK, MUTED, LINE = '#141922', '#5B6475', '#DCE3ED'
FONT = "font-family=\"'IBM Plex Sans', -apple-system, 'Segoe UI', Helvetica, Arial, sans-serif\""


def projects():
    out = []
    for d in sorted(p for p in ROOT.iterdir() if p.is_dir() and re.match(r'\d{4}-\d{2}-', p.name)):
        report = d / 'report.md'
        title = re.sub(r'^\d{4}-\d{2}-', '', d.name).replace('-', ' ').capitalize()
        if report.exists():  # a short "label:" in the report's front matter wins
            m = re.search(r'^label:\s*"?(.*?)"?\s*$', report.read_text(encoding='utf-8'), re.M)
            if m:
                title = m.group(1)
        f = d / 'sources' / 'sources.csv'
        rows = list(csv.DictReader(f.open(encoding='utf-8'))) if f.exists() else []
        out.append({'dir': d.name, 'title': title, 'rows': rows})
    return out


def study_type(row, title):
    s = row.get('studied_in', '').lower()
    if 'review' in s:
        return 'Reviews'
    if 'tissue' in s or 'in vitro' in s:
        return 'Lab and tissue studies'
    t = title.lower()
    target = 'cat' if ('feline' in t or 'cat' in t) else 'rabbit' if 'rabbit' in t else ''
    if target and target in s:
        return 'Target species'
    return 'Other species'


def card(w, h, title, sub, body):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" {FONT}>'
            f'<rect x="0.5" y="0.5" width="{w-1}" height="{h-1}" rx="8" fill="#FFFFFF" stroke="{LINE}"/>'
            f'<text x="28" y="40" font-size="17" font-weight="600" fill="{INK}">{html.escape(title)}</text>'
            f'<text x="28" y="62" font-size="13" fill="{MUTED}">{html.escape(sub)}</text>{body}</svg>')


def legend(items, x, y):
    out, cx = [], x
    for label, color in items:
        out.append(f'<rect x="{cx}" y="{y-10}" width="12" height="12" rx="2" fill="{color}"/>'
                   f'<text x="{cx+18}" y="{y}" font-size="12.5" fill="{MUTED}">{html.escape(label)}</text>')
        cx += 30 + 7.2 * len(label)
    return ''.join(out)


def hbars(projs, segments, title, sub, fname):
    w, left, right, bar_h, gap, top = 760, 250, 60, 26, 20, 114
    h = top + len(projs) * (bar_h + gap) - gap + 30
    total_max = max([sum(p['seg'].values()) for p in projs] + [1])
    scale = (w - left - right) / total_max
    body = [legend([(k, c) for k, c in segments], 28, 94)]
    for i, p in enumerate(projs):
        y = top + i * (bar_h + gap)
        body.append(f'<text x="28" y="{y+18}" font-size="13.5" fill="{INK}">{html.escape(p["title"][:34])}</text>')
        x = left
        for k, c in segments:
            v = p['seg'].get(k, 0)
            if v:
                body.append(f'<rect x="{x:.1f}" y="{y}" width="{v*scale:.1f}" height="{bar_h}" fill="{c}"/>')
                if v * scale > 22:
                    tc = '#FFFFFF' if c in (BLUE, BLUE_2) else INK
                    body.append(f'<text x="{x + v*scale/2:.1f}" y="{y+17.5}" font-size="12" text-anchor="middle" fill="{tc}">{v}</text>')
                x += v * scale
        body.append(f'<text x="{x+8:.1f}" y="{y+18}" font-size="13" font-weight="600" fill="{INK}">{sum(p["seg"].values())}</text>')
    (OUT / fname).write_text(card(w, h, title, sub, ''.join(body)), encoding='utf-8')


def vbars(counts, title, sub, fname):
    w, h, left, bottom, top = 760, 330, 70, 270, 92
    labels = list(counts)
    mx = max(counts.values()) or 1
    step = 5 if mx <= 30 else 10
    ymax = ((mx + step - 1) // step) * step
    plot_w = w - left - 40
    bw = plot_w / len(labels) * 0.5
    body = []
    for t in range(0, ymax + 1, step):
        y = bottom - (bottom - top) * t / ymax
        body.append(f'<line x1="{left}" x2="{w-40}" y1="{y:.1f}" y2="{y:.1f}" stroke="{LINE}"/>'
                    f'<text x="{left-10}" y="{y+4:.1f}" font-size="12" text-anchor="end" fill="{MUTED}">{t}</text>')
    for i, k in enumerate(labels):
        cx = left + plot_w / len(labels) * (i + 0.5)
        v = counts[k]
        y = bottom - (bottom - top) * v / ymax
        body.append(f'<rect x="{cx-bw/2:.1f}" y="{y:.1f}" width="{bw:.1f}" height="{bottom-y:.1f}" fill="{BLUE}"/>'
                    f'<text x="{cx:.1f}" y="{y-8:.1f}" font-size="13" font-weight="600" text-anchor="middle" fill="{INK}">{v}</text>'
                    f'<text x="{cx:.1f}" y="{bottom+22}" font-size="13" text-anchor="middle" fill="{MUTED}">{html.escape(k)}</text>')
    (OUT / fname).write_text(card(w, h, title, sub, ''.join(body)), encoding='utf-8')


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    ps = projects()
    n = sum(len(p['rows']) for p in ps)
    for p in ps:
        oa = sum(1 for r in p['rows'] if r.get('pmc'))
        p['seg'] = {'Free full text': oa, 'Subscription': len(p['rows']) - oa}
    hbars(ps, [('Free full text', BLUE), ('Subscription', BLUE_3)],
          'Studies cited in each project', f'{n} studies across {len(ps)} projects', 'studies-by-project.svg')
    types = [('Target species', BLUE), ('Other species', BLUE_2), ('Lab and tissue studies', BLUE_3), ('Reviews', BLUE_4)]
    for p in ps:
        c = {}
        for r in p['rows']:
            k = study_type(r, p['title'])
            c[k] = c.get(k, 0) + 1
        p['seg'] = c
    hbars(ps, types, 'Where the evidence comes from',
          'What each cited study was actually done in', 'evidence-by-type.svg')
    periods = {'Before 2000': 0, '2000–2009': 0, '2010–2019': 0, '2020 onward': 0}
    for p in ps:
        for r in p['rows']:
            try:
                y = int(r.get('year') or 0)
            except ValueError:
                continue
            k = 'Before 2000' if y < 2000 else '2000–2009' if y < 2010 else '2010–2019' if y < 2020 else '2020 onward'
            periods[k] += 1
    vbars(periods, 'When the cited studies were published', f'All {n} studies, by year of publication', 'studies-by-period.svg')
    print(f'{len(ps)} projects, {n} studies -> {OUT.relative_to(ROOT)}')


if __name__ == '__main__':
    main()
