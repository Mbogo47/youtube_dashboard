# YouTube Watch History Dashboard
A dashboard analysing my youtube watch history from 2019 - 2025

## Overview
This project is a data visualization dashboard that analyzes my YouTube watch history. It provides insights into my viewing habits and other key trends. The dashboard was created using Python, Pandas, and a visualization tool such as Tableau

## Live Link
[Access the Dashboard Here](https://public.tableau.com/app/profile/ivy.mbogo/viz/YoutubeWatchHistoryAnalysis2018-2025/YoutubeAnalytics)

## Process
### 1. Extracting Data
- Downloaded my YouTube watch history from Google Takeout.
- Extracted and loaded the JSON file into a pandas DataFrame for preprocessing.

### 2. Cleaning and Preprocessing Data
- Parsed relevant fields such as video titles, watch timestamps, and video categories.
- Converted timestamps into a datetime format.
- Removed any duplicate or irrelevant entries.
- Extracted additional metadata like video durations and channel names.

### 3. Data Analysis
- Aggregated watch time per day, week, and month.
- Identified the most-watched categories and channels.
- Calculated the average watch time per session.
- Analyzed viewing trends based on time of day.

### 4. Data Visualization
- Used Tableau to create interactive dashboards.
- Created bar charts, line graphs, and heatmaps to visualize trends.
- Designed a summary dashboard with key metrics like total watch time, and peak viewing hours.

### 5. Deployment & Sharing
- Exported dashboards as interactive reports.
- Shared insights through screenshots and a summary report.

## Technologies Used
- **Python**: Data preprocessing and analysis (pandas, json, datetime)
- **Tableau**: Data visualization and dashboard creation
- **Google Takeout**: Data extraction

## Future Improvements
- Integrate YouTube API for real-time data updates.
- Build a web-based dashboard using Streamlit or Flask.
- Add sentiment analysis for video comments.

## Conclusion
This project provided valuable insights into my YouTube consumption patterns and helped me understand my content preferences. The visual dashboard makes it easy to analyze trends and optimize my screen time effectively.

### Author: Ivy Njoki Mbogo
