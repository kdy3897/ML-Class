import cv2, numpy as np
import os
from PIL import Image

def match(c) :
    test = f'C:/Users/pc/PycharmProjects/CapstoneDesign/capture/{c}/'
    os.chdir(test)
    now_path = os.getcwd()
    print(now_path)

    path = f'C:/Users/pc/PycharmProjects/CapstoneDesign/capture/{c}/'
    file_list = os.listdir(path)

    cnt = 1
    count = 0
    while cnt <=(len(file_list)-2) :

        img1 = cv2.imread(f'C:/Users/pc/PycharmProjects/CapstoneDesign/capture/{c}/%d.jpg' %cnt)
        img2 = cv2.imread(f'C:/Users/pc/PycharmProjects/CapstoneDesign/capture/{c}/%d.jpg' %(cnt+1))
        gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
        gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

# ORB로 서술자 추출
        detector = cv2.ORB_create()
        kp1, desc1 = detector.detectAndCompute(gray1, None)
        kp2, desc2 = detector.detectAndCompute(gray2, None)
    # BF-Hamming으로 매칭

        matcher = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
        matches = matcher.match(desc1, desc2)

    # 매칭 결과를 거리기준 오름차순으로 정렬
        matches = sorted(matches, key=lambda x:x.distance)

    # 최소 거리 값과 최대 거리 값 확보
        min_dist, max_dist = matches[0].distance, matches[-1].distance

    # 최소 거리의 15% 지점을 임계점으로 설정
        ratio = 0.2
        good_thresh = (max_dist - min_dist) * ratio + min_dist
    # 임계점 보다 작은 매칭점만 좋은 매칭점으로 분류
        good_matches = [m for m in matches if m.distance < good_thresh]
        print('matches:%d/%d, min:%.2f, max:%.2f, thresh:%.2f' \
                %(len(good_matches),len(matches), min_dist, max_dist, good_thresh))
    # 좋은 매칭점만 그리기
        res = cv2.drawMatches(img1, kp1, img2, kp2, good_matches, None,
                        flags=cv2.DRAW_MATCHES_FLAGS_NOT_DRAW_SINGLE_POINTS)

        if good_thresh <= 27.0 :
            print( "Yes")
            count +=1

        else :
            print("No")
        cnt +=1
    # 결과 출력
    if count >= 6 :

        cv2.imshow('Good Match', res)
        img = cv2.imread('C:/Users/pc/PycharmProjects/CapstoneDesign/mark_O.png')
        cv2.imshow('Message', img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

        # 비율 O , 워터마크 O
    else :
        img = cv2.imread('C:/Users/pc/PycharmProjects/CapstoneDesign/mark_X.png')
        cv2.imshow('Message', img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

        # 비율 O, 워터마크 X
    return


def size(d) :

    test = f'C:/Users/pc/PycharmProjects/CapstoneDesign/capture/{d}/'
    os.chdir(test)
    now_path = os.getcwd()
    print(now_path)

    path = f'C:/Users/pc/PycharmProjects/CapstoneDesign/capture/{d}/'
    file_list = os.listdir(path)


    image1 = cv2.imread(f'C:/Users/pc/PycharmProjects/CapstoneDesign/capture/{d}/5.jpg')


    h, w, c = image1.shape

    print (h)
    print(w)
    print(c)

    ratio = round(w/h,1)
    print(ratio, 0)

    return ratio