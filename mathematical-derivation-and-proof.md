# Mathematical Derivation and Proof Audit

Use this checklist when a formula chain, theorem, error bound, or guarantee carries a material conclusion.

## Proof-obligation ledger

```csv
obligation_id,claim,kind,depends_on,assumptions,hypotheses_checked,evidence,status,counterexample_attempt,notes
O1,"...",identity,"","...","...","equations 3-5",passed,"boundary x=0","
O2,"...",imported_result,"O1","...","continuity; compactness","source and local check",open,"...",""
```

Allowed status values are `passed`, `repaired`, `approximate`, `heuristic`, `open`, and `refuted`. An open or refuted obligation cannot support a stronger downstream claim.

## Derivation audit

- The target statement and quantifier order are exact.
- Definitions, assumptions, domains, units and regularity conditions are separated.
- One invariant or global object remains stable through the derivation.
- Each step states its type and dependencies.
- Imported results are named or cited and all hypotheses are checked locally.
- Boundary, degenerate and equality cases are handled or explicitly excluded.
- Every approximation states regime, order, error or empirical validity range.
- Big-O or uniform claims expose parameter dependence.
- Changes of variables preserve domains, orientation and Jacobian factors.
- Interchanges of limits, derivatives, expectations, integrals and optimizers have conditions.
- Numerical or symbolic checks are labelled as checks, not proofs.
- The final paper statement is no stronger than the completed obligations.

## Status interpretation

| Status | Meaning | Permitted paper language |
|---|---|---|
| `JUSTIFIED_AS_STATED` | target follows under the declared assumptions | state the result with its assumptions |
| `JUSTIFIED_AFTER_REPAIR` | a corrected scope or extra assumption was required | publish only the repaired statement |
| `APPROXIMATE_WITH_BOUNDARY` | useful approximation in a declared regime | state regime, error evidence and failure boundary |
| `HEURISTIC_ONLY` | motivates a method but lacks a proof or controlled approximation | describe as heuristic or intuition |
| `NOT_JUSTIFIED` | a material gap or counterexample remains | remove the claim or present it as an open issue |

## Counterexample-first prompts

- What happens at zero, one, infinity, a singular boundary, or the smallest legal instance?
- Can the claimed monotonicity or inequality reverse under a legal parameter choice?
- Does a symmetry, permutation, rescaling, or unit change contradict the statement?
- Is a hidden independence, convexity, differentiability, compactness, positivity or uniqueness assumption required?
- Does the claim survive when an optimizer is nonunique or a matrix is rank deficient?
- Is the guarantee about the mathematical model, the numerical algorithm, or only the observed run?
