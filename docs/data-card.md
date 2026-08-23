# Data Card: Palmer Penguins

This Data Card follows the structure of the Data Cards convention
(Pushkarna et al., 2022), an emerging, people-centered approach to
dataset documentation for responsible AI.

## Dataset Summary

| Item            | Description                    |
| --------------- | ------------------------------ |
| Dataset         | Palmer Penguins                |
| Curated dataset | `penguins`                     |
| Observations    | 344 penguins                   |
| Species         | Adelie, Chinstrap, Gentoo      |
| Location        | Palmer Archipelago, Antarctica |
| Islands         | Biscoe, Dream, Torgersen       |
| Study period    | 2007-2009                      |
| Grain           | one penguin                    |

## Purpose

The Palmer Penguins dataset provides measurements and descriptive
attributes for penguins observed in the Palmer Archipelago.
The curated dataset was designed as an accessible dataset for
data exploration and visualization and is commonly used as an
alternative to the Iris dataset.

## Provenance

The underlying observations were collected by Dr. Kristen Gorman
and the Palmer Station Long Term Ecological Research program.
The `palmerpenguins` project made curated versions of the data
readily available for teaching, exploration, and analysis.

## Sources

The dataset is available via CSV or through Seaborn's `penguins`
dataset interface.

## Dataset Composition

The dataset contains observations representing individual penguins.
There are seven variables available.

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

## Possible Explorations

Reasonable analytical questions include:

- predicting penguin species
- predicting body mass from multiple morphological measurements
- predicting one morphological measurement from other measurement(s)
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

## Representation Considerations

The dataset contains observations from three species and three islands,
and those groups are not necessarily represented equally.
Model performance calculated across the complete held-out sample may therefore
hide differences in performance across species, sex, or island.

## References

- [Palmer Penguins project](https://allisonhorst.github.io/palmerpenguins/)
- [Palmer Penguins data documentation](https://allisonhorst.github.io/palmerpenguins/articles/intro.html)
- [Data Cards Playbook (toolkit)](https://pair-code.github.io/datacardsplaybook/)
- Data Cards convention: Pushkarna, Zaldivar, and Kjartansson (2022),
  _Data Cards:_
  _Purposeful and Transparent Dataset Documentation for Responsible AI_,
  ACM FAccT. <https://doi.org/10.1145/3531146.3533231>

---

[◄ Back to Home](index.md)
