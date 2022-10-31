<p align="center">
  <img src="https://i.ibb.co/9YNCKt0/thumb1.jpg">
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Version-1.0-green?style=for-the-badge">
  <img src="https://img.shields.io/github/license/inferiorak/MiProxy?style=for-the-badge">
  <img src="https://img.shields.io/github/stars/inferiorak/MiProxy?style=for-the-badge">
  <img src="https://img.shields.io/github/issues/inferiorak/MiProxy?color=red&style=for-the-badge">
  <img src="https://img.shields.io/github/forks/inferiorak/MiProxy?color=teal&style=for-the-badge">
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Author-InferiorAK-blue?style=flat-square">
  <img src="https://img.shields.io/badge/Maintained%3F-Yes-lightblue?style=flat-square">
  <img src="https://img.shields.io/badge/Written%20In-Python3.10.8-darkcyan?style=flat-square">
  <img src="https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2Finferiorak%2FMiProxy&title=Visitors&edge_flat=false"/></a>
</p>
<p align="center"><a href="https://github.com/inferiorak/MiProxy/releases/tag/MiProxy1.0">*** All Releases ***</a></p>

<br>

## Features

- Proxy Scraper
- IP Generator
- Proxy Validator
- Add Port to IP file

<br>

## Supported on

- Termux
- Linux
- Windows

<br>

## Tutorial
<a href="https://www.youtube.com/watch?v=pbOGn7vKvxk">Click Here</a>

## Installation

- Clone this repository -
  ```
  git clone https://github.com/inferiorak/MiProxy
  ```

- Now go to cloned directory -
  ```
  $ cd MiProxy
  $ pip3 install -r requirements.txt
  $ clear
  $ python3 miproxy.py
  ```
  
 ## Overview
 
 ```
 root@kali:~$ python3 miproxy.py -h
usage: miproxy.py [options]

Proxy Tool by MiTaseen

options:
  -h, --help            show this help message and exit
  -f [FILE], --file [FILE]
                        Proxy File
  -o [OUTPUT], --output [OUTPUT]
                        Output File
  -p [PORT], --port [PORT]
                        Set Port/Target Port
  --type [http/socks4/socks5]
                        Set Proxy Type
  -t [TIMEOUT], --timeout [TIMEOUT]
                        Set Timeout
  -v, --version         Print Version

Generate Random IP:
  Usage: python miproxy.py --generate --count [LOOP_COUNT] -o [out.ext]

  -g, --generate        Generate IP (Mode)
  -c [LOOP_COUNT], --count [LOOP_COUNT]
                        Amount of IP

Scrape Proxies:
  Usage: python miproxy.py --scrape -api [API_LINK] -o [out.ext]

  -sc, --scrape         Scrape Proxies with API (Mode)
  -api [API_LINK]       Paste your api

Check Proxies:
  Usage: python miproxy.py --check -f [proxies.txt] --type [http/socks4/socks5] -t
  [second] -o [out.ext] -dC/-dc/-rn/-ct/-dt/-isp/-zip/-lc/-all

  --check               Check Proxies (Mode)
  -dC, --dump-continent
                        Get Proxy Continent
  -dc, --dump-country   Get Proxy Country
  -rn, --region-name    Proxy region name
  -ct, --city           proxy city
  -dt, --district       proxy district
  -isp                  Proxy ISP
  -zip                  Country zip code
  -lc, --location       Proxy Location
  -a, --all             Dump All info

Check Proxies with custom url:
  Usage: python miproxy.py --check -u [test_url] -f [proxies.txt] --type
  [http/socks4/socks5] -t [second] -o [out.ext]

  -u [TEST_URL_LINK], --url [TEST_URL_LINK]
                        Proxy Checker URL

Add Port:
  Usage: python miproxy.py --add -f [ip_file.txt] -p [port] -o [out.ext]

  --add                 Add Port to IP (Mode)
```
