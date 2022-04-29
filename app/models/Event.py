""" Event Model """

from masoniteorm.models import Model


class Event(Model):
    """Event Model"""
    __fillable__ = ["title", "start", "end"]
    __dates__ = ["start","end"]

