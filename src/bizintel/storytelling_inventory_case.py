"""
storytelling_inventory_case.py - retail inventory project.

- Which product category has the highest demand,
  and when should inventory levels be increased?

This module demonstrates the final step of a Business Intelligence
workflow by transforming reporting-ready data into actionable
business insight.

Author: Your Name
Date: 2026-08

Business Question:

Business Question:

- Which product category has the highest demand, and during which
  months is inventory demand strongest?

Data Source:

- data/reporting/retail_inventory_reporting_case.csv

Output:

- docs/images/storytelling_inventory_category_custom_case.png
- docs/images/storytelling_inventory_monthly_custom_case.png

Run this module from the project root:

uv run python -m bizintel.storytelling_inventory_case
"""

# ==========================================================
# Imports
# ==========================================================

from numbers import Real
from pathlib import Path
from typing import Final

from datafun_toolkit.logger import log_path
import matplotlib.pyplot as plt
import pandas as pd

from bizintel.utils_logger import LOG, log_header
from bizintel.utils_viz import plot_bar, plot_line

# ==========================================================
# Constants
# ==========================================================

DATA_REPORTING: Final[Path] = Path("data/reporting")

REPORTING_FILE: Final[Path] = DATA_REPORTING / "retail_inventory_reporting_case.csv"


CHARTS_OUTPUT: Final[Path] = Path("docs/images")
STORYTELLING_CHART_FILE_1: Final[Path] = (
    CHARTS_OUTPUT / "storytelling_inventory_category_demand_case.png"
)

STORYTELLING_CHART_FILE_2: Final[Path] = (
    CHARTS_OUTPUT / "storytelling_inventory_monthly_demand_case.png"
)


def load_reporting_data(file_path: Path) -> pd.DataFrame:
    """
    Load and validate the reporting-ready dataset.

    """

    LOG.info("Loading reporting-ready data")

    if not file_path.exists():
        raise FileNotFoundError(f"Reporting file not found: {file_path}")

    df_reporting = pd.read_csv(file_path)

    required_columns = {
        "YearMonth",
        "Category",
        "TotalQuantitySold",
    }

    missing_columns = required_columns - set(df_reporting.columns)

    if missing_columns:
        raise ValueError(f"Missing columns: {sorted(missing_columns)}")

    if df_reporting.empty:
        raise ValueError("Reporting dataset contains no rows.")

    df_reporting["TotalQuantitySold"] = pd.to_numeric(
        df_reporting["TotalQuantitySold"],
        errors="coerce",
    )

    if df_reporting["TotalQuantitySold"].isna().any():
        raise ValueError("TotalQuantitySold contains invalid values.")

    LOG.info(f"Loaded {df_reporting.shape[0]} rows")

    LOG.info(f"Verified {df_reporting.shape[1]} columns")

    return df_reporting


# ==========================================================
# Section 3.1 Summarize Customer Sales
# ==========================================================


def summarize_category_demand(
    df_reporting: pd.DataFrame,
) -> pd.DataFrame:
    """
    Summarize total demand by product category.
    """

    LOG.info("Summarizing demand by category")

    df_category_demand: pd.DataFrame = (
        df_reporting.groupby(
            "Category",
            as_index=False,
        )
        .agg(TotalDemand=("TotalQuantitySold", "sum"))
        .sort_values(
            "TotalDemand",
            ascending=False,
        )
        .head(10)
    )

    df_category_demand["TotalDemand"] = df_category_demand["TotalDemand"].round(0)

    LOG.info(f"Categories summarized: {df_category_demand.shape[0]}")

    return df_category_demand


# ==========================================================
# Section 3.2 Select Top Customer
# ==========================================================


def select_top_category(
    df_category_demand: pd.DataFrame,
) -> str:
    """
    Select the customer with the highest sales.

    WHY:
    The second part of the story should follow the first result.
    We investigate the leading customer rather than choosing
    one before seeing the data.

    Args:
        df_category_demand:
            Customer sales summary sorted highest to lowest.

    Returns:
        Name of the top_category.
    """

    top_category: str = str(df_category_demand.iloc[0]["Category"])

    LOG.info(f"Selected top category: {top_category}")

    return top_category


# ==========================================================
# Section 3.3 Summarize Monthly Sales for Top Customer
# ==========================================================


def summarize_monthly_category_demand(
    df_reporting: pd.DataFrame,
    selected_category: str,
) -> pd.DataFrame:
    """
    Summarize monthly demand for one product category.

       WHY:
       This explains when the highest-demand product category
       performed most strongly.

       Args:
           df_reporting:
               Complete reporting-ready inventory data.

           selected_category:
               Product category selected from the first analysis.

       Returns:
           DataFrame containing YearMonth and TotalDemand.

    """

    LOG.info(f"Summarizing monthly demand for category: {selected_category}")

    df_selected: pd.DataFrame = df_reporting.loc[
        df_reporting["Category"] == selected_category
    ].copy()

    if df_selected.empty:
        raise ValueError("No demand found for selected category.")

    df_monthly_demand: pd.DataFrame = (
        df_selected.groupby(
            "YearMonth",
            as_index=False,
        )
        .agg(TotalDemand=("TotalQuantitySold", "sum"))
        .sort_values("YearMonth")
    )

    df_monthly_demand["TotalDemand"] = df_monthly_demand["TotalDemand"].round(2)

    LOG.info(f"Months summarized: {df_monthly_demand.shape[0]}")

    return df_monthly_demand


