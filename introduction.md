

# Introduction to Visualization in Data Science

Data visualization is the graphical representation of information and data. By using visual elements like charts, graphs, and maps, data visualization tools provide an accessible way to see and understand trends, outliers, and patterns in data.

**Course**: Visualization in Data Science (Lecture Series)

**Purpose.** This introduction collects the mathematical foundations, practical examples, code resources and project ideas you’ll need for a lecture series that teaches how to think about, design, and implement effective visualisations in data science.

---

## Learning outcomes

By the end of the course students should be able to:

* Explain core mathematical ideas behind dimensionality reduction and geometric intuitions used in visualization.
* Critically evaluate visualisations for clarity, integrity and potential misleading elements.
* Implement reproducible visual analysis workflows (R / RMarkdown / Tufte-style reports).
* Recreate canonical statistical graphics (e.g. Minard) and modern high-dimensional visualisations (t-SNE, heatmaps).
* Apply basic statistical diagnostics and mixed-effects model visualisations for real datasets.

---

## Suggested prerequisites

* Basic statistics (means, variance, regression)
* Linear algebra (vectors, matrices, eigenvectors) — refresher notes are provided below
* Some familiarity with R (or willingness to learn during labs)

---

## Course structure (recommended modules)

### 1. Mathematical foundations & dimensionality reduction

