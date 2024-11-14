from gtts import gTTS
import os
from pydub import AudioSegment

# 대화 텍스트 목록
dialogue = [
    "안녕하세요. 오늘 날씨가 정말 좋네요.",
    "맞아요! 이렇게 맑은 날씨는 정말 드물죠.",
    "계획이 있으신가요? 저는 공원에 갈까 생각 중이에요.",
    "좋은 생각이에요! 저도 함께 갈까요?",
    "물론이죠! 피크닉 준비를 해볼까요?",
    "네, 음식을 좀 준비해 볼게요. 과일과 샌드위치 어떠세요?",
    "완벽해요! 그럼 음료수는 제가 챙길게요.",
    "좋아요, 그럼 30분 후에 공원 입구에서 만나요!",
    "알겠습니다. 기대돼요!"
]

# 개별 문장을 음성으로 변환하고 파일로 저장
tts_segments = []
for i, sentence in enumerate(dialogue):
    tts = gTTS(text=sentence, lang='ko')
    filename = f"segment_{i}.mp3"
    tts.save(filename)
    tts_segments.append(AudioSegment.from_mp3(filename))

# 모든 세그먼트를 연결하여 하나의 오디오 파일로 만듦
final_audio = sum(tts_segments)

# 음성 길이가 1분이 될 때까지 반복하여 추가 (필요 시)
while len(final_audio) < 60000:  # 1분 = 60,000 밀리초
    final_audio += sum(tts_segments)

# 최종 오디오 파일을 MP3 및 WAV로 저장
mp3_filename = "1min_conversation.mp3"
wav_filename = "1min_conversation.wav"

final_audio.export(mp3_filename, format="mp3")
final_audio.export(wav_filename, format="wav")

print(f"1분짜리 대화 음성 파일이 생성되었습니다: {mp3_filename} 및 {wav_filename}")
