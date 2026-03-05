import requests
import json
import time

URL = "https://leetcode.com/graphql"

HEADERS = {
    "Content-Type": "application/json",
    "User-Agent": "Mozilla/5.0"
}

QUERY = """
query problemsetQuestionList($skip: Int!, $limit: Int!) {
  problemsetQuestionList: questionList(
    categorySlug: ""
    skip: $skip
    limit: $limit
    filters: {}
  ) {
    total: totalNum
    questions: data {
      questionFrontendId
      titleSlug
      difficulty
      topicTags {
        name
      }
    }
  }
}
"""

def fetch_all_problems():
    all_questions = []
    skip = 0
    limit = 100  # máximo permitido por requisição

    while True:
        print(f"Fetching problems {skip} - {skip + limit}...")

        payload = {
            "query": QUERY,
            "variables": {
                "skip": skip,
                "limit": limit
            }
        }

        response = requests.post(URL, json=payload, headers=HEADERS)
        data = response.json()

        questions = data["data"]["problemsetQuestionList"]["questions"]

        if not questions:
            break

        for q in questions:
            all_questions.append({
                "id": q["questionFrontendId"],
                "titleSlug": q["titleSlug"],
                "difficulty": q["difficulty"],
                "tags": [tag["name"] for tag in q["topicTags"]]
            })

        skip += limit
        time.sleep(0.3)  # evita rate limit

    return all_questions


if __name__ == "__main__":
    problems = fetch_all_problems()

    with open("leetcode_problems.json", "w", encoding="utf-8") as f:
        json.dump(problems, f, indent=4, ensure_ascii=False)

    print(f"\nSaved {len(problems)} problems to leetcode_problems.json")