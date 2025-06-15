from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die

# visualize the results
dice = Die()
results = []
for x in range(100):
    result= dice.roll()
    results.append(result) # this result variable is every time getting stored in results through appends 

print(result)

frequencies = []

for value in range(1, dice.num_sides+1):
    frequency = results.count(value)
    frequencies.append(frequency)


#print(frequencies)
x_values = list(range(1, dice.num_sides+1))
data = [Bar(x=x_values, y = frequencies)]

x_axis = {'title': 'Result'}
y_axis = {'title': 'Frequency of Result'}

layout = Layout(title='Result of rolling dice', xaxis= x_axis, yaxis= y_axis)

offline.plot({'data':data, 'layout': layout}, filename= 'd6.html')
