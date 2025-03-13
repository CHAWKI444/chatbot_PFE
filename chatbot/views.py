from django.shortcuts import render, redirect
from django.http import HttpResponse
from .rag.ingest import main
from .rag.query_rag import query_rag
from .forms import FichierForm

def run_ingest(request):
    if request.method == "POST" and "reset" in request.POST:
        main(reset=True)
        return HttpResponse("Base de données réinitialisée et documents ingérés avec succès.")
    main(reset=False)
    return HttpResponse("Documents ingérés avec succès.")

def ingest_form(request):
    return render(request, 'chatbot/ingest.html')

def chatbot_query(request):
    if request.method == "POST":
        query_text = request.POST.get("query")
        response_text, sources = query_rag(query_text)
        return render(request, 'chatbot/chatbot_response.html', {
            'query': query_text,
            'response': response_text,
            'sources': sources
        })
    return render(request, 'chatbot/chatbot_form.html')

def upload_fichier(request):
    if request.method == 'POST':
        form = FichierForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('upload_fichier')
    else:
        form = FichierForm()
    return render(request, 'chatbot/upload.html', {'form': form})