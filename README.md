# WebScrapeByBeautifulsoup4

## Overview
WebScrapeByBeautifulsoup4 is a Python project designed to scrape IPO data from a webpage, transform the data into a structured format, and export it to a CSV file. It uses **BeautifulSoup4**, **requests**, **pandas**, and **rich** libraries to handle web scraping, data manipulation, and console output formatting.

---

## Features
- **Web Scraping:** Extracts IPO data from a target webpage.
- **Data Transformation:** Converts the extracted HTML table into a structured format.
- **Data Export:** Saves the structured data into a CSV file for easy analysis.
- **Enhanced Logging:** Provides rich console output for better visualization and debugging.

---

## Requirements
- **IDE:** PyCharm
- **Environment:** Anaconda
- **Python Libraries:**
  - BeautifulSoup4
  - requests
  - pandas
  - rich

---

## Installation

To set up the project, ensure you have Python and pip installed. Follow these steps to install the required dependencies:

```bash
pip install beautifulsoup4
pip install requests
pip install pandas
pip install rich
```
---
## Usage

1. Clone or download the project directory `WebScrapeByBeautifulsoup4`.
2. Open the project in **PyCharm** or any Python-supported IDE.
3. Run the script `WebScrapeIntoHtmlMakeCSV.py` to scrape the IPO data.

### Expected Output:
- The scraped HTML content is saved as `RstData.html`.
- A CSV file named `CurrentIPOMainboard.csv` containing the IPO data is generated.
- Console outputs a summary of the data extraction process with visual enhancements provided by the `rich` library.

---

## Script Description

The main script, `WebScrapeIntoHtmlMakeCSV.py`, performs the following tasks:

1. **Fetch Webpage Data:**
   - Downloads the HTML content of the target webpage using the `requests` library.

2. **Parse HTML:**
   - Extracts table data from the downloaded HTML using `BeautifulSoup`.

3. **Data Conversion:**
   - Converts the extracted table data into a structured DataFrame using `pandas`.

4. **Export to CSV:**
   - Saves the structured data into a file named `CurrentIPOMainboard.csv`.

5. **Console Output:**
   - Logs the scraping progress and result using `rich`.

---

## Dependencies

- [BeautifulSoup4](https://pypi.org/project/beautifulsoup4/)
- [pandas](https://pypi.org/project/pandas/)
- [requests](https://pypi.org/project/requests/)
- [rich](https://pypi.org/project/rich/)

---

## File Structure
```
WebScrapeByBeautifulsoup4/
├── WebScrapeIntoHtmlMakeCSV.py
├── RstData.html (generated during execution)
├── CurrentIPOMainboard.csv (generated during execution)
```

---

## License
This project is released under the [MIT License](LICENSE). 

---

## Contribution
Contributions are welcome! If you'd like to contribute:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a Pull Request.

For major changes, please open an issue first to discuss what you would like to change.

---

## Acknowledgments
- **BeautifulSoup4** for HTML parsing.
- **pandas** for data manipulation.
- **requests** for handling HTTP requests.
- **rich** for enhanced console output.

Feel free to customize and improve this project further!
