##import codecademylib
import numpy as np
from matplotlib import pyplot as plt

survey_responses = ['Ceballos', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos','Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos', 
'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos', 'Ceballos', 'Ceballos', 'Ceballos',
'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Ceballos',
'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Ceballos']

total_ceballos = survey_responses.count('Ceballos')
print(total_ceballos)
total_survey_responses = len(survey_responses)
percentage_ceballos = (float(total_ceballos)/total_survey_responses * 100)
print(percentage_ceballos)

possible_surveys = np.random.binomial(total_survey_responses, 0.54, size=10000) / float(total_survey_responses)
print(possible_surveys)

plt.hist(possible_surveys, bins=20, range=(0, 1))
plt.xlabel("Possible Surveys")
plt.ylabel("Survey Responses")
plt.title("Possible Purveys per Survey Responses")

ceballos_loss_surveys = np.mean(possible_surveys < 0.5 )
print(ceballos_loss_surveys)

large_survey = np.random.binomial(7000.0, 0.54, size=10000) / float(7000)

ceballos_loss_new = np.mean(large_survey < 0.5 )
print(ceballos_loss_new)

plt.hist(large_survey, bins=20, range=(0, 1))
plt.show()




