---
name: academic-humanization
description: Audit and revise Chinese or English academic prose to reduce formulaic AI-writing patterns while preserving equations, citations, frozen numbers, terminology, meaning, length constraints, and scholarly register. Use only after technical content is stable, or when reviewing a completed draft for naturalness and authorship voice.
---

# Humanize Academic Writing

Improve authorship voice and sentence-level naturalness without changing scientific content. This is a controlled editorial pass, not a way to evade disclosure rules or disguise fabricated work.

## Protect before editing

Freeze and preserve:

- equations, symbols, units, numerical results, uncertainty, and table values;
- citation keys, reference numbers, hyperlinks, labels, and cross-references;
- technical terminology, abbreviations, model names, and stated assumptions;
- LaTeX commands, environments, file paths, and document structure unless explicitly in scope.

Record a compact glossary and rolling section summary for long documents.

## Workflow

1. Calibrate language, venue, discipline, author voice, and allowed degree of rewriting.
2. Audit first; identify exact passages and pattern types instead of declaring the whole document artificial.
3. Separate content problems from style problems. Escalate factual contradictions; silently fix minor style issues.
4. Rewrite locally, preserving the claim-evidence relationship and protected tokens.
5. Vary sentence rhythm and paragraph structure only where it improves clarity.
6. Compare before and after for semantic, numerical, citation, and terminology consistency.
7. Report material edits and any unresolved technical concern.

## Patterns to correct

- repetitive numbered templates and overly symmetrical three-part structures;
- formulaic openings, mechanical transitions, and paragraph-ending summaries;
- vague attribution, empty intensifiers, promotional claims, and unsupported novelty language;
- excessive signposting, headings, boldface, dashes, hedging, or synonym cycling;
- generic conclusions, textbook-like explanations, and contribution-list cliches;
- Chinese hidden colloquialisms or confessional phrases such as claims that nothing was fabricated;
- English AI stock phrases, manufactured punchlines, and unnatural avoidance of simple copular verbs.

## Preserve rather than over-correct

- necessary technical repetition;
- conventional disciplinary terminology;
- accurate cautious language supported by uncertainty;
- short direct sentences when they are clearest;
- genuine author preferences and minor human irregularity that do not harm comprehension.

## Output

Return an audit summary, revised text, protected-token consistency result, and a list of any sentence whose technical meaning could not be safely revised.

For a full manuscript, run this block once near the end. Do not chain multiple humanizers over the same passage unless the first pass fails a specific, named criterion.
