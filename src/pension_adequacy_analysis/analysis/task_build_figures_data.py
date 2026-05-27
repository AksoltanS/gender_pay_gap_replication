from pathlib import Path

import pandas as pd

from pension_adequacy_analysis.analysis.build_figures_data import (
    build_pension_by_country,
    build_pension_vs_poverty,
    build_poverty_by_country,
    build_regression_results,
)
from pension_adequacy_analysis.config import (
    ANALYSIS_DATA,
    PENSION_BY_COUNTRY_DATA,
    PENSION_VS_POVERTY_DATA,
    POVERTY_BY_COUNTRY_DATA,
    REGRESSION_RESULTS,
)

_FIGURES_PRODUCES = {
    "poverty_by_country": POVERTY_BY_COUNTRY_DATA,
    "pension_by_country": PENSION_BY_COUNTRY_DATA,
    "pension_vs_poverty": PENSION_VS_POVERTY_DATA,
    "regression_results": REGRESSION_RESULTS,
}


def task_build_figures_data(
    script: Path = Path(__file__),
    data: Path = ANALYSIS_DATA,
    produces: dict[str, Path] = _FIGURES_PRODUCES,
) -> None:
    """Task to build figure and table data for pension adequacy analysis."""
    df = pd.read_parquet(data)
    build_poverty_by_country(df).to_csv(produces["poverty_by_country"], index=False)
    build_pension_by_country(df).to_csv(produces["pension_by_country"], index=False)
    build_pension_vs_poverty(df).to_csv(produces["pension_vs_poverty"], index=False)
    build_regression_results(df).to_csv(produces["regression_results"], index=False)