# ==========================================================
# Section 4.1 Identify Key Results
# ==========================================================


def identify_key_results(
    df_category_demand: pd.DataFrame,
    df_monthly_demand: pd.DataFrame,
) -> None:
    """
    Identify factual results from the analysis.

    WHY:
    These results are supported by the data and will be used
    to write the final business story in docs/index.md.

    Args:
        df_category_demand:
            Product category demand summary.

        df_monthly_demand:
            Monthly demand for the top category.

    Returns:
        None
    """

    LOG.info("Identifying key results")

    top_category: str = str(df_category_demand.iloc[0]["Category"])

    top_category_demand: float = float(df_category_demand.iloc[0]["TotalDemand"])

    max_index: int = int(df_monthly_demand["TotalDemand"].idxmax())

    strongest_month: str = str(
        df_monthly_demand.loc[
            max_index,
            "YearMonth",
        ]
    )

    strongest_month_value: object = df_monthly_demand.loc[
        max_index,
        "TotalDemand",
    ]

    if pd.isna(strongest_month_value):
        raise ValueError("Strongest month demand value is missing.")

    if not isinstance(strongest_month_value, Real):
        raise TypeError("Strongest month demand must be numeric.")

    strongest_month_demand: float = float(strongest_month_value)

    LOG.info(f"Top category: {top_category}")

    LOG.info(f"Total demand: {top_category_demand:,.0f} units")

    LOG.info(f"Strongest month: {strongest_month}")

    LOG.info(f"Strongest month demand: {strongest_month_demand:,.0f} units")


# ==========================================================
# Section 4.2 Main Function
# ==========================================================


def main() -> None:
    """
    Run the retail inventory storytelling workflow.
    """

    log_header(
        LOG,
        "RETAIL INVENTORY STORYTELLING",
    )

    LOG.info("========================")
    LOG.info("START main()")
    LOG.info("========================")

    log_path(
        LOG,
        "Input reporting data:",
        REPORTING_FILE,
    )

    # STEP 1:
    # Load trusted reporting-ready data.

    LOG.info("Loading reporting data...")

    df_reporting = load_reporting_data(REPORTING_FILE)

    # STEP 2:
    # Compare product categories.

    LOG.info("Summarizing category demand...")

    df_category_demand = summarize_category_demand(df_reporting)

    # STEP 3:
    # Select the highest-demand category.

    LOG.info("Selecting top category...")

    top_category = select_top_category(df_category_demand)

    # STEP 4:
    # Analyze monthly performance.

    LOG.info("Summarizing monthly category demand...")

    df_monthly_demand = summarize_monthly_category_demand(
        df_reporting,
        top_category,
    )

    # STEP 5:
    # Create chart folder.

    CHARTS_OUTPUT.mkdir(
        parents=True,
        exist_ok=True,
    )

    # ======================================================
    # Chart 1: Category Demand Comparison
    # ======================================================

    LOG.info("Creating category demand chart...")

    plot_bar(
        df=df_category_demand,
        x="Category",
        y="TotalDemand",
        title="Demand by Product Category",
        xlabel="Product Category",
        ylabel="Units Sold",
        palette="Blues_d",
    )

    plt.savefig(
        STORYTELLING_CHART_FILE_1,
        bbox_inches="tight",
    )

    log_path(
        LOG,
        "Saved category demand chart:",
        STORYTELLING_CHART_FILE_1,
    )

    # ======================================================
    # Chart 2: Monthly Demand Trend
    # ======================================================

    LOG.info("Creating monthly category demand chart...")

    plot_line(
        df=df_monthly_demand,
        x="YearMonth",
        y="TotalDemand",
        title=(f"Monthly Demand for {top_category}"),
        xlabel="Month",
        ylabel="Units Sold",
    )

    plt.savefig(
        STORYTELLING_CHART_FILE_2,
        bbox_inches="tight",
    )

    log_path(
        LOG,
        "Saved monthly demand chart:",
        STORYTELLING_CHART_FILE_2,
    )

    # STEP 6:
    # Identify facts for the story.

    identify_key_results(
        df_category_demand,
        df_monthly_demand,
    )

    LOG.info("Showing charts...")

    plt.show()

    LOG.info("Retail inventory storytelling workflow complete.")

    LOG.info("========================")
    LOG.info("Executed successfully!")
    LOG.info("========================")


# ==========================================================
# Conditional Execution Guard
# ==========================================================

if __name__ == "__main__":
    main()
