import shapefile
import sys


def strip_attr(input_loc, strip_loc):
    input_shp = shapefile.Reader(input_loc)
    if input_shp.shapeType != shapefile.POINT:
        raise NotImplementedError("Polygons and lines not implemented yet")
    strip_shp = shapefile.Writer(input_shp.shapeType)
    for shape in input_shp.shapes():
        strip_shp.point(*shape.points[0])
    strip_shp.save(strip_loc)


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: strip_attr.py input_file stripped_file")
        sys.exit(1)
    strip_attr(*sys.argv[1:3])
