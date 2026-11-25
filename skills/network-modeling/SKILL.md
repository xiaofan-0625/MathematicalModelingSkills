---
name: network-modeling
description: Formulate and validate graph and network models with explicit node-edge semantics, direction, weights, temporal scope, null models, path and flow assumptions, and structural robustness. Use when relationships, connectivity, routing, diffusion, communities, or network interventions are central to a modeling task.
---

# Model Networks and Graphs

A graph is a modeling decision, not merely a data format. Changing edge meaning, direction, aggregation window, or weight interpretation can reverse centrality, path, community, and intervention results.

## Graph contract

Define node identity, edge-generating rule, direction, multiplicity, self-loop policy, weight unit, time window, missing-edge meaning, and whether the graph is static, temporal, bipartite, multilayer, spatial, or a projection. State whether a larger weight means stronger connection, greater capacity, higher probability, or greater cost; path algorithms require the correct transformation.

Audit duplicate nodes, parallel edges, isolated nodes, disconnected components, reciprocal edges, censored relationships, sampling bias, and attributes created after the prediction time. Preserve a stable mapping from source records to graph objects.

## Analysis workflow

1. Match the mathematical object to the question. Use connectivity for reachability, weighted shortest paths for cost, flow algorithms for capacity, matching for assignment, and diffusion models only when their transmission assumptions are credible.
2. Choose metrics by interpretation, not availability. Degree, closeness, betweenness, eigenvector centrality, PageRank, clustering, modularity, and assortativity answer different questions and can be undefined or misleading on disconnected or directed graphs.
3. Build simple structural baselines and an appropriate null model. Compare with degree-preserving rewiring, random graphs, temporal shuffles, or other constrained randomization rather than with an unrelated random graph.
4. For stochastic community detection, layouts, sampling, or heuristics, record seeds and repeat runs. Report stability across seeds, resolution parameters, and reasonable edge thresholds.
5. Validate path and flow outputs independently on small graphs and conservation constraints. Distinguish edge cost from capacity and strength; never invert weights silently.
6. Test robustness to edge removal, uncertain links, missing nodes, aggregation window, graph projection, and alternative direction/weight rules. Identify which structural changes reverse the recommendation.
7. Use graph visualization for explanation, not proof. Fix layout seeds, reduce occlusion, encode attributes consistently, and accompany dense networks with tables or distributions.

Do not infer causation from centrality or communities, treat a layout as geometry, or claim a detected partition is uniquely real. When the observed network is a sample, discuss the sampling mechanism and unobserved edges.

## Outputs and gate

Maintain a graph contract, node and edge tables, construction code, graph-level diagnostics, metric definitions, null-model results, seed manifest, and perturbation report. Export results with stable identifiers and enough metadata to reconstruct direction, weights, and time scope.

G3.5 passes only when graph construction is auditable, algorithms match weight/direction semantics, small-case checks pass, and central conclusions survive credible null and perturbation tests. Route final network figures to `scientific-visualization`.
