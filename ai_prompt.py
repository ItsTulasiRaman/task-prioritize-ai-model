from bardapi import Bard

token = 'XAi_7vf1VIgmqHenrw6mtVR8Y3O2XsNjVVsZxAr-GVxWbGkpbvMrzd-1ckq6Yz1Y66anFg.'
bard = Bard(token=token)
def generate_prompt():
    inputText = "{Meet George, Buy egg, SCM assignment tonight}. From the list of above todo important tasks orderwise. Display all sorted task within an array format [task1,task2]"
    content = bard.get_answer(inputText)['content']
    content = content.split('```')[1]
    return content

def input_text_update(textPrompt):
    inputText = textPrompt + ". From the list of above todo important tasks orderwise. Display all sorted task within an array format [task1,task2]"
    content = bard.get_answer(inputText)['content']
    content = content.split('```')[1]
    return content.split(',')

#print(generate_prompt())