import requests
import os
import platform
from .res.arguments import *
from .res.lin_col import *
from .res.urls import *

if platform.system() == "Linux":
    from .res.lin_col import *
elif platform.system() == "Windows":
    from .res.win_col import *
else:
    from .res.lin_col import *

url_api = url["url_api"]
url2_api = url["url2_api"]

def file(key):
    proxies_socks4 = open(args.file)
    outfile = ""
    if os.path.exists(args.output):
        outa = args.output+f"({{}})"
        cnot = 1
        while os.path.exists(outa.format(cnot)):
            cnot += 1
        outfile += outa.format(cnot)
    else:
        outfile += args.output
    cnt = 0
    for line in proxies_socks4:
        cnt += 1
        serial = str(cnt)+". "
        proxy = line.split("\n")[0]
        try:
            response_socks4 = requests.get(url=url2_api, proxies={"http":"socks4://"+proxy, "https":"socks4://"+proxy}, timeout=args.timeout)
            if response_socks4.status_code == 200:
                success = open(outfile,"a").write(proxy+f" | {key}: "+str(response_socks4.json()[key])+"\n")
                print(f"{g}{serial}{proxy} success | {key}: "+str(response_socks4.json()[key]))
            else:
                print(f"{y}{serial}{proxy} "+str(response_socks4.status_code))
        except KeyError:
            try:
                print(col(237,26,121,f"{serial}Info not Availabe"))
            except:
                print(f"{lp}{serial}Info not Availabe")
        except KeyboardInterrupt:
            print(f"{y}Process Stopped!")
            os._exit(1)
        except requests.exceptions.ChunkedEncodingError:
            pass
        except requests.exceptions.ConnectionError:
            print(f"{r}{serial}ConnectionError")
        except requests.exceptions.ReadTimeout:
            try:
                print(col(255,77,0,f"{serial}ReadTimeout"))
            except:
                print(f"{lr}{serial}ReadTimeout")
        except requests.exceptions.TooManyRedirects:
            try:
                print(col(107,0,194,f"{serial}Redirect Exceeded"))
            except:
                print(f"{p}{serial}Redirect Exceeded")

def url_file():
    proxies_socks4 = open(args.file)
    outfile = ""
    if os.path.exists(args.output):
        outa = args.output+f"({{}})"
        cnot = 1
        while os.path.exists(outa.format(cnot)):
            cnot += 1
        outfile += outa.format(cnot)
    else:
        outfile += args.output
    cnt = 0
    for line in proxies_socks4:
        cnt += 1
        serial = str(cnt)+". "
        proxy = line.split("\n")[0]
        # if (args.url).startwith("http://") or (args.url).startwith("https://"):
        try:
            print("working with"+str(args.url))
            response_socks4 = requests.get(url=args.url, proxies={"http":"socks4://"+proxy, "https":"socks4://"+proxy}, timeout=args.timeout)
            if response_socks4.status_code == 200:
                success = open(outfile,"a").write(proxy+"\n")
                print(f"{g}{serial}{proxy} success")
            else:
                print(f"{y}{serial}{proxy} "+str(response_socks4.status_code))
        except KeyError:
            try:
                print(col(237,26,121,f"{serial}Info not Availabe"))
            except:
                print(f"{lp}{serial}Info not Availabe")
        except KeyboardInterrupt:
            print(f"{y}Process Stopped!")
            os._exit(1)
        except requests.exceptions.ChunkedEncodingError:
            pass
        except requests.exceptions.ConnectionError:
            print(f"{r}{serial}ConnectionError")
        except requests.exceptions.ReadTimeout:
            try:
                print(col(255,77,0,f"{serial}ReadTimeout"))
            except:
                print(f"{lr}{serial}ReadTimeout")
        except requests.exceptions.TooManyRedirects:
            try:
                print(col(107,0,194,f"{serial}Redirect Exceeded"))
            except:
                print(f"{p}{serial}Redirect Exceeded")
        # except requests.exceptions.MissingSchema:
        #     print(f"{r}Use https:// or https://")


