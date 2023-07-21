import re
import pysrt
from pysrt import SubRipTime

srt_split_index = (
    #[1/10]
    (
        7, 10, 15, 16, 17, 18, 19, 22, 23, 25
    ),
    #[2/10]
    (
        44, 55, 56, 57, 64, 65, 66, 67, 68, 69
    ),
    #[3/10]
    (
        78, 79, 80, 81, 82, 83, 84, 85, 86, 87
    ),
    #[4/10]
    (
        88, 91, 92, 93, 94, 95, 96, 97, 98, 99
    ),
    #[5/10]
    (
        122, 123, 124, 126, 127, 128, 129, 131, 138, 148
    ),
    #[6/10]
    (
        150, 151, 154, 158, 176, 181, 182, 183, 190, 198
    ),
    #[7/10]
    (
        200, 201, 212, 215, 216, 226, 227, 228, 232, 233
    ),
    #[8/10]
    (
        246, 247, 248, 249, 253, 254, 256, 257, 258, 259
    ),
    #[9/10]
    (
        305, 318, 319, 347, 348, 365, 371, 372, 387, 388
    ),
    #[10/10]
    (
        509, 528, 533, 534, 542, 549, 550, 556, 565, 566
    )
)

# SRT 파일 읽기
subtitles = pysrt.open("C:\\Users\\idhpaul\\Videos\\4K Video Downloader\\Elon Musk The future we're building -- and boring   TED.ko.srt")


for i in range(10):
  for j in range(10):
        print(i, j)

        idx = srt_split_index[i][j]

        stub = subtitles[idx-1]

        print(stub.duration)

        f = open(str(i)+"_"+str(j+1)+".txt", 'w',encoding='utf8')
        # f.write("0\n")
        # f.write("00:00:00,000 --> ")
        # f.write(str(stub.duration)+"\n")
        f.write(stub.text)

        f.close()

