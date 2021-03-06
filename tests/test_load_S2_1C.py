import yt
import yt.extensions.geotiff

from yt_geotiff.data_structures import GeoTiffDataset
from yt_geotiff.testing import requires_file

s2_data = "Sentinel-2_sample_L1C/T33UXP_20170501T100031_B02.jp2"

@requires_file(s2_data)
def test_load():
    ds = yt.load(s2_data)
    assert isinstance(ds, GeoTiffDataset)
