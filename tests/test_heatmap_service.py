import os

from App.heatmap_service import heatmap_service


def getResourcePath():
    path = "resources/"
    abs_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "resources/")
    if os.path.isdir(path):
        return path
    elif os.path.isdir("test/resources/"):
        return "/test/resources/"
    elif abs_path:
        return abs_path

    raise IOError("Resources not found")


def test_heatmap_service():
    path = getResourcePath()
    result = heatmap_service("1", path)
    assert result == "Generated"
    assert os.path.isfile("1.png")
