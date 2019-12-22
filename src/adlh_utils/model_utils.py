# coding=UTF-8

from PIL import Image
from django.conf import settings
import os
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)

def resize_image_on_upload(*args, **kwargs):
    logger.debug('... starting resizing on post_save signal ... ')
    obj = kwargs.get("instance", None)
    if not obj:
        logger.error(' error, no instance! exiting without resizing. ')
        return
    im_file = getattr(obj, 'image', None)
    if not im_file:
        logger.error(' error, could not get image from instance! exiting without resizing. ')
        return
    max_width = 800
    max_height = 800
    try: 
        im = Image.open(im_file.path)
    except:
        logger.error(' error, could not open image! exiting without resizing. ')
        return

    logger.debug("Image '%s' has size (%d, %d) and limits are (%d, %d)" % (im_file.name, im.size[0], im.size[1], max_width, max_height))
    if im.size[0] > max_width or im.size[1] > max_height:
        logger.debug('... resizing')
        try: 
            rtc = os.popen("gm convert %(file)s -resize %(width)dx%(height)d %(file)s" % {'file': im_file.path, 'width': max_width, 'height': max_height})
            logger.debug('resized image')
        except:
            logger.error("couldn't resize image!")