* **Lecture + reading:** *Mathematics for data science & visualization* (notes & proofs).

  * Mathematics PDF: [https://github.com/neelsoumya/visualization_lecture/blob/main/mathematics_data_science.pdf](https://github.com/neelsoumya/visualization_lecture/blob/main/mathematics_data_science.pdf)
  * OSF teaching resources and activities: [https://osf.io/mnh8d/](https://osf.io/mnh8d/)
  * Teaching resources on the mathematics of dimensionality reduction: [https://www.researchgate.net/publication/375186575_Everything_you_wanted_to_know_about_the_mathematics_of_dimensionality_reduction_and_visualization_but_were_afraid_to_ask_Teaching_resources_and_activities](https://www.researchgate.net/publication/375186575_Everything_you_wanted_to_know_about_the_mathematics_of_dimensionality_reduction_and_visualization_but_were_afraid_to_ask_Teaching_resources_and_activities)

  
  * [University of Cambridge data visualization resources](https://cambiotraining.github.io/visual-data-communication/materials/functions-and-objects.html)

<!--
**Activities:** derive PCA from first principles (covariance, eigen-decomposition), small proof exercises, visualise principal components on simple 2D/3D datasets.
-->
**Activities:** Visualise principal components on simple 2D/3D datasets.
---

### 2. Perception, design principles & Tufte

* **Tufte & data-ink:** short reading and applied exercise.

  * Tufte’s Minard page (canonical example): [https://www.edwardtufte.com/tufte/minard](https://www.edwardtufte.com/tufte/minard)
  * Tufte-style RMarkdown package (make Tufte-inspired handouts): [https://github.com/rstudio/tufte](https://github.com/rstudio/tufte)
  * Practical notes on Tufte’s principles in R: [https://jtr13.github.io/cc19/tuftes-principles-of-data-ink.html](https://jtr13.github.io/cc19/tuftes-principles-of-data-ink.html)

**Activities:** produce a Tufte-style one-page analysis of a dataset using RMarkdown; critique a student-submitted plot for ‘data-ink’ waste.

---

### 3. High-dimensional thinking & dimensional imagination

* **Motivation & intuition:** resources to help students visualise higher dimensions and intuitive strategies.

  * Popular explanation: "Thinking outside the 10-dimensional box": [https://www.popularmechanics.com/science/math/a27737/visualize-higher-dimensions/](https://www.popularmechanics.com/science/math/a27737/visualize-higher-dimensions/)
  * Short video: [https://youtu.be/zwAD6dRSVyI](https://youtu.be/zwAD6dRSVyI)

**Activity:** interactive visual exercises and mental-model building (embedding spheres, hypercubes) and mapping to dimensionality reduction outputs.

---

### 4. Projections, maps & spatial visualization

* **Cartographic projections:** compare distortion trade-offs when mapping a sphere to a plane.

  * Primer on map projections: [https://whereexactlymaps.com/blogs/articles/an-introduction-to-map-projections](https://whereexactlymaps.com/blogs/articles/an-introduction-to-map-projections)
  * Gallery & discussion: [https://www.viewsoftheworld.net/?p=752](https://www.viewsoftheworld.net/?p=752)

**Activity:** small project building choropleth maps and experimenting with different projections and colour schemes.

---

### 5. Multivariate visualisation & case-studies

* **Classic and modern case studies:**

  * Minard analysis code and tutorials: [https://github.com/joannecheng/napoleon_analysis](https://github.com/joannecheng/napoleon_analysis)
  * Thoughtbot analysis blog: [https://thoughtbot.com/blog/analyzing-minards-visualization-of-napoleons-1812-march](https://thoughtbot.com/blog/analyzing-minards-visualization-of-napoleons-1812-march)
  * General visualization projects & inspiration: [https://nagix.github.io/](https://nagix.github.io/)

**Activity:** reproduce Minard, then redesign it for another historical dataset; present differences in communication and fidelity.

---

### 6. Good / bad visualisation — ethics & pitfalls

* **How to mislead & how to avoid it:** curated reads and examples.

  * 10 ways to mislead with data visualization: [https://policyviz.com/2023/02/07/10-ways-to-mislead-with-data-visualization/](https://policyviz.com/2023/02/07/10-ways-to-mislead-with-data-visualization/)
  * Misleading examples and commentary: [https://wpdatatables.com/data-visualization-examples/](https://wpdatatables.com/data-visualization-examples/) , [https://wpdatatables.com/misleading-data-visualization-examples/](https://wpdatatables.com/misleading-data-visualization-examples/)
  * Diverging color palettes & map-specific notes: [https://policyviz.com/2020/08/10/on-diverging-color-palettes-in-maps/](https://policyviz.com/2020/08/10/on-diverging-color-palettes-in-maps/)
  * Visual confusion catalogue: [https://viz.wtf/](https://viz.wtf/)
  * R graph gallery (practical recipes): [https://r-graph-gallery.com/](https://r-graph-gallery.com/)
  * Good/bad roundup: [https://www.oldstreetsolutions.com/good-and-bad-data-visualization](https://www.oldstreetsolutions.com/good-and-bad-data-visualization)
  * Qlik examples: [https://www.qlik.com/us/data-visualization/data-visualization-examples](https://www.qlik.com/us/data-visualization/data-visualization-examples)

**Activity:** group exercise — find an example that misleads and rewrite it to improve accuracy and clarity.

---

### 7. Practical coding & statistical modelling labs (R/Python)

* **Code repos & examples:**

  * ANOVA, linear mixed-effects examples (R): [https://github.com/neelsoumya/anova_linear_mixed_effects_examples](https://github.com/neelsoumya/anova_linear_mixed_effects_examples)
  * Tufte R Markdown package: [https://github.com/rstudio/tufte](https://github.com/rstudio/tufte)

**Labs:**

* Reproduce key figures (Minard) using provided code.
* Run LME models and produce diagnostic visualisations (residual plots, random effects plots).
* Dimensionality reduction lab: compute PCA, t-SNE, UMAP and compare embeddings visually.

---

### 8. Modern alternatives & troubleshooting

* **Broken charts & critique:** (a modern take on chart failure modes)

  * Broken charts essay / examples: [https://dominicroye.github.io/blog/2025-12-14-broken-charts/](https://dominicroye.github.io/blog/2025-12-14-broken-charts/)

**Activity:** peer review a visualization and provide a short written critique (1 page) plus a revised figure.

---

## Example datasets & illustrations

* IL10 project (t-SNE and heatmaps) — example images for lecture slides:

![Example tSNE](https://gut.bmj.com/content/gutjnl/70/6/1023/F3.large.jpg)

![Example heatmaps](https://gut.bmj.com/content/gutjnl/70/6/1023/F5.large.jpg)

(Use these to demonstrate cluster structure vs. heatmap summaries; ensure you note provenance and licensing if reused.)

---

## Suggested assessment & deliverables

* Short coding lab reports (RMarkdown, Tufte style) — 2 assignments
* Group project: reproduce + extend a historical or modern visualization (e.g. Minard rework, IL10 reproduction)
* Short critical essay: how visualisation can mislead and how to prevent it (1,000 words)
* [Assignments](assignments.md) page with more details on suggested assessment structure.

---

## Further reading & talks

* Great talks and recorded lectures (playlist): [https://www.youtube.com/watch?v=iipVlV4I_Vg&list=PLB2SCq-tZtVnXalwtfVPcjwy0xJbu-btN&index=4](https://www.youtube.com/watch?v=iipVlV4I_Vg&list=PLB2SCq-tZtVnXalwtfVPcjwy0xJbu-btN&index=4)

---

