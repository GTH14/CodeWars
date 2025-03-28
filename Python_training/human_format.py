import random as r

def format_duration(seconds):
    if seconds == 0:
        return "now"
    else:
        transform_list = [365*24*3600, 24*3600, 3600, 60]
        single_list = [" year", " day", " hour", " minute", " second"]
        multiple_list = [" years", " days", " hours", " minutes", " seconds"]
        remain_seconds = seconds
        formatted_time = []
        for format_index in range(4):
            value = remain_seconds//transform_list[format_index]
            remain_seconds = remain_seconds%transform_list[format_index]
            if value == 0:
                pass
            elif value == 1:
                formatted_time.append(str(value) + single_list[format_index])
            else:
                formatted_time.append(str(value) + multiple_list[format_index])
        
        if remain_seconds == 1:
            formatted_time.append(str(remain_seconds) + single_list[format_index+1])
        elif remain_seconds > 1:
            formatted_time.append(str(remain_seconds) + multiple_list[format_index+1])
        result = ""
        if len(formatted_time) == 1:
            return formatted_time[0]
        for new_index in range(len(formatted_time)):
            if new_index==len(formatted_time)-1:
                result += " and "+ formatted_time[new_index]
                continue
            elif new_index==0:
                result += formatted_time[new_index]
                continue
            result += ", " + formatted_time[new_index]
        return result
    
if __name__ == "__main__":
    for i in range(10):
        seconds = r.randint(0, 1000000000)
        print(seconds)
        print(format_duration(seconds))