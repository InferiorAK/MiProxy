# -*- coding: utf-8 -*-
#! /usr/bin/python3

__doc__ = """# 1st Release   :      24th Oct 2022 (GMT+6)
# MiProxy       :      Proxy Tool
# Version       :      1.0
# Lisence       :      MIT
# Copyright (C) 2022 InferiorAK"""

import main_imports
from main_imports import *
from core import *


# Generate Random IP
if args.generate:
    others.gen()

# Scrape Proxies
elif args.scrape:
    if args.api:
        others.scrp()
    else:
        print(exception)

# Check Proxy
elif args.check:
    # check http
    if args.type == "http":
        httpsc.http_check()
    elif args.type == "socks4":
        socks4sc.socks4_check()
    elif args.type == "socks5":
        socks5sc.socks5_check()
    else:
        print(exception)

# Add Port
elif args.add:
    if args.file:
        others.add_port()
    else:
        print(exception)

# Print Version
elif args.version:
    print(f"MiProxy {main_imports.__version__}")

else:
    print(__doc__)
    print("\n")
    parser.print_help()
