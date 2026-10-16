# BioPilot

**Uncertainty-aware active learning for protein engineering research.**

BioPilot investigates whether uncertainty-aware candidate selection can reduce the number of labelled protein variants needed to reach a predefined predictive-performance target, compared with random selection, sequence-diversity selection, and conventional supervised ranking.

> **Research status:** project setup. No benchmark task has been finalized, and no model results have been produced.

## Research question

Under a limited labelled-data budget, can uncertainty-aware active learning reach a predefined protein-fitness prediction target with fewer labelled examples than simpler selection policies?

This is a research hypothesis, not an established result. Retrospective benchmark simulations do not by themselves establish wet-lab performance.

## Research principles

- Define the biological target and assay before choosing the model.
- Audit data provenance, licensing, label semantics, and split construction.
- Keep test labels out of model selection and acquisition decisions.
- Compare against simple, meaningful baselines.
- Record uncertainty, variability, limitations, and negative results.
- Do not claim experimental or commercial validation without supporting evidence.

## Planned initial workflow

1. Audit candidate protein-fitness benchmark tasks.
2. Select one task and document its assay, target, licence, and split.
3. Build reproducible data-cleaning and exploratory-analysis tools.
4. Implement simple sequence-feature and nearest-neighbour baselines.
5. Evaluate frozen protein embeddings only if justified by results and compute budget.
6. Compare random, diversity, and uncertainty-guided acquisition policies.
7. Report label-budget curves, variability, calibration, and failure modes.

## Repository layout

```text
BioPilot/
├── docs/
│   ├── dataset_card_template.md
│   └── experiment_log.md
├── src/
│   └── biopilot/
├── tests/
├── notebooks/
├── data/                 # local data only; not committed
├── .gitignore
├── pyproject.toml
└── README.md
```

Some directories will appear in Git only after files are added to them.

## Requirements

- Python 3.11 or 3.12
- Git
- A terminal

## Setup

### 1. Clone the repository

```bash
git clone https://github.com/hathilal/BioPilot.git
cd BioPilot
```

### 2. Create and activate a virtual environment

**macOS / Linux**

```bash
python3.11 -m venv .venv
source .venv/bin/activate
```

**Windows PowerShell**

```powershell
py -3.11 -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 3. Install the project and development tools

```bash
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

### 4. Verify the environment

```bash
python --version
python -m pip check
pytest
```

The initial test suite contains a smoke test that checks whether the installed package exposes a non-empty version string. This is only a basic packaging check, not evidence that scientific code or models are correct.

## Data handling

Do not commit raw datasets, private laboratory data, credentials, or API keys. Before downloading or redistributing a dataset, check its licence and usage terms. Record its source, retrieval date, checksum where feasible, preprocessing, and split definition in the dataset card.

## Current milestone

**Milestone 1: repository scaffold and environment setup.**

Next: audit one benchmark task and decide whether its labels, assay definition, licence, and split are appropriate for a retrospective active-learning study.

## Development hardware and acceleration

The initial development machine reported an Intel Core i5-1240P CPU (16 logical CPUs), Intel Iris Xe integrated graphics, and 16 GiB RAM. No NVIDIA GPU was listed, and `nvidia-smi` could not communicate with an NVIDIA driver. Based on this evidence, CUDA is not the appropriate initial setup path.

Start with CPU-friendly baselines and measure runtime and memory before increasing model complexity. Useful practices include:
- Set estimator parallelism deliberately (for supported scikit-learn estimators, consider `n_jobs`), and benchmark rather than assuming more workers are faster.
- Cache sequence features or pretrained embeddings so active-learning rounds do not recompute them unnecessarily.
- Keep an eye on RAM use; protein-language-model embeddings and fine-tuning can exceed a laptop's practical memory/time budget.
- Consider Intel GPU acceleration only if a chosen framework explicitly supports the available Intel hardware and software stack; do not assume CUDA compatibility.

Hardware and available memory are machine-specific and may change. No GPU acceleration or model-training performance has yet been benchmarked for BioPilot.

