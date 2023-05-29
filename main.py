from translate import Translator
from plyer import notification

translator = Translator(to_lang="tr")
inputText = input("the text you want to translate : ")

translation = translator.translate(inputText)

notification.notify(
    title="Translate",
    message=translation,
    timeout=10,
    toast=False
)
