participants = [
    "Alice Wong",
    "Chen Wei",
    "David Kim",
    "Fatima Ali",
    "George Smith",
    "Hana Lee",
    "Audrey Hepburn",
    "James Stewart",
    "George Scott"
]

scores = [78, 92, 64, 87, 55, 73, 69, 96, 90]

qualification_score = 70
distinction_score = 90

for name, score in zip(participants, scores):
    print(f"{name}: {score}")

new_name = input("Enter participant's name: ").strip()
new_score_input = input("Enter participant's score: ").strip()

if new_name == "":
    print("Name cannot be empty!")
elif new_name in participants:
    print(f"{new_name} is already registered!")
else:
    try:
        new_score = float(new_score_input)
        if 0 <= new_score <= 100:
            participants.append(new_name)
            scores.append(new_score)
            print(f"{new_name} has been successfully registered!")
        else:
            print("Score must be between 0 and 100!")
    except ValueError:
        print("Score must be a number!")

search_name = input("Enter participant's name to search: ").strip()

if search_name in participants:
    index = participants.index(search_name)
    score = scores[index]
    print(f"Name: {search_name}")
    print(f"Score: {score}")
    if score > distinction_score:
        print("DISTINCTION")
    elif score >= qualification_score:
        print("QUALIFIED")
    else:
        print("NOT QUALIFIED")
else:
    print(f"{search_name} not found!")

for name, score in zip(participants, scores):
    if score > distinction_score:
        status = "DISTINCTION"
    elif score >= qualification_score:
        status = "QUALIFIED"
    else:
        status = "NOT QUALIFIED"
    print(f"{name}: {score} - {status}")

has_distinction = False
all_passed = True

for score in scores:
    if score > distinction_score:
        has_distinction = True
    if score < 50:
        all_passed = False

print(f"Has distinction: {has_distinction}")
print(f"All passed: {all_passed}")

update_name = input("Enter participant's name to update: ").strip()

if update_name in participants:
    index = participants.index(update_name)
    new_score_input = input("Enter new score: ").strip()
    try:
        new_score = float(new_score_input)
        if 0 <= new_score <= 100:
            scores[index] = new_score
            print(f"{update_name}'s score has been updated!")
        else:
            print("Score must be between 0 and 100!")
    except ValueError:
        print("Score must be a number!")
else:
    print(f"{update_name} not found!")

remove_name = input("Enter participant's name to withdraw: ").strip()

if remove_name in participants:
    index = participants.index(remove_name)
    participants.remove(remove_name)
    scores.pop(index)
    print(f"{remove_name} has been withdrawn!")
else:
    print(f"{remove_name} not found!")

pairs = list(zip(participants, scores))
pairs.sort(key=lambda x: x[1], reverse=True)

for rank, (name, score) in enumerate(pairs, start=1):
    print(f"#{rank}: {name} - {score}")

if scores:
    highest = max(scores)
    lowest = min(scores)
    average = sum(scores) / len(scores)
    
    highest_count = scores.count(highest)
    lowest_count = scores.count(lowest)
    
    distinction_count = sum(1 for score in scores if score > distinction_score)
    qualified_count = sum(1 for score in scores if qualification_score <= score <= distinction_score)
    not_qualified_count = sum(1 for score in scores if score < qualification_score)
    
    print(f"Highest Score: {highest} (found in {highest_count} participant(s))")
    print(f"Lowest Score: {lowest} (found in {lowest_count} participant(s))")
    print(f"Average Score: {average:.2f}")
    print(f"Participants with DISTINCTION: {distinction_count}")
    print(f"Participants QUALIFIED: {qualified_count}")
    print(f"Participants NOT QUALIFIED: {not_qualified_count}")

print("\n--- FINAL REPORT ---")
for rank, (name, score) in enumerate(pairs, start=1):
    if score > distinction_score:
        status = "DISTINCTION"
    elif score >= qualification_score:
        status = "QUALIFIED"
    else:
        status = "NOT QUALIFIED"
    print(f"Rank #{rank}: {name} - Score: {score} - {status}")

print(f"Total Participants: {len(pairs)}")
print(f"Highest Score: {highest} (achieved by {highest_count} participant(s))")
print(f"Lowest Score: {lowest} (achieved by {lowest_count} participant(s))")
print(f"Average Score: {average:.2f}")
print(f"Distinctions: {distinction_count}")
