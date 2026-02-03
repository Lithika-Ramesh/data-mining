# Run GMM Analysis on Google Colab (Full Directory + Dependencies)

This project is **one notebook inside a full directory** with data and dependencies. Use this flow so Colab has the whole repo and correct environment.

---

## Best approach: One notebook, full repo setup in first cell

The notebook **`unsupervised_gmm.ipynb`** already has a **Colab setup cell at the top**. When you open it from GitHub and run it, that cell:

1. **Clones the full repo** (branch `feat/unsupervised_gmm`) so you get:
   - `data-mining/data/final/encoded_unsupervised.csv`
   - `data-mining/gmm_analysis/` (this notebook + docs)
   - `data-mining/reports/` (outputs)
2. **Changes working directory** to `data-mining/gmm_analysis` so paths like `../data/` and `../reports/` work.
3. **Installs dependencies** from `requirements_gmm.txt` (pandas, numpy, scikit-learn, matplotlib, seaborn, plotly, etc.).

So you use **one notebook**, but Colab gets the **whole directory and dependencies** automatically.

---

## Steps to run on Colab

### 1. Open the notebook from GitHub

Use either:

- **Direct link**
  ```
  https://colab.research.google.com/github/Lithika-Ramesh/data-mining/blob/feat/unsupervised_gmm/gmm_analysis/unsupervised_gmm.ipynb
  ```

- **Or manually**
  - Go to [colab.research.google.com](https://colab.research.google.com)
  - **File → Open notebook → GitHub**
  - Repo: `Lithika-Ramesh/data-mining`
  - Branch: `feat/unsupervised_gmm`
  - File: `gmm_analysis/unsupervised_gmm.ipynb`

### 2. Run the first cell (Colab setup)

- Run **only the first cell** (the one titled “GOOGLE COLAB SETUP”).
- Wait until it finishes:
  - Cloning repo
  - Changing to `data-mining/gmm_analysis`
  - Installing from `requirements_gmm.txt`
  - Printing “Setup complete”

### 3. Run the rest of the notebook

- **Runtime → Run all** (or run cells one by one).

After step 2, the working directory is `data-mining/gmm_analysis`, so:

- `../data/final/encoded_unsupervised.csv` → correct data path
- `../reports/` → all outputs (CSVs, PNGs, HTML, etc.) go to the right place

---

## What you get

| Item              | How it’s handled in Colab                          |
|-------------------|----------------------------------------------------|
| Full directory    | First cell clones the whole `data-mining` repo   |
| Dependencies      | First cell runs `pip install -r requirements_gmm.txt` |
| Data              | From `data/final/encoded_unsupervised.csv` in repo |
| Outputs            | Written to `reports/` inside the cloned repo      |

---

## Optional: GPU

- **Runtime → Change runtime type → T4 GPU → Save**
- Then run the notebook as above (first cell, then Run all).

---

## If data is not in the repo (e.g. too large)

If `data/final/encoded_unsupervised.csv` is not in GitHub (e.g. Git LFS or not committed):

1. Upload the CSV to Google Drive.
2. In the **first cell**, after `os.chdir(WORK_DIR)`, add for example:
   ```python
   from google.colab import drive
   drive.mount("/content/drive")
   # Copy or symlink: /content/drive/MyDrive/encoded_unsupervised.csv -> ../data/final/
   ```
3. Or add a small block that downloads the file from a URL if you host it elsewhere.

For the standard case (data committed in the repo), the first cell is enough and no extra steps are needed.

---

## Summary

- **One notebook:** `gmm_analysis/unsupervised_gmm.ipynb`
- **Full directory:** Colab gets it by cloning the repo in the first cell
- **Dependencies:** Installed from `requirements_gmm.txt` in that same cell
- **Run:** Open from GitHub → Run first cell → Run all

This is the intended way to run the project on Colab with the full directory and dependencies.
