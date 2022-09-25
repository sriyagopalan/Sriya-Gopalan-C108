import pandas as pandas
import plotly.figure_factory as ff 

df = pd.read_csv('Sriya-Gopalan-C108-BellCurve/csv/data.csv')
figure = ff.createdistplot([df['Rating'].tolost()], ['Rating'], show_hist = False,)
figure.write_html('Sriya-Gopalan-C108-BellCurve/index.html', auto_open = True)