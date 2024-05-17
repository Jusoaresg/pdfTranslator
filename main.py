import translate
import io
import os
from pdf2docx import Converter
import fitz
import time 
import threading

threadsToUse = 6
checkForErrors = input("Deseja verificar por erros ? (Deixe vazio caso queira): ")

pdfFile = "sample.pdf"
pdfFile = input("Coloque o caminho para o arquivo pdf para ser traduzido: ")

errors = []

def countPages(pdfFile):
    pdf = fitz.open(pdfFile)
    pages = len(pdf)
    pdf.close()
    return pages

def checkErrors(start, end):
    cv = Converter(pdfFile)

    try:
        for i in range(int(start), int(end)):
            print(f'[PAGE INFO] Page: {i}')

            #n = f'out{i}.docx'
            output_stream = io.BytesIO()

            try:
                #cv.convert(n, start=i, end=i+1)
                cv.convert(output_stream, start=i, end=i+1)
                #os.remove(n)
            except Exception as ex:
                print("Error")
                errors.append(f'Error: {ex} in page {i}')
            finally:
                output_stream.close()

    except Exception as ex:
        print("Erro no for")
    finally:
        cv.close()


if(checkForErrors == ""):

    threads = []
    pages = countPages(pdfFile)
    pagesDivided = pages/threadsToUse
    for i in range(threadsToUse):
        if (i == 0): 
            start = 0;
            end = pagesDivided

        else:
            start = i * pagesDivided
            end = (i + 1) * pagesDivided

        thread = threading.Thread(target=checkErrors, args=(start, end))
        thread.start()
        threads.append(thread)

    for key, thread in enumerate(threads):
        thread.join()

    print(errors)

if len(errors) == 0:
    cv = Converter(pdfFile)
    cv.convert("output.docx")
    cv.close()

translate.translateDocx()
