# The twin runs alongside the machine
## Module 11 · Lesson 02

*An assembled twin that never sees real data is still just a simulation. This lesson connects the twin to the machine's logged data — feeding it the real inputs, aligning the time axes, and running it in replay to compare prediction against reality, step by step.*

---

## Why The Machine Needs This

The twin is assembled (Lesson 01), but to become a true digital twin it must *run on the machine's real data*. The machine logged complete task cycles in Module 09 — pressure, position, force, flow over time. The twin must ingest that data, align its clock to the machine's, feed itself the machine's actual inputs, and produce predictions to lay against the machine's actual outputs. This is the data synchronization that makes the twin live.

Without this, the twin and the machine never truly meet over real operation; the twin remains a standalone predictor. The machine needs to run its twin in *replay mode* — stepping through a logged cycle, feeding measured inputs, comparing predicted outputs — so it can see, concretely, how well the twin mirrors reality across an entire task. This is the practical mechanics of synchronization, and the prerequisite for fault detection (Lesson 03).

**Benchmark task supported:** Autonomous Manipulation (the live twin monitors the autonomous task) and all benchmarks (synchronized comparison is how the machine validates and watches itself).

---

## 1. The machine's problem

The machine has two streams of information that have never been properly joined: the twin's *predictions* (what the model says should happen) and the machine's *measurements* (what the sensors logged actually happened). To compare them, the machine must overcome several practical mismatches:

- **Different time axes.** The log has timestamps from the real run; the twin starts its own clock at zero. They must be aligned so that "the twin's prediction at t=1.5 s" corresponds to "the machine's measurement at t=1.5 s."
- **Different sample rates.** The sensors might log at 100 Hz; the twin might step at a different rate. The data must be resampled so the two are comparable point-for-point.
- **Which signals are inputs vs. outputs.** The twin must be *fed* the machine's actual inputs (the valve commands) and *predict* the outputs (position, pressure) — not fed everything, or there is nothing to compare.

Get these wrong and the comparison is meaningless — a prediction at one moment compared to a measurement at another tells the machine nothing. The machine's problem: synchronize the logged data with the twin so it can run in replay and compare prediction to reality, correctly aligned, signal by signal.

---

## 2. The concept: replay mode and synchronization

**Replay mode.** The machine runs its twin in **replay**: it steps through a logged task cycle in time, and at each step:
1. Reads the machine's *actual input* at this time (the valve command) from the log.
2. Feeds that input to the twin, advancing the twin's model one step.
3. Reads the machine's *actual output* at this time (measured position, pressure) from the log.
4. Compares the twin's *predicted* output to the machine's *measured* output.

This produces, across the whole cycle, two aligned traces for each output signal — predicted and measured — ready to compare. Replay mode is how the machine runs its twin against history, validating it and looking for faults, without needing the machine live.

**Data synchronization — the three alignments.** To make the comparison valid:

- **Time alignment:** offset the twin's clock to match the log's start, so corresponding points share a time.
- **Resampling:** interpolate the log (or the twin output) onto a common time grid, so both have values at the same instants — even if the sensor and the twin ran at different rates.
- **Input/output split:** designate the valve command as the input fed to the twin, and position/pressure/force as the outputs the twin predicts and the comparison checks.

**The measured-vs-predicted overlay.** The payoff is the overlay: the twin's predicted position and the machine's measured position on the same axis, across the task. When they track closely, the twin is synchronized — a faithful live mirror. The gap between them (the residual, Lesson 03) is the signal the machine watches for faults. This overlay is the operating picture of a digital twin: two traces that should coincide, and the meaning in their difference.

