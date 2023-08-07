import librosa
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

def load_audio(audio_file):
    # WAV 파일을 불러옵니다.
    y, sr = librosa.load(audio_file)
    
    return y, sr

def compare_similarity(file1, file2):
    # 두 WAV 파일을 불러옵니다.
    y1, sr1 = load_audio(file1)
    y2, sr2 = load_audio(file2)
    
    # 두 WAV 파일의 길이를 동일하게 맞춥니다. (길이가 다른 경우)
    min_len = min(len(y1), len(y2))
    y1 = y1[:min_len]
    y2 = y2[:min_len]
    
    # 두 WAV 파일의 시계열 데이터 간의 유사성을 측정합니다.
    similarity = cosine_similarity(y1.reshape(1, -1), y2.reshape(1, -1))
    
    return similarity[0][0]

if __name__ == "__main__":
    # 비교할 두 개의 WAV 파일 경로
    wav_file1 = "1.wav"
    wav_file2 = "1_sep.wav"
    
    similarity_score = compare_similarity(wav_file1, wav_file2)
    print(f"두 WAV 파일의 유사도: {similarity_score}")