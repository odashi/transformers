# This file is autogenerated by the command `make fix-copies`, do not edit.
# flake8: noqa
from ..utils import DummyObject, requires_backends


class ImageProcessingMixin(metaclass=DummyObject):
    _backends = ["vision"]

    def __init__(self, *args, **kwargs):
        requires_backends(self, ["vision"])


def rescale(*args, **kwargs):
    requires_backends(rescale, ["vision"])


def resize(*args, **kwargs):
    requires_backends(resize, ["vision"])


def to_pil_image(*args, **kwargs):
    requires_backends(to_pil_image, ["vision"])


class ImageFeatureExtractionMixin(metaclass=DummyObject):
    _backends = ["vision"]

    def __init__(self, *args, **kwargs):
        requires_backends(self, ["vision"])


class BeitFeatureExtractor(metaclass=DummyObject):
    _backends = ["vision"]

    def __init__(self, *args, **kwargs):
        requires_backends(self, ["vision"])


class BeitImageProcessor(metaclass=DummyObject):
    _backends = ["vision"]

    def __init__(self, *args, **kwargs):
        requires_backends(self, ["vision"])


class CLIPFeatureExtractor(metaclass=DummyObject):
    _backends = ["vision"]

    def __init__(self, *args, **kwargs):
        requires_backends(self, ["vision"])


class CLIPImageProcessor(metaclass=DummyObject):
    _backends = ["vision"]

    def __init__(self, *args, **kwargs):
        requires_backends(self, ["vision"])


class ConditionalDetrFeatureExtractor(metaclass=DummyObject):
    _backends = ["vision"]

    def __init__(self, *args, **kwargs):
        requires_backends(self, ["vision"])


class ConvNextFeatureExtractor(metaclass=DummyObject):
    _backends = ["vision"]

    def __init__(self, *args, **kwargs):
        requires_backends(self, ["vision"])


class ConvNextImageProcessor(metaclass=DummyObject):
    _backends = ["vision"]

    def __init__(self, *args, **kwargs):
        requires_backends(self, ["vision"])


class DeformableDetrFeatureExtractor(metaclass=DummyObject):
    _backends = ["vision"]

    def __init__(self, *args, **kwargs):
        requires_backends(self, ["vision"])


class DeiTFeatureExtractor(metaclass=DummyObject):
    _backends = ["vision"]

    def __init__(self, *args, **kwargs):
        requires_backends(self, ["vision"])


class DeiTImageProcessor(metaclass=DummyObject):
    _backends = ["vision"]

    def __init__(self, *args, **kwargs):
        requires_backends(self, ["vision"])


class DetrFeatureExtractor(metaclass=DummyObject):
    _backends = ["vision"]

    def __init__(self, *args, **kwargs):
        requires_backends(self, ["vision"])


class DonutFeatureExtractor(metaclass=DummyObject):
    _backends = ["vision"]

    def __init__(self, *args, **kwargs):
        requires_backends(self, ["vision"])


class DPTFeatureExtractor(metaclass=DummyObject):
    _backends = ["vision"]

    def __init__(self, *args, **kwargs):
        requires_backends(self, ["vision"])


class DPTImageProcessor(metaclass=DummyObject):
    _backends = ["vision"]

    def __init__(self, *args, **kwargs):
        requires_backends(self, ["vision"])


class FlavaFeatureExtractor(metaclass=DummyObject):
    _backends = ["vision"]

    def __init__(self, *args, **kwargs):
        requires_backends(self, ["vision"])


class FlavaImageProcessor(metaclass=DummyObject):
    _backends = ["vision"]

    def __init__(self, *args, **kwargs):
        requires_backends(self, ["vision"])


class FlavaProcessor(metaclass=DummyObject):
    _backends = ["vision"]

    def __init__(self, *args, **kwargs):
        requires_backends(self, ["vision"])


class GLPNFeatureExtractor(metaclass=DummyObject):
    _backends = ["vision"]

    def __init__(self, *args, **kwargs):
        requires_backends(self, ["vision"])


class GLPNImageProcessor(metaclass=DummyObject):
    _backends = ["vision"]

    def __init__(self, *args, **kwargs):
        requires_backends(self, ["vision"])


class ImageGPTFeatureExtractor(metaclass=DummyObject):
    _backends = ["vision"]

    def __init__(self, *args, **kwargs):
        requires_backends(self, ["vision"])


class ImageGPTImageProcessor(metaclass=DummyObject):
    _backends = ["vision"]

    def __init__(self, *args, **kwargs):
        requires_backends(self, ["vision"])


class LayoutLMv2FeatureExtractor(metaclass=DummyObject):
    _backends = ["vision"]

    def __init__(self, *args, **kwargs):
        requires_backends(self, ["vision"])


