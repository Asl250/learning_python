# or  and  not

# temp = 25
# is_raining = False
#
# if temp > 35 or temp < 0 or is_raining:
#     print('Outdoor event cancelled')
# else:
#     print('Outdoor event is still scheduled')


temp = 17
is_sunny = False

if temp >= 25 and is_sunny:
    print('its hot outside')
    print('its sunny')
elif temp <= 0 and is_sunny:
    print('its cold outside')
    print('its sunny')
elif 28 > temp > 0 and is_sunny :
    print('its warm outside')
    print('its sunny')
elif temp >= 25 and not is_sunny:
        print('its hot outside')
        print('its cloudy')
elif temp <= 0 and not is_sunny:
        print('its cold outside')
        print('its cloudy')
elif 28 > temp > 0 and not is_sunny:
        print('its warm outside')
        print('its cloudy')
