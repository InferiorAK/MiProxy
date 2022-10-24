import os
import platform
from core.res import *
from core.res import __version__

if platform.system() == "Linux":
    from core.res.lin_col import *
    r = lin_col.r
    g = lin_col.g
    y = lin_col.y
    col = lin_col.col
elif platform.system() == "Windows":
    from core.res.win_col import *
    r = win_col.r
    g = win_col.g
    y = win_col.y
    p = win_col.p
    lr = win_col.lr
    lp = win_col.lp
else:
    from core.res.lin_col import *
    r = lin_col.r
    g = lin_col.g
    y = lin_col.y
    col = lin_col.col

args = arguments.args
parser = arguments.parser

exception = f'''
{"MiProxy "+__version__}

Usage:  python {os.path.basename(__file__)} --generate --count [LOOP_COUNT] -o [out.ext]
        python {os.path.basename(__file__)} --scrape -api [API_LINK] -o [out.ext]
        python {os.path.basename(__file__)} --check -f [proxies.txt] --type [http/socks4/socks5] -t [second] -o [out.ext] -dC/-dc/-rn/-ct/-dt/-isp/-zip/-lc/-all
        python {os.path.basename(__file__)} --check -u [test_url] -f [proxies.txt] --type [http/socks4/socks5] -t [second] -o [out.ext]
        python {os.path.basename(__file__)} --add -f [ip_file.txt] -p [port] -o [out.ext]
'''