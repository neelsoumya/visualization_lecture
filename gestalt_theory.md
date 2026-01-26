# Gestalt theory of data visualization

- Gestalt theory, originating from psychology, emphasizes that humans perceive visual elements as organized patterns or wholes rather than just a collection of individual parts.

- In data visualization, applying Gestalt principles can enhance the clarity and effectiveness of visual representations. 

- Key principles include:
    - **Proximity**: Elements that are close to each other are perceived as related. In data visualization, grouping related data points or categories can help viewers quickly understand relationships.
    
    - **Similarity**: Elements that look similar are perceived as part of the same group. Using consistent colors, shapes, or sizes for related data can reinforce connections.
    
    - **Continuity**: The eye is drawn to continuous lines and patterns. Designing visualizations with smooth transitions and flows can guide viewers through the data more intuitively.
    
    - **Closure**: The mind tends to fill in missing information to create a complete image. Visualizations that suggest shapes or patterns can engage viewers and encourage them to explore the data further.
    
    - **Figure-Ground**: This principle involves distinguishing an object (figure) from its background (ground). Effective use of contrast and spacing can help highlight important data points.

- By leveraging these Gestalt principles, data visualizations can become more intuitive, making it easier for viewers to interpret and derive insights from complex datasets.

- Overall, Gestalt theory provides valuable guidelines for designing data visualizations that are not only aesthetically pleasing but also functionally effective in conveying information.

## Examples

