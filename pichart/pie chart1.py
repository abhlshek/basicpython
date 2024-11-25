import matplotlib.pyplot as plt
labels=['category A','category B','category C','category D']
sizes=[15,30,45,10]
plt.pie(sizes,labels=labels,autopct='1%.1f%%',startangle=140)
plt.title('my pie chart')
plt.show()
