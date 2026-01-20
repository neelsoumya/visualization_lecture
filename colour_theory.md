# Color theory for data visualization — Lesson plan


## Learning objectives

By the end of this lesson students will be able to:

* Explain the basic properties of color (hue, saturation, value/brightness) and common color spaces (RGB, HSL/HSV, CIELAB).
* Distinguish when to use qualitative, sequential, diverging, and cyclical color maps.
* Choose perceptually appropriate, accessible palettes for different data types.
* Identify common color-misuse patterns (e.g. rainbow maps) and fix them.
* Apply color palettes in Python (matplotlib / seaborn) and test designs for color-blind viewers.


## Code in Python

- [iPython notebook](https://github.com/neelsoumya/visualization_lecture/blob/main/colour_theory.ipynb)

---

## Lecture outline (45–60 minutes)

### 1. Quick warm-up (5 min)

* Show three short examples and ask students to say which is easiest to interpret: a bar chart using many bright hues, a heatmap with the "rainbow" colormap, and the same heatmap using a perceptually uniform map (e.g., *viridis*). Use responses to motivate why color choice matters.

### 2. Color basics (8–10 min)

* **Hue** — the type of color (red, blue, green).
* **Saturation / Chroma** — intensity of the hue (washed out vs vivid).
* **Value / Lightness / Brightness** — how light or dark the color is.
* **Color spaces** — why RGB is device-oriented, while HSL/HSV is intuitive for humans; introduce perceptual spaces such as CIELAB (Lab) and why they matter: equal steps in Lab try to correspond to equal perceived differences.

### 3. Types of data and palette types (10–12 min)

* **Qualitative (categorical)** — many distinct hues, no ordering (e.g., species, countries). Use palettes where colors are clearly different (e.g., Set1, Tableau, Okabe‑Ito).
* **Sequential** — ordered data that goes from low → high (e.g., population density). Use single-hue or multi-hue palettes that vary mainly in lightness (e.g., viridis, cividis, single‑hue blues).
* **Diverging** — data with a meaningful midpoint (e.g., anomaly from zero). Use two contrasting hues with a neutral middle (e.g., `RdBu`, custom blue–white–red where lightness is monotonic away from center).
* **Cyclic** — data that wraps (e.g., wind direction, time of day) — use cyclical palettes where the ends match.

### 4. Perception and accessibility (8–10 min)

* **Perceptual uniformity** — a change in data should appear as a uniform change in color; colormaps like *viridis* and *cividis* are designed for that.
* **Luminance and ordering** — humans perceive lightness differences more reliably than hue differences; where ordering matters, map to lightness.
* **Color-blindness** — brief intro to common types (deuteranopia, protanopia, tritanopia). Emphasize testing and using colorblind-friendly palettes (Okabe‑Ito, ColorBrewer single-hue or colorblind-safe sets).
* **Contrast and text readability** — check that text labels and background contrast is sufficient.

### 5. Common pitfalls (5 min)

* **Rainbow / jet** maps: distort data by introducing artificial boundaries and non-monotonic lightness.
* **Using hue to encode magnitude** — hue is categorical; avoid using it alone for ordered numbers.
* **Too many hues** — humans can reliably distinguish only ~8–12 categorical colors.
* **Relying on color alone** — always consider redundant encodings (shape, line style, labels).

### 6. Quick demo (5–10 min)

* Live code: show the same chart with *jet*, *viridis*, and a diverging palette; convert to grayscale or run a colorblind simulation to show problems.

---

## Practical guidelines (cheat sheet)

* **If data is ordered → use sequential** palettes that vary in lightness.
* **If data has a central reference → use diverging** palettes with neutral midpoint.
* **If data is categorical → use qualitative** palettes ensuring distinct hues and similar lightness when no ordering is intended.
* **Prefer perceptually uniform** palettes for continuous data (e.g., viridis, cividis, inferno, plasma, magma, cubehelix).
* **Test for color-blindness** and for grayscale readability.
* **Annotate important values** instead of expecting viewers to decode colors alone.

---

## Example code snippets (Python)

### Matplotlib — sequential and diverging maps

```python
import matplotlib.pyplot as plt
import numpy as np

# example data
x = np.linspace(0, 10, 100)
y = np.sin(x)

# sequential colormap for a heatmap
Z = np.outer(np.sin(x), np.cos(x))
plt.figure()
plt.imshow(Z, cmap='viridis')
plt.title('Sequential: viridis')
plt.colorbar()

# diverging example
plt.figure()
plt.imshow(Z - Z.mean(), cmap='RdBu', vmin=-np.max(np.abs(Z)), vmax=np.max(np.abs(Z)))
plt.title('Diverging: RdBu (centered)')
plt.colorbar()

plt.show()
```

### Seaborn — categorical palette and palette chooser

```python
import seaborn as sns
import matplotlib.pyplot as plt

# categorical (qualitative)
pal = sns.color_palette('Set2')
sns.palplot(pal)
plt.title('Qualitative palette: Set2')
plt.show()

# using viridis as a seaborn palette
sns.heatmap(np.random.rand(10,10), cmap='viridis')
plt.title('heatmap with viridis')
plt.show()
```

### Checking contrast & simulating color-blindness (notes)

* Matplotlib doesn't simulate color blindness directly; for testing in code you can use libraries like `colorspacious` or `colour` to simulate deuteranopia/protanopia. For classroom demos, many online simulators and design tools exist. Also, converting to grayscale (`plt.cm.gray`) provides a quick check for monotonic lightness.

---

## Exercises / Lab ideas (45–60 minutes)

### Short warm-up (10 min)

* Give students 3 small charts (each using a different colormap) and ask them to rank which are easiest to interpret and why.

### Main lab (30–40 min)

* **Dataset options:** (pick one) global life expectancy by country, median income by region, or air-quality index time series.
* Tasks:

  1. Create a visualization that encodes a continuous variable (e.g., density, index) as a choropleth or heatmap — try `viridis` and `jet`, compare and write 150 words explaining which is better and why.
  2. Produce a categorical bar chart with 10 categories — choose an appropriate qualitative palette and justify the choice.
  3. Reproduce one of the visualizations for a color-blind viewer (simulate or convert to a recommended color‑blind palette) and comment on differences.

### Advanced challenge (optional)

* Design a color scheme for a dashboard (3–4 coordinated charts) ensuring accessibility, brand consistency, and contrast. Deliver a short style guide (colors + usage rules + hex codes).

---

## Assessment / rubric ideas

* **Correctness (30%)** — Did the student choose a palette appropriate to data type and mapping?
* **Accessibility (30%)** — Did the student test for color-blindness/grayscale and ensure label contrast?
* **Explanation (20%)** — Is the justification clear and grounded in color theory (lightness, perceptual uniformity)?
* **Aesthetics & clarity (20%)** — Visual appeal without sacrificing interpretability (legible text, good contrast, limited decorative color use).

---

## Common references & tools (names only)

* ColorBrewer (palette suggestions for mapping types)
* Viridis / cividis / inferno / plasma / magma (perceptually uniform colormaps)
* Okabe‑Ito / Color Universal Design palettes (color-blind friendly palettes)
* `colorspacious`, `colour`, and `colorcet` (Python libraries for advanced color work and simulation)

---

## Quick slide summary (for printing on one page)

* Use **sequential** for ordered scales, **diverging** for data with a meaningful midpoint, **qualitative** for categories.
* Prefer **perceptually uniform** palettes for continuous data — map magnitude to **lightness** not hue.
* **Don't use rainbow/jet** for quantitative scales.
* Test for **color-blindness** and for **grayscale** readability.
* Use **redundant encodings** and good labels; color is one channel among many.


- [Next: Gestalt Theory in Data Visualization](gestalt_theory.md)