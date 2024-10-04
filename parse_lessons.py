import requests
from bs4 import BeautifulSoup

main_path = 'https://ru.hexlet.io/courses/python-basics'
headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 YaBrowser/24.7.0.0 Safari/537.36',
    'Cookie': 'roistat_first_visit=3003913; ___dc=d313b698-98da-4e6e-a12d-2c133789faab; hexlet_user_id=849116; ajs_user_id=%22849116%22; _rid=44e3ec0b5cce48259870dfe46697b3e9; _rid_anm_id=44e3ec0b5cce48259870dfe46697b3e9; tildauid=1722842630445.648993; cookie_accepted=true; browser_time_zone=Europe/Moscow; _hexlet_session2=KPA69ydZy%2FnE9Nm60nALD4x%2FAaHi4CNxBwJbhstt%2F2w8JXzUgWkdudeiiZvpxrYTTBSwa965zVEefBIT%2FISUSJcVqu%2Be2tKfM0D1y79x14xf0ZkC%2B3W9YesgvC54qKLTcfDlni%2FzleZ2yiR82VNDcG99nYMzvoH1u0yD4zyO2yXKVtxzRpzRepFjTkFvdHskYCyqufHEwQlmZTmQ6%2BAfy2hMuwWvjQuT3dXLBQ9Rx5Cuao6is4I3NKfzh5JMDi4WyCJQl0I2WBqt5ZKJRklZMeBfT1aBmIU4KaNo4VxJMu6lm3ECgj9VyNkh17rNboGGoQFRNj0g4YY2CrRaxoKfgHatk%2BSHe%2Fx252gyZNMwBF402OVBlMCCgK4hBf7LEKpxlHBX3XOS%2Bco%2BhGFcLJ3w59HNgMSHPKt6UNPuuD1v%2FaU4FbNrt5dyUMq4snd8sxqYsIv2xJyP2yjnDy99joX6a4zPaB4jB3B09GRgaGjidEJsSa2dL1dTT3s8DzTmQfL%2FYby4kB8qihghdxbRpEF8x1ATf2ocQg%3D%3D--CdPYgSV8%2FD9SMrLt--Vfe0%2F9pEcDAhMmLWZM4N1A%3D%3D; ph_phc_qfyA3rLLRWvDfi4ZHSzzHhpz5num5AcPGev1NyfOvkn_posthog=%7B%22distinct_id%22%3A%22018ea8e6-b44c-73b5-a33e-4062e123f6fd%22%2C%22%24sesid%22%3A%5B1728043784673%2C%220192571a-5976-79d0-8798-4c6566c3e633%22%2C1728038197622%5D%7D; _hexlet_session2=wU1VMkClcK7beF32CpFsrGbkqD7CPYR8ofyFEWW3uKDIw0LeN16L9BD%2FcDn7Dcn9EkvqFftt%2FCCc4dzZxkiy%2BrnGPF0ILettH2ZJnlmEWDJuUDvRn02B6zp%2BXRL9vwXt19nQi9qsY%2FMHsFyvmz7SMefNgznpW5NMpFEn2bgNNFxj%2FTTGBrN1bXpf9Aim%2BY%2BhuqCA5Cs3HYLYfqzWBZBQvB4xLAWbRpH70byyocGZn5Vh64L0Pav3dP6mRjjERWp%2F4TOpIJxROd51wRWvjix9VTTxYrW8mdTLmKIxgc8sU9jhPH8phDkvAQtJiEu5KxgnBYUdwKhPiX44sXwn8wNHEWvcezPr%2Bg7nUSGJ%2FpGXCVcx5ecy1ZyNvjnYnCPR1zCjon%2FzZxWH574ST0b9Rb%2FY4pH12a12dDEocSajsZyw340GrJ%2FnpDoWIh0AwkqyfMHHdlmmNdWjgGbBVBSvHWjpJR9pNIsCIAtNOMzmuUGRMU0tleKMS6z%2B86%2Fzz2LSjoR5UuxiSZzDnU7m%2FDWfz0J8j%2BbyOEZ5Pw%3D%3D--35VJrPYIRkVU4GhJ--%2FftlyO5YqkpF6WN3Gm2Szg%3D%3D',
    'Content-Type': 'application/x-www-form-urlencoded'
}


def get_lesson_id(url):
    r = requests.get('https://ru.hexlet.io' + url, headers=headers)
    soup = BeautifulSoup(r.text, 'html.parser')
    # </button><input type="hidden" name="tota_ai[action]" value="explain_theory" autocomplete="off" /><input type="hidden" name="tota_ai[lesson_id]" value="2185" autocomplete="off" /></form></li>
    return int(
        soup.find('input', attrs={'name': 'tota_ai[lesson_id]'}).get('value'))


r = requests.get(main_path, headers=headers)
soup = BeautifulSoup(r.text, 'html.parser')
# html body.min-vh-100 main.mb-5 div.container-xl div.row div.col-12.col-md-7.col-lg-8 ul.list-group li.list-group-item div.row.my-2 div.col h3.h5 a.text-decoration-none.text-body.me-2
lessons = soup.find_all('a', class_='text-decoration-none text-body me-2')
# get href and content
parsed_lessons = dict()
c = 0
for lesson in lessons:
    lref = lesson['href']
    parsed_lessons[lesson.text] = (get_lesson_id(lref), lref.replace('/theory_unit', ''))
    c += 1
    print(f'Прогресс {c}/{len(lessons)}')
print(parsed_lessons)
