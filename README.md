# Financial Agent

**Financial Agent** is a multi-agent AI system that provides real-time financial insights and web-based information retrieval. It utilizes advanced AI models and tools like Yahoo Finance and DuckDuckGo to deliver actionable, structured, and accurate data.

---

## Features

1. **Web Search Agent**:
   - Performs web searches using DuckDuckGo.
   - Provides detailed results with sources.
   - Displays responses in Markdown format for readability.

2. **Finance Agent**:
   - Fetches financial data via Yahoo Finance tools.
   - Capabilities include:
     - Stock prices
     - Analyst recommendations
     - Stock fundamentals
     - Company news
   - Presents data in structured tables.

3. **Multi-Agent Collaboration**:
   - Combines outputs of the Web Search and Finance Agents for comprehensive responses.
   - Ensures data reliability with source inclusion.

---

## Installation and Setup

### Prerequisites
- Python 3.8 or higher
- An API key for Groq and OpenAI

### Step 1: Clone the Repository
```bash
git clone <repository-url>
cd financial-agent
```

### Step 2: Install Dependencies
Install the required Python libraries:
```bash
pip install -r requirements.txt
```

### Step 3: Configure Environment Variables
1. Create a `.env` file in the project directory.
2. Add your API keys as follows:
```env
PHI_API_KEY="your_phi_api_key"
GROQ_API_KEY="your_groq_api_key"
OPENAI_API_KEY="your_openai_api_key"
```

### Step 4: Run the Application
```bash
python app.py
```

---

## Usage
1. Launch the script by running `python app.py`.
2. Enter a stock name or ticker symbol when prompted.
3. The system will provide:
   - A summary of analyst recommendations.
   - The latest company news.

Example:
```plaintext
Enter the stock name or ticker symbol: TSLA
```

Output:
```plaintext
### Analyst Recommendations for TSLA
| Metric               | Value      |
|----------------------|------------|
| Strong Buy          | 20         |
| Buy                | 15         |
| Hold               | 10         |

### Latest News for TSLA
- Tesla announces new model...
- Market trends favor EV sector...

(Source: DuckDuckGo, Yahoo Finance)
```

---

## Project Structure

- **`app.py`**: Main application script that initializes and coordinates the agents.
- **`.env`**: Stores API keys securely.
- **`requirements.txt`**: Lists the required Python dependencies.

---

## Technologies Used
- **Programming Language**: Python
- **Libraries**:
  - `phidata`: For agent modeling and integration.
  - `yfinance`: To fetch financial data.
  - `duckduckgo-search`: For web search functionality.
  - `python-dotenv`: For environment variable management.
  - `fastapi` and `uvicorn`: For optional API hosting.
- **APIs**:
  - DuckDuckGo Search API
  - Yahoo Finance API

---

## Contribution
Contributions are welcome! Please follow these steps:
1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add feature-name"
   ```
4. Push to your branch:
   ```bash
   git push origin feature-name
   ```
5. Submit a pull request.

---

## License

This project is licensed under the [MIT License](LICENSE).

---

## Contact
For questions or feedback, contact:
- **Email**: [prabhakars367@gmail.com](mailto:prabhakars367@gmail.com)
- **LinkedIn**: [https://www.linkedin.com/in/prabhakars367/](https://www.linkedin.com/in/prabhakars367/)

