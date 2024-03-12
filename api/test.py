from requests import get, post


print(get('http://127.0.0.1:5000/api/jobs').json())
# print(post('http://127.0.0.1:5000/api/jobs', json={'team_leader': 3,
#                                                    'job': 'president',
#                                                    'work_size': 22,
#                                                    'collaborators': 'I do not know',
#                                                    'start_date': 'ten years ago',
#                                                    'end_date': '-',
#                                                    'is_finished': False}).text)
