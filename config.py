# CONSTANTS, DO NOT EDIT
tg_bot_token = '5752939129:AAEgzu1dum8dcjw1oGe9ncEtuCSQeF34Ppo'
start = '/start'
cancel = '/cancel'
commands = [start, cancel]
email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,15}\b'

# EDIT MESSAGES HERE

# FIRST MESSAGE WHEN USER STARTS A CONVERSATION (In addition to a message 2 buttons appear)
intro_message = '''Hi!

Here is Unbench helper :) 
What questions do you have?'''

# TEXT INSIDE FIRST BUTTON
main_option_question = 'Ask a question'

# TEXT INSIDE SECOND BUTTON
main_option_website = 'Back to the platform'

# WEBSITE (Attached to second button)
website_url = 'https://unbench.us/'

# ASK USER TO PROVIDE A QUESTION
ask_question_message = 'Please write your question and our manager will contact you ASAP 🙂'

# ASK WHERE A USER WANTS TO GET ANSWERED VIA TELEGRAM
ask_source_message = "We'd love to hear from you! Where would you like us to respond?"

# BUTTON 1 TEXT, WHEN USER WANTS TO GET ANSWERED VIA TELEGRAM
communication_option_tg = 'Telegram'

# BUTTON 1 TEXT, WHEN USER WANTS TO GET ANSWERED VIA EMAIL
communication_option_email = 'Email'

# MESSAGE TO ASK AN EMAIL ADDRESS
ask_email_message = 'Whats your email?'

# MESSAGE IF EMAIL WAS INCORRECT
invalid_email_message = 'Oooops. Looks like this is invalid email. Try again'

# CALENDLY LINK ATTACHED TO THE LAST MESSAGE
calendly_url = 'https://calendly.com/alyona-honcharenko/35min?month=2023-03'

# FINAL MESSAGE THAT BOT SENDS WHEN THE QUESTION IS RECEIVED
bye_message = f'''Thanks for your question. 
Lets win more deals,
Cheers

P.S.: Still a bit confused?🤓 Book a call with the Head of the Platform Alyona - <a href="{calendly_url}">click to book a tour</a>.\n\nTo start again click /start'''

# IN ADDITION TO THE FINAL MESSAGE OR WHEN USER USES A /cancel COMMAND BOT SEND THIS MESSAGE TO SUGGEST USER START THE CONVERSATION AGAIN
cancel_message = 'Good. Click /start if you want to resume the conversation'