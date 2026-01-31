# Run This Project in the Cloud (Full Directory)

**Repo:** [Lithika-Ramesh/data-mining](https://github.com/Lithika-Ramesh/data-mining)  
**Branch:** `feat/unsupervised_gmm`

Use one of the links below to open the **whole directory** in the cloud and run the notebook with dependencies.

---

## Best option: whole directory in the cloud

### 1. GitHub Codespaces (recommended – full dir, same as local)

**One link → full repo, VS Code in browser, all deps.**

| | |
|---|---|
| **Open in Codespaces** | [**https://codespaces.new/Lithika-Ramesh/data-mining?ref=feat/unsupervised_gmm**](https://codespaces.new/Lithika-Ramesh/data-mining?ref=feat/unsupervised_gmm) |

- You get the **entire repo** (data, notebooks, reports, everything).
- Full **VS Code** in the browser (same experience as Cursor/VS Code).
- **Dependencies:** in the terminal run:  
  `cd gmm_analysis && pip install -r requirements_gmm.txt`
- Then open `gmm_analysis/unsupervised_gmm.ipynb` and run it.
- **Free tier:** 60 hours/month for personal accounts.

**Steps:** Click link → wait for Codespace to start → open `gmm_analysis/unsupervised_gmm.ipynb` → run first cell (or Run All).

---

### 2. Gitpod (full dir, VS Code–style)

**One link → full repo in Gitpod.**

| | |
|---|---|
| **Open in Gitpod** | [**https://gitpod.io/#https://github.com/Lithika-Ramesh/data-mining/tree/feat/unsupervised_gmm**](https://gitpod.io/#https://github.com/Lithika-Ramesh/data-mining/tree/feat/unsupervised_gmm) |

- You get the **whole directory** (same as cloning the branch).
- VS Code–style IDE in the browser.
- **Dependencies:** in project root:  
  `cd gmm_analysis && pip install -r requirements_gmm.txt`
- Then open `gmm_analysis/unsupervised_gmm.ipynb` and run.
- **Free tier:** 50 hours/month.

---

### 3. Google Colab (notebook + clone in first cell)

**One link → notebook only; first cell clones repo and installs deps.**

| | |
|---|---|
| **Open in Colab** | [**https://colab.research.google.com/github/Lithika-Ramesh/data-mining/blob/feat/unsupervised_gmm/gmm_analysis/unsupervised_gmm.ipynb**](https://colab.research.google.com/github/Lithika-Ramesh/data-mining/blob/feat/unsupervised_gmm/gmm_analysis/unsupervised_gmm.ipynb) |

- Opens **only** the GMM notebook.
- The **first cell** in the notebook clones the repo and runs `pip install -r requirements_gmm.txt`, so you effectively get the **whole dir** (and data) for that session.
- Good **free GPU** (e.g. T4) and RAM.
- No full IDE; best for “run this one notebook in the cloud.”

**Steps:** Click link → Run the first (setup) cell → Run All.

---

## Comparison

| | Codespaces | Gitpod | Colab |
|---|------------|--------|--------|
| **Whole directory** | Yes (full repo) | Yes (full repo) | Yes (cloned in first cell) |
| **IDE** | VS Code in browser | VS Code–style | Notebook only |
| **Dependencies** | You run `pip install -r ...` once | Same | First cell runs it |
| **GPU** | No (CPU) | No (CPU) | Yes (free T4) |
| **Free tier** | 60 h/month | 50 h/month | Free (with limits) |
| **Best for** | Full project, multi-file, like local | Same | Single notebook, max speed/GPU |

---

## Recommendation

- **You want “add link of my GitHub repo (branch) and run it in any cloud with whole dir”:**
  - **Best:** **GitHub Codespaces** – one link, full repo, full IDE, same layout as local.  
    → [**https://codespaces.new/Lithika-Ramesh/data-mining?ref=feat/unsupervised_gmm**](https://codespaces.new/Lithika-Ramesh/data-mining?ref=feat/unsupervised_gmm)
- **If you prefer a Colab-style “just run the notebook” with GPU:** use the **Colab** link above; the first cell gives you the whole dir for that run.

---

## Quick links (copy-paste)

```
# Full directory + IDE (recommended)
https://codespaces.new/Lithika-Ramesh/data-mining?ref=feat/unsupervised_gmm

# Full directory + Gitpod
https://gitpod.io/#https://github.com/Lithika-Ramesh/data-mining/tree/feat/unsupervised_gmm

# Notebook in Colab (first cell clones whole dir + deps)
https://colab.research.google.com/github/Lithika-Ramesh/data-mining/blob/feat/unsupervised_gmm/gmm_analysis/unsupervised_gmm.ipynb
```

Use the Codespaces link when you want “my GitHub repo, my branch, whole dir, run in any cloud.”
