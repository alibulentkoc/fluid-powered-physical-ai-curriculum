# Contributing to the Fluid-Powered Physical AI Curriculum

Thank you for your interest in contributing. This curriculum is open-source and community-driven. Contributions of all kinds are welcome: lessons, labs, diagrams, code examples, corrections, and extensions.

---

## What We Need Most

1. **Module content** — lessons following the 12-part topic template (see below)
2. **Lab procedures** — hands-on experiments with clear equipment lists and safety notes
3. **Diagrams and figures** — circuit schematics, system diagrams, annotated photographs
4. **Code examples** — Python simulations, Arduino sketches, Raspberry Pi scripts
5. **Corrections** — technical errors, unclear explanations, broken links

---

## Module Design Standard

Every module follows this architecture:

```
modules/moduleXX_title/
├── manifest.md          # Learning objectives, prerequisites, outline
├── introduction.md      # Motivation and framing
├── lessons/             # Topic-level content files
├── exercises/           # Problem sets and coding exercises
└── summary.md           # Module recap and connections forward
```

### Lesson Template (12 Parts)

Each topic-level lesson should include these sections:

1. **Why This Matters** — motivate before explaining
2. **Physical Intuition** — build the mental model, no equations yet
3. **Mathematical Foundations** — governing equations with derivation
4. **Visual Explanation** — diagram, schematic, or annotated figure
5. **Engineering Example** — real system that uses this concept
6. **Worked Example** — solve a specific numerical problem step by step
7. **Interactive Demonstration** — code cell, simulation, or lab activity
8. **Coding Exercise** — hands-on Python or Arduino task
9. **Knowledge Check** — 3–5 questions to confirm understanding
10. **Challenge Problem** — harder extension for advanced learners
11. **Common Mistakes** — what people get wrong and why
12. **Key Takeaways** — 3–5 bullet summary

### Module Narrative Requirement

Every module must make a clear statement connecting its content to the capstone: **the Intelligent Fluid-Powered Agricultural Manipulation Cell**. No module should feel like a standalone chapter. The connection should be explicit and appear in the manifest and the introduction.

---

## Writing Style Guidelines

- Lead with intuition, not formalism
- Use active voice
- Prefer concrete examples from agriculture, industrial machinery, or fluid power practice
- Do not frame hydraulics as superior to electric actuation — frame it as a distinct and important domain
- Avoid academic boilerplate ("In this section, we will explore...")
- Be direct, modular, and application-driven

---

## Code Style

- **Python**: follow PEP 8, use type hints, include docstrings
- **Arduino**: comment every function, use meaningful variable names
- **Simulations**: include a brief header describing what the script models
- All code should run with clearly stated dependencies

---

## Diagram and Figure Standards

- Use SVG or high-resolution PNG (min 150 DPI)
- Label all components clearly
- Hydraulic circuit diagrams should follow ISO 1219 symbol conventions where practical
- Store in `assets/figures/` or `assets/diagrams/`
- Reference figures in lessons by relative path

---

## Pull Request Process

1. Fork the repository
2. Create a branch: `feature/moduleXX-topic-name` or `fix/description`
3. Follow the templates above
4. Open a pull request with a clear description of what was added or changed
5. Link to the relevant module manifest if adding content

---

## Safety and Accuracy

Hydraulic systems operate at high pressure and can be dangerous. All lab content must:

- Include appropriate safety warnings
- Specify maximum working pressures for demonstrations
- Reference applicable standards (ISO, NFPA) where relevant
- Not encourage improvised high-pressure hardware

If you are unsure about a safety statement, flag it in the PR for review.

---

## Questions?

Open an issue or start a discussion in the repository. We welcome questions, suggestions, and proposals for new modules or labs.
