import os
from google.cloud import texttospeech

# Google Cloud 서비스 계정 키 파일 경로
key_file_path = '/home/jetson/Desktop/LangChain-StoryBot-main/tts_module/ai-tory-d429a82ee164.json'

# 텍스트를 음성으로 변환할 텍스트
text = """hello"""

def gtts(str, fileName):
    # Google Cloud Text-to-Speech API 클라이언트 초기화
    client = texttospeech.TextToSpeechClient.from_service_account_json(key_file_path)

    # 음성 합성 매개변수 설정 (WaveNet 사용)
    voice = texttospeech.VoiceSelectionParams(
        language_code="ko-KR", name="ko-KR-Neural2-A", ssml_gender=texttospeech.SsmlVoiceGender.FEMALE
    )

    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.LINEAR16,
            speaking_rate=0.9,  # speaking_rate를 조절하여 음성을 느리게 만듭니다.
            pitch= -3.6
    )
    # 텍스트를 음성으로 변환
    input_text = texttospeech.SynthesisInput(text=str)
    response = client.synthesize_speech(
        input=input_text, voice=voice, audio_config=audio_config
    )

    # WaveNet으로 생성된 음성을 파일로 저장
    with open(f"/home/jetson/Desktop/LangChain-StoryBot-main/assist/wav/{fileName}.wav", "wb") as out_file:
        out_file.write(response.audio_content)

    # 음성 파일 재생 (예: macOS)
    os.system(f"aplay /home/jetson/Desktop/LangChain-StoryBot-main/assist/wav/{fileName}.wav")

story = """"
어느 겨울날 눈처럼 하얀 피부, 밤하늘처럼 새까만 머리카락, 사과처럼 붉은 입술을 가진 예쁜 여자아이가 태어났어요.
하얀 눈을 닮았다고 하여 백설공주라고 이름 붙였죠.
하지만 탄생의 기쁨도 잠시 불행히도 왕비는 병으로 세상을 떠나고 말았답니다.
왕은 왕비가 죽고 얼마 지나지 않아 새로운 왕비를 맞이합니다.
예쁘긴 했지만 잘난 체하고 뽐내길 좋아하는 왕비였어요.
그녀는 신비한 거울에게 세상에서 누가 가장 아름다운지 물어보곤 했답니다.
시간이 지나 백설공주가 예쁘게 자라고 신기한 거울이 백설공주가 새 왕비보다 더 이쁘다고 하자 화가 난 새 왕비는 사냥꾼에게 숲으로 백설공주를 데려가 죽이라고 명령했어요.
하지만 사냥꾼은 공주를 차마 죽이지 못하고 풀어줬어요.
공주는 울퉁불퉁 돌밭을 넘고 뾰족뾰족 가시밭을 지나 내달리는 중 자그마한 오두막집을 발견합니다.
삐걱!
문을 열고 들어간 오두막의 살림살이는 모두 작고 접시, 컵, 침대가 일곱 개씩 있었지요.
배가 고파진 백설공주는 오물오물 빵과 꿀꺽꿀꺽 포도주를 먹기 시작했어요.
이 작은 집은 금을 캐는 일곱 난쟁이들의 집이었어요.
일곱 난쟁이들에게 그동안 있던 일을 이야기해주는 백설공주는 일곱 난쟁이들과 함께 지내게 되었답니다.
한편, 왕비는 백설공주가 죽었다고 생각했지만 거울의 세상에서 제일 아름다운 사람은 백설공주라는 말에 얼굴이 붉으락 푸르락 충격을 받고 직접 백설공주를 죽이기로 결심합니다.
왕비는 할머니로 변장하고 백설공주를 예쁜 비단 끈으로 유혹한 뒤 허리를 꽉꽉 졸라 매 버렸어요.
숨을 못 쉬게 된 백설공주는 쓰러졌지만 다행히 돌아온 일곱 난쟁이들 덕에 살아나고 난쟁이들은 백설공주에게 혼자 있을때는 아무에게도 문을 열어주지 말라고 이야기 합니다.
왕비는 신나서 성으로 돌아갔지만 거울의 이야기로 백설공주가 또 살아 있다는 것을 알고 이번에는 머리핀에 독을 발라 백설공주 머리에 꽂았어요.
독이 몸에 퍼졌지만 일곱 난쟁이들의 도움으로 또 목숨을 부지합니다.
성으로 돌아간 왕비는 또 화가 납니다.
왜냐하면 백설공주가 아직도 살아있다는 이야기를 거울에게 듣기 때문이죠.
왕비는 할머니로 변장하고 백설공주에게 찾아가 독이 든 사과를 권하지만 당연히 백설공주는 경계하고 문도 열어주지 않죠!
하지만 새 왕비는 사과를 반으로 쪼개 푸른 쪽을 자신이 먹고 붉은 쪽을 백설공주에게 줍니다.
경계를 푼 백설공주는 와사삭 사과를 먹고 독 때문에 쓰러지고 맙니다.
알고 보니 독을 반쪽에만 넣어둔 거였어요.
쓰러진 백설공주에게 난쟁이들이 옷의 끈도 풀어보고 머리핀도 빼고 물도 먹여 보았지만 일어나지 못했어요.
백설공주를 유리관에 넣고 사흘 밤낮으로 슬퍼하는 난쟁이들 앞에 이웃나라 왕자가 찾아왔어요.
백설공주에게 한눈에 반한 왕자는 자신이 소중히 지킬 테니 백설공주를 달라고 부탁하고 난쟁이들도 넘겨주기로 합니다.
관을 옮기는 도중 거친 길 때문에 관이 흔들리자 백설공주 목구멍에 걸려있던 독사과 조각이 툭! 나오고 왕자는 이를 기뻐하며 공주에게 청혼합니다.
두 사람의 결혼식날 새 왕비도 찾아옵니다.
왜냐하면 거울이 세상에서 제일 아름다운 건 이웃나라 왕자의 새 신부라고 했기 때문이죠.
결혼식에 온 새 왕비는 놀랍니다.
죽은 줄 알았던 백설공주가 그 새 신부였기 때문이죠. 왕자는 새 왕비를 보곤 달 구어진 쇠 구두를 내밀며 이걸 신고 춤을 추던가 아니면 다시는 나타나지 말라고 해요.
그 뒤 새 왕비를 본 사람은 없었다고 합니다.
"""
#gtts(story, 'snow_white')