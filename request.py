import requests

url = 'http://localhost:5000/predict_api'
r = requests.post(url,json={'experience', 'test_score', 'interview_score'})

print(r.json())