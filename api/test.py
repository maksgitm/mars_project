from requests import get, post, delete, put


# всё ок
print(post('http://127.0.0.1:5000/api/jobs', json={
                                                        'team_leader': 20,
                                                        'job': 'president',
                                                        'work_size': 12,
                                                        'collaborators': 'qwqwqw',
                                                        'start_date': 'ten years ago',
                                                        'end_date': '-',
                                                        'is_finished': False
                                                      }).json())
# вместо булева значения в "is_finished" передано число
print(post('http://127.0.0.1:5000/api/jobs', json={
                                                        'team_leader': 20,
                                                        'job': 'president',
                                                        'work_size': 22,
                                                        'collaborators': 'qwqwqw',
                                                        'start_date': 'ten years ago',
                                                        'end_date': '-',
                                                        'is_finished': 123
                                                      }).json())
# аргумент "end_date" не передан
print(post('http://127.0.0.1:5000/api/jobs', json={
                                                        'team_leader': 20,
                                                        'job': 'president',
                                                        'work_size': 22,
                                                        'collaborators': 'qwqwqw',
                                                        'start_date': 'ten years ago',
                                                        'is_finished': 123
                                                      }).json())
# пустой запрос
print(post('http://127.0.0.1:5000/api/jobs', json={}).json())

# print(get('http://127.0.0.1:5000/api/jobs').json())

# print(put('http://127.0.0.1:5000/api/jobs/2', json={'team_leader': 22,
#                                                     'work_size': 22,
#                                                     'collaborators': 'qwqwqw',
#                                                     'start_date': 'ten years ago',
#                                                     'end_date': '-',
#                                                     'is_finished': False}).json())
# print(put('http://127.0.0.1:5000/api/jobs/88', json={'team_leader': 3,
#                                                      'job': 'president',
#                                                      'work_size': 22,
#                                                      'collaborators': 'qwqwqw',
#                                                      'start_date': 'ten years ago',
#                                                      'end_date': '-',
#                                                      'is_finished': False}).json())
# print(get('http://127.0.0.1:5000/api/jobs').json())
#
#
# print(post('http://127.0.0.1:5000/api/jobs', json={'team_leader': 3,
#                                                    'job': 'president',
#                                                    'work_size': 22,
#                                                    'collaborators': 'I do not know',
#                                                    'start_date': 'ten years ago',
#                                                    'end_date': '-',
#                                                    'is_finished': False}).text)
