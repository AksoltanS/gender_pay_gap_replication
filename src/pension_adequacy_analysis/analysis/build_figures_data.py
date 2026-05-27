"""Functions to build figure and table data for pension adequacy analysis."""

import pandas as pd
import statsmodels.api as sm


def build_poverty_by_country(df: pd.DataFrame) -> pd.DataFrame:
    """Build data for the elderly poverty by country figure."""
    poverty_by_country = (
        df[["country", "country_code", "elderly_poverty_rate"]]
        .drop_duplicates()
        .sort_values("elderly_poverty_rate", ascending=False)
        .reset_index(drop=True)
    )
    return poverty_by_country


def build_pension_by_country(df: pd.DataFrame) -> pd.DataFrame:
    """Build data for the pension replacement rate by country figure."""
    pension_by_country = (
        df[["country", "country_code", "pension_replacement_rate"]]
        .drop_duplicates()
        .sort_values("pension_replacement_rate", ascending=True)
        .reset_index(drop=True)
    )
    return pension_by_country


def build_pension_vs_poverty(df: pd.DataFrame) -> pd.DataFrame:
    """Build data for the pension vs poverty scatter plot."""
    pension_vs_poverty = (
        df[
            [
                "country",
                "country_code",
                "pension_replacement_rate",
                "elderly_poverty_rate",
                "gdp_per_capita",
            ]
        ]
        .drop_duplicates()
        .reset_index(drop=True)
    )

    return pension_vs_poverty


def build_regression_results(df: pd.DataFrame) -> pd.DataFrame:
    """Build OLS regression results for Table 1b.

    Args:
        df: Analysis DataFrame with all variables.

    Returns:
        DataFrame with regression coefficients, standard errors, and p-values.
    """
    X = sm.add_constant(df[["pension_replacement_rate", "gdp_per_capita"]])
    y = df["elderly_poverty_rate"]
    model = sm.OLS(y, X).fit()

    return pd.DataFrame(
        {
            "variable": model.params.index,
            "coefficient": model.params.values,
            "std_error": model.bse.values,
            "p_value": model.pvalues.values,
            "ci_low": model.conf_int()[0].values,
            "ci_high": model.conf_int()[1].values,
        }
    )
