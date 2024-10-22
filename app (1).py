
import gradio as gr

# Ethics DataCard content for forest wildfire prediction model
datacard_content = """
# Ethics DataCard for Forest Wildfire Prediction Model

## Dataset Overview
- **Input Variables**: Temperature, Humidity, Wind Speed, Rainfall, Fuel Moisture, Vegetation Type, Slope, Region
- **Output Variables**: Fire Size, Fire Duration, Suppression Cost, Fire Occurrence

## Data Collection Process
- The data sources for this app include NASA, location-specific weather data, United States Forest Service, vegetation reports, and topographical data.
- The data is collected from public and licensed sources we gained the right to use. In doing this it was ensured that by private/ personal information would be anonymized to protect everyone's privacy rights.  

## Bias Considerations
- **Potential Bias**: 
    - Different values and priorities that other cultures have towards different lands (e.g., rural or indigenous lands).
    - Most data sources might be focused in specific regions causing a geographical bias to occur, skewing the data.
- **Mitigation**: 
    - To avoid disrespecting a culture the model will cross-reference the data with a list of what cultures are on record in that area. It will then pit out a warning about what cultures they effect.
    - The model will minimize this bias by cross-referencing the data with other sets to monitor the data collection happening in order to always make sure the data is diversified.

## Fairness & Justice
- Thia model is designed to predict wildfires in diverse geographical locations. To minimize the possible consequences of fires to communities.
- SThe system will combine multiple machine-learning models to reduce the effects of individual model errors. Therefore, prohibiting the odds of a false positive or negative occuring. 

## Privacy and Security
- Gathering  most of the information from government websites as well to minimize the amount of personal data being leaked.
- Anything found from a personal social media account will not be used unless someone has consented for it to be.

## Sustainability and Environmental Impact
- By reducing forest fires you are protecting the wildlife and the environment they live in. 
- By identifying locations that are at higher risk deforestation could decreased by being ahead of the situation and planning ways to preserve the environment based off of the predictions.

## Model Limitations
- The model's accuracy well depend on the data any skewness present in them. In areas with limited forest fire data, predictions may be less precise. To address this situation, the model is continually updated with new climate information.

## Accountability and Transparency
- The model's for performance will be monitored over time, to adapt the model to new climate events so that it stays current.
- Everyone with accesss to the app will be informed up front abou tthe model and the limitations it has. As well of the tradeoffs that could happen if a false prediction occurs.
- When a false prediction does occur there will be a way for users to send feedback on any inaccurracies they have experienced.

## Societal Impact
- By giving access to data to predict forest fires, communities wll be able to better prepare themselves for fires that may occur based on the predictions.
- This app also will improve public safety by helping government servces no where fire will occur quicker.
"""

# Function to display the DataCard
def display_datacard():
    return datacard_content

# Gradio interface to display the ethics DataCard
iface = gr.Interface(fn=display_datacard, inputs=[], outputs="markdown")

# Launch the Gradio interface
iface.launch()
