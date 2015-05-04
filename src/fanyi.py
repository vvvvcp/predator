import urllib2
import json
import re
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
def convertjson(dresult):
    try:
        ddata=json.loads(dresult)
        result1=ddata["trans_result"]
        result2=result1[0]["dst"]
    except:
        return "error"
    return result2

def fanyi(input):
    url='http://openapi.baidu.com/public/2.0/bmt/translate?client_id=BYmhcXRTFZWi9G4awm0OOshG&q=%s&from=auto&to=auto'
    #input=raw_input("input:")
    full=url%input
    data=urllib2.urlopen(full)
    Data=data.read()
    result=convertjson(Data)
    print result
    return result

if __name__=='__main__':
    file_object = open('messages.po','r')
    file_write = open('msgbackup.po','w+')
    lines=file_object.readlines()
    for line in lines:
        if "msgid" in line:
            findmsg=re.findall(r"\"(.+?)\"",line)
            file_write.write(line)
            print findmsg[0]
            result=fanyi(findmsg[0])
            file_write.write("msgstr \"%s\""%result)
            file_write.write("\n\n")
        #if "msgstr" in line:
         #   line.repalce("msgstr \"%s\""%result)
            #print"huxiao"
            #file_object.write("msgstr \"%s\""%result)
    file_object.close()
    file_write.close()
