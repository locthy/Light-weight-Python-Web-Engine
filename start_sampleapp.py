#
# Copyright (C) 2025 pdnguyen of HCMC University of Technology VNU-HCM.
# All rights reserved.
# This file is part of the CO3093/CO3094 course,
# and is released under the "MIT License Agreement". Please see the LICENSE
# file that should have been included as part of this package.
#
# WeApRous release
#
# The authors hereby grant to Licensee personal permission to use
# and modify the Licensed Source Code for the sole purpose of studying
# while attending the course
#


"""
start_sampleapp
~~~~~~~~~~~~~~~~~

This module provides a sample RESTful web application using the WeApRous framework.

It defines basic route handlers and launches a TCP-based backend server to serve
HTTP requests. The application includes a login endpoint and a greeting endpoint,
and can be configured via command-line arguments.
"""



import json
import threading
import time
import sys
import os
import argparse

sys.path.append(os.getcwd())

from daemon.weaprous import WeApRous

PORT = 8000
app = WeApRous()


def _parse_body(body):
    """Normalize WeApRous body -> Python dict."""
    if isinstance(body, dict):
        return body
    if isinstance(body, (bytes, bytearray)):
        body = body.decode("utf-8", errors="ignore")
    if isinstance(body, str):
        body = body.strip()
        if not body:
            return {}
        try:
            return json.loads(body)
        except Exception:
            return {}
    return {}


def _json(obj):
    """Always return JSON string for WeApRous."""
    return json.dumps(obj)


@app.route('/login', methods=['POST'])
def login(headers="guest", body="anonymous"):
    print("[SampleApp] Logging in {} to {}".format(headers, body))
    return _json({"message": "Login logged to console"})


@app.route('/hello', methods=['GET'])
def hello(headers, body):
    print("[SampleApp] ['PUT'] Hello in {} to {}".format(headers, body))
    return _json({"message": "Hello logged to console"})



if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog='Backend', description='', epilog='Backend daemon')
    parser.add_argument('--server-ip', default='0.0.0.0')
    parser.add_argument('--server-port', type=int, default=PORT)

    args = parser.parse_args()
    ip = args.server_ip
    port = args.server_port

    app.prepare_address(ip, port)
    app.run()