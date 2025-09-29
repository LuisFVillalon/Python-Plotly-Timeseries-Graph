# ========= 0. Import Libraries =========
# pandas: for loading and working with tabular data (CSV files, dataframes, etc.)
# plotly.graph_objs: for creating interactive plots
# plotly.subplots.make_subplots: for making figures with multiple y-axes
import pandas as pd
import plotly.graph_objs as go
from plotly.subplots import make_subplots

# ========= 1. Load Data =========
# Define the path to the CSV file that contains EEG and ECG signals.
file_path = "EEG and ECG data_02_raw.csv"

# Open the CSV file in read mode ("r").
# Read all lines into a list, but skip any line that starts with '#' (these are metadata or comments).
with open(file_path, "r") as f:
    lines = [line for line in f if not line.startswith("#")]

# pandas.read_csv usually expects either a file path or a file-like object.
# We currently have our data as a list of strings (lines).
# 1. "".join(lines) combines all lines into one long string.
# 2. StringIO turns that string into a "file-like object" that pandas can read as if it were a file.
from io import StringIO
df = pd.read_csv(StringIO("".join(lines)))

# ========= 2. Select Relevant Columns =========
# Name of the column that stores the time axis (x-axis of the plot).
time_col = "Time"

# List of EEG channel names.
eeg_channels = ["Fz","Cz","P3","C3","F3","F4","C4","P4",
                "Fp1","Fp2","T3","T4","T5","T6",
                "O1","O2","F7","F8","A1","A2","Pz"]

# Dictionary mapping ECG channel names from the file to more user-friendly labels.                
ecg_channels = {"X1:LEOG": "ECG Left", "X2:REOG": "ECG Right"}

# Column name for the CM (common reference electrode).
cm_col = "CM"

# Build a list of columns that we actually want to keep.
# Some datasets may not contain every EEG or ECG channel, so we only include the ones that exist in the dataframe.
cols_to_plot = [
    c for c in [time_col] + eeg_channels + list(ecg_channels.keys()) + [cm_col] 
    if c in df.columns
]

# Filter the dataframe to only keep these relevant columns.
df = df[cols_to_plot]

# ========= 3. Build Plot =========
# Create a plotly figure that supports multiple y-axes.
# secondary_y=True means we will plot some signals on the left y-axis and others on the right y-axis.
fig = make_subplots(specs=[[{"secondary_y": True}]])

# ---- EEG signals (measured in microvolts, µV) ----
# Loop through each EEG channel name.
for ch in eeg_channels:
    # If that channel exists in the dataframe, add it to the plot.
    if ch in df.columns:
        fig.add_trace(
            go.Scatter(
                x=df[time_col],    # x-axis is time
                y=df[ch],          # y-axis is the EEG signal for this channel
                mode="lines",      # plot as a line graph
                name=f"EEG {ch}",  # legend label
                line=dict(width=1) # line thickness
            ),
            secondary_y=False      # EEG signals are plotted on the left y-axis
        )

# ---- ECG signals (measured in millivolts, mV) ----
# Also include CM reference on the right y-axis.
for ch, label in ecg_channels.items():
    # If that channel exists in the dataframe, add it to the plot.
    if ch in df.columns:
        fig.add_trace(
            go.Scatter(
                x=df[time_col],     # x-axis is time
                y=df[ch],           # y-axis is ECG signal
                mode="lines",       # line plot
                name=label,         # use friendly label (ECG Left, ECG Right)
                line=dict(width=1.5) # slightly thicker line
            ),
            secondary_y=True        # ECG signals are plotted on the right y-axis
        )

# Add CM reference line if the column exists.
if cm_col in df.columns:
    fig.add_trace(
        go.Scatter(
            x=df[time_col],
            y=df[cm_col],
            mode="lines",
            name="CM Reference",       # label in legend
            line=dict(width=1, dash="dot")  # thinner dotted line style
        ),
        secondary_y=True                # also plotted on right y-axis
    )

# ========= 4. Layout / Scaling =========
# Configure the look and behavior of the plot.
fig.update_layout(
    title="EEG and ECG Signals (Scrollable)",

    # X-axis: show time in seconds, add a range slider so user can scroll/zoom, linear scaling, initial view from 10s to 10.3s.
    xaxis=dict(title="Time (s)", rangeslider=dict(visible=True), type="linear", range=[10,10.3]),

    # Left Y-axis: EEG signals in microvolts
    yaxis=dict(title="EEG (µV)"),

    # Right Y-axis: ECG and CM signals in millivolts
    yaxis2=dict(title="ECG / CM (mV)", overlaying="y", side="right"),

    # Hover mode: show one tooltip that includes all values at the same time point
    hovermode="x unified",

    # Legend: place it horizontally below the plot
    legend=dict(orientation="h", y=-0.5, x=0, xanchor="left", yanchor="top"),
)

# ========= 5. Show =========
fig.show()
