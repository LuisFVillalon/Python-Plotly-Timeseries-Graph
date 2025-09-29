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

## Acknowledgments

This project was developed with the assistance of **ChatGPT**, which I used as a learning aid to better understand the features offered by Plotly and how to implement them. ChatGPT helped me explore different visualization options (such as dual y-axes, range sliders, and channel selection) and guided me in adapting these features to build the graph design I envisioned.  

---

## Demo:
[screen-capture (5).webm](https://github.com/user-attachments/assets/6d6bf6b2-eafc-4dd5-bb25-f11654dbd047)

---

## Requirements
Make sure you have **Python 3.8+** installed. Then install dependencies:

```bash
pip install pandas plotly

