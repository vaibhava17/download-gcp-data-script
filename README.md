# Setup and Execution Guide

This guide will walk you through installing Python, the Google Cloud CLI, logging in with your Google account, setting up a Python environment using Zsh on macOS, and executing a Python script to download files from Google Cloud Storage.

## Prerequisites

### 1. Install Python

#### Check if Python is Installed
1. Open your terminal and run:
    ```sh
    python3 --version
    ```
   - If Python is installed, the terminal will display the version number. If not, proceed with the steps below.

#### Install Python via Homebrew
1. **Install Homebrew** (if not already installed):
    ```sh
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
    ```
2. **Install Python**:
    ```sh
    brew install python
    ```
3. **Verify the Installation**:
    ```sh
    python3 --version
    ```

### 2. Install Google Cloud CLI

#### Install Google Cloud SDK
1. **Download the Google Cloud SDK**:
   - Visit the [Google Cloud SDK installation page](https://cloud.google.com/sdk/docs/install) and download the appropriate file for your system under step 2.

2. **Install the SDK**:
    ```sh
    cd ~/Downloads
    tar -xvzf google-cloud-cli-*.tar.gz
    ./google-cloud-sdk/install.sh
    ```

3. **Initialize and Authenticate**:
    - Initialize the SDK and authenticate with your Google account:
    ```sh
    gcloud init
    gcloud auth login
    gcloud config set project <project-id>
    ```

## Downloading the CVs

### 1. Export Data from MySQL

1. **Open MySQL Workbench**:
   - Execute the provided query to fetch the data with `file.sql` in the same directory as Python script (`download_from_csv.py`).
   - Export the results as a CSV file named `data_list.csv`.
   - Place this file in the same directory as your Python script (`download_from_csv.py`).

### 2. Execute the Python Script

1. **Navigate to the Script Directory**:
    ```sh
    cd ~/Downloads/csv_script
    ```

2. **Run the Script**:
    ```sh
    python3 download_from_csv.py
    ```

    - The script will download the files specified in `cv_list.csv` from Google Cloud Storage.
