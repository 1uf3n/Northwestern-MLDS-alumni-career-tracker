# MLDS 422 Homework 6 — Alumni lookup

This project scrapes Northwestern's MLDS alumni directory for the classes of 2013–2025, answers three analysis questions, and provides an interactive lookup tool.

## Files

- `HW6.ipynb`: scraping code, short explanations, results, and conclusions; all eight code cells have been run.
- `mlds_student_lookup.py`: the `MLDSStudentLookup` class and interactive search program.
- `data/alumni.pkl`: the required DataFrame with Name, Year, Role, and Company.
- `data/alumni.csv`: a readable copy for inspecting on GitHub.
- `data/source_details.csv`: original job text and source URLs for checking the extraction.
- `screenshots/`: four Terminal screenshots showing searches by Name, Year, Role, and Company.
- `requirements.txt`: Python dependencies.
- `.gitignore`: keeps environments, caches, and secrets out of GitHub.

## Setup (Python 3.12)

Open a terminal in this project folder. Create and activate a new environment:

```bash
conda create -n mlds-hw6 python=3.12 -y
conda activate mlds-hw6
python -m pip install -r requirements.txt
```

Alternatively, with Python 3.12 installed:

```bash
python3.12 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

On Windows, activate a venv with `.venv\Scripts\activate`.

## Run order

1. Start Jupyter in this folder:

   ```bash
   python -m notebook HW6.ipynb
   ```

2. Choose **Run All** and save the notebook. The notebook downloads the public pages and writes the data files. Internet access is needed for scraping. Its saved outputs are already included.
3. Run the lookup tool:

   ```bash
   python mlds_student_lookup.py
   ```

4. Enter a field followed by a value. Try these four searches:

   | Field | Value |
   |---|---|
   | Name | Scott |
   | Year | 2013 |
   | Role | senior manager |
   | Company | Google |

   Field names and values ignore capitalization. Values match part of the text. Enter `exit` at either prompt to finish. Invalid fields and blank values show a message so you can try again. No matches produce a clear message.

## Results and limits

Collected November 16, 2026: **544 alumni across 13 class years**.

The five most common listed company names are TransUnion (15), Meta (13), Amazon (12), Facebook (12), and Coupa Software (8). Employer names are grouped without case differences; corporate aliases are not merged. In particular, Facebook and Meta remain separate website labels.

Two insights:

- The 2025 directory lists 57 people versus 30 for 2013, a 90% increase in listed class size.
- 87 of 394 known employment roles (22.1%) contain the word “senior.” Generic Graduate Student labels are excluded from that denominator.

The 2024 and 2025 cards currently say “Graduate Student” and do not list employers. Other entries also have missing details. They remain in the data with missing values; no current jobs are invented. The website may be outdated, so these results describe its listings rather than verified current employment. Company-only text and descriptions without “at” use reusable parsing rules, with the original text preserved in `source_details.csv`.

Source: https://www.mccormick.northwestern.edu/machine-learning-data-science/people/alumni/

## Screenshots and final submission

The screenshots show four completed searches:

| Field | Search | Matches | Screenshot |
|---|---|---:|---|
| Name | Scott | 1 | [Name](screenshots/name_output.png) |
| Year | 2013 | 30 | [Year](screenshots/year_output.png) |
| Role | senior manager | 11 | [Role](screenshots/role_output.png) |
| Company | Google | 5 | [Company](screenshots/company_output.png) |

The repository includes the executed notebook, lookup script, saved data, screenshots, and environment requirements. The assignment also asks for a project ZIP submitted through Canvas. Exclude `.venv`, caches, and secret files when creating that ZIP.

Only load pickle files you created or trust. The included pickle was generated from this notebook.
