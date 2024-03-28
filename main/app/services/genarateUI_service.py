import gradio as gr
from main.app.services.mode_service import ModeService

class GenerateUI():
    def __init__(self):
        self.__function = ModeService().answer_question

    def generate_ui(self):
        iface = gr.Interface(fn=self.__function,
                             inputs=[gr.Textbox(label="Context", placeholder="Enter the text here...", lines=7),
                                     gr.Textbox(label="Question", placeholder="Enter your question here...")],
                             outputs=gr.Textbox(label="Answer"),
                             title="Question and Answer Assistant",
                             description="Provide a context and ask a question based on that context. The assistant will find the answer for you.")
        return iface
