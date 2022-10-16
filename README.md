# My Family Tree
[![Python 3.6](https://img.shields.io/badge/python-3.6-blue.svg)](https://www.python.org/downloads/release/python-360/)

This repository renders family tree from spreadsheet(.xlsx) as an SVG(.html). The current family tree is hosted on the github pages https://abhishekpalani.github.io/MyFamilyTree/. The page is updated on every merge of a pull request.

## Notes to Contributors
Like any github repos, contributors must work on own branch and create a pull request. Feel free to fork the repository to create own family tree.
### Tools required:
- Python 3.6+ - Download from https://www.python.org/downloads/
- Python IDE - PyCharm (Preferred) Download from https://www.jetbrains.com/pycharm/download/
- Graphviz - Download from http://www.graphviz.org/download/
- Spreadsheet Editor - Microsoft Office Excel or Google Sheets
### Command to run locally:
```python src\familyTreeGenerator.py 137 src\KumaraguruFamily.xlsx | dot -Tsvg > index.html```
