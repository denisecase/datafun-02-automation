# Data Card: Palmer Penguins

This Data Card documents the dataset used by the
`penguins-body-mass` experiment.

It follows the general transparency goals of Google's
Data Cards Playbook:
describe dataset provenance, composition,
intended use, limitations, and considerations
not apparent from the data.

## Dataset Summary

| Item                                | Description                    |
| ----------------------------------- | ------------------------------ |
| Dataset                             | Palmer Penguins                |
| Curated dataset                     | `penguins`                     |
| Observations                        | 344 penguins                   |
| Species                             | Adelie, Chinstrap, Gentoo      |
| Location                            | Palmer Archipelago, Antarctica |
| Islands                             | Biscoe, Dream, Torgersen       |
| Study period                        | 2007-2009                      |
| Grain                               | one penguin                    |
| Primary use here                    | supervised regression          |
| Target in this experiment           | `body_mass_g`                  |
| Selected feature in this experiment | `flipper_length_mm`            |

## Purpose

The Palmer Penguins dataset provides measurements and descriptive
attributes for penguins observed in the Palmer Archipelago.

The curated dataset was designed as an accessible dataset for
data exploration and visualization and is commonly used as an
alternative to the Iris dataset.

This project uses it for a small supervised regression experiment:

> How well can **flipper length** predict **penguin body mass**?

## Provenance

The underlying observations were collected by Dr. Kristen Gorman
and the Palmer Station Long Term Ecological Research program.

The `palmerpenguins` project made curated versions of the data
readily available for teaching, exploration, and analysis.

This project obtains the dataset through Seaborn's `penguins`
dataset interface.

## Dataset Composition

The dataset contains 344 observations representing individual penguins.

The variables available through the Seaborn version used in this project are:

- `species`
- `island`
- `bill_length_mm`
- `bill_depth_mm`
- `flipper_length_mm`
- `body_mass_g`
- `sex`

The dataset includes three penguin species:

- Adelie
- Chinstrap
- Gentoo

## Missing Data

Some observations contain missing values.

For this experiment, only two columns are required:

- `flipper_length_mm`
- `body_mass_g`

Two of the 344 observations are missing one of these required values.

The declared experiment policy drops those observations, leaving:

```text
342 modeling observations
```

No values are imputed.

## Intended Use

The dataset is appropriate for:

- education
- exploratory data analysis
- visualization
- introductory statistical analysis
- supervised machine-learning experiments
- demonstrating reproducible analytical workflows

In this repository, the dataset is used to demonstrate a clear
baseline-versus-candidate regression experiment.

## Additional Exploration

Other reasonable analytical questions include:

- predicting penguin species
- predicting body mass from multiple morphological measurements
- comparing measurements across species
- examining differences among islands
- studying relationships among bill dimensions, flipper length,
  and body mass

Those are separate analytical experiments and should have their own
declared assumptions, selected features, evaluation methods, and conclusions.

## Limitations

The dataset is small and represents penguins observed in a specific
geographic region and study period.

Results should therefore not automatically be generalized to:

- all penguin species
- all geographic populations
- different ecological conditions
- future populations
- other biological species

Measurements also contain missing values, and some variables may be
associated with species, sex, island, or other biological structure.

A predictive relationship observed in this dataset should not be interpreted
automatically as a causal relationship.

## Representation Considerations

The dataset contains observations from three species and three islands,
and those groups are not necessarily represented equally.

Model performance calculated across the complete held-out sample may therefore
hide differences in performance across species, sex, or island.

A more advanced experiment could evaluate those groups separately.

## Experiment-Specific Use

The feature choice is intentionally constrained.
This repository uses only:

```text
flipper_length_mm → body_mass_g
```

The purpose is to determine whether one interpretable morphological feature
provides useful predictive information beyond a mean-value baseline.

## Project Data Processing

The project:

1. loads the Palmer Penguins dataset
2. observes the available columns
3. validates the selected feature and target
4. selects `flipper_length_mm` and `body_mass_g`
5. drops observations missing either required value
6. performs the declared train/test experiment

## References

- [Palmer Penguins project](https://allisonhorst.github.io/palmerpenguins/)
- [Palmer Penguins data documentation](https://allisonhorst.github.io/palmerpenguins/articles/intro.html)
- [Google Data Cards Playbook](https://sites.research.google/datacardsplaybook/)
