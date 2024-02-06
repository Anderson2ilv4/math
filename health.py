def health_care(height, weight, age):
    imc = weight / height**2
    water_drink = (35 * weight) / 1000
    print('ICM classification'.center(55))
    print('''-Under weight: IMC lass than 18,5
            \r-Normal weight (Health): IMC between 18,5 and 24,9
            \r-Overweight: IMC between 25 and 29,9
            \r-Obesity Class I: IMC between 30 and 34,9
            \r-Obesity Class II: IMC between 35 and 39,9
            \r-Obesity Class III (Morbid obesity): IMC equal or more than 40\n''')
    if age < 14:
        sleep_time = 'You should sleep more than 8 hours a day!'
    elif 14 <= age <= 17:
        sleep_time = 'You should sleep 8 to 10 hours a day!'
    elif 18 <= age <= 64:
        sleep_time = 'You should sleep 7 to 9 hours a day!'
    else:
        sleep_time = 'You sould sleep 7 to 8 hours a day!'
    return f'''You are {height}m tall, have {weight}kg and you are {age} years old
    \rYour IMC = {imc:.2f}
    \rYou shoul drink {water_drink}l of water a day'''