**Real-time vs. replay.** Replay runs on logged data (after the fact); a *real-time* twin runs live, stepping in lockstep with the operating machine. Replay is simpler and ideal for validation and teaching; real-time is the operational goal (Lesson 04's dashboard). The mechanics are the same — feed inputs, predict outputs, compare — only the timing differs.

---

## 3. Mathematical model

**Time alignment.** Given a log starting at wall-clock $t_0$ and the twin starting at 0, align by offset:
$$t_{twin} = t_{log} - t_0$$
so the twin's step $k$ corresponds to the log sample at the same elapsed time.

**Resampling.** If the log is sampled at times $\{t_i\}$ and the twin steps at $\{\tau_j\}$, interpolate the log onto the twin's grid (linear interpolation):
$$y_{log}(\tau_j) = y_i + \frac{\tau_j - t_i}{t_{i+1} - t_i}(y_{i+1} - y_i), \quad t_i \le \tau_j \le t_{i+1}$$
Now both twin and log have values at every $\tau_j$, comparable point-for-point.

**The replay loop.** At each aligned step $j$:
$$u_j = u_{log}(\tau_j) \quad\text{(input fed to twin)}$$
$$\hat{y}_j = \text{twin.step}(u_j) \quad\text{(predicted output)}$$
$$y_j = y_{log}(\tau_j) \quad\text{(measured output)}$$
$$\text{store } (\tau_j, \hat{y}_j, y_j) \quad\text{for comparison}$$

**Agreement over the cycle.** The overall fidelity, per output signal:
$$\text{RMS residual} = \sqrt{\frac{1}{N}\sum_j (\hat{y}_j - y_j)^2}$$
A small RMS residual relative to the signal's range means the twin is synchronized — mirroring the machine across the whole task.

---

## 4. Visual explanation

![Digital Twin Workflow](https://alibulentkoc.github.io/fluid-powered-physical-ai-curriculum/assets/figures/digital_twin_workflow.svg)

*Figure: digital twin workflow — see full diagram above.* (replay-mode comparison)

Picture the replay as a playhead moving along the task timeline. At each moment, the log supplies the real valve command (the input), the twin computes its predicted position, and the log supplies the measured position — and the two are plotted together. As the playhead sweeps the cycle, two traces grow side by side: the twin's prediction and the machine's measurement, ideally overlapping. The figure shows them nearly coincident for a healthy, synchronized twin, with the small gap between them (the residual) shaded below. This sweeping comparison is the twin running alongside the machine — the live mirror in action, even in replay.

---

## 5. Engineering example

**Why replay mode is where the twin earns trust**

Before the machine trusts its twin to detect faults or guide decisions, it must *see* the twin track reality across a complete, real task — not just a single validation point (Module 10) but the whole cycle, moment by moment. Replay mode provides exactly this: the machine takes a logged task and watches the twin predict it, step by step, and sees the prediction track the measurement through startup, extension, hold, retraction, and stop.

This builds justified trust. If the twin tracks the measured position to within 1% across the entire cycle, the machine knows its twin is faithful — and therefore that any *future* divergence is a real signal, not model error. The replay comparison is the twin's report card, earned over a whole task rather than asserted. And because it runs on logged data, it costs nothing and risks nothing — the machine can replay many cycles, across many conditions, building confidence in the twin before relying on it operationally.

This is also where the machine discovers the twin's *limits* — the conditions or signals where it tracks less well — guiding the parameter refinement of Lesson 04. Replay mode is thus both the validation and the diagnosis of the twin itself: the machine learning exactly how much, and where, to trust its digital counterpart.

---

## 6. Worked example

**The machine replays a logged cycle.** The workcell logged a task cycle at 100 Hz (Module 09). The twin steps at 100 Hz. Run replay and compare position.

*Synchronization:*
- Time alignment: log starts at $t_0$; subtract it so both start at 0. ✓
- Resampling: log and twin both at 100 Hz — already aligned, no interpolation needed. ✓
- Input/output: feed the logged valve command to the twin; compare predicted vs. measured position. ✓

*Replay (per phase):*
| Phase | Twin predicted | Measured | Residual |
|-------|----------------|----------|----------|
| Extend | tracks 0→150 mm | 0→150 mm | small, grows slightly with friction |
| Hold | holds 150 mm | holds 150 mm | near zero |
| Retract | tracks 150→0 mm | 150→0 mm | small |

*Overall:* position RMS residual ~1.5 mm over the 150 mm stroke (~1%). The twin tracks the measured position closely across the whole cycle — synchronized. The slightly larger residual during extension hints that the twin's friction is a touch low (the real machine lags slightly), a refinement for Lesson 04.

The machine has run its twin alongside a real task and confirmed it mirrors reality. The twin is now demonstrably live and synchronized — ready to detect faults (Lesson 03), because the machine knows what "healthy" looks like: small residuals everywhere.

---

## 7. Interactive demonstration

```python
def resample(log_times, log_values, target_times):
    """Linear-interpolate logged data onto the twin's time grid."""
    out = []
    for t in target_times:
        # find bracketing log samples
        for i in range(len(log_times)-1):
            if log_times[i] <= t <= log_times[i+1]:
                frac = (t - log_times[i]) / (log_times[i+1] - log_times[i])
                out.append(log_values[i] + frac*(log_values[i+1]-log_values[i]))
                break
        else:
            out.append(log_values[-1])
    return out

# Log sampled at 50 Hz, twin steps at 100 Hz -> resample needed
log_t = [0.0, 0.02, 0.04, 0.06]
log_pos = [0.0, 1.8, 3.6, 5.4]
twin_t = [0.0, 0.01, 0.02, 0.03, 0.04, 0.05, 0.06]
aligned = resample(log_t, log_pos, twin_t)
print("Resampling log (50 Hz) onto twin grid (100 Hz):")
for t, p in zip(twin_t, aligned):
    print(f"  t={t:.2f}s -> measured position {p:.2f} mm")
print("\nNow twin prediction and measurement share a time grid -> comparable.")
```

Run it. Resampling aligns mismatched sample rates so prediction and measurement can be compared point-for-point.

---

## 8. Coding exercise

Create `code/module11/twin_replay.py` that:

1. Loads a logged task cycle (or generates a synthetic one)
2. Aligns the time axes and resamples to a common grid
3. Runs the twin in replay: feeds logged inputs, produces predicted outputs
4. Plots measured vs. predicted (position, pressure) and reports the RMS residual

This is the twin running alongside the machine — synchronized replay, the basis for monitoring.

---

## 9. Knowledge check

1. What three mismatches must the machine overcome to synchronize log and twin?
2. Describe the replay loop, step by step.
3. Why must the twin be *fed* the inputs but *predict* the outputs?
4. What does the measured-vs-predicted overlay show, and what is the gap between them?
5. How does replay mode differ from a real-time twin?

---

## 10. Challenge problem

The machine logs a task at 200 Hz, but its twin steps at 100 Hz, and the log's clock starts at 14:32:05 while the twin starts at 0.

**a)** What must the machine do to the time axes before comparing?

**b)** The sample rates differ (200 vs. 100 Hz). What operation aligns them, and onto which grid?

