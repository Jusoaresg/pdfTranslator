from deep_translator import GoogleTranslator
import docx

def checkInteger(string):
    try:
        int(string)
        return True
    except ValueError:
        return False

def translateDocx():
    doc = docx.Document("output.docx")

    print(len(doc.paragraphs))



    for key, i in enumerate(doc.paragraphs):

        if(i.text != "" and checkInteger(i.text) == False):
            print(key)
            #print(i.text)
            translated = GoogleTranslator(source="en", target="pt").translate(i.text)
            i.text = translated

    doc.save("outputTranslated.docx")
