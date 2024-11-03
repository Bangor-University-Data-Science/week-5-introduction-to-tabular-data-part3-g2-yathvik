def answer_conceptual_questions():
    answer_dict = {
        "Q1": "A",  
        "Q2": "B",  
        "Q3": "C",  
        "Q4": "A", 
        "Q5": "A"   
    }
    return answer_dict

print("Answers to the multiple-choice questions.")
for k,v in answer_conceptual_questions().items():
    print(f"{k}: {v}")
