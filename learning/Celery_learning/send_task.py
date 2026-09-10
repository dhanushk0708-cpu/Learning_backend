from tasks import analyze_complaint

result = analyze_complaint.delay(
    101,
    "Large pothole near school"
)

print("Task ID:", result.id)
print("Task Status:", result.status)
print("Task Result:", result.get())