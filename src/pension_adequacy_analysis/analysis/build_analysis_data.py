import pandas as pd


def build_analysis_data(
    elderly_poverty: pd.DataFrame,
    pension_replacement: pd.DataFrame,
    gdp: pd.DataFrame,
    year: int = 2022,
) -> pd.DataFrame:
    """Merge cleaned datasets for a single year cross-country analysis."""
    ep = elderly_poverty[elderly_poverty["year"] == year][
        ["country_code", "country", "elderly_poverty_rate"]
    ]
    pr = pension_replacement[["country_code", "pension_replacement_rate"]]
    gdp_year = gdp[gdp["year"] == year][["country_code", "gdp_per_capita"]]

    return (
        ep.merge(pr, on="country_code", how="inner")
        .merge(gdp_year, on="country_code", how="inner")
        .reset_index(drop=True)
    )
