import pygal
from die import Die
#create a D6 and a D10 dice
die_1=Die()
die_2=Die()


#make some rolls and store result in list
results=[]
for roll_num in range(5000):
    result=die_1.roll()+die_1.roll()
    results.append(result)

#analize the results
frequencies = []
max_result=die_1.num_sides+die_2.num_sides
for value in range(2,max_result+1):
    frequency=results.count(value)
    frequencies.append(frequency)

#visualize the result
hist=pygal.Bar()
hist.title="Results of rolling two D6 dice 1000 times"
hist.x_labels=['2','3','4','5','6','7','8','9','10','11','12','13','14','15','16']
hist.x_title="Result"
hist.y_title="Frequency of Result"

hist.add('D6+D10',frequencies)
hist.render_to_file('Python game/die_visual3.svg')