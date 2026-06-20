# Physical AI Style Guide

*Mandatory reading before developing any lesson, lab, figure, or code in this curriculum.*

This document captures what makes a Physical AI curriculum compelling — and how to reproduce that experience for a fluid-powered intelligent machine. It is the reference every contributor checks their work against.

---

## The one thing to remember

> Students are not learning hydraulics. Students are building an intelligent machine. Hydraulics is one of the tools.

If you internalize nothing else, internalize that. Every decision below follows from it.

---

## Why the Physical AI Curriculum works

The Physical AI Curriculum succeeds because the student watches a robot become more capable, chapter by chapter. The robot is the protagonist. Servos, sensors, and code are introduced *because the robot needs them to do something it couldn't do before* — never as topics in their own right.

The student is never asked to "learn servos." They are asked to "make the arm move to a position," and servos appear as the answer. The motivation always precedes the mechanism.

Our machine is the Smart Agricultural Workcell. Our tools are hydraulics, sensing, and control. The experience must feel the same: the machine wants to do something, hits a wall, and the lesson's concept is the tool that breaks through.

---

## The Physical AI lesson pattern

Every lesson follows this order. The machine problem always comes first.

```
Machine Problem  →  Concept  →  Mathematical Model  →  Computational Model  →  Machine Improvement
```

**Not** the textbook order:

```
Concept  →  Theory  →  Example         ← FORBIDDEN as the lesson's spine
```

### What each stage does

1. **Machine Problem** — The machine cannot yet do something. State it concretely, tied to a benchmark task. *"The workcell cannot move the end-effector to a target because it has no way to meter flow."*
2. **Concept** — The idea that solves the problem. Introduced as the answer to the problem, not as a definition. *"Flow control valves restrict flow to set speed."*
3. **Mathematical Model** — The equations that let you size and predict it. *Quantify* the solution.
4. **Computational Model** — Code that simulates the behavior. Make it run.
5. **Machine Improvement** — The machine can now do the thing. Concrete, observable. *"The workcell can now move at a controlled, repeatable speed — Precision Positioning is now achievable."*

---

## The four narrative quality tests

Every lesson must pass all four. If it fails any, revise before shipping.

### Test 1 — Machine Necessity
*Can a student explain, in one minute, why the machine needs this concept?*
The opening must make the need unmistakable. If the student would say "because the textbook covers it next," the lesson fails.

### Test 2 — Capability Growth
*Can a student identify what new capability the machine gained?*
The lesson must end with a concrete, observable new ability. "Understands viscosity better" fails. "Can keep its fluid in the pump's safe range across its operating temperature" passes.

### Test 3 — Digital Twin
*Can a student identify what changed in the digital twin?*
Every lesson contributes a parameter, equation, model, or validation to the twin. If nothing changed in the twin, say why explicitly — but most lessons should move it forward.

### Test 4 — Machine Sketch
*After the lesson, could a student draw a more capable machine than before?*
If the student's whiteboard sketch is unchanged — just a longer list of hydraulic facts — the lesson failed. The machine must visibly gain something.

---

## Mandatory lesson sections

Every lesson carries these, in this position:

**Opening (before any theory):**
```
## Why The Machine Needs This
```
The machine problem. One or two paragraphs. No equations, no definitions.

**Closing (after Key Takeaways):**
```
## Machine Capability Added
```
Concrete and observable. Often phrased as a before/after:

> **Before this lesson the machine could not:** meter its cylinder speed.
> **After this lesson the machine can:** move at a controlled, repeatable velocity set by a flow control valve.

---

## Writing rules

**Lead with the machine, not the concept.**
- ❌ "A gear pump is a positive-displacement pump."
- ✅ "The workcell cannot execute Precision Positioning because it has no source of hydraulic flow. It needs a device that turns shaft rotation into fluid motion — a pump."

**Name the benchmark task.** Every lesson states which of the three it serves (Precision Positioning, Force-Controlled Interaction, Autonomous Manipulation). If a concept maps to none, question whether it belongs.

**The machine appears in every section.** Worked examples use the workcell's real numbers. Common mistakes are framed as ways the *machine* would fail. Even the math is "the workcell's cylinder," not "a cylinder."

**No orphan concepts.** If you introduce something the machine doesn't need, cut it or justify it. The test: could this paragraph be read without knowing the machine exists? If yes, rewrite it.

---

## Figure philosophy

Figures tell machine stories. They should teach on their own.

| Prefer | Avoid |
|--------|-------|
| Machine evolution | Component catalogs |
| Capability growth | Taxonomies |
| Control flow | Reference tables as art |
| Energy flow | "Types of X" diagrams |
| Perception-to-action flow | Decontextualized schematics |

A figure titled "Machine Capability Growth Across Modules" is good. A figure titled "Taxonomy of Hydraulic Pumps" is forbidden.

---

## Code philosophy

Code demonstrates machine behavior, not isolated arithmetic.

| Prefer | Avoid |
|--------|-------|
| Cylinder motion simulation | Single-formula calculators with no system context |
| Pressure dynamics simulation | Unit converters as an end in themselves |
| Digital twin components | Decontextualized equation evaluators |

A helper function (unit conversion, an orifice formula) is fine *as a building block* of a simulation. It is not fine as the deliverable. Every code file should connect to the machine — ideally to the digital twin.

---

## Lab philosophy

Labs are machine-development activities, not experiments for their own sake. Every lab answers: *how did today's work improve the Smart Agricultural Workcell?*

Every lab report connects:
```
Observation → Measurement → Engineering Interpretation → Machine Implication → Digital Twin Implication
```

The last two are the point. A lab that stops at interpretation is a physics class. A lab that reaches the machine and the twin is building an intelligent machine.

---

## The benchmark tasks are sacred

Three first-class objects the whole curriculum orbits:

1. **Precision Positioning** — move the end-effector to a target.
2. **Force-Controlled Interaction** — apply controlled force without damage.
3. **Autonomous Manipulation** — sense a target and execute a full sequence.

Every module advances at least one. Every lesson identifies which it supports. Content that maps to none is suspect.

---

## When a decision is unclear

> Choose the option that strengthens the machine's story.

This overrides convenience, tradition, and textbook habit. If two structures are equally correct, pick the one where the machine is more visibly the protagonist.

---

*Companion documents: `MACHINE_STORY.md` (the machine), `BENCHMARK_TASKS.md` (the tasks), `MODULE_ARTIFACT_MAP.md` (the artifacts), `../curriculum/CAPABILITY_GROWTH_MAP.md` (the evolution at a glance), `../curriculum/CURRICULUM_NARRATIVE.md` (the full story).*
