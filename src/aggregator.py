import json

def save_to_file(data: list[dict], filename: str):
    combined = {
        "type": "FeatureCollection",
        "features": [feature for day in data for feature in day.get("features", [])]
    }
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(combined, f, ensure_ascii=False, indent=2)
    print(f"Saved {len(combined['features'])} earthquakes to {filename}")
