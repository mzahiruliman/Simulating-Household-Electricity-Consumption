# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def simulateOld():
    # OLD SIMULATION
    # Initialize variables
    day = []
    energyPerDay = []
    totEnPerMonth = 0
    j = 0
    for i in range(30):
        j += 1
        day.append(j)
        totEn = totalEnergyOld()
        energyPerDay.append(totEn)
        totEnPerMonth += totEn

    bill = calculateBill(totEnPerMonth)
    print("Total energy used for a month is {:.2f} kWh".format(totEnPerMonth))
    print("The total bill is RM {:.2f}\n".format(bill))
    average(totEnPerMonth)

    """ #UNCOMMENT IF WANT TO USE#
    #Create dataframe to display energy utilization patterns for 30 days
    total = {'Day':day,'energyPerDay':energyPerDay}
    df = pd.DataFrame(total)
    print(df.to_string(index=False))
    """
    # Display Energy vs Day graph
    x = day
    y = energyPerDay

    plt.plot(x, y)
    plt.title('Energy vs Day (Old)')
    plt.xlabel('Day')
    plt.ylabel('Energy (kWh)')
    plt.show()


def simulate():
    # NEW SIMULATION
    # Initialize variables
    day = []
    energyPerDay = []
    totEnPerMonth = 0
    j = 0

    # In sequence: weekends, weekday, weekends etc for 30 days
    for i in range(2):
        j += 1
        day.append(j)
        totEn = totalEnergyWeekend()
        energyPerDay.append(totEn)
        totEnPerMonth += totEn
    for i in range(5):
        j += 1
        day.append(j)
        totEn = totalEnergyWeekday()
        energyPerDay.append(totEn)
        totEnPerMonth += totEn
    for i in range(2):
        j += 1
        day.append(j)
        totEn = totalEnergyWeekend()
        energyPerDay.append(totEn)
        totEnPerMonth += totEn
    for i in range(5):
        j += 1
        day.append(j)
        totEn = totalEnergyWeekday()
        energyPerDay.append(totEn)
        totEnPerMonth += totEn
    for i in range(2):
        j += 1
        day.append(j)
        totEn = totalEnergyWeekend()
        energyPerDay.append(totEn)
        totEnPerMonth += totEn
    for i in range(5):
        j += 1
        day.append(j)
        totEn = totalEnergyWeekday()
        energyPerDay.append(totEn)
        totEnPerMonth += totEn
    for i in range(2):
        j += 1
        day.append(j)
        totEn = totalEnergyWeekend()
        energyPerDay.append(totEn)
        totEnPerMonth += totEn
    for i in range(5):
        j += 1
        day.append(j)
        totEn = totalEnergyWeekday()
        energyPerDay.append(totEn)
        totEnPerMonth += totEn
    for i in range(2):
        j += 1
        day.append(j)
        totEn = totalEnergyWeekend()
        energyPerDay.append(totEn)
        totEnPerMonth += totEn

    bill = calculateBill(totEnPerMonth)
    print("Total energy used for a month is {:.2f} kWh".format(totEnPerMonth))
    print("The total bill is RM {:.2f}\n".format(bill))
    average(totEnPerMonth)

    """ #UNCOMMENT IF WANT TO USE#
    #Create dataframe to display energy utilization patterns for 30 days
    total = {'Day':day,'energyPerDay':energyPerDay}
    df = pd.DataFrame(total)
    print(df.to_string(index=False))
    """
    # Display Energy vs Day graph
    x = day
    y = energyPerDay

    plt.plot(x, y)
    plt.title('Energy vs Day (New)')
    plt.xlabel('Day')
    plt.ylabel('Energy (kWh)')
    plt.show()

# Function to preview appliances time usage and its calculations assuming all the appliances usage are in the range of 0-24 hours


def totalEnergyOld():
    df = pd.read_excel('devicePower.xlsx', sheet_name='deviceWeekend')
    randVar = []
    randVar = np.random.randint(0, 24, 16)
    df = df.assign(time=randVar)
    totalEnergy, energyList = calculateEnergy(df)
    df = df.assign(energy=energyList)
    return totalEnergy

# Function to consolidate all appliances time usage probabilities during weekdays


def totalEnergyWeekday():
    df = pd.read_excel('devicePower.xlsx', sheet_name='deviceWeekday')
    randVar = []

    randVar.append(np.random.randint(0, 7))
    randVar.append(np.random.randint(0, 7))
    randVar.append(np.random.randint(0, 24))
    randVar.append(24)
    randVar.append(np.random.randint(0, 8))
    randVar.append(np.random.randint(0, 5))
    randVar.append(np.random.randint(0, 5))
    randVar.append(np.random.randint(0, 8))
    randVar.append(np.random.randint(0, 24))
    randVar.append(np.random.randint(0, 6))
    randVar.append(24)

    df = df.assign(time=randVar)
    totalEnergy, energyList = calculateEnergy(df)
    df = df.assign(energy=energyList)
    return totalEnergy

