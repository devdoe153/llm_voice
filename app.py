import os
import json
import time
import streamlit as st
from streamlit_option_menu import option_menu


save_dir = os.path.join('.', "SpeechNote")
os.makedirs(save_dir, exist_ok=True)
list_notes = os.listdir(save_dir)

st.set_page_config(page_title="SpeechNote", page_icon="🎤")
st.title("SpeechNote 🎤")
st.write("SpeechNote is a tool that helps you take notes with voices")

sound_file = st.file_uploader("Upload a sound file", type=["mp3", "wav"], disabled=False)

# transcript = None
# summary = None

if "transcript" not in st.session_state:
    st.session_state.transcript = None

if "summary" not in st.session_state:
    st.session_state.summary = None

######### side bar ###########
with st.sidebar:
    selected = option_menu(
        "Notes",
        ["New"] + list_notes,
        menu_icon="book",
        default_index=0,
    )

if selected != "New":
    file_list = os.listdir(os.path.join(save_dir, selected))

    for file in file_list:
        extention = os.path.splitext(file)[1]
        if extention in [".wav", ".mp3", ".ogg", ".flac"]:
            sound_file = open(os.path.join(save_dir, selected, file), "rb")
            break

##############################

### sound file 읽고 저장 ###

if sound_file:
    st.audio(sound_file, format="audio/wav")

    if sound_file.__class__.__name__ == "UploadedFile":
        soundfile_name = sound_file.name
    else:
        soundfile_name = file


    file_name = os.path.splitext(soundfile_name)[0]
    file_path = os.path.join(save_dir, file_name)
    os.makedirs(file_path, exist_ok=True)

    soundfile_path = os.path.join(file_path, soundfile_name)
    transcriptfile_path = os.path.join(file_path, f"{file_name}.jsonl")
    summaryfile_path = os.path.join(file_path, f"{file_name}_summary.txt")

    with open(soundfile_path, 'wb') as f:
        f.write(sound_file.read())

#############

####### transcribe, summarize 버튼 추가 ########


col1, col2 = st.columns(2)
transcript_bnt = col1.button("Transcribe")
speaker_num_slider = col1.slider("Number of speakers", min_value=1, max_value=10, value=1)
summary_bnt = col2.button("Summarize")

if transcript_bnt:
    with st.spinner("Transcribing..."):
        time.sleep(3)
        st.session_state.transcript = [
            {
                "label":"speaker1",
                "start":0.0,
                "end":1.0,
                "text":"Hello, world!"
            },
            {
                "label":"speaker2",
                "start":0.0,
                "end":1.0,
                "text":"Hi, world!"
            }
        ]

    with open(transcriptfile_path, "w") as f:
        for segment in st.session_state.transcript:
            json.dump(segment, f, ensure_ascii=False)
            f.write("\n")

if st.session_state.transcript is not None:
    st.write("Transcript:")
    for item in st.session_state.transcript:
        st.text_area(f"{item['label']} ({item['start'] - item['end']})", item['text'])

    ####### download #########
    download_data = ""
    for item in st.session_state.transcript:
        speaker = item['label']
        text = item['text']
        download_data += f"{speaker}: {text}\n"

    st.download_button(
        label="Download Transcript",
        data=download_data,
        file_name=f"{file_name}.txt",
        mime="application/txt",
    )

    ###############

if summary_bnt and st.session_state.transcript is not None:
    with st.spinner("Summarizing ..."):
        time.sleep(3)
        st.session_state.summary = "Hello world! Hi there!"

    with open(summaryfile_path, "w") as f:
        f.write(st.session_state.summary)

if st.session_state.summary is not None:
    st.write("Summary:")
    st.text_area("Summary", st.session_state.summary)

###########################################    






