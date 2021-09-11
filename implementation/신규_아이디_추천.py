#-*- coding:utf-8 -*-

# 카카오 2021 공채 기출: 신규 아이디 추천
# idea: 시뮬레이션, 문자열 (구현)
# 예외처리 잘 해야함! 특히 연속 마침표 치환, 인덱싱 조심
# 정규식, 문자열 관련 함수 익혀두기

import re

def solution(new_id):
    # 1. 대문자 -> 소문자
    new_id = new_id.lower()
    # 2. 문자 제거
    new_id = re.sub('[^a-z0-9-_.]', '', new_id)
    # 3. 연속 마침표 치환
    temp = new_id
    while True:
        temp = new_id.replace('..', '.')
        if new_id == temp:
            break
        new_id = temp
    # 4. 마침표 처음이나 끝 제거
    if len(new_id) != 0 and new_id[0] == '.': new_id = new_id.lstrip('.')
    if len(new_id) != 0 and new_id[-1] == '.': new_id = new_id.rstrip('.')
    # 5. 빈 문자열
    if len(new_id) == 0: new_id = "a"
    # 6. 길이 제한
    if len(new_id) >= 16: new_id = new_id[:15]
    if new_id[-1] == '.': new_id = new_id.rstrip('.')
    # 7. 2자 이하
    while len(new_id) <= 2:
        new_id = new_id + new_id[-1]
    
    answer = new_id
    return answer