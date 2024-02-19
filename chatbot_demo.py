import chatbot
import gradio as gr

kpmg_chat = chatbot.Chatbot("KPMG")

def chatbot_demo(question:str,history=[]):
    response = kpmg_chat.information(question)
    print(response)
    return response

gr.ChatInterface(title="이직 상담 친구",
                 fn = chatbot_demo,
                 description="지원하신 회사에 대해서 어떤 질문이든 해주세요~",
                 examples=[["회사에 대해서 소개해줘"], ["회사에서 하려는 프로젝트가 정확히 뭐야?"], ["내가 맡게될 역할이 뭘까?"], ['면접은 언제 가능해?']],
                 theme="soft",
                retry_btn="다시보내기 ↩",
                undo_btn="이전챗 삭제 ❌",
                clear_btn="전챗 삭제 💫"
                 ).launch(share = True, server_port = 7860)
    