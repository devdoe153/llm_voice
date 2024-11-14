from gtts import gTTS
from pydub import AudioSegment

# 대화 내용: 두 남자가 대화를 나누는 형식
dialogue = [
    "안녕하세요, 오늘 날씨가 정말 좋네요.",  # 첫 번째 남자
    "네, 정말 그러네요. 이런 날엔 나가서 운동하기 딱이죠.",  # 두 번째 남자
    "운동 좋아하시나 봐요? 요즘 어떤 운동 하세요?",  # 첫 번째 남자
    "저는 주로 조깅을 합니다. 요즘은 주말마다 산책도 하고요.",  # 두 번째 남자
    "좋네요. 저도 조깅 해봐야겠어요. 좋은 하루 되세요!",  # 첫 번째 남자
    "네, 즐거운 하루 되세요!"  # 두 번째 남자
]

# 각 대화문을 TTS로 변환하고 음성 파일로 저장
tts_segments = []
for sentence in dialogue:
    tts = gTTS(text=sentence, lang='ko')
    tts.save("temp.mp3")
    tts_segments.append(AudioSegment.from_mp3("temp.mp3"))

# 모든 세그먼트를 연결하여 하나의 오디오 파일로 만듦
final_audio = sum(tts_segments)

# 전체 길이를 30초로 제한 (필요시 앞 부분 자르기)
final_audio = final_audio[:30000]  # 30초 (밀리초 단위)

# MP3 파일로 저장
mp3_filename = "conversation_30s.mp3"
final_audio.export(mp3_filename, format="mp3")

print(f"대화 음성 파일이 생성되었습니다: {mp3_filename}")
