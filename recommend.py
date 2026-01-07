users = {
    "Alice": ["Python", "JavaScript"],
    "Bob": ["Java", "Python"],
    "Charlie": ["JavaScript", "Go"]
}

def recommend(user):
    liked = users.get(user, [])
    suggestions = set()

    for u, items in users.items():
        if u != user and any(item in liked for item in items):
            suggestions.update(items)

    return suggestions - set(liked)

if __name__ == "__main__":
    name = input("Enter user name: ")
    recs = recommend(name)
    print("Recommendations:", list(recs))