**c)** After synchronization, the twin's predicted position leads the measured position by a constant 0.05 s. What might cause this, and is it a twin error or a synchronization error?

**d)** Why is it essential to feed the twin the *logged valve command* rather than letting the twin choose its own command?

---

## 11. Common mistakes

**Comparing unaligned time axes.** A prediction at one instant compared to a measurement at another is meaningless. Align the clocks first.

**Ignoring sample-rate mismatch.** If the log and twin run at different rates, their points do not correspond. Resample onto a common grid before comparing.

**Feeding the twin the measured outputs.** If the twin is given the measured position, it cannot *predict* it — there is nothing to compare. Feed only the inputs (commands); let the twin predict the outputs.

**Trusting the twin without a full-cycle replay.** A single validation point is not enough. Replay a whole task (and several) to see where and how well the twin tracks before relying on it.

---

## 12. Key takeaways

- To become live, the twin must run on the machine's real logged data — fed the actual inputs, compared to the actual outputs.
- Synchronization requires three alignments: time (match the clocks), resampling (common time grid), and input/output split (feed commands, predict outputs).
- Replay mode steps through a logged cycle, feeding inputs and comparing predicted to measured outputs across the whole task.
- The measured-vs-predicted overlay is the operating picture of the twin; the gap between them (the residual) is the fault signal.
- Replay is where the twin earns trust — tracking reality across a full task — and reveals its limits for refinement.

---

## Machine Capability Added

> **Before this lesson the machine could not:** run its twin on real data — the twin and the machine's actual operation never properly met.
>
> **After this lesson the machine can:** run its twin in synchronized replay against logged task cycles — feeding real inputs, comparing predicted to measured outputs across the whole task, confirming the twin mirrors reality.

The machine now has a **synchronized, live twin**. You can feed the machine's real logged data to the twin, align the time axes and sample rates, run replay, and see the twin track the real machine across an entire task. This is the twin running alongside the machine — the live mirror, demonstrated over real operation, ready to detect faults.

**Digital twin contribution:** the data-synchronization and replay machinery make the twin *live* — connected to the machine's real operation, not just assembled. The twin can now run against any logged cycle, producing the aligned measured-vs-predicted comparison that fault detection (Lesson 03) and parameter refinement (Lesson 04) are built on.

---

*Lesson 02 — Version 0.1 | Next: Lesson 03 — The twin watches over the machine (residual analysis and fault detection)*


---

## AI Learning Companion

Copy any prompt below into Claude, ChatGPT, or another AI assistant.

**Tutor prompt** — explain it another way

```
Re-explain this lesson from Module 11 (Digital Twin) of the Fluid-Powered Physical AI curriculum: "The twin runs alongside the machine". Teach it through the running machine — the Smart Agricultural Workcell — using physical intuition first, then the math. Keep hydraulic terminology precise.
```

**Practice prompt** — generate more exercises

```
Give me 5 practice problems for this lesson ("The twin runs alongside the machine", Module 11 — Digital Twin) on the Smart Agricultural Workcell, with full worked solutions. Mix conceptual and numerical.
```

**Explore prompt** — connect it to the real world

```
Show me how this lesson's concept ("The twin runs alongside the machine") appears in real agricultural, construction, or industrial hydraulic machines, with concrete examples and typical numbers.
```

## Global Learning Support

Need this lesson in another language? Copy a prompt below into an AI assistant. English remains the authoritative source.

**Supported languages (initial):** English · Español · 中文 (Simplified Chinese) · Türkçe

```
I just studied this lesson ("The twin runs alongside the machine", Module 11 — Digital Twin) from the Fluid-Powered Physical AI curriculum.
Explain it in [Spanish / Simplified Chinese / Turkish]. Keep hydraulic and mathematical terminology in English where commonly used.
Then provide: a short summary, three practice questions, and one challenge problem.
```
