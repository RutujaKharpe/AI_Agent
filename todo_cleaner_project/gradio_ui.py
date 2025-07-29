# 📄 gradio_ui.py
import gradio as gr
from main import run_pipeline

def handle_input(task_input):
    try:
        return run_pipeline(task_input)
    except Exception as e:
        return f"❌ Error: {str(e)}"

with gr.Blocks(title="🧠 To-Do List Cleaner & Prioritizer") as demo:
    gr.Markdown(
        """
        # 🧹 To-Do List Cleaner & Prioritizer
        Organize, categorize, and prioritize your messy task list using AI 🚀  
        ---
        🔹 *Input your tasks (comma, newline, or sentence separated)*  
        🔹 *Get back structured, categorized, and priority-tagged tasks*
        """
    )

    with gr.Row():
        with gr.Column(scale=3):
            task_input = gr.Textbox(
                label="📝 Your Task List",
                lines=8,
                placeholder="e.g., Buy milk, call boss, book tickets, finish project by Monday...",
                show_copy_button=True
            )
            submit_btn = gr.Button("✨ Clean & Prioritize")

        with gr.Column(scale=2):
            result_output = gr.Textbox(
                label="📋 Cleaned & Prioritized Output",
                lines=8,
                interactive=False,
                show_copy_button=True
            )

    submit_btn.click(fn=handle_input, inputs=task_input, outputs=result_output)

    gr.Markdown("___")
    gr.Markdown(
        "Made with ❤️ using [Gradio](https://gradio.app) and OpenAI | © 2025"
    )

demo.launch()

