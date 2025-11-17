import csv

bugs = [
    ["Player falls through map at bridge location", "Critical", "Gameplay", "P0"],
    ["Game crashes when opening inventory with 50+ items", "Critical", "Performance", "P0"],
    ["UI button text overlaps in Hindi language", "High", "UI", "P1"],
    ["Frame rate drops to 15 FPS during smoke grenade", "High", "Performance", "P1"],
    ["No footstep audio when crouching on metal", "Medium", "Audio", "P2"],
    ["Wrong weapon icon displayed in loadout", "Low", "UI", "P3"],
    ["Teammate name tags flicker rapidly", "Medium", "UI", "P2"],
    ["Vehicle physics glitch on steep terrain", "High", "Gameplay", "P1"],
    ["Login button unresponsive after 3 attempts", "Critical", "UI", "P0"],
    ["Network lag spikes in matchmaking lobby", "Medium", "Network", "P2"],
    ["Character model clips through walls", "High", "Gameplay", "P1"],
    ["Audio desync in cutscenes", "Medium", "Audio", "P2"],
    ["Leaderboard not updating after match", "Low", "Network", "P3"],
    ["Settings menu freezes on controller input", "High", "UI", "P1"],
    ["Weapon reload animation stutters", "Low", "Gameplay", "P3"],
    ["Voice chat cuts out randomly", "High", "Audio", "P1"],
    ["Map markers disappear intermittently", "Medium", "UI", "P2"],
    ["Game server timeout during peak hours", "Critical", "Network", "P0"],
    ["Achievement progress not saving", "Medium", "Gameplay", "P2"],
    ["Shop purchase confirmation missing", "High", "UI", "P1"],
]

with open("bug_data.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Bug Description", "Severity", "Type", "Priority"])
    writer.writerows(bugs)

print("✅ Sample data created: bug_data.csv")
print(f"📊 Total bugs generated: {len(bugs)}")
```

---

#### **File 3: `requirements.txt`**
```
google-generativeai==0.3.2
