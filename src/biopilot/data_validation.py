from collections.abc import Sequence

import numpy as np
import pandas as pd


def validate_fitness_dataframe(
    df: pd.DataFrame,
    sequence_column: str = "sequence",
    target_column: str = "target",
    split_column: str | None = None,
    allowed_splits: Sequence[str] = ("train", "validation", "test"),
) -> list[str]:
    """Return validation errors; an empty list means no errors were found."""
    required_columns = [sequence_column, target_column]

    if split_column is not None:
        required_columns.append(split_column)

    missing_columns = [
        column for column in required_columns if column not in df.columns
    ]
    if missing_columns:
        return [f"Missing required columns: {missing_columns}"]

    if df.empty:
        return ["Dataset contains no rows."]

    errors: list[str] = []
    sequences = df[sequence_column]
    targets = df[target_column]

    if sequences.isna().any():
        errors.append("Sequence column contains missing values.")

    non_missing_sequences = sequences.dropna()
    is_string = non_missing_sequences.map(
        lambda value: isinstance(value, str)
    )

    if not is_string.all():
        errors.append("Sequence column contains non-string values.")
    else:
        if non_missing_sequences.map(
            lambda value: not value.strip()
        ).any():
            errors.append("Sequence column contains empty sequences.")

        if non_missing_sequences.duplicated().any():
            errors.append("Sequence column contains duplicate sequences.")

    numeric_targets = pd.to_numeric(targets, errors="coerce")
    target_array = numeric_targets.to_numpy(dtype=float, na_value=np.nan)

    if targets.isna().any() or np.isnan(target_array).any():
        errors.append("Target column contains missing or non-numeric values.")
    elif not np.isfinite(target_array).all():
        errors.append("Target column contains non-finite values.")

    if split_column is not None:
        splits = df[split_column]

        if splits.isna().any():
            errors.append("Split column contains missing values.")
        else:
            invalid_splits = [
                value
                for value in splits.unique()
                if not isinstance(value, str) or value not in allowed_splits
            ]
            if invalid_splits:
                labels = sorted(repr(value) for value in invalid_splits)
                errors.append(f"Unknown split labels: {labels}")

    return errors
