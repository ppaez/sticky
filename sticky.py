'Create template for printing sticky notes'

import sys


SVG_MAIN_TEMPLATE = '''\
<svg xmlns="http://www.w3.org/2000/svg" width="8.5in" height="11in">
{content}</svg>
'''
SVG_RECTANGLE_TEMPLATE = '''\
  <rect x="{x}in" y="{y}in" width="{w}in" height="{h}in" fill="{color}" stroke="black"/>
'''
SVG_TEXT_TEMPLATE = '''\
  <text x="{x}in" y="{y}in" style="font-size:20" fill="black">{text}</text>
'''
NOTE_WIDTH = 3
NOTE_HEIGHT = 3
COLUMNS = (1, 5)
ROWS = (0.5, 4, 7.5)

cells = []
for row in ROWS:
    for column in COLUMNS:
        cells.append((column, row))


values = open('values').read().splitlines()
content = ''
for value in values:
    if value == '-':
        if not cells:
            break
        cell = cells.pop(0)
        x_rect, y_rect = cell
        x_text = x_rect + 0.1
        y_text = y_rect + 0.4
        content += SVG_RECTANGLE_TEMPLATE.format(x=x_rect, y=y_rect,
                                                 w=NOTE_WIDTH, h=NOTE_HEIGHT,
                                                 color='none')
    else:
        content += SVG_TEXT_TEMPLATE.format(x=round(x_text, 2), y=round(y_text, 2),
                                            text=value)
        y_text += 0.4
        

svg_text = SVG_MAIN_TEMPLATE.format(content=content)

name = sys.argv[1]
f = open(name, 'w')
f.write(svg_text)
