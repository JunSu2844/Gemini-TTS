

# text_to_speech 모듈 사용(speak 클래스)
from text_to_speech import speak

# gemini_api 에서 configure_gemini : API 사용할 수 있는 함수
# get_gemini_response : Gemini 모델의 요청 처리
from gemini_api import get_gemini_response, configure_gemiai

# 1. Gemini API 설정
API_KEY = "MY_API_KEY"
configure_gemiai(API_KEY)

# 2. 유저 입력 및 응답 처리 루프

while True :
    user_input = input('(종료 명령어 : exit) \n'
                       '사용 모델 : Gemini-2.0-flash \n'
                       '무엇이든 물어보세요 : ')

    if user_input == 'exit':
        print('Gemini-2.0-flash 종료 합니다.')
        break

    # 3. Gemini API 응답 가져오기
    response_text = get_gemini_response(user_input)


    # 4. 응답을 음성으로 변환 후 출력
    speak(response_text)
    #speak가 리턴해주는 값은 객체인데 그걸 response.text로 하여 문자열로 받음

    # 5. 응답 텍스트 출력
    print(response_text)
