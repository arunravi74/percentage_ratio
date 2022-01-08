#Function to Calculate Percentage
def score(correct_answer,candidate_response):
    correct_answer = correct_answer.split(" ")
    candidate_response = candidate_response.split(" ")
    answer_dict = {}
    response_dict = {}    
    for i in (correct_answer):
        i = i.strip(".,")
        if not i.isnumeric():
            if len(i) > 6:
                answer_dict[i] = 3
            elif 7>len(i)>4  :
                answer_dict[i] = 1     
        else:
            answer_dict[i] = 4
    for j in candidate_response:
        j = j.strip(".,")
        if not j.isnumeric():
            if len(j) > 6:
                response_dict[j] = 3
            elif 7>len(j)>4  :
                response_dict[j] = 1     
        else:
            response_dict[j] = 4
    #Sum of points for each word in the Correct Response String.
    maximum_possible_score = sum(answer_dict.values())
    #Sum of points for each word in the Candidate Response.
    points_scored = sum(response_dict.values())
    #To find Percentage
    percentage_ratio = (points_scored/maximum_possible_score) * 100

    return percentage_ratio

out = score("There are twenty-four hours in a day, 30 days in a month, and 12 months in the calendar year.","There are Twenty-Four hours in a day. A year has 14 months.")
print (f"percentage_ratio is {out:.2f}%")