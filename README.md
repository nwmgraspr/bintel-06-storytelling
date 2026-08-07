# bintel-06-storytelling

[![Workflow Guide](https://img.shields.io/badge/Pro--Guide-pro--analytics--02-green)](https://denisecase.github.io/pro-analytics-02/workflow-b-apply-example-project/)
[![Python 3.14](https://img.shields.io/badge/python-3.14%2B-blue?logo=python)](./pyproject.toml)
[![MIT](https://img.shields.io/badge/license-see%20LICENSE-yellow.svg)](./LICENSE)

> Professional Python project: BI storytelling with smart sales data.

## Project Description

This project focuses on addressing one specific business goal
end to end and telling a story with data.

We learn to:

- define a clear business question and KPI (key performance indicator)
- use reporting-ready data to answer the business question
- summarize and analyze the relevant data
- create connected charts that support the findings
- identify meaningful business insights
- write a clear, actionable business recommendation
- tell a story with data

## Working Files

You'll work with these areas:

- **data/reporting** - reporting-ready data generated earlier
- **docs/** - project narrative and documentation
- **src/bizintel/** - the app is an example; run only (copy to a new file for your work)
- **pyproject.toml** - update authorship & links
- **zensical.toml** - update authorship & links

## Instructions (pro-analytics-02)

Follow the
[step-by-step workflow guide](https://denisecase.github.io/pro-analytics-02/workflow-b-apply-example-project/)
to complete:

1. Phase 1. **Start & Run**
2. Phase 2. **Change Authorship**
3. Phase 3. **Read & Understand**
4. Phase 4. **Modify**
5. Phase 5. **Apply**

## Challenges

Challenges are expected.
Sometimes instructions may not quite match your operating system.
When issues occur, share screenshots, error messages, and details about what you tried.
Working through issues is part of implementing professional projects.

## Success

After completing Phase 1. **Start & Run**,
you'll have your own GitHub project,
and running the example module will print out:

```shell
========================
Executed successfully!
========================
```

A new file `project.log` will appear in the root project folder.

## Command Reference

### Commands Used fo Custom Project

Create the inventory dataset:

```powershell
uv run python create_inventory_data.py

- Prepare the raw inventory data:
uv run python -m bizintel.prepare_inventory_case

- Create reporting-ready data:
uv run python -m bizintel.reporting_inventory_case

-Generate storytelling analysis and charts:
uv run python -m bizintel.storytelling_inventory_case

- Building documentation
uv run zensical build

### In a machine terminal (open in your `Repos` folder)

After you get a copy of this repo in your own GitHub account,
open a machine terminal in your `Repos` folder:

```shell
# Replace username with YOUR GitHub username.
git clone https://github.com/nwmgraspr/bintel-06-storytelling

cd bintel-06-storytelling
code .
```

### In a VS Code terminal

These are listed for convenience.
For best results, follow the detailed instructions in
[pro-analytics-02 guide](https://denisecase.github.io/pro-analytics-02/).

```shell
uv self update
uv python pin 3.14
uv lock --upgrade
uv sync --extra dev --extra docs --upgrade

uvx pre-commit install
uvx pre-commit autoupdate

git add -A
uvx pre-commit run --all-files
# repeat if changes were made
uvx pre-commit run --all-files

# OPTIONAL: run the example module
uv run python -m bizintel.app_case

# TASK 1: run the example storytelling module for an example problem
uv run python -m bizintel.storytelling_case

# TASK 2: run your own storytelling module that looks at a different problem
# add your command in the line below


# run common chores
uv run ruff format .
uv run ruff check . --fix
uv run python -m pyright
uv run python -m pytest
uv run python -m zensical build

# save progress
git add -A
git commit -m "update"
git push -u origin main
```

</details>

## Notes

- Use the **UP ARROW** and **DOWN ARROW** in the terminal to scroll through past commands.
- Use `CTRL+f` to find (and replace) text within a file.
- You do not need to add to or modify `tests/`. They are provided for example only.
- Many files are silent helpers. Explore as you like, but nothing is required.
- You do NOT need to understand everything; understanding builds naturally over time.

## Troubleshooting >>>

If you see something like this in your terminal: `>>>` or `...`
You accidentally started Python interactive mode.
It happens.
Press `Ctrl+c` (both keys together) or `Ctrl+Z` then `Enter` on Windows.

## Example Output (Custom Project)

```shell
2026-08-07 14:48:35 | INFO | BI | === RUN START ===
2026-08-07 14:48:35 | INFO | BI | project=RETAIL INVENTORY STORYTELLING
2026-08-07 14:48:35 | INFO | BI | repo_dir=bintel-06-storytelling
2026-08-07 14:48:35 | INFO | BI | python=3.14.6
2026-08-07 14:48:35 | INFO | BI | os=Windows 10
2026-08-07 14:48:35 | INFO | BI | shell=powershell
2026-08-07 14:48:35 | INFO | BI | cwd=.
2026-08-07 14:48:35 | INFO | BI | github_actions=False
2026-08-07 14:48:35 | INFO | BI | ========================
2026-08-07 14:48:35 | INFO | BI | START main()
2026-08-07 14:48:35 | INFO | BI | ========================
2026-08-07 14:48:35 | INFO | BI | Input reporting data: = data\reporting\retail_inventory_reporting_case.csv
2026-08-07 14:48:35 | INFO | BI | Loading reporting data...
2026-08-07 14:48:35 | INFO | BI | Loading reporting-ready data
2026-08-07 14:48:35 | INFO | BI | Loaded 15 rows
2026-08-07 14:48:35 | INFO | BI | Verified 6 columns
2026-08-07 14:48:35 | INFO | BI | Summarizing category demand...
2026-08-07 14:48:35 | INFO | BI | Summarizing demand by category
2026-08-07 14:48:35 | INFO | BI | Categories summarized: 3
2026-08-07 14:48:35 | INFO | BI | Selecting top category...
2026-08-07 14:48:35 | INFO | BI | Selected top category: Electronics
2026-08-07 14:48:35 | INFO | BI | Summarizing monthly category demand...
2026-08-07 14:48:35 | INFO | BI | Summarizing monthly demand for category: Electronics
2026-08-07 14:48:35 | INFO | BI | Months summarized: 5
2026-08-07 14:48:35 | INFO | BI | Creating category demand chart...
2026-08-07 14:48:35 | INFO | BI | Creating chart: Demand by Product Category
2026-08-07 14:48:36 | INFO | BI | Saved category demand chart: = docs\images\storytelling_inventory_category_demand_case.png
2026-08-07 14:48:36 | INFO | BI | Creating monthly category demand chart...
2026-08-07 14:48:36 | INFO | BI | Creating chart: Monthly Demand for Electronics
2026-08-07 14:48:36 | INFO | BI | Saved monthly demand chart: = docs\images\storytelling_inventory_monthly_demand_case.png
2026-08-07 14:48:36 | INFO | BI | Identifying key results
2026-08-07 14:48:36 | INFO | BI | Top category: Electronics
2026-08-07 14:48:36 | INFO | BI | Total demand: 179 units
2026-08-07 14:48:36 | INFO | BI | Strongest month: 2025-03
2026-08-07 14:48:36 | INFO | BI | Strongest month demand: 60 units
2026-08-07 14:48:36 | INFO | BI | Showing charts...
2026-08-07 14:48:42 | INFO | BI | Retail inventory storytelling workflow complete.
2026-08-07 14:48:42 | INFO | BI | ========================
2026-08-07 14:48:42 | INFO | BI | Executed successfully!
2026-08-07 14:48:42 | INFO | BI | ========================
```

## Findings and Visuals

The custom Business Intelligence project analyzed retail inventory data to determine which product category had the highest demand and identify the period when inventory levels should be increased.

The analysis found that **Electronics** was the highest-demand product category, with a total demand of **179 units sold**. A deeper analysis showed that demand peaked in **March 2025**, when **60 units** were sold. These findings suggest that inventory managers should increase stock levels for Electronics before periods of historically high demand.

### Figure 1. Total Demand by Product Category

![Demand by Product Category](./docs/images/storytelling_inventory_category_demand_case.png)

**Discussion**

This bar chart compares total units sold across all product categories. Electronics had the highest overall demand, making it the most important category for additional inventory analysis.

### Figure 2. Monthly Demand for Electronics

![Monthly Demand for Electronics](./docs/images/storytelling_inventory_monthly_demand_case.png)

**Discussion**

This line chart shows the monthly demand trend for Electronics. Demand reached its highest level in **March 2025**, indicating that inventory planning should prioritize additional stock before this period to reduce the risk of stock shortages.
Replace these placeholders with screenshots from your own project run:

## Project Documentation

Additional project instructions, terms, and notes:

[docs/index.md](docs/index.md)

## Citation

[CITATION.cff](./CITATION.cff)

## License

[MIT](./LICENSE)
