import streamlit as st

st.title("Vorhersage der deutschen CO2 Emissionen")

"Autor: Jan Reinartz"

from scipy.stats import linregress
st.subheader("Vorhersage")

years = [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020]
emissions_per_year = [10.3, 10.0, 10.1, 10.2, 9.7, 9.7, 9.7, 9.5, 9.1, 8.5, 7.7]

regression_result = linregress(years, emissions_per_year)
scipy_slope = regression_result.slope
scipy_intercept = regression_result.intercept

def scipy_model(desired_year):
    model_result = scipy_slope * desired_year + scipy_intercept
    return model_result

desired_year = st.number_input('Jahr', value=2022)

prediction = scipy_model(desired_year)
prediction_rounded = round(prediction, 2)

"Die Vorhersage der Emissionen für das ausgewählte Jahr ist:"

st.write(prediction_rounded)

"Tonnen pro Kopf pro Jahr"
#%%

st.title("Test Nummer 2")

"Autor: Jan Reinartz"

from scipy.stats import linregress
st.subheader("German Military expenditure as a share of GDP")

years = [1950, 1960, 1970, 1980, 1990, 2000, 2010, 2020]
spendings = [3.97, 3.77, 3.01, 2.96, 2.52, 1.36, 1.27, 1.40]

regression_result = linregress(years, spendings)
scipy_slope = regression_result.slope
scipy_intercept = regression_result.intercept

def scipy_model(desired_year):
    model_result = scipy_slope * desired_year + scipy_intercept
    return model_result

desired_year = st.number_input('Jahr', value=1990)

prediction = scipy_model(desired_year)
prediction_rounded = round(prediction, 2)

"Die Vorhersage der Ausgaben für das ausgewählte Jahr ist:"

st.write(prediction_rounded)

"% vom GDP"