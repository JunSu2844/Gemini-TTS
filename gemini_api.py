

# gemini 라이브러리 선언 애칭 gemai
import google.generativeai as gemai

# 1. API 키 설정
def configure_gemiai(api_key):
    """Gemini API 키 설정"""
    gemai.configure(api_key=api_key)

# 2.Gemini 모델 가져오기
def get_gemini_response(user_input, model_name="gemini-2.0-flash"):
    """Gemini 모델을 사용하여 응답 생성"""
    model = gemai.GenerativeModel(model_name)
    response = model.generate_content(user_input)
    # 여기가 핵심! 응답을 문자열로 변환
    return response.text