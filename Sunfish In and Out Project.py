name =input('What is your Name? ')
print ('Hi ' + name)
print('Welcome to SylaDH Productive Hour Calculator')
print('This program is made as a compliment for Sunfish Flexi hour schedule')
print ('Please use Yes or No to answer the following questions')

print('Did you go to work on the following days? ')
monday = input ('Monday? ')
if monday == 'Yes':
        mondayhr = input('How many productive hours have you worked? ')
else:
    mondayhr = 0

tuesday = input('Tuesday? ')
if tuesday == 'Yes':
        tuesdayhr = input ('How many productive hours have you worked? ')
else:
        tuesdayhr = 0

wednesday = input('Wednesday? ')
if wednesday == 'Yes':
        wednesdayhr = input ('How many productive hours have you worked? ')
else:
        tuesdayhr = 0

thursday = input('Thursday? ')
if thursday == 'Yes':
        thursdayhr = input ('How many productive hours have you worked? ')
else:
        tuesdayhr = 0

friday = input('Friday? ')
if friday == 'Yes':
        fridayhr = input('How many productive hours have you worked? ')
else:
        fridayhr = 0

mhr = int(mondayhr)
tuehr = int(tuesdayhr)
wedhr = int(wednesdayhr)
thuhr = int(thursdayhr)
frihr = int(fridayhr)

totalhrs = mhr + tuehr + wedhr + thuhr +frihr
requiredhr = input('How many hours are you required to work? ')
rhr = int(requiredhr)
lackinghr = rhr - totalhrs
if lackinghr > 0:
    print ('You still need to work for ', lackinghr, 'hr')
else:
    print ('You can go home now')
