# Week 3 Detailed Plan
## APIs & Integration

**Dates:** October 28 - November 3, 2025  
**Goal:** Master API calls, JSON handling, build API-integrated projects

---

## WEEK 3 OVERVIEW

### Learning Focus:
- REST API fundamentals
- Python requests library
- JSON data manipulation
- API authentication (keys, tokens)
- Error handling for API calls
- Building API-integrated tools

### Weekly Goals:
- [ ] Understand REST APIs
- [ ] Make GET/POST requests
- [ ] Handle JSON responses
- [ ] API authentication practiced
- [ ] 2-3 API projects built
- [ ] 7 consecutive days 🟩×7

---

## DAY 13 - MONDAY, OCT 28

### Morning (6-8 AM)
**REST API Basics**
- Video: Corey Schafer Python Requests
- OR Read: Real Python Requests Guide
- Topics: GET, POST, status codes, JSON

**Practice:**
```python
import requests

# Simple GET request
response = requests.get('https://jsonplaceholder.typicode.com/posts/1')
print(response.status_code)
print(response.json())
```

### Evening (7-9 PM)
- Try 3-5 different free APIs
- Practice error handling
- Git push

**Goal:** Understand HTTP requests ✅

---

## DAY 14 - TUESDAY, OCT 29

### Morning (6-8 AM)
**API Authentication & Headers**
- Learn: API keys, headers, parameters
- Practice with APIs requiring keys

### Evening (7-9 PM)
- Build: Weather app (OpenWeather API)
- Handle errors gracefully
- Git push

**Goal:** API authentication working ✅

---

## DAY 15 - WEDNESDAY, OCT 30

### Morning (6-8 AM)
**POST Requests & Data Sending**
- Learn: Sending data to APIs
- Practice: POST, PUT, DELETE

### Evening (7-9 PM)
- Build: Simple data sender
- Practice different HTTP methods
- Git push

**Goal:** CRUD operations with APIs ✅

---

## DAY 16 - THURSDAY, OCT 31

### Morning (6-8 AM)
**JSON Handling Deep Dive**
- Parse complex JSON
- Nested data access
- JSON to DataFrame (Pandas review!)

### Evening (7-9 PM)
- Build: API data analyzer
- Practice JSON manipulation
- Git push

**Goal:** Comfortable with JSON ✅

---

## DAY 17 - FRIDAY, NOV 1

### Morning (6-8 AM)
**Error Handling & Retries**
- Handle timeouts
- Retry logic
- Rate limiting

### Evening (7-9 PM)
- Improve previous projects
- Add robust error handling
- Git push

**Goal:** Production-ready API calls ✅

---

## WEEKEND - DAYS 18-19 (NOV 2-3)

### Saturday
**Project: API Integration Tool**
Choose one:
1. News aggregator (NewsAPI)
2. GitHub stats viewer
3. Currency converter with live rates

Build it end-to-end!

### Sunday
- Polish project
- Add features
- Document in README
- Deploy/showcase

---

## FREE APIs TO PRACTICE

**No authentication:**
- JSONPlaceholder: https://jsonplaceholder.typicode.com/
- Cat Facts: https://catfact.ninja/fact
- Random User: https://randomuser.me/api/
- Dog API: https://dog.ceo/api/breeds/image/random

**With free keys:**
- OpenWeather: https://openweathermap.org/api
- NewsAPI: https://newsapi.org/
- GitHub API: https://api.github.com/

---

## RESOURCES

**Tutorials:**
- Corey Schafer Requests: YouTube
- Real Python: https://realpython.com/python-requests/
- Requests docs: https://requests.readthedocs.io/

**Practice:**
- Public APIs list: https://github.com/public-apis/public-apis

---

## SUCCESS METRICS

By Nov 3:
- [ ] Comfortable making API calls
- [ ] Handle JSON data easily
- [ ] Error handling implemented
- [ ] 2-3 API projects built
- [ ] 7 days coded 🟩×7

---

*Week 3: API Integration Mastery* 🚀