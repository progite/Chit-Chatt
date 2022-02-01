from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer

bot = ChatBot('Chatter',
            logic_adapters=[{
            'import_path': 'chatterbot.logic.BestMatch',
            'default_response': 'Brrr. I am not smart enough to understand that',
            'maximum_similarity_threshold': 0.90
        }],
            read_only = True,
            preprocessors=['chatterbot.preprocessors.clean_whitespace',
                        'chatterbot.preprocessors.unescape_html',
                        'chatterbot.preprocessors.convert_to_ascii']
                        )


training_data = open('training_data.txt',encoding = 'utf8').read().splitlines()
trainer = ListTrainer(bot)
trainer.train(training_data)
trainer.train("chatterbot.corpus.english")
trainer.train("chatterbot.corpus.english.conversations" )
name = input('Enter Your Name: ')

print ('Start Conversation. Print bye/Bye to leave convo')

while True:

    request = input(name+': ')

    if request=="Bye" or request=='bye':
        print('Bot: Bye')
        break
    else:
        response=bot.get_response(request)
        print('Chatter: ', response)
