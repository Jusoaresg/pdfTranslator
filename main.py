import multiprocessing
from pdf2docx.converter import cpu_count
import translate
<<<<<<< Updated upstream
import os
=======
import io
>>>>>>> Stashed changes
from pdf2docx import Converter
import fitz
import threading
from tqdm import tqdm

class Colors:
    RED = "\033[91m"
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    ENDTEXT = '\033[0m'


threadsToUse = 6
checkForErrors = input("Deseja verificar por erros ? (Deixe vazio caso queira): ")

pdfFile = "sample.pdf"
pdfFile = input("Coloque o caminho para o arquivo pdf para ser traduzido: ")

#docxFile = "out.docx"

errors = []

def countPages(pdfFile):
    pdf = fitz.open(pdfFile)
    pages = len(pdf)
    pdf.close()
    return pages

def checkErrors(start, end):
    for i in range(int(start), int(end)):
        print(f'[PAGE INFO] Page: {i}')

<<<<<<< Updated upstream
        cv = Converter(pdfFile)
        n = f'out{i}.docx'

        try:
            cv.convert(n, start=i, end=i+1)
            os.remove(n)
        except Exception as ex:
            print("Error")
            errors.append(f'Error: {ex} in page {i}')
=======
    try:
        for i in range(int(start), int(end)):
            print(f'{Colors.GREEN} [PAGE INFO] Page: {i} {Colors.ENDTEXT}')

            output_stream = io.BytesIO()

            try:
                cv.convert(output_stream, start=i, end=i+1)
            except Exception as ex:
                print(f'{Colors.RED} [Error]: {ex} in page {i} {Colors.ENDTEXT}')
                errors.append(f'Error: {ex} in page {i}')
            finally:
                output_stream.close()

                print(Colors.WARNING)
                progressBar.update(1)

    except Exception as ex:
        print("Erro no for")
    finally:
        progressBar.close()
>>>>>>> Stashed changes
        cv.close()


if(checkForErrors == ""):

    threads = []
    pages = countPages(pdfFile)
    pagesDivided = pages/threadsToUse

    progressBar = tqdm(leave=False, total=pages, desc=f'{Colors.WARNING}  [Error check progress]', unit="pg")

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

    #pages = countPages(pdfFile)
    #quarterPages = pages/4

    #x1 = threading.Thread(target=checkErrors, args=(0, quarterPages))
    #x1.start()

    #x2 = threading.Thread(target=checkErrors, args=(quarterPages+1, quarterPages*2))
    #x2.start()

    #x3 = threading.Thread(target=checkErrors, args=(quarterPages*2 + 1, quarterPages*3))
    #x3.start()

    #x4 = threading.Thread(target=checkErrors, args=(quarterPages*3 + 1, quarterPages*4))
    #x4.start()

    #x1.join()
    #x2.join()
    #x3.join()
    #x4.join()

    print(errors)

    #checkErrors()

if len(errors) == 0:
    cv = Converter(pdfFile)
    #cv.convert("output.docx")
    cv.convert("output.docx", start=0, end=countPages(pdfFile), multi_processing=True, cpu_count=threadsToUse)
    cv.close()

translate.translateDocx(threadsToUse)
