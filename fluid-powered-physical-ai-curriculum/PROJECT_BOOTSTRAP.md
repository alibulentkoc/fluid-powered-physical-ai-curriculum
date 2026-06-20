# Project Bootstrap

How to get started with the Fluid-Powered Physical AI Curriculum — whether you are a learner, an instructor, or a contributor.

---

## For Learners

### What You Need to Begin

**Software (free):**
- Python 3.10 or later
- Jupyter Notebook or JupyterLab (`pip install jupyterlab`)
- NumPy, SciPy, Matplotlib (`pip install numpy scipy matplotlib`)
- Arduino IDE (for embedded control modules, Module 10+)

**Hardware (optional, for labs):**
- Low-pressure hydraulic demonstration kit (pneumatic substitute acceptable for early modules)
- Arduino Uno or compatible board
- Pressure sensor (0–100 PSI, analog output preferred for early labs)
- See individual lab files for full equipment lists

**Background Recommended:**
- Algebra and basic trigonometry
- Some exposure to physics (force, pressure, energy)
- Some exposure to programming (any language)

See `docs/prerequisites.md` for a detailed skills assessment.

### Starting Point

1. Read `README.md` to understand the curriculum arc and the capstone platform.
2. Read `curriculum/module01_manifest.md` for Module 1 learning objectives and structure.
3. Begin with `modules/module01_foundations/introduction.md`.
4. Work through lessons in order. Do not skip the exercises — they build toward the capstone.

---

## For Instructors

### Course Integration

This curriculum is designed to be modular. You can:
- Teach it as a standalone 12-module course (~one semester)
- Extract individual modules for integration into existing fluid power or mechatronics courses
- Use the capstone project as a semester-long team project

### Recommended Pacing

| Phase | Modules | Weeks (approx) |
|-------|---------|---------------|
| Foundations | 01–04 | 4–5 weeks |
| Components and Control | 05–08 | 4–5 weeks |
| Intelligence Layer | 09–11 | 3–4 weeks |
| Capstone | 12 | 3–4 weeks |

### Instructor Notes

See `coaches/` directory for tutor prompts, discussion questions, and grading guidance as they are developed.

---

## For Contributors

1. Read `CONTRIBUTING.md` carefully before writing any content.
2. Review `ARCHITECT_DECISIONS.md` to understand key design choices already made.
3. Check `TODO.md` for the current priority list.
4. Check `master_progress.md` for detailed status of each file and module.
5. Follow the module design standard and lesson template described in `CONTRIBUTING.md`.

---

## Repository Clone

```bash
git clone https://github.com/[org]/fluid-powered-physical-ai-curriculum.git
cd fluid-powered-physical-ai-curriculum
```

---

## Environment Setup (Python)

```bash
python -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate
pip install numpy scipy matplotlib jupyter pandas
```

Verify:
```bash
python -c "import numpy, scipy, matplotlib; print('Environment ready.')"
```

---

## First Code Example

After Module 1, run the Pascal's Law calculator in `code/module01/pascals_law.py`:

```bash
python code/module01/pascals_law.py
```

This confirms your Python environment is working and gives you a first interactive tool from the curriculum.
