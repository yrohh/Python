# 주의
# 1..단과 2..단의 경우 주석 처리하여 순서대로 실행
# 카카오톡 토큰 출력의 경우, 인증코드를 이용하여 한 번만 수행하고 한 번 더 수행 필요할 시 인증코드를 다시 받아야 함

# 참고 링크
# https://ai-creator.tistory.com/170 - 토큰 받기
# https://kangprog.tistory.com/97 - 토큰 받기
# https://github.com/conda/conda/issues/8273 - ssl 에러 해결
# https://ai-creator.tistory.com/23?category=759438 - 메시지 전송


# 1.. 카카오톡 토큰 출력
import requests

url = 'https://kauth.kakao.com/oauth/token'
rest_api_key = 'REST_API_KEY 붙여넣기'
redirect_uri = 'https://localhost.com' # APP에서 등록한 redirect_url
authorize_code = '받은 인증코드 붙여넣기' 
 
data = {
        'grant_type':'authorization_code',
        'client_id':rest_api_key,
        'redirect_uri':redirect_uri,
        'code': authorize_code,
    }

response = requests.post(url, data=data)
tokens = response.json()
print(tokens["access_token"])


import json
import requests

url = "https://kapi.kakao.com/v2/api/talk/memo/default/send"

# 2.. 토큰 이용하여 메시지 전송
headers = {
    "Authorization": "Bearer " + 'access token 붙여넣기'
}


data = {
    "template_object" : json.dumps({ "object_type" : "text",
                                     "text" : "Hello, world!",
                                     "link" : {
                                                 "web_url" : "www.naver.com"
                                              }
    })
}

response = requests.post(url, headers=headers, data=data) # 이 부분이 메시지 전송절
print(response.status_code) # 200이 나오면 성공
if response.json().get('result_code') == 0:
    print('메시지를 성공적으로 보냈습니다.')
else:
    print('메시지를 성공적으로 보내지 못했습니다. 오류메시지 : ' + str(response.json()))
