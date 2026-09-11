
def process_events(events: list[dict]) -> dict:
    seen = set()
    result = {}

    for event in events:
        uid = event["user_id"]
        ts = event["timestamp"]
        action = event["action"]

        event_key = (uid, ts)
        if event_key in seen:
            continue
        seen.add(event_key)
        print("seen: ", seen)

        # Step 2: Ensure user entry exists
        if uid not in result:
            result[uid] = {}
        print("event key: ", event_key)

        # Step 3: Increment the action count
        
        result[uid][action] = result[uid].get(action, 0) + 1
            

        
    return result
"""
# Example Output:
{
    "user_1": {"click": 2, "login": 1},
    "user_2": {"view": 4}
}
"""
raw_events = [
    # user_1 actions
    {"user_id": "user_1", "timestamp": 100, "action": "login"},
    {"user_id": "user_1", "timestamp": 105, "action": "click"},
    {"user_id": "user_1", "timestamp": 110, "action": "click"},
    # user_2 actions
    {"user_id": "user_2", "timestamp": 200, "action": "view"},
    {"user_id": "user_2", "timestamp": 205, "action": "view"},
    {"user_id": "user_2", "timestamp": 210, "action": "view"},
    {"user_id": "user_2", "timestamp": 215, "action": "view"},
]
print(process_events(raw_events))