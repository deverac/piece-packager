import base64
import os
import re
import sys
import xml.etree.ElementTree as ET # Use XML parser to read SVG.

from io import StringIO

# This script packages multiple files, each containing a chess piece, into
# a single SVG file. Once packaged, the pieces can be referenced by their
# two-letter id. (e.g. 'wk', 'bp')
#
# Any PNG file can be packaged. Packaging an SVG may or may not succeed
# depending on how 'complex' the SVG file is.
#
# When combining SVG files, ids and classnames (and their references) must be
# updated in order to avoid conflicts. e.g.
#    <pattern id="pattern0"
#    <g clip-path="url(#clip0_1_13)">
#    <g filter="url(#filter0_d_301_31)">
#    <path style="opacity:1;fill:url(#linearGradient4170);fill-opacity:1;
#    <use xlink:href="#image0_2_151"
#
# CSS styles (and their references) must also be updated. e.g.
#     <style>.wpcls-1,.wpcls-2,.wpcls-3{stroke-width:0}.wpcls-1,.wpcls-5

def get_start(s):

    if s.startswith('bishop'): return 'b'
    if s.startswith('king'): return 'k'
    if s.startswith('knight'): return 'n'
    if s.startswith('pawn'): return 'p'
    if s.startswith('queen'): return 'q'
    if s.startswith('rook'): return 'r'

    if s.startswith('black'): return 'b'
    if s.startswith('white'): return 'w'

    if s.startswith('b'): return 'b' # black or bishop
    if s.startswith('w'): return 'w'
    if s.startswith('k'): return 'k'
    if s.startswith('n'): return 'n'
    if s.startswith('p'): return 'p'
    if s.startswith('q'): return 'q'
    if s.startswith('r'): return 'r'
    return ''


def get_end(s):
    if s.endswith('bishop'): return 'b'
    if s.endswith('king'): return 'k'
    if s.endswith('knight'): return 'n'
    if s.endswith('pawn'): return 'p'
    if s.endswith('queen'): return 'q'
    if s.endswith('rook'): return 'r'

    if s.endswith('black'): return 'b'
    if s.endswith('white'): return 'w'

    if s.endswith('-b'): return 'b'
    if s.endswith('-w'): return 'w'
    if s.endswith('_b'): return 'b'
    if s.endswith('_w'): return 'w'

    if s.endswith('b'): return 'b' # black or bishop
    if s.endswith('w'): return 'w'
    if s.endswith('k'): return 'k'
    if s.endswith('n'): return 'n'
    if s.endswith('p'): return 'p'
    if s.endswith('q'): return 'q'
    if s.endswith('r'): return 'r'
    return ''


def generate_all_piece_ids():
    ary = []
    for color in ['w', 'b']:
        for piece in ['b', 'k', 'n', 'p', 'q', 'r']:
            ary.append(f'{color}{piece}')
    return ary


def get_piece_id_from_file(nm):
    s = nm.lower().replace('.svg', '').replace('.png', '')
    if len(s) > 1:
        id = get_start(s) + get_end(s)
        if len(id) == 2:
            if id in SWAPPED_PIECE_IDS:
                id = id[1] + id[0]
            return id
    return ''


def is_svg_file(str):
    return str.lower().endswith('.svg')


def is_png_file(str):
    return str.lower().endswith('.png')


def get_filenames_for_pieces(pieces_dir):
    filenames = {}

    for base_dir, dirs, files in os.walk(pieces_dir):
        print(f'Processing {base_dir}')
        for fnc in [is_svg_file, is_png_file]: # Find SVG before PNG files.
            for file in sorted(files):
                if (base_dir == pieces_dir): # Exclude subdirectories
                    piece_id = get_piece_id_from_file(file)
                    if len(piece_id) == 2:
                        dat_file = os.path.join(base_dir, file)
                        if fnc(dat_file):
                            if piece_id not in filenames:
                                filenames[piece_id] = []
                            filenames[piece_id].append(dat_file)
    return filenames


def write_svg(filenames, tgt_svg):
    svgElem = ET.Element("svg")
    svgElem.set('xmlns', 'http://www.w3.org/2000/svg')
    svgElem.set('width', str(TILE_SZ))
    svgElem.set('height', str(TILE_SZ))
    #svgElem.append(ET.Comment('A comment'))
    for piece_id in sorted(filenames.keys()):
        fnames = filenames[piece_id]
        if len(fnames) > 0:
            file = fnames[0]
            if is_svg_file(file):
                process_svg_file(file, svgElem, piece_id)
            elif is_png_file(file):
                process_png_file(file, svgElem, piece_id)
            else:
                print('bad file')

    tree = ET.ElementTree(svgElem)

    ET.indent(tree, '  ')
    tree.write(tgt_svg, encoding='utf-8', xml_declaration=False)


def sanity_check_piece_ids(src_dir, names):
    piece_ids = names.keys()
    for piece_id in ALL_PIECE_IDS:
        if piece_id not in piece_ids:
            print(f'    warning:{src_dir}: missing piece-id ({id})')

    for piece_id in piece_ids:
        if piece_id not in ALL_PIECE_IDS:
             # We should never get here.
            print(f'    warning:{src_dir}: found unknown piece-id ({id}) for {names[piece_id]}')


