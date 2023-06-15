from bardapi import Bard

token = 'XAi_7vf1VIgmqHenrw6mtVR8Y3O2XsNjVVsZxAr-GVxWbGkpbvMrzd-1ckq6Yz1Y66anFg.'
bard = Bard(token=token)
def generate_prompt():
    inputText = "{Meet George, Buy egg, SCM assignment tonight}. \nFrom the above todo sort based on the important tasks. Display only the sorted task within an array format [task1,task2], without any further explanation."
    content = bard.get_answer(inputText)['content']
    content = content.split('```')[1]
    return content

def input_text_update(textPrompt):
    inputText = textPrompt + "\nFrom the above todo sort based on the important tasks. Display only the sorted task within an array format [task1,task2], without any further explanation"
    content = bard.get_answer(inputText)['content']
    content = content.split('```')[1]
    return content.split(',')

#print(generate_prompt())