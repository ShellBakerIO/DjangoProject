import datetime
import requests


def clean_vacancy(vacancy):
    salary_from = vacancy['salary']['from']
    salary_to = vacancy['salary']['to']
    currency = vacancy['salary']['currency']
    key_skills = ', '.join(x['name'] for x in vacancy['key_skills'])

    if salary_from is not None and salary_to is not None and salary_from != salary_to:
        salary_text = f"от {'{0:,}'.format(salary_from).replace(',', ' ')} до {'{0:,}'.format(salary_to).replace(',', ' ')} {currency}"
    elif salary_from is not None:
        salary_text = f"{'{0:,}'.format(salary_from).replace(',', ' ')} {currency}"
    elif salary_to is not None:
        salary_text = f"{'{0:,}'.format(salary_to).replace(',', ' ')} {currency}"
    else:
        salary_text = 'Нет данных'

    vacancy['salary'] = salary_text
    vacancy['key_skills'] = key_skills

    return vacancy

def get_vacancies():
    try:
        params = {
            'text': 'Backend',
            'specialization': 1,
            'page': 1,
            'per_page': 100,
        }
        data = []
        info = requests.get('https://api.hh.ru/vacancies', params).json()
        for row in info['items']:
            if not row['salary'] is None:
                data.append({'id': row['id'], 'published_at': row['published_at']})
        data = sorted(data, key=lambda x: x['published_at'])
        vacancies = []
        for vacancy in data[len(data) - 10:]:
            vacancies.append(clean_vacancy(requests.get(f'https://api.hh.ru/vacancies/{vacancy["id"]}').json()))
        return vacancies
    except Exception as e:
        print(e)
        print(datetime.datetime.now())
        return []

if __name__ == "__main__":
    get_vacancies()