# Vertical Hello Darkness REGEX example

import re
foo = "hello darkness"
for c in foo:
    re.sub("(.)","||"+c+"||", c)
