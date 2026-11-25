---
name: mathematical-derivation-and-proof
description: Derive, verify, repair, and scope mathematical formulas, propositions, proofs, approximation chains, and algorithmic guarantees in modeling projects. Use when a result depends on a nontrivial derivation or proof; not for routine equation typesetting or unsupported theorem-like prose.
---

# Derive and Audit Mathematical Claims

A polished formula chain is not evidence that each implication is valid. Preserve the distinction among exact identities, consequences of stated assumptions, approximations, numerical observations, heuristics, and conjectures.

## Claim contract

Before manipulating symbols, state:

- the exact target and whether it is an identity, proposition, bound, approximation, algorithm guarantee, or interpretation;
- domains, units, quantifiers, regularity conditions, boundary or initial conditions, and excluded cases;
- the invariant or global object that organizes the derivation;
- imported lemmas, inequalities, conservation laws, or external results and the hypotheses each requires;
- the strength needed by the model and paper, including what would remain useful if the strongest claim fails.

## Workflow

1. Normalize notation and assumptions. Define every symbol before use and distinguish assumptions from definitions and derived facts.
2. Build a dependency map from the target back to premises, intermediate identities, lemmas, approximations, numerical checks, and external results. Do not let a convenient proxy silently replace the target object.
3. Try to break the claim first using dimensional checks, degenerate and boundary cases, small enumerated instances, sign and monotonicity checks, quantifier reversal, and plausible counterexamples.
4. Label every nontrivial step as `identity`, `deduction`, `imported_result`, `approximation`, `numerical_evidence`, `heuristic`, or `interpretation`. Record the assumptions discharged at that step.
5. For a proof, choose an explicit strategy and isolate substantial subclaims as proof obligations. Verify every imported theorem's hypotheses, inequality direction, constant dependence, limit or integral interchange, and equality condition.
6. For an approximation, identify the expansion parameter, regime, order, remainder or error evidence, stability range, and the point where the exact model becomes approximate.
7. Use symbolic algebra, differentiation, numerical substitution, property tests, enumeration, or an independent implementation as error detectors when useful. Such checks can falsify a derivation but do not by themselves prove a general statement.
8. Assign one status: `JUSTIFIED_AS_STATED`, `JUSTIFIED_AFTER_REPAIR`, `APPROXIMATE_WITH_BOUNDARY`, `HEURISTIC_ONLY`, or `NOT_JUSTIFIED`. Never repair a proof by silently strengthening assumptions or weakening the conclusion.
9. Propagate the accepted statement, assumptions, scope, and status into the modeling blueprint and paper. Preserve rejected claims and counterexamples in the audit record.

## Common proof failures

- undefined or changing objects, symbols, domains, or probability spaces;
- hidden assumptions introduced by words such as “obviously”, “similarly”, or “without loss of generality”;
- a local or sampled result written as a global theorem;
- exchanging expectation, derivative, integral, limit, minimum, or maximum without applicable conditions;
- asymptotic notation whose constants depend on the quantity claimed to be uniform;
- confusing solver convergence, simulation evidence, or random numerical tests with proof;
- proving a normalized or simplified statement while publishing the stronger original statement;
- citing a theorem by name without checking its hypotheses at the point of use.

## Required outputs

For a substantive derivation, maintain:

- `求解/计划/derivation_contract.md`: exact target, assumptions, notation, invariant object and intended claim strength;
- `求解/计划/proof_obligations.csv`: obligation, dependencies, hypotheses, evidence, status and owner;
- `求解/问题X/结果/derivation_report.md`: numbered steps, counterexample attempts, repairs, checks, final status and non-claims;
- deterministic symbolic or numerical check code when such checks were used.

The gate passes only when the paper statement matches what was actually derived, every material assumption is visible, proof obligations are discharged or explicitly open, approximations have a stated regime, and no computational check is misrepresented as general proof.

Read [mathematical-derivation-and-proof.md](../../references/mathematical-derivation-and-proof.md) for the obligation ledger and audit checklist.
