from nltk.chat.util import Chat, reflections

#construisons le dialogue 
pairs =[
    ['je m\'appele (.*)', ['Hello ! %1, comment vas tu?']],
    ['(hi|hello|hey|holla|hola)', ['Hey there !', 'Hi there !', 'Hey !']],
    ['(.*) et toi ?', ['je me prénom kristal']],
    ['(.*) d\'ou viens-tu ?', ['j\'ai été conçu au Gabon plus précisement a Libreville']],
    ['(.*) ta crée ?', ['le Master Lipakumu m\'a crée en utilisant python et le package nltk ']],
    ['(.*)aider(.*)',['comment puis-je vous aider?']]
]


chat = Chat(pairs, reflections)

chat.converse()