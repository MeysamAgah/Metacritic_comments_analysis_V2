

def prepare_text_from_comments(data:dict):
    all_comments = ""
    for i in range(len(data['quotes'])):
        all_comments += f"Review #{i+1}:\n"
        all_comments += f"""
'quote: {data['quotes'][i]}'
'score': {data['scores'][i]}
'date': {data['dates'][i]}
'author': {data['authors'][i]}
"""
        all_comments +="\n------------------------------------------------------------\n"

    return all_comments
