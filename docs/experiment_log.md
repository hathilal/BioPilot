# BioPilot Experiment Log

Record each run so that its purpose, configuration, and result can be reconstructed. Never fill in results before a run has actually completed.

## Run template

### Identification

- **Run ID:**
- **Date/time and timezone:**
- **Git commit SHA:**
- **Dataset version and checksum:**
- **Configuration file / parameters:**
- **Environment / Python version:**
- **Hardware:**

### Question and hypothesis

- **Question:**
- **Hypothesis:**
- **What result would falsify the hypothesis?**

### Method

- **Model / acquisition policy:**
- **Training data and label budget:**
- **Validation protocol:**
- **Test protocol:**
- **Random seeds / repeated runs:**
- **Metrics and why they are appropriate:**

### Results

- **Observed results:**
- **Variability / confidence intervals:**
- **Runtime and peak memory:**
- **Warnings or failures:**

### Interpretation

- **What does the result support?**
- **What does it not establish?**
- **Error analysis:**
- **Possible leakage or confounders:**
- **Next action:**

---

## Research decision log

| Date | Decision | Alternatives | Evidence | Rationale | Consequence |
|---|---|---|---|---|---|
| 2026-10-16 | Begin with repository scaffold before modeling | Start model first | Project requirements | Establish reproducibility and data governance first | Audit benchmark after setup |
