#!/usr/bin/env python

import os
import json

print("Content-Type: application/json\r")
print("\r")

print(json.dumps(dict(os.environ)))