- [Link to Google Colab notebook with examples](https://github.com/neelsoumya/visualization_lecture/blob/main/gestalt_visualization.ipynb)

- A scatter plot that uses color coding to group related data points, applying the principle of similarity.

```python
import matplotlib.pyplot as plt
import numpy as np
# Sample data
x = np.random.rand(50)
y = np.random.rand(50)
colors = np.random.choice(['red', 'blue'], size=50)
plt.scatter(x, y, c=colors)
plt.title('Scatter Plot with Similarity Principle')
plt.show()
```


- A bar chart where bars representing related categories are placed close together, utilizing the principle of proximity.

```python
import matplotlib.pyplot as plt
# Sample data
categories = ['A', 'B', 'C', 'D']
values1 = [5, 7, 3, 4]
values2 = [6, 8, 4, 5]
x = np.arange(len(categories))
width = 0.35
plt.bar(x - width/2, values1, width, label='Group 1')
plt.bar(x + width/2, values2, width, label='Group 2')
plt.xticks(x, categories)
plt.title('Bar Chart with Proximity Principle')
plt.legend()
plt.show()
```

- A line graph that smoothly connects data points, demonstrating the principle of continuity.

```python
import matplotlib.pyplot as plt
# Sample data
x = np.linspace(0, 10, 100)
y = np.sin(x)
plt.plot(x, y)
plt.title('Line Graph with Continuity Principle')
plt.show()
```

- A pie chart that suggests a complete circle even if some segments are missing, illustrating the principle of closure.

```python
import matplotlib.pyplot as plt
# Sample data
sizes = [30, 20, 25, 15]
labels = ['A', 'B', 'C', 'D']
plt.pie(sizes, labels=labels, startangle=90)
plt.title('Pie Chart with Closure Principle')
plt.show()
```

- A heatmap that uses contrasting colors to differentiate between high and low values, applying the figure-ground principle.

```python
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
# Sample data
data = np.random.rand(10, 10)
sns.heatmap(data, cmap='coolwarm')
plt.title('Heatmap with Figure-Ground Principle')
plt.show()
```

## 🤔❓ Applications to modern data science

- tSNE and UMAP visualizations often leverage Gestalt principles to help users identify clusters and patterns in high-dimensional data.

- Also makes interpretation of tSNE plots difficult when these principles are not effectively applied.

- Dashboards and data reporting tools use these principles to create intuitive layouts that facilitate quick comprehension of key metrics.

- Interactive visualizations (_plotly_) often incorporate Gestalt principles to enhance user engagement and understanding, such as through hover effects that highlight related data points.

## Visual perception principles

- Gestalt principles are part of a broader set of visual perception principles that influence how we interpret visual information. Other important principles include:

    - **Preattentive Processing**: Certain visual properties (like color, shape, and size) are processed rapidly by the human brain before conscious attention is directed. Effective data visualizations leverage preattentive attributes to highlight important information quickly.

    - **Color Theory**: The use of color can significantly impact the readability and interpretability of data visualizations. Understanding color relationships (complementary, analogous, etc.) helps in creating visually appealing and effective graphics.

    - **Visual Hierarchy**: Establishing a clear visual hierarchy through size, color, and placement helps guide the viewer's eye to the most important elements first.

    - **Balance and Alignment**: Proper alignment and balance in design contribute to a cohesive and organized appearance, making it easier for viewers to process information.

    - **Contrast**: Using contrast effectively can help differentiate between different data points or categories, enhancing clarity.

## Use of colour in data visualization

- Use blue in large regions

- Use red and green in the centers of attention

- 🧩🚀 _Concept_ edges of retina not sensitive to red and green

- Use black, white and yellow in peripheral regions


## 🎮 Colour activity

- [Colour activity](https://color.method.ac/)


## 💡 Glyphs and visual variables

- Visual variables are attributes that can be manipulated to represent data in visualizations. Common visual variables include:

    - **Position**: The location of an element on a chart or graph, often used to represent quantitative data.

    - **Size**: The dimensions of an element, which can indicate magnitude or importance.

    - **Shape**: Different shapes can represent different categories or types of data.

    - **Color**: Color can convey information about categories, values, or intensity.

    - **Orientation**: The angle or direction of an element can provide additional context or meaning.

    - **Texture**: Patterns or textures can differentiate between areas in a visualization.

- Glyphs are visual representations that combine multiple visual variables to encode complex data. Examples of glyphs include:  

    - **Chernoff Faces**: Use facial features (like eyes, nose, mouth) to represent multivariate data.

    - **Star Plots**: Use radial lines extending from a central point to represent multiple variables.

    - **Glyph Maps**: Combine position with other visual variables to represent data on geographical maps.

    - [Glyph maps by Hadley Wickham](https://vita.had.co.nz/papers/glyph-maps.pdf)


## Change blindness
- Change blindness is a phenomenon where significant changes in a visual scene go unnoticed by the observer.

- This occurs because our attention is limited, and we often focus on specific elements while ignoring others.

- In data visualization, change blindness can impact how effectively information is communicated. 

- If important changes in data are not visually highlighted, viewers may miss critical insights.
- To mitigate change blindness in data visualizations, designers can use techniques such as:
    - **Animation**: Smooth transitions can help draw attention to changes over time.
    - **Highlighting**: Using color or size changes to emphasize important data points.
    - **Annotations**: Adding text or markers to indicate significant changes.


- 🎮💡🛠️ Watch the following [videos](https://www.youtube.com/watch?v=vJG698U2Mvo&list=PLB228A1652CD49370) to see examples of [change blindness](http://www.simonslab.com/videos.html).


## Optical illusions

- Optical illusions are visual phenomena that deceive the eye and brain, leading to misinterpretations of visual information.
- In data visualization, optical illusions can inadvertently affect how data is perceived, potentially leading to misunderstandings or misinterpretations.
- Common types of optical illusions that can impact data visualization include:
    - **Ambiguous Illusions**: Images that can be interpreted in multiple ways, which can lead to confusion in data representation.
    - **Distorting Illusions**: Visual elements that distort perception, such as misleading scales or axes.
    - **Paradoxical Illusions**: Images that create impossible scenarios, which can confuse viewers.
- To avoid optical illusions in data visualization, designers should:
    - Use clear and consistent scales.
    - Avoid overly complex designs that can confuse viewers.
    - Test visualizations with diverse audiences to ensure clarity.


## Resources

- [The pyschology behind data visualization](https://towardsdatascience.com/the-psychology-behind-data-visualization-techniques-68ef12865720/)

- [Principles of proportional ink](https://clauswilke.com/dataviz/proportional-ink.html#:~:text=This%20concept%20has%20been%20termed,the%20data%20values%20they%20represent)


- **John Stasko — Visual Perception (CS7450 lecture notes, Georgia Tech)**  
  [link](https://faculty.cc.gatech.edu/~stasko/7450/16/Notes/perception.pdf)

- **Jacques Bertin — Semiology of Graphics (excerpt PDF)**  
  [link](https://digitalsocietyschool.org/wp/wp-content/uploads/2020/09/Bertin_Semiology_of_Graphics_Excerpt_2016.pdf)

- **Alberto Cairo — The Functional Art (sample pages)**  
  [link](https://ptgmedia.pearsoncmg.com/images/9780321834737/samplepages/0321834739.pdf)

- **Preattentive properties & Gestalt perception (lecture slides)**  
  [link](https://dmice.ohsu.edu/bedricks/courses/cs631_fall_2016/lectures/week2_lec1b.pdf)

- **Gestalt Principles in Data Visualization (student paper)**  
  [link](https://ecommons.luc.edu/cgi/viewcontent.cgi?article=1786&context=ures)

- **Exploring the use of Gestalt’s principles (ResearchGate / case study)**  
  [link](https://www.researchgate.net/publication/328571584_Exploring_the_Use_of_Gestalt%27s_Principles_in_Improving_the_Visualization_User_Experience_and_Comprehension_of_COBie_Data_Extension)

- **Interaction Design Foundation — What are the Gestalt Principles?**  
  [link](https://www.interaction-design.org/literature/topics/gestalt-principles)

- **Principles of Data Visualization — Artificium (PDF)**  
  [link](https://artificium.us/lessons/54.info-viz/l-54-103-build-explntry-viz/resources/principles-of-data-visualization.pdf)

- **Lecture: Pre-attentive attributes & Gestalt (PDF)**  
  [link](https://bbrejova.github.io/viz/pdf/L09_Preattentive_and_Gestalt.pdf)

- **The Gestalt Principles — Data Action Lab (handout PDF)**  
  [link](https://www.data-action-lab.com/wp-content/uploads/2021/05/ACFO-DV-4.pdf)


- [Next: Assignment](assignment.md)

