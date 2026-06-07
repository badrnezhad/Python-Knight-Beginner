tickets = [
    {"id": 101, "priority": "low"},
    {"id": 102, "priority": "medium"},
    {"id": 103, "priority": "high"},
    {"id": 104, "priority": "high"}
]

for ticket in tickets:
    if ticket["priority"] == "high":
        print(ticket["id"])
        break
