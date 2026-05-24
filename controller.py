import time
import flet as ft
import model as md

class SpellChecker(object):

    def __init__(self, view):
        self._multiDic = md.MultiDictionary()
        self._view = view

    def handleSentence(self, e):
        self._view._lv.controls.clear()
        language= self._view._lingua.value
        modality = self._view._modalita.value
        txtIn = self._view._txtIn.value

        if txtIn == "":
            self._view._lv.controls.append(ft.Text("Errore, inserisci un testo"))
            self._view.update()

        if language is None:
            self._view._lv.controls.append(ft.Text("Errore, seleziona una lingua"))
            self._view.update()

        if modality is None:
            self._view._lv.controls.append(ft.Text("Errore, seleziona una modalità"))
            self._view.update()

        txtIn = replaceChars(txtIn.lower())
        language = replaceChars(language.lower())
        words = txtIn.split()
        paroleErrate = " - "

        match modality:

            case "Default":
                t1 = time.time()
                parole = self._multiDic.searchWord(words, language)
                for parola in parole:
                    if not parola.corretta:
                        paroleErrate = paroleErrate + str(parola) + " - "
                t2 = time.time()
                self._view._lv.controls.append(ft.Text(f"Frase inseirta: {txtIn}\n"
                                                        f"Parole errate: {paroleErrate}\n"
                                                        f"Tempo della ricerca: {t2 - t1}"))

                self._view._txtIn.value = ""
                self._view.page.update()

            case "Linear":
                t1 = time.time()
                parole = self._multiDic.searchWordLinear(words, language)
                for parola in parole:
                    if not parola.corretta:
                        paroleErrate = paroleErrate + str(parola) + " "
                t2 = time.time()
                self._view._lv.controls.apppend(ft.Text(f"Frase inseirta: {txtIn}\n"
                                                        f"Parole errate: {paroleErrate}\n"
                                                        f"Tempo della ricerca: {t2 - t1}"))

                self._view._txtIn.value = ""
                self._view.page.update()

            case "Dichotomic":
                t1 = time.time()
                parole = self._multiDic.searchWordDichotomic(words, language)
                for parola in parole:
                    if not parola.corretta:
                        paroleErrate = paroleErrate + str(parola) + " - "
                t2 = time.time()
                self._view._lv.controls.apppend(ft.Text(f"Frase inserita: {txtIn}\n"
                                                        f"Parole errate: {paroleErrate}\n"
                                                        f"Tempo della ricerca: {t2 - t1}"))
                self._view._txtIn.value = ""
                self._view.page.update()

            case _:
                return None

    def printMenu(self):

        print("______________________________\n" +
              "      SpellChecker 101\n"+
              "______________________________\n " +
              "Seleziona la lingua desiderata\n"
              "1. Italiano\n" +
              "2. Inglese\n" +
              "3. Spagnolo\n" +
              "4. Exit\n" +
              "______________________________\n")

def replaceChars(text):
    chars = "\\`*_{}[]()>#+-.!$?%^;,=_~"
    for c in chars:
        text = text.replace(c, "")
    return text
