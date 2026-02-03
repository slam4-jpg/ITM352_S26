# Try to append to a tuple. It wont work!
#Name: Sidney Lam
#Date: February 2, 2026

survery_respondents = (1012, 1035, 1021, 1053 )
print("Original survey respondents tuple:", survery_respondents)    
# survery_respondents.append(1054)  # This will cause an error
survey_respondents = survery_respondents + (1054,)
print("After adding 1054:", survey_respondents)