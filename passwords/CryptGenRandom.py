#!/usr/bin/env python3

import sys
import string

if sys.version_info < (3, 6): # Python 3.5.10 or lower
    import random
else: # Python 3.6 and above
    import secrets

def getRandPwd(length):
    alphabet = string.ascii_letters + string.digits # [a-zA-Z0-9]
    if sys.version_info < (3, 6):
        rng = random.SystemRandom()
        return ''.join(rng.choice(alphabet) for _ in range(length))
    else:
        return ''.join(secrets.choice(alphabet) for _ in range(length))

password = getRandPwd(32)
print(password)