"""
prepare_inventory_case.py - retail inventory preparation.

This module prepares raw retail inventory data
for downstream BI analysis.

Workflow:

raw data
    ↓
prepared data
    ↓
warehouse
    ↓
reporting
    ↓
storytelling

Business Purpose:

Clean and enrich retail inventory transactions
by creating monthly reporting fields and inventory metrics.

Input:

- data/raw/retail_inventory_case.csv

Output:

- data/prepared/retail_inventory_prepared_case.csv

Run this module from the project root:

uv run python -m bizintel.prepare_inventory_case
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

DATA_RAW: Final[Path] = Path("data/raw")

DATA_PREPARED: Final[Path] = Path("data/prepared")


RAW_FILE: Final[Path] = DATA_RAW / "retail_inventory_case.csv"


PREPARED_FILE: Final[Path] = DATA_PREPARED / "retail_inventory_prepared_case.csv"
# ==========================================================
# Load Raw Data Function
# ==========================================================


def load_raw_data(file_path: Path) -> pd.DataFrame:
    """
    Load and validate raw retail inventory data.

    WHY:
    The preparation stage begins with trusted raw data.
    We verify the required columns before transforming
    the dataset.

    Args:
        file_path:
            Path to the raw inventory CSV.

    Returns:
        Validated pandas DataFrame.
    """

    LOG.info("Loading raw inventory data")

    if not file_path.exists():
        raise FileNotFoundError(f"Raw inventory file not found: {file_path}")

    df: pd.DataFrame = pd.read_csv(file_path)

    required_columns: set[str] = {
        "TransactionID",
        "SaleDate",
        "ProductID",
        "ProductName",
        "Category",
        "Region",
        "QuantitySold",
        "UnitPrice",
        "InventoryBeforeSale",
    }

    missing_columns: set[str] = required_columns - set(df.columns)

    if missing_columns:
        raise ValueError(f"Missing required columns: {sorted(missing_columns)}")

    if df.empty:
        raise ValueError("Raw inventory dataset contains no rows.")

    LOG.info(f"Loaded {df.shape[0]} raw rows")

    LOG.info(f"Verified {df.shape[1]} columns")

    return df


# ==========================================================
# Prepare Inventory Data Function
# ==========================================================


def prepare_inventory_data(
    df_raw: pd.DataFrame,
) -> pd.DataFrame:
    """
    Clean and enrich raw inventory data.

    WHY:
    The preparation stage transforms raw transactions
    into analysis-ready data.

    Creates:
        - YearMonth
        - Revenue
        - InventoryAfterSale

    Args:
        df_raw:
            Raw inventory transaction DataFrame.

    Returns:
        Prepared inventory DataFrame.
    """

    LOG.info("Preparing inventory data")

    df_prepared: pd.DataFrame = df_raw.copy()

    # Convert SaleDate to datetime.
    df_prepared["SaleDate"] = pd.to_datetime(
        df_prepared["SaleDate"],
        errors="coerce",
    )

    if df_prepared["SaleDate"].isna().any():
        raise ValueError("SaleDate contains invalid values.")

    # Create monthly reporting dimension.
    df_prepared["YearMonth"] = df_prepared["SaleDate"].dt.to_period("M").astype(str)

    # Convert numeric columns.
    numeric_columns: list[str] = [
        "QuantitySold",
        "UnitPrice",
        "InventoryBeforeSale",
    ]

    for column in numeric_columns:
        df_prepared[column] = pd.to_numeric(
            df_prepared[column],
            errors="coerce",
        )

        if df_prepared[column].isna().any():
            raise ValueError(f"{column} contains invalid values.")

    # Calculate revenue.
    df_prepared["Revenue"] = df_prepared["QuantitySold"] * df_prepared["UnitPrice"]

    # Calculate remaining inventory.
    df_prepared["InventoryAfterSale"] = (
        df_prepared["InventoryBeforeSale"] - df_prepared["QuantitySold"]
    )

    # Round currency values.
    df_prepared["Revenue"] = df_prepared["Revenue"].round(2)

    LOG.info(f"Prepared {df_prepared.shape[0]} rows")

    LOG.info(f"Prepared {df_prepared.shape[1]} columns")

    return df_prepared


# ==========================================================
# Save Prepared Data Function
# ==========================================================


def save_prepared_data(
    df_prepared: pd.DataFrame,
    file_path: Path,
) -> None:
    """
    Save prepared inventory data.

    WHY:
    The prepared dataset becomes the trusted input
    for the next BI stages.

    Args:
        df_prepared:
            Prepared inventory DataFrame.

        file_path:
            Output CSV path.

    Returns:
        None
    """

    LOG.info("Saving prepared inventory data")

    file_path.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    df_prepared.to_csv(
        file_path,
        index=False,
    )

    log_path(
        LOG,
        "Saved prepared data:",
        file_path,
    )
    # ==========================================================


# Main Function
# ==========================================================


def main() -> None:
    """
    Run the inventory preparation workflow.
    """

    log_header(
        LOG,
        "RETAIL INVENTORY PREPARATION",
    )

    LOG.info("========================")
    LOG.info("START main()")
    LOG.info("========================")

    log_path(
        LOG,
        "Input raw data:",
        RAW_FILE,
    )

    # Step 1:
    # Load raw inventory data.

    df_raw = load_raw_data(
        RAW_FILE,
    )

    # Step 2:
    # Prepare inventory data.

    df_prepared = prepare_inventory_data(
        df_raw,
    )

    # Step 3:
    # Save prepared dataset.

    save_prepared_data(
        df_prepared,
        PREPARED_FILE,
    )

    LOG.info("========================")
    LOG.info("Inventory preparation complete")
    LOG.info("Executed successfully!")
    LOG.info("========================")


# ==========================================================
# Conditional Execution Guard
# ==========================================================


if __name__ == "__main__":
    main()
