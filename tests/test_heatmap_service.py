import os
from unittest import TestCase

from App.heatmap_service import heatmap_service


class Test(TestCase):
    def test_heatmap_service(self):
        gpx = "resources/2019-09-13_93366270_Zum_Apfelbaum.gpx"
        path = os.path.dirname(gpx)
        result = heatmap_service("1", path)
        assert result == "Generated"
        assert os.path.isfile("1.png")
