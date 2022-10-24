from argparse import ArgumentParser

# Arguments
parser = ArgumentParser(description="Proxy Tool by MiTaseen", usage="%(prog)s [options]")
parser.add_argument(
    "-f", "--file",
    type=str,
    nargs="?",
    help="Proxy File"
)
parser.add_argument(
    "-o", "--output",
    type=str,
    nargs="?",
    default="output.txt",
    help="Output File"
)
# parser.add_argument(
#     "-ip",
#     type=str,
#     metavar="[IP_ADRESS]",
#     dest="ip",
#     help="Type Single IP"
# )
parser.add_argument(
    "-p", "--port",
    nargs="?",
    type=int,
    default=5678,
    help="Set Port/Target Port"
)
parser.add_argument(
    "--type",
    type=str,
    choices=["http", "socks4", "socks5"],
    metavar="[http/socks4/socks5]",
    help="Set Proxy Type"
)
parser.add_argument(
    "-t", "--timeout",
    type=float,
    nargs="?",
    default=2,
    help="Set Timeout"
)
parser.add_argument(
    "-v", "--version",
    action="store_true",
    help="Print Version"
)

# Generate Random IP
usage_gen = '''
Usage: python %(prog)s --generate --count [LOOP_COUNT] -o [out.ext]
'''
generate = parser.add_argument_group("Generate Random IP", usage_gen)
generate.add_argument(
    "-g", "--generate",
    action="store_true",
    help="Generate IP (Mode)"
)
generate.add_argument(
    "-c", "--count",
    metavar="LOOP_COUNT",
    type=int,
    nargs="?",
    default=10,
    help="Amount of IP"
)

# scrape options
usage_scrape = '''
Usage: python %(prog)s --scrape -api [API_LINK] -o [out.ext]
'''
scrape = parser.add_argument_group("Scrape Proxies", usage_scrape)
scrape.add_argument(
    "-sc","--scrape",
    action="store_true",
    help="Scrape Proxies with API (Mode)"
)
scrape.add_argument(
    "-api",
    metavar="API_LINK",
    type=str,
    dest="api",
    nargs="?",
    help="Paste your api"
)

# check proxies
usage_check = "Usage: python %(prog)s --check -f [proxies.txt] --type [http/socks4/socks5] -t [second] -o [out.ext] -dC/-dc/-rn/-ct/-dt/-isp/-zip/-lc/-all"
check = parser.add_argument_group("Check Proxies", description=usage_check)
check.add_argument(
    "--check",
    action="store_true",
    help="Check Proxies (Mode)"
)
check.add_argument(
    "-dC", "--dump-continent",
    dest="dC",
    action="store_true",
    help="Get Proxy Continent"
)
check.add_argument(
    "-dc", "--dump-country",
    dest="dc",
    action="store_true",
    help="Get Proxy Country"
)
check.add_argument(
    "-rn", "--region-name",
    dest="rn",
    action="store_true",
    help="Proxy region name"
)
check.add_argument(
    "-ct", "--city",
    dest="ct",
    action="store_true",
    help="proxy city"
)
check.add_argument(
    "-dt", "--district",
    dest="dt",
    action="store_true",
    help="proxy district"
)
check.add_argument(
    "-isp",
    dest="isp",
    action="store_true",
    help="Proxy ISP"
)
check.add_argument(
    "-zip",
    dest="zip",
    action="store_true",
    help="Country zip code"
)
check.add_argument(
    "-lc", "--location",
    dest="lc",
    action="store_true",
    help="Proxy Location"
)
check.add_argument(
    "-a","--all",
    dest="all",
    action="store_true",
    help="Dump All info"
)

# check proxues with custom url/api
usage_custom = "Usage: python %(prog)s --check -u [test_url] -f [proxies.txt] --type [http/socks4/socks5] -t [second] -o [out.ext]"
check_custom = parser.add_argument_group("Check Proxies with custom url", description=usage_custom)
check_custom.add_argument(
    "-u","--url",
    type=str,
    default="http://ip-api/json",
    metavar="[TEST_URL_LINK]",
    dest="url",
    help="Proxy Checker URL"
)

# add port
usage_add = "Usage: python %(prog)s --add -f [ip_file.txt] -p [port] -o [out.ext]"
add = parser.add_argument_group("Add Port", description=usage_add)
add.add_argument(
    "--add",
    action="store_true",
    help="Add Port to IP (Mode)"
)

args = parser.parse_args()

# <------>