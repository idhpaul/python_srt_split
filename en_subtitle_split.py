import re
import pysrt
from pysrt import SubRipTime

srt_split_index = (
    #[1/10]
    (
        7,
        10,
        15,
        16,
        17,
        18,
        19,
        22,
        23,
        25
    ),
    #[2/10]
    (
        44,
        55,
        56,
        57,
        64,
        65,
        66,
        67,
        68,
        69
    ),
    #[3/10]
    (
        78,
        79,
        80,
        81,
        82,
        83,
        84,
        85,
        86,
        87
    ),
    #[4/10]
    (
        88,
        92,
        93,
        94,
        95,
        96,
        97,
        98,
        99,
        100
    ),
    #[5/10]
    (
        123,
        124,
        125,
        127,
        128,
        129,
        130,
        132,
        139,
        149
    ),
    #[6/10]
    (
        151,
        152,
        155,
        159,
        177,
        182,
        183,
        184,
        191,
        199
        
    ),
    #[7/10]
    (
        201,
        202,
        213,
        216,
        217,
        227,
        228,
        229,
        233,
        234
    ),
    #[8/10]
    (
        247,
        248,
        249,
        250,
        254,
        255,
        257,
        258,
        259,
        260
    ),
    #[9/10]
    (
        306,
        319,
        320,
        348,
        349,
        366,
        372,
        373,
        388,
        389
    ),
    #[10/10]
    (
        510,
        529,
        534,
        535,
        543,
        550,
        551,
        557,
        566,
        567
    )
)

# SRT 파일 읽기
subtitles = pysrt.open("C:\\Users\\idhpaul\\Videos\\4K Video Downloader\\Elon Musk The future we're building -- and boring   TED.en.srt")


for i in range(10):
  for j in range(10):
        print(i, j)

        idx = srt_split_index[i][j]

        stub = subtitles[idx-1]

        print(stub.duration)

        f = open(str(i)+"_"+str(j+1)+".en.srt", 'w')
        f.write("0\n")
        f.write("00:00:00,000 --> ")
        f.write(str(stub.duration)+"\n")
        f.write(stub.text)

        f.close()

