def activity_selection(start_times, finish_times):
    n = len(start_times)
    selected_activities = []

    print("Sorting activities based on their finish times...")
    # Sort activities based on their finish times
    activities = sorted(zip(start_times, finish_times), key=lambda x: x[1])
    print("Sorted activities:", activities)

    # The first activity always gets selected
    selected_activities.append(activities[0])
    last_finish_time = activities[0][1]
    print(f"Selecting first activity: {activities[0]}")

    # Consider the rest of the activities
    for i in range(1, n):
        if activities[i][0] >= last_finish_time:
            selected_activities.append(activities[i])
            last_finish_time = activities[i][1]
            print(f"Selecting activity: {activities[i]}")
        else:
            print(f"Skipping activity: {activities[i]}")

    return selected_activities

# Example usage
start_times = [1, 3, 0, 5, 8, 5]
finish_times = [2, 4, 6, 7, 9, 9]
selected_activities = activity_selection(start_times, finish_times)
print("Selected activities:", selected_activities)