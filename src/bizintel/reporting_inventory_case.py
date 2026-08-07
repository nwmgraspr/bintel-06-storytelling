"""
reporting_inventory_case.py - retail inventory reporting.

Creates a reporting-ready dataset from prepared inventory data.

BI Workflow:

raw
↓
prepared
↓
reporting
↓
analysis
↓
storytelling

Business Question:

Which product category has the highest demand,
and when is demand strongest?

Input:

- data/prepared/retail_inventory_prepared_case.csv

Output:

- data/reporting/retail_inventory_reporting_case.csv

Run:

uv run python -m bizintel.reporting_inventory_case
"""

# ==========================================================
# Imports
# ==========================================================

from pathlib import Path
from typing import Final

from datafun_toolkit.logger import log_path
import pandas as pd

from bizintel.utils_logger import LOG, log_header

# ==========================================================
# Constants
# ==========================================================

DATA_PREPARED: Final[Path] = Path("data/prepared")

DATA_REPORTING: Final[Path] = Path("data/reporting")


PREPARED_FILE: Final[Path] = DATA_PREPARED / "retail_inventory_prepared_case.csv"


REPORTING_FILE: Final[Path] = DATA_REPORTING / "retail_inventory_reporting_case.csv"
# ==========================================================
# Load Prepared Data Function
# ==========================================================


def load_prepared_data(
    file_path: Path,
) -> pd.DataFrame:
    """
    Load and validate prepared inventory data.

    WHY:
    The reporting stage should use trusted prepared data.
    We do not repeat cleaning work here.

    Args:
        file_path:
            Path to the prepared inventory CSV.

    Returns:
        Validated prepared DataFrame.
    """

    LOG.info("Loading prepared inventory data")

    if not file_path.exists():
        raise FileNotFoundError(f"Prepared file not found: {file_path}")

    df_prepared: pd.DataFrame = pd.read_csv(file_path)

    required_columns: set[str] = {
        "YearMonth",
        "ProductName",
        "Category",
        "Region",
        "QuantitySold",
        "Revenue",
        "InventoryAfterSale",
    }

    missing_columns: set[str] = required_columns - set(df_prepared.columns)

    if missing_columns:
        raise ValueError(f"Missing required columns: {sorted(missing_columns)}")

    if df_prepared.empty:
        raise ValueError("Prepared inventory dataset contains no rows.")

    LOG.info(f"Loaded {df_prepared.shape[0]} prepared rows")

    LOG.info(f"Verified {df_prepared.shape[1]} columns")

    return df_prepared


# ==========================================================
# Create Reporting Dataset Function
# ==========================================================


def create_inventory_reporting(
    df_prepared: pd.DataFrame,
) -> pd.DataFrame:
    """
    Create reporting-ready inventory summary.

    WHY:
    Reporting datasets are designed for business analysis.
    We summarize transaction-level data into useful measures.

    Args:
        df_prepared:
            Prepared inventory DataFrame.

    Returns:
        Reporting-ready DataFrame.
    """

    LOG.info("Creating inventory reporting dataset")

    df_reporting: pd.DataFrame = (
        df_prepared.groupby(
            [
                "YearMonth",
                "Category",
                "ProductName",
            ],
            as_index=False,
        )
        .agg(
            TotalQuantitySold=(
                "QuantitySold",
                "sum",
            ),
            TotalRevenue=(
                "Revenue",
                "sum",
            ),
            AverageInventoryRemaining=(
                "InventoryAfterSale",
                "mean",
            ),
        )
        .sort_values(
            [
                "YearMonth",
                "TotalQuantitySold",
            ],
            ascending=[
                True,
                False,
            ],
        )
    )

    # Round decimal reporting values.
    df_reporting["TotalRevenue"] = df_reporting["TotalRevenue"].round(2)

    df_reporting["AverageInventoryRemaining"] = df_reporting[
        "AverageInventoryRemaining"
    ].round(2)

    LOG.info(f"Reporting rows created: {df_reporting.shape[0]}")

    LOG.info(f"Reporting columns created: {df_reporting.shape[1]}")

    return df_reporting


# ==========================================================
# Save Reporting Data Function
# ==========================================================


def save_reporting_data(
    df_reporting: pd.DataFrame,
    file_path: Path,
) -> None:
    """
    Save reporting-ready inventory data.

    WHY:
    The reporting dataset is the trusted input
    for analysis and storytelling.

    Args:
        df_reporting:
            Reporting-ready inventory DataFrame.

        file_path:
            Output CSV path.

    Returns:
        None
    """

    LOG.info("Saving reporting inventory data")

    file_path.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    df_reporting.to_csv(
        file_path,
        index=False,
    )

    log_path(
        LOG,
        "Saved reporting data:",
        file_path,
    )
    # ==========================================================


# Main Function
# ==========================================================


def main() -> None:
    """
    Run the inventory reporting workflow.
    """

    log_header(
        LOG,
        "RETAIL INVENTORY REPORTING",
    )

    LOG.info("========================")
    LOG.info("START main()")
    LOG.info("========================")

    log_path(
        LOG,
        "Input prepared data:",
        PREPARED_FILE,
    )

    # Step 1:
    # Load prepared inventory data.

    df_prepared = load_prepared_data(
        PREPARED_FILE,
    )

    # Step 2:
    # Create reporting dataset.

    df_reporting = create_inventory_reporting(
        df_prepared,
    )

    # Step 3:
    # Save reporting dataset.

    save_reporting_data(
        df_reporting,
        REPORTING_FILE,
    )

    LOG.info("========================")
    LOG.info("Inventory reporting complete")
    LOG.info("Executed successfully!")
    LOG.info("========================")
    # ==========================================================


# Conditional Execution Guard
# ==========================================================


if __name__ == "__main__":
    main()
