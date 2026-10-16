import pandas as pd

from biopilot.data_validation import validate_fitness_dataframe


def test_valid_dataframe_has_no_errors() -> None:
    df = pd.DataFrame(
        {
            "sequence": ["ACDE", "FGHI", "KLMN"],
            "target": [0.1, 0.5, 0.9],
            "split": ["train", "train", "test"],
        }
    )

    assert validate_fitness_dataframe(df, split_column="split") == []


def test_missing_required_column_is_reported() -> None:
    df = pd.DataFrame({"sequence": ["ACDE"]})

    errors = validate_fitness_dataframe(df)

    assert any("Missing required columns" in error for error in errors)


def test_missing_target_is_reported() -> None:
    df = pd.DataFrame(
        {"sequence": ["ACDE", "FGHI"], "target": [0.1, None]}
    )

    errors = validate_fitness_dataframe(df)

    assert any("missing or non-numeric" in error for error in errors)


def test_duplicate_sequences_are_reported() -> None:
    df = pd.DataFrame(
        {"sequence": ["ACDE", "ACDE"], "target": [0.1, 0.2]}
    )

    errors = validate_fitness_dataframe(df)

    assert any("duplicate sequences" in error for error in errors)


def test_unknown_split_is_reported() -> None:
    df = pd.DataFrame(
        {
            "sequence": ["ACDE"],
            "target": [0.1],
            "split": ["holdout"],
        }
    )

    errors = validate_fitness_dataframe(df, split_column="split")

    assert any("Unknown split labels" in error for error in errors)



def test_empty_dataframe_is_rejected() -> None:
    df = pd.DataFrame(columns=["sequence", "target"])

    errors = validate_fitness_dataframe(df)

    assert "Dataset contains no rows." in errors


def test_empty_sequence_is_reported() -> None:
    df = pd.DataFrame(
        {"sequence": ["ACDE", "   "], "target": [0.1, 0.2]}
    )

    errors = validate_fitness_dataframe(df)

    assert any("empty sequences" in error for error in errors)


def test_non_string_sequence_is_reported() -> None:
    df = pd.DataFrame(
        {"sequence": ["ACDE", 123], "target": [0.1, 0.2]}
    )

    errors = validate_fitness_dataframe(df)

    assert any("non-string values" in error for error in errors)


def test_infinite_target_is_rejected() -> None:
    df = pd.DataFrame(
        {"sequence": ["ACDE", "FGHI"], "target": [0.1, float("inf")]}
    )

    errors = validate_fitness_dataframe(df)

    assert any("non-finite values" in error for error in errors)


def test_missing_split_is_reported() -> None:
    df = pd.DataFrame(
        {
            "sequence": ["ACDE", "FGHI"],
            "target": [0.1, 0.2],
            "split": ["train", None],
        }
    )

    errors = validate_fitness_dataframe(df, split_column="split")

    assert any("Split column contains missing values" in error for error in errors)
