# Student Performance Analysis Using Python

## Project Overview

This project analyzes student academic performance using Python. It explores the relationship between study hours, attendance, and marks through data analysis and visualization.

## Technologies Used

- Python
- Pandas
- Matplotlib
- Seaborn
- Streamlit

## Features

- Load student data from a CSV file
- Calculate average, highest, and lowest marks
- Analyze attendance and study hours
- Visualize study hours versus marks
- Visualize attendance versus marks
- Display a correlation heatmap
- Interactive dashboard with filters
- View student records and download filtered data as CSV

## Sample Results

Based on the original sample dataset:

- Total students: 8
- Average marks: 69.12
- Highest marks: 94
- Lowest marks: 42
- Average attendance: 81.88%

## Project Structure

- `data.csv` - Sample student dataset
- `analysis.py` - Python analysis code
- `app.py` - Interactive Streamlit dashboard
- `study_hours_vs_marks.png` - Generated chart
- `README.md` - Project documentation

## How to Run

Install the required libraries:

```bash
python -m pip install streamlit pandas matplotlib seaborn
```

Run the analysis script:

```bash
python analysis.py
```

Launch the dashboard:

```bash
python -m streamlit run app.py
```

Open the local URL shown in the terminal.

## Dataset

This project uses sample student data created for educational purposes. The dataset includes student IDs, study hours, attendance, and marks.

## Output

The project provides summary statistics, visual charts, and an interactive dashboard to explore student performance.

## Future Improvements

- Analyze a larger dataset
- Add more interactive filters
- Explore machine learning for performance prediction
- Deploy the dashboard online

## Author

Imran