def socks4_check():
    if args.file:
        if args.timeout:
            if args.output:
                if args.dC:
                    file("continent")
                elif args.dc:
                    file("country")
                elif args.rn:
                    file("regionName")
                elif args.ct:
                    file("city")
                elif args.dt:
                    file("district")
                elif args.zip:
                    file("zip")
                elif args.lc:
                    key1,key2 = "lat","lon"
                    proxies_socks4 = open(args.file)
                    outfile = ""
                    if os.path.exists(args.output):
                        outa = args.output+f"({{}})"
                        cnot = 1
                        while os.path.exists(outa.format(cnot)):
                            cnot += 1
                        outfile += outa.format(cnot)
                    else:
                        outfile += args.output
                    cnt = 0
                    for line in proxies_socks4:
                        cnt += 1
                        serial = str(cnt)+". "
                        proxy = line.split("\n")[0]
                        try:
                            response_socks4 = requests.get(url=url2_api, proxies={"http":"socks4://"+proxy, "https":"socks4://"+proxy}, timeout=args.timeout)
                            if response_socks4.status_code == 200:
                                success = open(outfile,"a").write(proxy+" | location: "+str(response_socks4.json()[key1])+","+str(response_socks4.json()[key2])+"\n")
                                print(f"{g}{serial}{proxy} success | location: "+str(response_socks4.json()[key1])+","+str(response_socks4.json()[key2]))
                            else:
                                print(f"{y}{serial}{proxy} "+str(response_socks4.status_code))
                        except KeyError:
                            try:
                                print(col(237,26,121,f"{serial}Info not Availabe"))
                            except:
                                print(f"{lp}{serial}Info not Availabe")
                        except KeyboardInterrupt:
                            print(f"{y}Process Stopped!")
                            os._exit(1)
                        except requests.exceptions.ChunkedEncodingError:
                            pass
                        except requests.exceptions.ConnectionError:
                            print(f"{r}{serial}ConnectionError")
                        except requests.exceptions.ReadTimeout:
                            try:
                                print(col(255,77,0,f"{serial}ReadTimeout"))
                            except:
                                print(f"{lr}{serial}ReadTimeout")
                        except requests.exceptions.TooManyRedirects:
                            try:
                                print(col(107,0,194,f"{serial}Redirect Exceeded"))
                            except:
                                print(f"{p}{serial}Redirect Exceeded")
                elif args.isp:
                    file("isp")
                elif args.all:
                    proxies_socks4 = open(args.file)
                    outfile = ""
                    if os.path.exists(args.output):
                        outa = args.output+f"({{}})"
                        cnot = 1
                        while os.path.exists(outa.format(cnot)):
                            cnot += 1
                        outfile += outa.format(cnot)
                    else:
                        outfile += args.output
                    cnt = 0
                    for line in proxies_socks4:
                        cnt += 1
                        serial = str(cnt)+". "
                        proxy = line.split("\n")[0]
                        try:
                            response_socks4 = requests.get(url=url2_api, proxies={"http":"socks4://"+proxy, "https":"socks4://"+proxy}, timeout=args.timeout)
                            if response_socks4.status_code == 200:
                                res = str(response_socks4.json())
                                out = " | "+res.replace(","," |").replace("'","").replace("{","").replace("}","")
                                success = open(outfile,"a").write(proxy+out+"\n")
                                print(f"{g}{serial}{proxy}"+out)
                            else:
                                print(f"{y}{serial}{proxy} "+str(response_socks4.status_code))
                        except KeyError:
                            try:
                                print(col(237,26,121,f"{serial}Info not Availabe"))
                            except:
                                print(f"{lp}{serial}Info not Availabe")
                        except KeyboardInterrupt:
                            print(f"{y}Process Stopped!")
                            os._exit(1)
                        except requests.exceptions.ChunkedEncodingError:
                            pass
                        except requests.exceptions.ConnectionError:
                            print(f"{r}{serial}ConnectionError")
                        except requests.exceptions.ReadTimeout:
                            try:
                                print(col(255,77,0,f"{serial}ReadTimeout"))
                            except:
                                print(f"{lr}{serial}ReadTimeout")
                        except requests.exceptions.TooManyRedirects:
                            try:
                                print(col(107,0,194,f"{serial}Redirect Exceeded"))
                            except:
                                print(f"{p}{serial}Redirect Exceeded")
                else:
                    if args.file is None:
                        pass
                    else:
                        proxies_socks4 = open(args.file)
                        outfile = ""
                        if os.path.exists(args.output):
                            outa = args.output+f"({{}})"
                            cnot = 1
                            while os.path.exists(outa.format(cnot)):
                                cnot += 1
                            outfile += outa.format(cnot)
                        else:
                            outfile += args.output
                        cnt = 0
                        for line in proxies_socks4:
                            cnt += 1
                            serial = str(cnt)+". "
                            proxy = line.split("\n")[0]
                            try:
                                response_socks4 = requests.get(url=url_api, proxies={"http":"socks4://"+proxy, "https":"socks4://"+proxy}, timeout=args.timeout)
                                if response_socks4.status_code == 200:
                                    success = open(outfile,"a").write(proxy+"\n")
                                    print(f"{g}{serial}{proxy} success")
                                else:
                                    print(f"{y}{serial}{proxy} "+str(response_socks4.status_code))
                            except KeyError:
                                try:
                                    print(col(237,26,121,f"{serial}Info not Availabe"))
                                except:
                                    print(f"{lp}{serial}Info not Availabe")
                            except KeyboardInterrupt:
                                print(f"{y}Process Stopped!")
                                os._exit(1)
                            except requests.exceptions.ChunkedEncodingError:
                                pass
                            except requests.exceptions.ConnectionError:
                                print(f"{r}{serial}ConnectionError")
                            except requests.exceptions.ReadTimeout:
                                try:
                                    print(col(255,77,0,f"{serial}ReadTimeout"))
                                except:
                                    print(f"{lr}{serial}ReadTimeout")
                            except requests.exceptions.TooManyRedirects:
                                try:
                                    print(col(107,0,194,f"{serial}Redirect Exceeded"))
                                except:
                                    print(f"{p}{serial}Redirect Exceeded")
        elif args.url:
            if args.timeout:
                if args.output:
                    url_file()
        else:
            pass
    else:
        print(r+"Input Proxy File")