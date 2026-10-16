# Dataset audit: FLIP2 Alpha Amylase (preliminary)

**Status:** candidate selected for a small, CPU-friendly pilot; data has not yet been downloaded or independently inspected.

## Research fit

BioPilot asks whether uncertainty-aware active learning can reach a predeclared held-out predictive-performance target with fewer labelled examples than random sampling, sequence-diversity selection, and predicted-fitness ranking.

## Candidate benchmark

- Benchmark: FLIP2, Alpha Amylase (Amylase), `one-to-many` split.
- Official source: https://flip.protein.properties/
- Dataset page reports 3,706 variants and 488 single mutants.
- Biological task: alpha-amylase variants; reported assay concerns stain-removal activity.
- Split semantics: training variants have one mutation; test variants have more than one mutation.
- Dataset-specific license reported by the benchmark page: MIT. The FLIP2 benchmark also describes overall data redistribution under CC-BY 4.0; verify the dataset's bundled README/provenance and license file before redistributing any downloaded data.
- Official data format: compressed CSV with `sequence`, `target`, `set`, and `validation` columns.

## Why this is a pilot, not the final benchmark decision

The reported size is manageable for a laptop CPU and avoids requiring CUDA or a large protein language model. The predefined one-to-many split provides a biologically relevant generalization test to variants with more mutations. However, active learning on this benchmark would be a retrospective simulation: the labels already exist in the public dataset, and treating unqueried training labels as hidden simulates an assay budget. It does not demonstrate real wet-lab cost savings.

## Required checks before modeling

1. Download only the selected split and its dataset-specific README/provenance.
2. Confirm the exact file URL, license, attribution/citation, and source assay publication.
3. Inspect row counts by `set` and `validation`, target units/transformations, missing values, duplicate sequences, and sequence lengths/alphabet.
4. Confirm no test rows or test labels enter feature fitting, acquisition, hyperparameter selection, or stopping decisions.
5. Audit train/test sequence overlap and mutation-count distribution; document the split's intended generalization regime.
6. Define a validation protocol using only training data before choosing a target-performance threshold.
7. Pre-register initial label budget, acquisition batch size, random seeds, repeated trials, metrics, and stopping criterion.

## Proposed initial experiment design (not yet implemented)

- Fixed held-out test: official FLIP2 test split; never used for acquisition or model selection.
- Simulated query pool: rows assigned to official training set. Start with a reproducible small labelled seed; treat the rest of the training labels as unavailable until selected.
- Methods: random sampling; sequence-diversity sampling; uncertainty sampling; predicted-fitness ranking as a separate exploitation comparator.
- Use the same initial labelled seeds, query budget, model family, and evaluation schedule across methods where applicable.
- CPU-friendly first baseline: one-hot sequence encoding with a regularized regression model; uncertainty estimation method to be selected and justified before implementation.
- Primary metric candidate: Spearman rank correlation on the fixed test set, because ranking variants is central to fitness prioritization. Also report a regression metric and performance-versus-label-budget curves.
- Report mean and uncertainty across repeated seeds; define the target threshold using validation-only evidence, not by inspecting the test results.

## Current decision

Proceed with Alpha Amylase `one-to-many` as the **pilot candidate**, conditional on verifying the actual file, label definition, and license from the downloaded dataset documentation. Do not begin model training until the audit is complete.
