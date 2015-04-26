from pelican import signals
from pelican.readers import BaseReader

import re
import ipdb
import subprocess

#Purpose of this Plugin:
Find the following tags in articles:
    {%mini /path/to/img %}  -> shrink these images to 800x600
    {%mini->large /path/to/img %} -> shrink these images as before, but make a link to the original size img
    {%slide /path/to/img1 ... /path/to/imgn %} -> make a slideshow out of these images. combinable with mini!

def test(instance):
    if instance._content is not None:
        #Find all image links
        links = re.findall("(\(|<img\s*src\=\">).*jpg\)", instance._content)
        #~ instance._content = "<html><body>{}</body></html".format(subprocess.check_output("pwd"))
        return instance
# This is how pelican works.
def register():
    signals.content_object_init.connect(test)

