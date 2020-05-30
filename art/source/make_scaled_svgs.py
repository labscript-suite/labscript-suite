# This is a script to generate svgs of various sizes. Although the svgs named e.g.
# "<name>_32nx32n" are scalable (ideally to integer multiples of 32x32), some tools can
# only display them at their native sizes, so for convenience we generate a few copies
# at power-of-two sizes.

from pathlib import Path
import svgutils.transform as sg
import string

SCALE_FACTORS = 2, 4, 8

def splitunit(s):
    """Get a string of a number with a unit like 8.96mm and return (8.96, "mm")"""
    num = s.rstrip(string.ascii_letters)
    unit = s[len(num):]
    return float(num), unit

def scale_svg(path, name, w, h, scale_factor):
    """Given an svg of size (w, h), make an svg scaled by scale_factor and save a file
    in the same directory named name_WxH.svg where W = scale_factor x w and H =
    scale_factor x h"""
    W = scale_factor * w
    H = scale_factor * h
    # scaled_image = sg.SVGFigure(f'{W}mm', f'{H}mm')

    image = sg.fromfile(path)
    width, width_unit = splitunit(image.width)
    height, height_unit = splitunit(image.height)
    image.set_size(
        (f"{scale_factor * width}{width_unit}", f"{scale_factor * height}{height_unit}")
    )
    dest = Path(path.parent, f"{name}_{W}x{H}.svg")
    print(f"saving {dest}")
    image.save(dest)


def main():
    art = Path(__file__).absolute().parent.parent

    for path in art.iterdir():
        if path.suffix != '.svg':
            continue
        try:
            name, resolution = path.stem.split('_')
            w, h = resolution.split('x')
        except ValueError:
            continue
        if not (w.endswith('n') and h.endswith('n')):
            continue
        w, h = [int(d[:-1]) for d in (w, h)]
        for scale_factor in SCALE_FACTORS:
            scale_svg(path, name, w, h, scale_factor)


if __name__ == '__main__':
    main()
