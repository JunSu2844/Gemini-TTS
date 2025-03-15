import os
import time

from gtts import *
import playsound


# MP3 파일 크기 확인 함수
def get_file_size(file_path):
    """ 파일 크기를 반환, 없으면 -1 """
    return os.path.getsize(file_path) if os.path.isfile(file_path) else -1

# MP3 파일 크기 검사 후 재생하는 함수
def wait_for_file_stabilization(file_path, check_interval=2, max_checks=5):
    """ 파일 크기가 일정 시간 동안 볂나지 않으면 재생 """
    previous_size = get_file_size(file_path)

    if previous_size == -1 :
        print("❌ 파일이 존재하지 않습니다.")
        return

    checks = 0
    while checks < max_checks :
        time.sleep(check_interval)
        current_size = get_file_size(file_path)

        if current_size == previous_size :
            print("✅ 파일 크기 변동 없음, MP3 재생 시작!")
            playsound.playsound(file_path)
            return
        else :
            print("⏳ 파일 크기 변화 감지 중...")
            previous_size = current_size
            checks += 1

    print("⚠️ 일정 시간 동안 파일 크기가 안정되지 않음.")

# 텍스트를 음성으로 변환 후 재생
def speak(text, filename="geminiTest-TTS.mp3") :
    """ 텍스트를 음성으로 변환 후 MP3 저장 및 재생"""
    tts = gTTS(text=text, lang='ko')
    tts.save(filename) # 파일 저장
    wait_for_file_stabilization(filename) # 안정화 후 재생

