# coding: utf-8
import requests
import json
'''
    使用联众打码平台API进行在线识别验证码
'''

def main(api_username, api_password, file_name, api_post_url, yzm_min, yzm_max, yzm_type, tools_token):
    '''
            main() 参数介绍
            api_username    （API账号）             --必须提供
            api_password    （API账号密码）         --必须提供
            file_name       （需要识别的图片路径）   --必须提供
            api_post_url    （API接口地址）         --必须提供
            yzm_min         （识别结果最小长度值）        --可空提供
            yzm_max         （识别结果最大长度值）        --可空提供
            yzm_type        （识别类型）          --可空提供
            tools_token     （工具或软件token）     --可空提供
    '''
    # api_username ='warflor'
    # api_password = 'lianzhong0608.'
    # file_name = 'E:/code.png'
    # api_post_url = "http://v1-http-api.jsdama.com/api.php?mod=php&act=upload"
    # yzm_min = '1'
    # yzm_max = '8'
    # yzm_type = '1013'
    # tools_token = api_username

    # proxies = {'http': 'http://127.0.0.1:8888'}
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
        'Accept-Encoding': 'gzip, deflate',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:53.0) Gecko/20100101 Firefox/53.0',
        # 'Content-Type': 'multipart/form-data; boundary=---------------------------227973204131376',
        'Connection': 'keep-alive',
        'Host': 'v1-http-api.jsdama.com',
        'Upgrade-Insecure-Requests': '1'
    }

    files = {
        'upload': (file_name, open(file_name, 'rb'), './code.png')
    }

    data = {
        'user_name': api_username,
        'user_pw': api_password,
        'yzm_minlen': yzm_min,
        'yzm_maxlen': yzm_max,
        'yzmtype_mark': yzm_type,
        'zztool_token': tools_token
    }
    s = requests.session()
    # r = s.post(api_post_url, headers=headers, data=data, files=files, verify=False, proxies=proxies)
    r = s.post(api_post_url, headers=headers, data=data, files=files, verify=False)
    # print(r.text)
    result=r.json()
    code=result['data']['val']
    # print(code)
    return code
# 下载验证码
'''
def download_vcode():
    try:
        url = 'http://www.5itest.cn/captcha_num?0.4733862790517711'
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'}
        s = requests.session()
        resp = s.get(url, headers=headers, verify=False)
        file_name = 'E:/code.png'
        with open(file_name, 'wb') as f:
            f.write(resp.content)
    except Exception as e:
        print(e)
'''

if __name__ == '__main__':
    # download_vcode()
    main('warflor',
         'lianzhong0608.',
         './code.png',
         "http://v1-http-api.jsdama.com/api.php?mod=php&act=upload",
         '1',
         '8',
         '1013',
         '')

    '''
		main() 参数介绍
		api_username    （API账号）             --必须提供
		api_password    （API账号密码）         --必须提供
		file_name       （需要识别的图片路径）   --必须提供
		api_post_url    （API接口地址）         --必须提供
		yzm_min         （识别结果最小长度值）        --可空提供
		yzm_max         （识别结果最大长度值）        --可空提供
		yzm_type        （识别类型）          --可空提供
		tools_token     （工具或软件token）     --可空提供
    '''
