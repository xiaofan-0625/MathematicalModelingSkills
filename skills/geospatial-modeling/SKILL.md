---
name: geospatial-modeling
description: Build and audit spatial mathematical models with explicit coordinate reference systems, geometry quality, spatial joins, distance semantics, spatial validation, privacy, and map evidence. Use when locations, regions, routes, rasters, adjacency, or geographic distance affect the model.
---

# Model Geospatial Evidence

Spatial data are not ordinary table columns. Coordinate systems, geometry repair, aggregation scale, and spatial dependence can change the answer while leaving code syntactically correct.

## Spatial contract

Record source layer, stable feature key, geometry type, coordinate reference system (CRS), spatial resolution, time stamp, provenance, precision, units, privacy class, and the role each layer plays. Count missing, empty, invalid, duplicate, mixed, and out-of-domain geometries separately.

Never guess a CRS from coordinate ranges. Assigning CRS metadata is different from transforming coordinates. Longitude/latitude are angular coordinates: use a justified projected CRS or a geodesic method for distance, area, buffers, tolerances, and nearest-neighbor operations. Document datum, axis order, area of use, and treatment of antimeridian or projection-boundary crossings when relevant.

## Modeling workflow

1. Define the spatial estimand and support: point, line, polygon, grid cell, network segment, or region-time unit. State whether the model is about proximity, containment, connectivity, exposure, flow, or spatial dependence.
2. Validate topology before and after repair, overlay, clipping, dissolving, rasterization, or resampling. Preserve originals and quantify features that collapse, split, multiply, or change type.
3. Declare join predicates and expected cardinality before spatial joins. Audit unmatched features, boundary-only matches, ties, and row multiplication afterward.
4. Justify distance and neighborhood definitions. Euclidean, geodesic, travel-time, network, contiguity, and kernel distance are not interchangeable.
5. Test sensitivity to spatial resolution, zoning, boundary choice, precision grid, and neighborhood scale. Treat the modifiable areal unit problem and ecological fallacy as model risks.
6. Detect spatial autocorrelation in outcomes or residuals when it matters. Use spatial or grouped holdouts instead of random splits when nearby observations would leak information.
7. Preserve denominators and missingness in choropleths. Record classification method, units, date, normalization, and no-data meaning; a visually strong map is not evidence of causal effect.
8. Generalize or aggregate precise coordinates, addresses, trajectories, and small-area attributes before public release when re-identification is plausible.

## Outputs and gate

Store a layer inventory, CRS/measurement decision, geometry audit, join-cardinality report, spatial split definition, and machine-readable derived layers. Reopen exported artifacts and verify feature counts, schema, CRS, and geometry types.

The relevant G3/G3.5 gate passes only when measurement units and predicates are correct, spatial leakage is controlled, results survive credible scale or neighborhood changes, and maps trace to the same frozen data as the paper. Use [visual-evidence-design.md](../../references/visual-evidence-design.md) for final map and figure QA.
