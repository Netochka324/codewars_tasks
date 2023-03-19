def format_duration(seconds):
    time = []
    if seconds == 0:
        return 'now'
    else:
        time_dict = {' second': seconds%60, ' minute': (seconds//60)%60, ' hour': (seconds//3600)%24,
                     ' day': (seconds//(24*60*60))%365, ' year': seconds//(365*24*60*60)}
        for i in reversed(time_dict.keys()):
            if time_dict[i] == 1:
                time.append(str(time_dict[i]) + i)
            elif time_dict[i]:
                time.append(str(time_dict[i]) + i + 's')
        return ', '.join(time[:-1]) + ' and ' + time[-1] if len(time) > 1 else time[0]


print(format_duration(366254))
print(format_duration(1))  # == "1 second")
print(format_duration(62))  # == "1 minute and 2 seconds")
print(format_duration(120))  # == "2 minutes")
print(format_duration(3600))  # == "1 hour")
print(format_duration(3662))  # == "1 hour, 1 minute and 2 seconds")
