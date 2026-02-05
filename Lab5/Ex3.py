responses = [5, 7, 3, 8]
respondent_ids = (1012, 1035, 1021, 1053)

survery_dict= dict(zip(respondent_ids,responses))
print("Survey responses with respondent IDs:", survery_dict)

print(f"respondent {respondent_ids[2]} gave a response of {survery_dict[respondent_ids[2]]}")