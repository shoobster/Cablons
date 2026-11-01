"""Generates circuit-trace SVG art in the style of the Cablons logo mark."""
import random

DIRS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def circuit(width=900, height=620, seed=7, traces=55, cell=24, cls="trace", left_bias=0.0):
    rnd = random.Random(seed)
    cols, rows = width // cell, height // cell
    occupied = set()
    paths, nodes, pads = [], [], []
    attempts = 0
    i = 0
    while i < traces and attempts < traces * 6:
        attempts += 1
        # start somewhere in the grid, denser toward the right
        t = rnd.random() ** 0.6
        x = int(left_bias * cols + t * (cols - left_bias * cols))
        y = rnd.randint(1, rows - 1)
        if (x, y) in occupied:
            continue
        dx, dy = rnd.choice(DIRS)
        pts = [(x, y)]
        occupied.add((x, y))
        length = rnd.randint(7, 20)
        for _ in range(length):
            r = rnd.random()
            if r < 0.12:            # 45 degree jog
                if dx != 0 and dy == 0:
                    dy = rnd.choice([-1, 1])
                elif dy != 0 and dx == 0:
                    dx = rnd.choice([-1, 1])
                else:
                    if rnd.random() < 0.5: dy = 0
                    else: dx = 0
            elif r < 0.38:          # 90 degree turn
                if dx != 0 and dy != 0:
                    if rnd.random() < 0.5: dy = 0
                    else: dx = 0
                elif dx != 0:
                    dy = rnd.choice([-1, 1]); dx = 0
                else:
                    dx = rnd.choice([-1, 1]); dy = 0
            nx, ny = x + dx, y + dy
            if nx < 0 or ny < 1 or ny >= rows or nx > cols or (nx, ny) in occupied:
                break
            x, y = nx, ny
            occupied.add((x, y))
            pts.append((x, y))
            if dx != 0 and dy != 0 and rnd.random() < 0.7:
                if rnd.random() < 0.5: dy = 0
                else: dx = 0
        if len(pts) < 5:
            continue
        d = "M" + " L".join(f"{px*cell},{py*cell}" for px, py in pts)
        paths.append((d, i))
        for (ex, ey), chance in ((pts[-1], 0.9), (pts[0], 0.35)):
            if rnd.random() < chance:
                if rnd.random() < 0.85:
                    nodes.append((ex * cell, ey * cell, i))
                else:
                    pads.append((ex * cell, ey * cell, i))
        i += 1
    out = [f'<svg class="circuit" viewBox="0 0 {width} {height}" fill="none" aria-hidden="true" focusable="false">']
    out.append('<defs><linearGradient id="goldline" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#905e26"/><stop offset="0.5" stop-color="#f5ec9b"/><stop offset="1" stop-color="#905e26"/></linearGradient></defs>')
    for d, i in paths:
        out.append(f'<path class="{cls}" style="--i:{i}" d="{d}" pathLength="1"/>')
    for x, y, i in nodes:
        out.append(f'<circle class="node" style="--i:{i}" cx="{x}" cy="{y}" r="4.5"/>')
    for x, y, i in pads:
        out.append(f'<rect class="node" style="--i:{i}" x="{x-4.5}" y="{y-4.5}" width="9" height="9"/>')
    out.append("</svg>")
    return "\n".join(out)

if __name__ == "__main__":
    svg = circuit()
    html = f'<html><body style="background:#070b14;margin:0"><style>.trace{{stroke:url(#goldline);stroke-width:1.5;stroke-linecap:round;stroke-linejoin:round}}.node{{fill:#070b14;stroke:#f5ec9b;stroke-width:1.5}}</style>{svg}</body></html>'
    open("/tmp/claude-0/-home-claude/e8b11f7f-a1ea-5be0-a460-a374e091f483/scratchpad/circuit-test.html", "w").write(html)
