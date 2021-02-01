#  Copyright (c) 2021, Manfred Moitzi
#  License: MIT License
from typing import Union, List, Dict, Iterable

from ezdxf.entities import Text, Attrib, Hatch
from ezdxf.lldxf import const
from ezdxf.math import Matrix44
from ezdxf.render import Path, nesting
from ezdxf.tools import text, fonts

AnyText = Union[Text, Attrib]


# Each char consists of one or more paths!


def make_paths_from_str(s: str,
                        font: fonts.FontFace,
                        halign: int = const.LEFT,
                        valign: int = const.BASELINE,
                        m: Matrix44 = None) -> List[Path]:
    """ Convert a single line string `s` into a list of
    :class:`~ezdxf.render.path.Path` objects. All paths are returned in a single
    list. The path objects are created for the text height
    of one drawing unit as cap height (height of uppercase letter "X") and the
    insertion point is (0, 0). The paths  are aligned to this insertion point.
    BASELINE means the bottom of the letter "X".

    Args:
         s: text to convert
         font: font face definition
         halign: horizontal alignment: LEFT=0, CENTER=1, RIGHT=2
         valign: vertical alignment: BASELINE=0, BOTTOM=1, MIDDLE=2, TOP=3
         m: transformation :class:`~ezdxf.math.Matrix44`

    """
    return []


def group_char_paths(paths: Iterable[Path]) -> List[nesting.Polygon]:
    """ Group paths created from text strings or entities by their base
    characters. e.g. "abc" returns a list of 3 polygon structures, each polygon
    has an outer contour and maybe holes as :class:`~ezdxf.render.path.Path`
    objects::

        ff = fonts.FontFace(family="Arial)
        paths = make_paths_from_str("abc", ff)

        for polygon in group_char_paths(paths)
            contour = polygon[0]
            # check if holes are present:
            if len(polygon) > 1:
                # multiple nested holes are possible:
                for hole in polygon[1]:
                    # hole is a Path() object
                    pass

    This is the basic tool to create HATCH entities from paths.

    """
    # The fast_bbox_detection() function was not designed for this task,
    # but works very well for characters,
    # The center of the hole bounding boxes are always inside the
    # bounding box of the outer contour and outer contours do not overlap.
    return nesting.fast_bbox_detection(paths)


def make_hatches_from_str(s: str,
                          font: fonts.FontFace,
                          halign: int = const.LEFT,
                          valign: int = const.BASELINE,
                          dxfattribs: Dict = None,
                          m: Matrix44 = None) -> List[Hatch]:
    """ Convert a single line string `s` into a list of virtual
    :class:`~ezdxf.entities.Hatch` entities.
    The path objects are created for the text height of one drawing unit as cap
    height (height of uppercase letter "X") and the insertion point is (0, 0).
    The HATCH entities are aligned to this insertion point. BASELINE means the
    bottom of the letter "X".

    Args:
         s: text to convert
         font: font face definition
         halign: horizontal alignment: LEFT=0, CENTER=1, RIGHT=2
         valign: vertical alignment: BASELINE=0, BOTTOM=1, MIDDLE=2, TOP=3
         dxfattribs: additional DXF attributes
         m: transformation :class:`~ezdxf.math.Matrix44`

    """
    dxfattribs = dxfattribs or dict()
    color = dxfattribs.get('color', 7)

    return []


def make_paths_from_entity(entity: AnyText) -> List[Path]:
    """ Convert text content from DXF entities TEXT, ATTRIB and ATTDEF into a
    list of :class:`~ezdxf.render.Path` objects. All paths are returned in a
    single list.
    The paths are located at the location of the source entity, but don't expect
    a 100% match compared to CAD applications.

    """
    return []


def make_hatches_from_entity(entity: AnyText) -> List[Hatch]:
    """ Convert text content from DXF entities TEXT, ATTRIB and ATTDEF into a
    list of virtual :class:`~ezdxf.entities.Hatch` entities.
    The hatches are located at the location of the source entity, but don't
    expect a 100% match compared to CAD applications.

    """
    return []
