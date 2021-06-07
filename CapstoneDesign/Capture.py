import cv2
import pafy
import os
# 유튜브 url 에서 캡쳐하기 # url =

# "캡쳐하고싶은유튜브동영상주소"
# 유튜브 url 주소
# video = pafy.new(url)
# best = video.ge
# tbest(preftype="mp4")
# vidcap = cv2.VideoCapture()
# vidcap.open(best.url)
# 로컬 저장소에 있는 동영상에서 캡쳐하기

def capture(a) :

    videoFile = f"C:/Users/pc/PycharmProjects/CapstoneDesign/testvideo/{a}.mp4" #동영상 파일 주소
    vidcap = cv2.VideoCapture()
    vidcap.open(videoFile)

    fps = vidcap.get(cv2.CAP_PROP_FPS)
    frame_count = vidcap.get(cv2.CAP_PROP_FRAME_COUNT)
    duration = frame_count / fps
    print("영상의 길이 : ", duration, "초")

    count = 0 # count 번째 사진e
    increase_width = round(duration/10, 1) # 여기서 몇초마다 찍을건지 세팅하면 됌.
    second = 0
    success = True

    
    while success and second <= duration:
        success,image = vidcap.read()
        vidcap.set(cv2.CAP_PROP_POS_MSEC, second * 1000)
        print(second, "초 에서 캡쳐")
        cv2.imwrite(f"C:/Users/pc/PycharmProjects/CapstoneDesign/capture/{a}/%d.jpg" % count, image) # 저장시킬 위치 주소
        print("saved image %d.jpg" % count)
        count += 1
        second += increase_width
        if cv2.waitKey(10) == 27:
            break
