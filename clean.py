import json
import pandas as pd

# Load the JSON file
with open("watch-history.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# Extract relevant fields
cleaned_data = []
for entry in data:
    title = entry.get("title", "Unknown")
    watch_time = entry.get("time", "Unknown")
    
    # Extract channel name if available
    subtitles = entry.get("subtitles", [])
    channel_name = subtitles[0]["name"] if subtitles else "Unknown"

    cleaned_data.append({"Title": title, "Channel Name": channel_name, "Watch Time": watch_time})

# Convert to DataFrame
df = pd.DataFrame(cleaned_data)

# Save to CSV for easy loading into Tableau
df.to_csv("cleaned_watch_history.csv", index=False)

print("✅ Cleaning complete! File saved as cleaned_watch_history.csv")
