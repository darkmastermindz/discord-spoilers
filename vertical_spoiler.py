import re
foo = "hello darkness"
for c in foo:
    re.sub("(.)","||"+c+"||", c)
