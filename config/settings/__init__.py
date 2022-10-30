import os

from .base import *

# you need to set "myproject = 'prod'" as an environment variable
# in your OS (on which your website is hosted)
#if os.environ['config'] == 'production':
from .development import *
#else:
 #  from .dev import *