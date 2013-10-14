#!/usr/bin/env python
#-*- coding: utf-8 -*-

import os
os.sys.path.append('..')
import aesgearman
import string
import random

datatosend = {
    'sfirts_1': 'param ' + ''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(256)),
    'sfirts_2': 'param ' + ''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(256)),
    'sfirts_3': 'param ' + ''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(256)),
    'sfirts_4': 'param ' + ''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(256)),
    'sfirts_5': 'param ' + ''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(256)),
    'sfirts_6': 'param ' + ''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(256)),
    'sfirts_7': 'param ' + ''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(256)),
    'sfirts_7': 'param ' + ''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(256)),
    'sfirts_8': 'param ' + ''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(256)),
    'sfirts_9': 'param ' + ''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(256)),
    'sfirts_10': 'param ' + ''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(256)),
    'sfirts_11': 'param ' + ''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(256)),
    'sfirts_12': 'param ' + ''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(256)),
    'sfirts_13': 'param ' + ''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(256)),
    'sfirts_14': 'param ' + ''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(256)),
}

if __name__ == "__main__":
    gm_client = aesgearman.AESJSON_GearmanClient(['localhost'], aeskey='12345678123456781234567812345678')
    s = gm_client.submit_job('aesjsontest', datatosend, background=False)
    print s.result

