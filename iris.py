import streamlit as st
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

# Cache dataset
@st.cache_data
def load_data():
    return load_iris()

# Cache model training
@st.cache_resource
def train_model():
    iris = load_data()
    X_train, X_test, y_train, y_test = train_test_split(
        iris.data, iris.target, test_size=0.2, random_state=42
    )
    model = RandomForestClassifier()
    model.fit(X_train, y_train)
    return model, iris

model, iris = train_model()

# Species images
species_images = {
    "setosa": "https://upload.wikimedia.org/wikipedia/commons/a/a7/Irissetosa1.jpg",
    "versicolor": "https://upload.wikimedia.org/wikipedia/commons/4/41/Iris_versicolor_3.jpg",
    "virginica": "https://upload.wikimedia.org/wikipedia/commons/f/f8/Iris_virginica_2.jpg"
}

# Species descriptions (measurement ranges)
species_descriptions = {
    "setosa": "Sepal length: 4.3–5.8 cm\nSepal width: 2.3–4.4 cm\nPetal length: 1.0–1.9 cm\nPetal width: 0.1–0.6 cm",
    "versicolor": "Sepal length: 4.9–7.0 cm\nSepal width: 2.0–3.4 cm\nPetal length: 3.0–5.1 cm\nPetal width: 1.0–1.8 cm",
    "virginica": "Sepal length: 4.9–7.9 cm\nSepal width: 2.2–3.8 cm\nPetal length: 4.5–6.9 cm\nPetal width: 1.4–2.5 cm"
}

@st.cache_data
def get_image(species):
    return species_images[species]


# Streamlit UI
st.title("🌸 Iris Flower Classifier")
st.write("Enter flower measurements to predict the species:")

# Use a form so prediction runs only when you click "Predict"
with st.form("iris_form"):
    sepal_length = st.slider("Sepal Length (cm)", 4.0, 8.0, 5.0)
    sepal_width = st.slider("Sepal Width (cm)", 2.0, 4.5, 3.0)
    petal_length = st.slider("Petal Length (cm)", 1.0, 7.0, 4.0)
    petal_width = st.slider("Petal Width (cm)", 0.1, 2.5, 1.0)
    submit = st.form_submit_button("Predict")

if submit:
    prediction = model.predict([[sepal_length, sepal_width, petal_length, petal_width]])
    predicted_species = iris.target_names[prediction[0]]

    st.subheader("🌼 Predicted Species:")
    st.header(predicted_species.capitalize())

    # Show image + description side by side
    col1, col2 = st.columns([2, 1])
    with col1:
        st.image(
            get_image(predicted_species),
            
            use_container_width=True
        )
        st.markdown(
    f"<p style='font-size:20px; text-align:center;'>Iris {predicted_species.capitalize()}</p>",
    unsafe_allow_html=True
)

    with col2:
        st.markdown("**Typical Measurement Ranges:**")
        st.text(species_descriptions[predicted_species])