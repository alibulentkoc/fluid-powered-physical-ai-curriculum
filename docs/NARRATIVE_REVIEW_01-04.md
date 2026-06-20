# Narrative Review — Modules 01–04

*Performed under Directive 006. Purpose: identify lesson sections that follow the textbook pattern (Concept → Example) and convert them to the Physical AI pattern (Machine Problem → Concept → Solution → Machine Improvement). This is a targeted strengthening pass, not a full rewrite.*

---

## Method

Each lesson was checked against the four narrative quality tests:
1. **Machine Necessity** — is the need explainable in one minute?
2. **Capability Growth** — is the new capability identifiable?
3. **Digital Twin** — is the twin change identifiable?
4. **Machine Sketch** — could the student draw a more capable machine?

The `## Why The Machine Needs This` and `## Machine Capability Added` brackets (added under Directive 005) mean Tests 1, 2, and 3 pass structurally for all 17 lessons. This review targets **Test 4 and narrative flow** — the lesson *interiors*, where some sections still open by referencing the curriculum or the concept rather than the machine's problem.

---

## Findings

### Structural redundancy (all lessons)
Every lesson now has both `## Why The Machine Needs This` (machine problem) and `## 1. Why this matters` (legacy section). Two "why" sections in a row dilutes the machine-problem-first punch. **Resolution:** the legacy `## 1. Why this matters` sections are reframed to *continue from* the machine problem into the concept, rather than restating motivation. The machine-problem framing lives in the dedicated opening section; section 1 now transitions into the concept.

### Weak openings — reference the curriculum, not the machine
These section-1 openings led with the course structure or the concept's importance rather than the machine's problem. Flagged for targeted rewrite:

| Lesson | Weak opening (paraphrased) | Fix |
|--------|---------------------------|-----|
| M03 L03 contamination | "Module 02 introduced the filter and the Beta ratio. This lesson goes deeper…" | Lead with the machine's problem: the valve that controls every motion is being jammed by invisible particles |
| M04 L01 bernoulli | "Module 04 is the mathematical core of the curriculum's first half…" | Lead with: the machine's twin must predict flow, and flow is governed by energy conservation |
| M04 L05 simulation | "This is the payoff lesson of Module 04…" | Lead with: the machine's twin is just equations until it runs — assemble and run it |
| M03 L01 what fluid does | "It is easy to think of hydraulic fluid as just the stuff that fills the system…" | Lead with: the machine transmits all its power through this fluid; the wrong fluid means no reliable motion |

### Strong openings — no change needed
These already lead with the machine and pass all four tests:
- M01 L03 (the workcell's cylinder must exert 500 N to grip a fruit…)
- M02 L02 valves (a pump and cylinder alone make a machine that does one thing once…)
- M02 L03 cylinders (the component that does the work the workcell exists to do…)
- M04 L03 force balance (a moving cylinder is a dynamic system the twin must predict…)
- M04 L04 pressure dynamics (a perfectly rigid system would respond instantly — the machine doesn't…)

---

## Rewrites applied

Each flagged section was converted to open with the machine's concrete problem, then flow into the concept. The "before this lesson the machine could not / after this lesson the machine can" framing was added to every `## Machine Capability Added` section to make capability growth concrete and observable (Test 2, Test 4).

See the commit and the lessons themselves for the applied changes. No lesson was rewritten wholesale; only the flagged openings and the capability statements were strengthened.

---

## Result

After this pass, all 17 lessons:
- Open with the machine's problem (dedicated section), then transition into the concept (no double-motivation)
- Close with a concrete before/after capability statement
- Identify their benchmark task
- State their digital twin contribution

The four narrative quality tests pass for all lessons in Modules 01–04.

---

*Performed before Module 05, per the Directive 006 review gate.*