def process_png_file(file, svgElem, pc_id):
    g = ET.SubElement(svgElem, 'g')
    g.set('id', pc_id)

    img = ET.SubElement(g, 'image')
    img.set("width", str(TILE_SZ))
    img.set("height", str(TILE_SZ))
    img.set('href', "data:image/png;base64,"+b64encode(file))


def process_svg_file(file, svgElem, pc_id):
    g = ET.SubElement(svgElem, 'g')
    g.set('id', pc_id)

    with open(file, 'r') as f:
        dat = f.read()

        # Remove namespace
        it = ET.iterparse(StringIO(dat))
        for _, el in it:
            _, _, el.tag = el.tag.rpartition('}')
        xml_root = it.root

        # Copy root attributes.
        for attrib in xml_root.attrib:
            if attrib == 'fill':
                g.set(attrib, xml_root.attrib[attrib])

        # Compute scaling transform
        if 'viewBox' in xml_root.attrib:
            # viewBox values can be separated by comma or space
            [minx, miny, width, height] = map(float, xml_root.attrib['viewBox'].replace(',', ' ').split(' '))
            aspectRatio = height / width 
            szX = TILE_SZ
            szY = szX * aspectRatio
            scaleX = szX / width
            scaleY = szY / height
            g.set('transform','scale('+str(scaleX)+' '+str(scaleY)+')')
            svgElem.set('viewbox', str(minx)+' '+str(miny)+' '+str(width)+' '+str(height))
        elif 'width' in xml_root.attrib and 'height' in xml_root.attrib:
            wid = float(xml_root.attrib['width'])
            hgt = float(xml_root.attrib['height'])
            aspectRatio = hgt / wid 
            szX = TILE_SZ
            szY = szX * aspectRatio
            scaleX = szX / wid
            scaleY = szY / hgt
            g.set('transform','scale('+str(scaleX)+' '+str(scaleY)+')')
        else:
            print('warning: no size found')

        if xml_root is not None:
            depth = 1
            add_children(pc_id, xml_root, g, depth)


def construct_class_name(pc_id, str):
    return ' '.join(map(lambda cls: pc_id+cls, str.split()))


def adjust_id(pc_id, pfx, txt):
    if txt.startswith(pfx):
        return pfx + pc_id + txt[len(pfx):]
    return txt


def add_children(pc_id, src, tgt, depth):
    for child in src:
        tg = ET.SubElement(tgt, child.tag)

        for attr in child.attrib:
            if attr == 'id':
                tg.set(attr, pc_id+child.attrib[attr])
            elif attr == 'class':
                tg.set(attr, construct_class_name(pc_id, child.attrib[attr]))
            elif attr == 'style':
                tg.set(attr, child.attrib[attr].replace('url(#', 'url(#'+pc_id))

            elif attr.endswith('}href'):
                tg.set('href', adjust_id(pc_id, '#', child.attrib[attr]))
            else:
                tg.set(attr, adjust_id(pc_id, 'url(#', child.attrib[attr]))

        if (child.tag == 'style'):
            tg.text = prepend_piece_id_to_classnames(pc_id, child.text)
        elif child.tag == 'metadata':
            pass
        elif child.tag == 'namedview': # non-SVG tag
            pass
        else:
            add_children(pc_id, child, tg, depth+1)


def prepend_piece_id_to_classnames(pc_id, css_styles):
    ary = []
    opens = css_styles.split('{')
    for op in opens:
        closes = op.split('}')
        if len(closes) == 1:
            class_names = add_prefix_to_classnames(pc_id, closes[0])
            ary.append(class_names + '{')
        else:
            css_code = closes[0]
            ary.append(css_code+'}')
            class_names = closes[1].strip()
            if len(class_names):
                ary.append(add_prefix_to_classnames(pc_id, class_names) + '{')
    return ''.join(ary)


def add_prefix_to_classnames(pfx, name_str):
    ary = []
    parts = name_str.split('.')
    for part in parts:
        if len(part):
            ary.append(pfx+part)
        else:
            ary.append(part)
    return '.'.join(ary)


def b64encode(nm):
    with open(nm, 'rb') as inp:
        b64str = base64.b64encode(inp.read()).decode('utf-8')
    return b64str


def process_piece_dir(src_dir, out_dir):
    dir_parts = os.path.normpath(src_dir).split(os.path.sep)
    tgt_dir = os.path.join(out_dir, *dir_parts[0:-1])
    os.makedirs(tgt_dir, exist_ok=True)
    tgt_svg = os.path.join(tgt_dir, dir_parts[-1]+'.svg')

    names = get_filenames_for_pieces(src_dir)
    write_svg(names, tgt_svg)

    sanity_check_piece_ids(src_dir, names)


ALL_PIECE_IDS = sorted(generate_all_piece_ids())
SWAPPED_PIECE_IDS = sorted(map(lambda id: id[1]+id[0], ALL_PIECE_IDS))
    
OUT_DIR='out'
TILE_SZ=40

if len(sys.argv) == 2:
    process_piece_dir(sys.argv[1], OUT_DIR)
else:
    DIRECTORIES = 1
    for parent_dir in ['png', 'svg']:
        for subdir in sorted(next(os.walk(parent_dir))[DIRECTORIES]):
            piece_dir = os.path.join(parent_dir, subdir)
            process_piece_dir(piece_dir, OUT_DIR)
