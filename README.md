======================
django-adlh-utils
======================

A collection of scripts and template helpers

Quick start
-----------

1) Add ap to settings.py:
```python
# setting.py
INSTALLED_APPS = (
    ...
    'adlh_utils',
)
```

2) Use the utils on your models.

```python
from adlh_utils.model_utils import resize_image_on_upload
#....
post_save.connect(resize_image_on_upload, sender=Image)

```

3) That's it! 
