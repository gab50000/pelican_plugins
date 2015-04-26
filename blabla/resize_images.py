from pelican import signals
from pelican.readers import BaseReader

import ipdb

def test(instance):
    if instance._content is not None:
        instance._content = "<html><head></head><body><p>Blablabla</p></body>"
        return instance
# This is how pelican works.
def register():
    signals.content_object_init.connect(test)

