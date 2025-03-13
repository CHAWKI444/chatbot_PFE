from django.core.management.base import BaseCommand
from chatbot.rag.test_rag import test_franchise_concepts, test_franchise_requirements

class Command(BaseCommand):
    help = 'Run RAG tests'

    def handle(self, *args, **options):
        print("Running RAG tests...")
        test_franchise_concepts()
        test_franchise_requirements()
        print("Tests completed.")