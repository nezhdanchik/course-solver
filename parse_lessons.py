import requests
from bs4 import BeautifulSoup

main_path = 'https://ru.hexlet.io/courses/python-development-overview'
headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    'Cookie': 'your cookie',
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
