# Multichannel Signal Viewer

An interactive Python/Plotly tool for loading, cleaning, and visualizing multichannel time-series data (e.g., EEG, ECG).  
The viewer supports **dual y-axes** to handle different signal scales, a **scrollable/zoomable timeline**, and flexible channel selection.  

---

## Features
- Load CSV data with optional metadata lines (`#`) automatically skipped.
- Plot EEG signals (µV) on the **left y-axis**.
- Plot ECG/CM signals (mV) on the **right y-axis**.
- Interactive timeline with scroll and zoom controls.
- Support for varying datasets (handles missing channels gracefully).
- Clean and extensible design for other biosignal or time-series data.  

---

## Requirements
Make sure you have **Python 3.8+** installed. Then install dependencies:

```bash
pip install pandas plotly
