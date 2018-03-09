#!/usr/bin/env python3

import logging
import bumper
import sys, socket

logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s %(levelname)-8s %(message)s')

conf_address = ("0.0.0.0", 8007)
xmpp_address = ("0.0.0.0", 5223)

# start conf server (async)
conf_server = bumper.ConfServer(conf_address, ssl=False, async=True)

# start xmpp server (sync)
xmpp_server = bumper.XMPPServer(xmpp_address)

conf_server.disconnect()
