# import matplotlib.pyplot as plt
# import numpy as np

# x = np.linspace(0, 1)
# plt.plot(x, np.exp(x))
# plt.xlabel(r'$0 \leq x < 1$')
# plt.ylabel(r'$e^x$')
# plt.title('Exponential function')
# plt.show()

#%%

from datetime import datetime
from swmfpy.web import get_omni_data
import matplotlib.pyplot as plt
import numpy as np

'''
Description: This code plots the Al on my birthday
'''

start_time = datetime(1999, 2, 9) # YYYY, MM, DD
end_time = datetime(1999, 2, 10) # YYYY, MM, DD
data = get_omni_data(start_time, end_time)
data.keys()


al = data['al']
birthday = data['times']
plt.plot(birthday, al)
plt.xlabel('Time (MM-DD HR)')
plt.xticks(rotation=45)
plt.ylabel('AL')
plt.title('AL on Feb 9, 1999')
plt.show()