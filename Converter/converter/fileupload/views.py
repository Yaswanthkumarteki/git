from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import FileUploadMF
from moviepy.editor import VideoFileClip
import os, shutil
import pandas as pd
import pdfplumber
from docx import Document
# Create your views here.
def uploadVideo(request):
    directory = 'media/userfiles'

    # Remove the directory and all its contents
    if os.path.exists(directory):
        shutil.rmtree(directory)
        print(f"Directory '{directory}' and its contents have been removed")

    # Create a new directory
    os.mkdir(directory)
    print(f"Directory '{directory}' has been created")

    if request.method == "POST":
        print(request.POST)
        fileform = FileUploadMF(request.POST,request.FILES)
        file_name = str(request.FILES['file'].name)
        file_extension = request.FILES['file'].name.split('.')[1].lower()
        print(file_extension)
        if file_extension in ('mp4', '3gp', 'webm', 'ogg'):
            if fileform.is_valid():
                print('file saved')
                fileform.save()
                video_file = VideoFileClip(f'media/userfiles/{file_name}')
                audio = video_file.audio
                audio.write_audiofile("media/userfiles/audio.mp3")
                video_file.close()
                resp = {'status_message': "File Upload Successfully", "module": "Video to Audio", 'error':False, 'success': True, 'file_name': 'audio.mp3'}
            # print("file",file)

        
        else:
            resp = {'status_message': "Please upload only mp4, 3gp, ogg file format", "Video to Audio": "Error", 'error':True}
        return render(request,'download.html', context=resp)
    else:
        resp = {'Status': "Error", "Module": "Video to Audio"}
        return render(request,'index.html', context=resp)
    

def uploadCSV(request):
    directory = 'media/userfiles'

    # Remove the directory and all its contents
    if os.path.exists(directory):
        shutil.rmtree(directory)
        print(f"Directory '{directory}' and its contents have been removed")

    # Create a new directory
    os.mkdir(directory)
    print(f"Directory '{directory}' has been created")

    if request.method == "POST":
        print(request.POST)
        fileform = FileUploadMF(request.POST,request.FILES)
        file_name = str(request.FILES['file'].name)
        file_extension = request.FILES['file'].name.split('.')[1].lower()
        print(file_extension)
        if file_extension in ('csv'):
            if fileform.is_valid():
                print('file saved')
                fileform.save()
                df = pd.read_csv(f'media/userfiles/{file_name}')
                df.to_excel(f'media/userfiles/Excel.xlsx',sheet_name='sheet1', index=False)
                resp = {'status_message': "File Upload Successfully", "module": "CSV to Excel", 'error':False, 'success': True, 'file_name': 'Excel.xlsx'}

        
        else:
            resp = {'status_message': "Please upload CSV file", "module": "CSV to Excel", 'error':True}
        return render(request,'download.html', context=resp)
    else:
        resp = {'Status': "Error", "Module": "CSv to Excel"}
        return render(request,'index.html', context=resp)
    

def uploadExcel(request):
    directory = 'media/userfiles'

    # Remove the directory and all its contents
    if os.path.exists(directory):
        shutil.rmtree(directory)
        print(f"Directory '{directory}' and its contents have been removed")

    # Create a new directory
    os.mkdir(directory)
    print(f"Directory '{directory}' has been created")
    print('upload excel trigerred')

    if request.method == "POST":
        print(request.POST)
        fileform = FileUploadMF(request.POST,request.FILES)
        sheet_name = request.POST.get('sheet_name')
        print(sheet_name)
        file_name = str(request.FILES['file'].name)
        file_extension = request.FILES['file'].name.split('.')[1].lower()
        print(file_extension)
        try:
            if file_extension in ('xlsx'):
                if fileform.is_valid():
                    print('file saved')
                    fileform.save()
                    df = pd.read_excel(f'media/userfiles/{file_name}', sheet_name=sheet_name)
                    df.to_csv(f'media/userfiles/csvfile.csv', index=False)
                    resp = {'status_message': "File Upload Successfully", "module": "Excel to CSV", 'error':False, 'success': True, 'file_name': 'csvfile.csv'}

            
            else:
                resp = {'status_message': "Please upload .xlsx file only", "module": "Excel to CSV", 'error':True}
            return render(request,'download.html', context=resp)
        except Exception as e:
            resp = {'status_message': e, "module": "Excel to CSV", 'error':True}
            return render(request,'download.html', context=resp)

    else:
        print(" in Except")
        resp = {'Status': "Error", "Module": "Excel to CSV"}
        return render(request,'index.html', context=resp)
    

def uploadPDF(request):
    directory = 'media/userfiles'

    # Remove the directory and all its contents
    if os.path.exists(directory):
        shutil.rmtree(directory)
        print(f"Directory '{directory}' and its contents have been removed")

    # Create a new directory
    os.mkdir(directory)
    print(f"Directory '{directory}' has been created")
    print('upload PDF trigerred')

    if request.method == "POST":
        print(request.POST)
        fileform = FileUploadMF(request.POST,request.FILES)
        file_name = str(request.FILES['file'].name)
        file_extension = request.FILES['file'].name.split('.')[1].lower()
        print(file_extension)
        try:
            if file_extension in ('pdf'):
                if fileform.is_valid():
                    print('file saved')
                    fileform.save()
                    with pdfplumber.open(f'media/userfiles/{file_name}') as pdf:
                        text = ""
                        # Extract text from each page
                        for page in pdf.pages:
                            text += page.extract_text()
                    
                            # Create a new Word document
                            doc = Document()
                            # Add the extracted text to the Word document
                            doc.add_paragraph(text)

                            # Save the Word document
                            doc.save(f'media/userfiles/wordfile.doc')
                    resp = {'status_message': "File Upload Successfully", "module": "PDF to Word Doc", 'error':False, 'success': True, 'file_name': 'worddoc.doc'}

            
            else:
                resp = {'status_message': "Please upload .doc file only", "module": "PDF to Word Doc", 'error':True}
            return render(request,'download.html', context=resp)
        except Exception as e:
            resp = {'status_message': e, "module": "PDF to Word Doc", 'error':True}
            return render(request,'download.html', context=resp)

    else:
        print(" in Except")
        resp = {'Status': "Error", "Module": "Excel to CSV"}
        return render(request,'index.html', context=resp)