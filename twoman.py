from gtts import gTTS
from pydub import AudioSegment

# ffmpeg 경로 설정
AudioSegment.converter = "C:\\Users\\602-8\Downloads\\ffmpeg-master-latest-win64-gpl\\bin\\ffmpeg.exe"
AudioSegment.ffprobe = "C:\\Users\\602-8\Downloads\\ffmpeg-master-latest-win64-gpl\\bin\\ffprobe.exe"

# 대화 내용: 두 남자의 대화
dialogue = [
    ("안녕하세요, 오늘 어떻게 지내세요?", "ko"),  # 첫 번째 남자의 대사
    ("안녕하세요! 오늘 날씨가 정말 좋네요.", "ko"),  # 두 번째 남자의 대사
    ("네, 그러게요. 이런 날씨엔 산책하기 딱 좋죠.", "ko"),
    ("맞아요, 주말에 산에 가는 것도 좋을 것 같아요.", "ko"),
    ("좋은 생각이에요! 같이 가실래요?", "ko"),
    ("그럼요, 시간 정해서 알려주세요.", "ko")
]

# 음성 파일 생성 및 저장
tts_segments = []
for i, (sentence, lang) in enumerate(dialogue):
    tts = gTTS(text=sentence, lang=lang)
    filename = f"segment_{i}.mp3"
    tts.save(filename)
    tts_segments.append(AudioSegment.from_mp3(filename))

# 모든 세그먼트를 연결하여 하나의 오디오 파일로 만듦
final_audio = sum(tts_segments)

# MP3 및 WAV 파일로 저장
mp3_filename = "male_conversation.mp3"
wav_filename = "male_conversation.wav"

final_audio.export(mp3_filename, format="mp3")
final_audio.export(wav_filename, format="wav")

print(f"대화 음성 파일이 생성되었습니다: {mp3_filename} 및 {wav_filename}")
