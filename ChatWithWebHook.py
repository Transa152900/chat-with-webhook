from dhooks import Webhook, Embed

eort = (input("Отправить сообщение Панелью(E) или отправить сообщением (T)"))
if eort == ("T"):
	webhook = (input("Введите URL вебхука: "))
	hook = Webhook(webhook)
	for i in range(999):
		text = (input("Введите сообщение: "))
		hook.send(text)
if eort == ("E"):
	webhook = (input("Введите URL вебхука: "))
	hook = Webhook(webhook)
	for i in range(999):
		text = (input("Введите сообщение: "))
		embed = Embed(
    		description=text,
    		timestamp='now'  # sets the timestamp to current time
    		)
		hook.send(embed=embed)



