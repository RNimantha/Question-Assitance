import torch
from transformers import AutoModelForQuestionAnswering, AutoTokenizer, pipeline

class ModelDefine():
    def __init__(self):
        # Load the model and tokenizer
        model_name = "deepset/roberta-base-squad2"
        self.model = AutoModelForQuestionAnswering.from_pretrained(model_name)
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)

        # Setup the pipeline
        self.nlp = pipeline('question-answering', model=self.model, tokenizer=self.tokenizer)

    def answer_question(self, context, question):
        """
        Takes a context and a question, and returns the answer based on the context.
        """
        result = self.nlp(question=question, context=context)
        return result['answer']