class LayoutLMv2ImageProcessor(metaclass=DummyObject):
    _backends = ["vision"]

    def __init__(self, *args, **kwargs):
        requires_backends(self, ["vision"])


class LayoutLMv3FeatureExtractor(metaclass=DummyObject):
    _backends = ["vision"]

    def __init__(self, *args, **kwargs):
        requires_backends(self, ["vision"])


class LayoutLMv3ImageProcessor(metaclass=DummyObject):
    _backends = ["vision"]

    def __init__(self, *args, **kwargs):
        requires_backends(self, ["vision"])


class LevitFeatureExtractor(metaclass=DummyObject):
    _backends = ["vision"]

    def __init__(self, *args, **kwargs):
        requires_backends(self, ["vision"])


class LevitImageProcessor(metaclass=DummyObject):
    _backends = ["vision"]

    def __init__(self, *args, **kwargs):
        requires_backends(self, ["vision"])


class MaskFormerFeatureExtractor(metaclass=DummyObject):
    _backends = ["vision"]

    def __init__(self, *args, **kwargs):
        requires_backends(self, ["vision"])


class MobileNetV2FeatureExtractor(metaclass=DummyObject):
    _backends = ["vision"]

    def __init__(self, *args, **kwargs):
        requires_backends(self, ["vision"])


class MobileNetV2ImageProcessor(metaclass=DummyObject):
    _backends = ["vision"]

    def __init__(self, *args, **kwargs):
        requires_backends(self, ["vision"])


class MobileViTFeatureExtractor(metaclass=DummyObject):
    _backends = ["vision"]

    def __init__(self, *args, **kwargs):
        requires_backends(self, ["vision"])


class MobileViTImageProcessor(metaclass=DummyObject):
    _backends = ["vision"]

    def __init__(self, *args, **kwargs):
        requires_backends(self, ["vision"])


class OwlViTFeatureExtractor(metaclass=DummyObject):
    _backends = ["vision"]

    def __init__(self, *args, **kwargs):
        requires_backends(self, ["vision"])


class PerceiverFeatureExtractor(metaclass=DummyObject):
    _backends = ["vision"]

    def __init__(self, *args, **kwargs):
        requires_backends(self, ["vision"])


class PerceiverImageProcessor(metaclass=DummyObject):
    _backends = ["vision"]

    def __init__(self, *args, **kwargs):
        requires_backends(self, ["vision"])


class PoolFormerFeatureExtractor(metaclass=DummyObject):
    _backends = ["vision"]

    def __init__(self, *args, **kwargs):
        requires_backends(self, ["vision"])


class PoolFormerImageProcessor(metaclass=DummyObject):
    _backends = ["vision"]

    def __init__(self, *args, **kwargs):
        requires_backends(self, ["vision"])


class SegformerFeatureExtractor(metaclass=DummyObject):
    _backends = ["vision"]

    def __init__(self, *args, **kwargs):
        requires_backends(self, ["vision"])


class SegformerImageProcessor(metaclass=DummyObject):
    _backends = ["vision"]

    def __init__(self, *args, **kwargs):
        requires_backends(self, ["vision"])


class VideoMAEFeatureExtractor(metaclass=DummyObject):
    _backends = ["vision"]

    def __init__(self, *args, **kwargs):
        requires_backends(self, ["vision"])


class VideoMAEImageProcessor(metaclass=DummyObject):
    _backends = ["vision"]

    def __init__(self, *args, **kwargs):
        requires_backends(self, ["vision"])


class ViltFeatureExtractor(metaclass=DummyObject):
    _backends = ["vision"]

    def __init__(self, *args, **kwargs):
        requires_backends(self, ["vision"])


class ViltImageProcessor(metaclass=DummyObject):
    _backends = ["vision"]

    def __init__(self, *args, **kwargs):
        requires_backends(self, ["vision"])


class ViltProcessor(metaclass=DummyObject):
    _backends = ["vision"]

    def __init__(self, *args, **kwargs):
        requires_backends(self, ["vision"])


class ViTFeatureExtractor(metaclass=DummyObject):
    _backends = ["vision"]

    def __init__(self, *args, **kwargs):
        requires_backends(self, ["vision"])


class AudioSpectogramTransformerFeatureExtractor(metaclass=DummyObject):
    _backends = ["vision"]

    def __init__(self, *args, **kwargs):
        requires_backends(self, ["vision"])


class YolosFeatureExtractor(metaclass=DummyObject):
    _backends = ["vision"]

    def __init__(self, *args, **kwargs):
        requires_backends(self, ["vision"])