# Function to consolidate all appliances time usage probabilities during weekends


def totalEnergyWeekend():
    df = pd.read_excel('devicePower.xlsx', sheet_name='deviceWeekend')
    randVar = []

    randVar.append(np.random.randint(0, 12))
    randVar.append(np.random.randint(0, 7))
    randVar.append(np.random.randint(0, 24))
    randVar.append(np.random.uniform(0, 1))
    randVar.append(24)
    randVar.append(np.random.randint(0, 2))
    randVar.append(np.random.randint(0, 8))
    randVar.append(np.random.randint(0, 12))
    randVar.append(np.random.randint(0, 12))
    randVar.append(np.random.randint(0, 24))
    randVar.append(np.random.randint(0, 24))
    randVar.append(np.random.randint(0, 12))
    randVar.append(24)
    randVar.append(np.random.randint(0, 2))
    randVar.append(np.random.randint(0, 2))
    randVar.append(np.random.randint(0, 2))

    df = df.assign(time=randVar)
    totalEnergy, energyList = calculateEnergy(df)
    df = df.assign(energy=energyList)
    return totalEnergy

# Function to calculate the energy using the data


def calculateEnergy(df):
    energyList = []
    totalEnergy = 0
    for i in range(len(df)):
        energy = df['power_max'].iloc[i] * df['time'].iloc[i]
        energyList.append(energy)
        totalEnergy += energy
    totEnInKwh = totalEnergy/1000
    return totEnInKwh, energyList

# Function to calculate the average daily electrical bills and energy consumption


def average(energy):
    aver = energy/30
    bill = calculateBill(aver)
    print("Average total energy per day used is {:.2f} kWh".format(aver))
    print("Average total bill per day is RM {:.2f}\n".format(bill))

# Function to calculate the monthly bills


def calculateBill(energy):
    rate = 0
    totalCharge = 0
    if energy == 0:
        totalCharge = 3
        return totalCharge
    elif energy < 201:
        rate1 = 0.2180
        limitEnergyPerBlock1 = 200
        block = energy * rate1

    elif energy > 200 and energy < 301:
        rate1 = 0.2180
        rate2 = 0.3340
        limitEnergyPerBlock1 = 200
        energyremaining = energy - limitEnergyPerBlock1
        block = limitEnergyPerBlock1 * rate1 + (energyremaining) * rate2

    elif energy > 300 and energy < 601:
        rate1 = 0.2180
        rate2 = 0.3340
        rate3 = 0.5160
        limitEnergyPerBlock1 = 200
        limitEnergyPerBlock2 = 100
        energyremaining = energy - limitEnergyPerBlock1 - limitEnergyPerBlock2
        block = limitEnergyPerBlock1 * rate1 + \
            limitEnergyPerBlock2 * rate2 + energyremaining * rate3

    elif energy > 600 and energy < 901:
        rate1 = 0.2180
        rate2 = 0.3340
        rate3 = 0.5160
        rate4 = 0.5460
        limitEnergyPerBlock1 = 200
        limitEnergyPerBlock2 = 100
        limitEnergyPerBlock3 = 300
        energyremaining = energy - limitEnergyPerBlock1 - \
            limitEnergyPerBlock2 - limitEnergyPerBlock3
        block = limitEnergyPerBlock1 * rate1 + limitEnergyPerBlock2 * \
            rate2 + limitEnergyPerBlock3 * rate3 + energyremaining * rate4

    elif energy > 900:
        rate1 = 0.2180
        rate2 = 0.3340
        rate3 = 0.5160
        rate4 = 0.5460
        rate5 = 0.5710
        limitEnergyPerBlock1 = 200
        limitEnergyPerBlock2 = 100
        limitEnergyPerBlock3 = 300
        limitEnergyPerBlock4 = 300
        energyremaining = energy - limitEnergyPerBlock1 - \
            limitEnergyPerBlock2 - limitEnergyPerBlock3 - limitEnergyPerBlock4
        block = limitEnergyPerBlock1 * rate1 + limitEnergyPerBlock2 * rate2 + \
            limitEnergyPerBlock3 * rate3 + limitEnergyPerBlock4 * \
            rate4 + energyremaining * rate5
    return block


# calling simulate functions to start the simulation
print("SIMULATING MODEL BEFORE IN DEPTH ASSUMPTIONS ARE MADE: ")
simulateOld()
print("SIMULATING MODEL AFTER IN DEPTH ASSUMPTIONS ARE MADE: ")
simulate()
