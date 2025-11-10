# Import the matplotlib.pyplot submodule and name it plt
import matplotlib.pyplot as plt
import pandas as pd

seattle_weather=pd.read_csv("seattle_weather.csv")
austin_weather=pd.read_csv("austin_weather.csv")
seattle_weather["MONTH"] = seattle_weather["MONTH"].astype(str)
austin_weather["MONTH"] = austin_weather["MONTH"].astype(str)
# Use the "ggplot" style and create new Figure/Axes
plt.style.use("ggplot")
fig,ax=plt.subplots()
ax.plot(seattle_weather["MONTH"], seattle_weather["MLY-TAVG-NORMAL"])
plt.show()
# Use the "Solarize_Light2" style and create new Figure/Axes
plt.style.use('Solarize_Light2')
fig,ax=plt.subplots()
ax.plot(austin_weather["MONTH"], austin_weather["MLY-TAVG-NORMAL"])
plt.show()