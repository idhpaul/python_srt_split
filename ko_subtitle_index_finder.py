import re
import pysrt
from pysrt import SubRipTime

def split_time(time_str):
  """
  time_str: 문자열로 된 시간

  Returns:
    hour: 시간
    min: 분
    second: 초
    ms: 밀리초
  """

  match = re.match(r'(\d{2}):(\d{2}):(\d{2})\.(\d{3})', time_str)
  hour = int(match.group(1))
  min = int(match.group(2))
  second = int(match.group(3))
  ms = int(match.group(4))

  return hour, min, second, ms

def find_index_srt(srt, h,m,s,ms):
  
    t1=SubRipTime(h,m,s,ms)

    for i in range(len(srt)):
        s1=srt[i]

        if t1 == s1.start:
            return s1.index

video_split_timestamp = (
    #[1/10]
    (
        ('00:00:27.200', '00:00:31.296'),
        ('00:00:34.320', '00:00:35.870'),
        ('00:00:53.760', '00:00:59.296'),
        ('00:00:59.320', '00:01:02.176'),
        ('00:01:02.200', '00:01:06.016'),
        ('00:01:06.040', '00:01:08.016'),
        ('00:01:08.040', '00:01:09.656'),
        ('00:01:14.320', '00:01:16.774'),
        ('00:01:16.800', '00:01:18.136'),
        ('00:01:20.880', '00:01:22.735')
    ),
    #[2/10]
    (
        ('00:02:19.280', '00:02:21.576'),
        ('00:02:49.640', '00:02:56.016'),
        ('00:02:56.040', '00:02:58.816'),
        ('00:02:58.840', '00:03:02.136'),
        ('00:03:14.280', '00:03:18.056'),
        ('00:03:18.080', '00:03:21.736'),
        ('00:03:21.760', '00:03:23.999'),
        ('00:03:24.023', '00:03:29.416'),
        ('00:03:29.440', '00:03:33.416'),
        ('00:03:33.440', '00:03:37.936')
    ),
    #[3/10]
    (
        ('00:04:01.800', '00:04:05.776'),
        ('00:04:05.800', '00:04:08.656'),
        ('00:04:08.680', '00:04:11.856'),
        ('00:04:11.880', '00:04:16.135'),
        ('00:04:16.160', '00:04:19.736'),
        ('00:04:19.760', '00:04:23.416'),
        ('00:04:23.440', '00:04:26.656'),
        ('00:04:26.680', '00:04:30.576'),
        ('00:04:30.600', '00:04:33.456'),
        ('00:04:33.480', '00:04:36.696')
    ),
    #[4/10]
    (
        ('00:04:36.720', '00:04:41.616'),
        ('00:04:48.400', '00:04:50.736'),
        ('00:04:50.760', '00:04:52.976'),
        ('00:04:53.000', '00:04:55.216'),
        ('00:04:55.240', '00:04:59.896'),
        ('00:04:59.920', '00:05:02.976'),
        ('00:05:03.000', '00:05:05.136'),
        ('00:05:05.160', '00:05:09.336'),
        ('00:05:09.360', '00:05:13.576'),
        ('00:05:13.600', '00:05:16.576')
    ),
    #[5/10]
    (
        ('00:06:12.600', '00:06:16.456'),
        ('00:06:16.480', '00:06:19.416'),
        ('00:06:19.440', '00:06:22.496'),
        ('00:06:25.840', '00:06:28.400'),
        ('00:06:32.000', '00:06:34.696'),
        ('00:06:34.720', '00:06:37.280'),
        ('00:06:38.440', '00:06:43.056'),
        ('00:06:45.200', '00:06:48.760'),
        ('00:07:09.280', '00:07:12.816'),
        ('00:07:41.320', '00:07:46.776')
    ),
    #[6/10]
    (
        ('00:07:50.520', '00:07:54.880'),
        ('00:07:56.440', '00:08:00.376'),
        ('00:08:05.080', '00:08:10.096'),
        ('00:08:17.240', '00:08:21.856'),
        ('00:09:07.600', '00:09:13.296'),
        ('00:09:27.040', '00:09:29.896'),
        ('00:09:29.920', '00:09:31.536'),
        ('00:09:31.560', '00:09:35.616'),
        ('00:09:49.000', '00:09:51.880'),
        ('00:10:19.560', '00:10:22.536')
    ),
    #[7/10]
    (
        ('00:10:24.560', '00:10:27.136'),
        ('00:10:27.160', '00:10:28.640'),
        ('00:10:50.880', '00:10:53.496'),
        ('00:10:57.040', '00:11:01.920'),
        ('00:11:03.320', '00:11:08.016'),
        ('00:11:38.040', '00:11:42.336'),
        ('00:11:42.360', '00:11:46.976'),
        ('00:11:47.000', '00:11:48.896'),
        ('00:12:02.120', '00:12:04.336'),
        ('00:12:04.360', '00:12:09.416')
    ),
    #[8/10]
    (
        ('00:12:43.280', '00:12:48.256'),
        ('00:12:48.280', '00:12:49.536'),
        ('00:12:49.560', '00:12:53.856'),
        ('00:12:53.880', '00:12:56.240'),
        ('00:13:03.960', '00:13:07.656'),
        ('00:13:07.680', '00:13:11.760'),
        ('00:13:16.320', '00:13:20.896'),
        ('00:13:20.920', '00:13:25.575'),
        ('00:13:25.600', '00:13:27.776'),
        ('00:13:27.800', '00:13:31.199')
    ),
    #[9/10]
    (
        ('00:15:56.960', '00:16:01.760'),
        ('00:16:44.400', '00:16:46.536'),
        ('00:16:46.560', '00:16:49.280'),
        ('00:18:14.280', '00:18:16.576'),
        ('00:18:16.600', '00:18:20.000'),
        ('00:19:06.280', '00:19:08.256'),
        ('00:19:28.120', '00:19:31.416'),
        ('00:19:31.440', '00:19:32.821'),
        ('00:20:06.120', '00:20:07.376'),
        ('00:20:07.400', '00:20:10.560')
    ),
    #[10/10]
    (
        ('00:26:25.480', '00:26:27.736'),
        ('00:27:21.200', '00:27:22.536'),
        ('00:27:31.280', '00:27:35.216'),
        ('00:27:35.240', '00:27:36.440'),
        ('00:27:57.480', '00:27:58.840'),
        ('00:28:16.640', '00:28:20.256'),
        ('00:28:20.280', '00:28:24.760'),
        ('00:28:38.320', '00:28:42.376'),
        ('00:29:06.200', '00:29:10.296'),
        ('00:29:10.320', '00:29:13.576')
    )
)
ko_video_split_time_idx=[]
ko_video_split_time_idx_j = []

# SRT 파일 읽기
subtitles = pysrt.open("C:\\Users\\idhpaul\\Videos\\4K Video Downloader\\Elon Musk The future we're building -- and boring   TED.ko.srt")

for i in range(10):
  for j in range(10):

    time_str = video_split_timestamp[i][j][0]
    h, m, s, ms = split_time(time_str)

    idx = find_index_srt(subtitles,h,m,s,ms)
    print(idx,time_str)

    ko_video_split_time_idx.append(idx)


print(ko_video_split_time_idx)

list_of_100_values = ko_video_split_time_idx

list_of_10_groups = [list_of_100_values[i:i + 10] for i in range(0, len(list_of_100_values), 10)]

print(list_of_10_groups)

