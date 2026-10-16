# BioPilot development workflow

## Agreed working style

Develop and document the project locally first, keep changes in GitHub, and record decisions and progress in the Notion project charter. Use Kaggle later for dataset-backed model training and experiments.

## Responsibilities by environment

- **Local laptop:** learn Python and ML concepts, develop small modules, run unit tests, inspect code, and commit changes. Keep computation CPU-friendly.
- **GitHub:** version-control source code, tests, dataset cards, experiment protocols, and documentation. Do not commit datasets, secrets, large model weights, or generated artifacts.
- **Notion:** record decisions, milestones, experiment summaries, open questions, and next actions.
- **Kaggle (later):** run the prepared training notebook, use available CPU/GPU resources, evaluate models, and export experiment artifacts.

## Development sequence

1. Confirm repository structure and understand the package/test setup.
2. Implement and test data-validation utilities without requiring a live download.
3. Document the selected benchmark's provenance, target, official split, and license.
4. Prepare a training pipeline with clear separation of train, validation, and test data.
5. Move the dataset-backed notebook to Kaggle when the user is ready; validate actual schema before fitting.
6. Establish a baseline, then tune and compare models using validation data only.
7. Consider protein language model embeddings or fine-tuning only after the baseline is measured.
8. Build an agent with explicit approval gates for new datasets, expensive jobs, and publishing artifacts.

## Reproducibility and evaluation rules

- Never claim a model has trained unless the run actually completed.
- Never tune against held-out test labels.
- Record data source/version, split definition, preprocessing, random seed, software versions, metrics, and artifact locations.
- Evaluate generalization to unseen protein variants, not training accuracy alone.
- Retrospective active-learning simulations are not evidence of real wet-lab cost savings.

## Current status

The package smoke test has previously passed locally. No FLIP2 dataset download or model training has been confirmed. The Kaggle download guide is reference material for the later cloud-training stage, not a task that must be completed now.
