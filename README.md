# 🎮 AI-Powered Bug Report Classifier

> Automated game QA tool using Google Gemini AI to classify bugs by severity, type, and priority

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Gemini](https://img.shields.io/badge/Google-Gemini--Pro-red.svg)

## 📋 Overview

AI-powered tool for game QA teams to automatically classify bug reports using Google Gemini Pro API and prompt engineering. Reduces manual triage time by 70% and standardizes bug classification.

## ✨ Features

- 🤖 **Gemini AI Integration**: Google's latest AI for accurate classification
- ⚡ **Instant Classification**: Bugs categorized by severity (Critical/High/Medium/Low)
- 🎯 **Type Identification**: Gameplay, UI, Performance, Audio, Network, Other
- 📊 **Priority Assignment**: P0-P3 for sprint planning
- 💾 **Automated Logging**: Timestamped classification history
- 📈 **Data Export**: CSV for Tableau/Google Sheets visualization

## 🛠️ Tech Stack

- Python 3.8+
- Google Gemini Pro API
- CSV, JSON, Datetime libraries

## 📦 Installation

### 1. Clone repository
```bash
git clone https://github.com/OfficialYashOp/bug-classifier.git
cd bug-classifier
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Get Gemini API Key (FREE)
- Visit: https://makersuite.google.com/app/apikey
- Click "Get API Key"
- Copy your key
- Open `bug_classifier.py` and replace `your-api-key-here` on line 6

## 🚀 Usage

### Run Bug Classifier
```bash
python bug_classifier.py
```

### Generate Sample Data
```bash
python generate_sample_data.py
```

## 📊 Sample Output

**Input:**
```
Bug: "Game crashes when opening inventory with 50+ items"
```

**Output:**
```json
{
    "severity": "Critical",
    "type": "Performance",
    "priority": "P0",
    "suggested_steps": "1. Launch game 2. Collect 51+ items 3. Open inventory 4. Observe crash"
}
```

## 🧪 Test Cases

Try these bugs:

1. "Player falls through map at coordinates X:245 Y:890"
2. "Frame rate drops to 15 FPS during smoke grenade"
3. "UI button text overlaps in Hindi language"
4. "No footstep audio when crouching on metal"
5. "Server timeout during peak hours"

## 📈 Data Visualization

Import `bug_data.csv` into:
- **Tableau**: Interactive dashboards
- **Google Sheets**: Pie/bar charts
- **Excel**: Pivot tables

**Insights:**
- Bug distribution by type
- Severity breakdown
- Priority vs Type heatmap

## 🎯 Use Cases

- Speed up bug triage by 70%
- Standardize classification across teams
- Generate automated QA reports
- Identify recurring bug patterns

## 📁 Project Structure
```
bug-classifier/
├── bug_classifier.py          # Main AI tool
├── generate_sample_data.py    # Sample data generator
├── requirements.txt           # Dependencies
├── README.md                  # Documentation
└── bug_data.csv              # Generated data
```

## 🔮 Future Enhancements

- [ ] Jira integration
- [ ] Multi-language support
- [ ] Pattern detection
- [ ] Web UI
- [ ] Batch processing

## 🎓 Learning Outcomes

- AI integration in QA workflows
- Prompt engineering techniques
- Data-driven testing
- Automation in game QA

## 👤 Author

**Yash Pandey**

Game QA Enthusiast | YouTube Gaming Creator (35K+ subs)

- LinkedIn: [linkedin.com/in/yashpandeyofficial007](https://linkedin.com/in/yashpandeyofficial007)
- GitHub: [github.com/OfficialYashOp](https://github.com/OfficialYashOp)
- Email: Pandey97828@gmail.com

## 🙏 Acknowledgments

- Google AI for Gemini Pro
- EA Games for inspiration
- Game QA community

## 📄 License

MIT License - Free for personal and commercial use

---

**⭐ If you found this helpful, star the repo!**

Built with ❤️ for game QA | Powered by Google Gemini
