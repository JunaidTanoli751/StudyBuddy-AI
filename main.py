# from agents import Agent , Runner , OpenAIChatCompletionsModel,AsyncOpenAI, RunConfig
# import os 
# import chainlit as cl
# from dotenv import load_dotenv
# load_dotenv()


        


# gemini_api_key  = os.getenv("GEMINI_API_KEY")


# external_client = AsyncOpenAI(
#     api_key=gemini_api_key,
#     base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
# )
# model = OpenAIChatCompletionsModel(
#     model  = "gemini-2.5-flash",
#     openai_client=external_client,
# )
# config  = RunConfig(
#     model= model,
#     model_provider=external_client,
#     tracing_disabled=True
# )

# agent = Agent(
#     name="StudyBuddy AI",
#     instructions=(
#         "You are a friendly tutor called StudyBuddy AI. "
#         "Explain concepts from any subject in simple terms, provide examples, "
#         "quiz the user, and give hints for problem-solving. "
#         "You can handle multi-step math problems, code examples, and theory explanations."
#     )
# )


    


# @cl.on_message
# async def handle_message(message:cl.Message):
#     result  =await  Runner.run(
#     agent ,
#     input =  message.content,
#     run_config  =  config
#      )  
#     await cl.Message(content = result.final_output).send()
    

# from agents import Agent, Runner, OpenAIChatCompletionsModel, AsyncOpenAI, RunConfig
# import os
# import chainlit as cl
# from dotenv import load_dotenv

# load_dotenv()

# # =====================
# # Gemini Setup
# # =====================
# gemini_api_key = os.getenv("GEMINI_API_KEY")

# external_client = AsyncOpenAI(
#     api_key=gemini_api_key,
#     base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
# )

# model = OpenAIChatCompletionsModel(
#     model="gemini-2.5-flash",
#     openai_client=external_client,
# )

# config = RunConfig(
#     model=model,
#     model_provider=external_client,
#     tracing_disabled=True
# )

# # =====================
# # Agent Instructions
# # =====================
# agent = Agent(
#     name="StudyBuddy AI",
#     instructions="""
# You are StudyBuddy AI, a friendly tutor.

# Rules:
# - If user says "start quiz <topic>", begin an interactive quiz.
# - Ask ONE question at a time.
# - Wait for user's answer.
# - Check correctness.
# - Explain briefly.
# - Then ask next question.

# Keep questions beginner-friendly.
# """
# )

# # =====================
# # Session State
# # =====================
# # cl.user_session:
# # quiz_active: bool
# # quiz_topic: str
# # last_question: str

# # =====================
# # Helper Functions
# # =====================
# async def ask_quiz_question(topic):
#     prompt = f"""
# Create ONE quiz question on topic: {topic}
# Do NOT give the answer.
# Just output the question clearly.
# """
#     result = await Runner.run(agent, input=prompt, run_config=config)
#     question = result.final_output.strip()

#     cl.user_session.set("last_question", question)

#     await cl.Message(
#         content=f"🧠 **Quiz Question ({topic})**\n\n{question}"
#     ).send()


# async def check_answer(user_answer):
#     question = cl.user_session.get("last_question")

#     prompt = f"""
# Question:
# {question}

# User Answer:
# {user_answer}

# Check if the answer is correct.
# Reply in this format:

# Correct/Incorrect
# Short explanation (2–3 lines)
# """
#     result = await Runner.run(agent, input=prompt, run_config=config)
#     return result.final_output


# # =====================
# # Main Handler
# # =====================
# @cl.on_message
# async def handle_message(message: cl.Message):
#     user_input = message.content.lower()

#     # START QUIZ
#     if user_input.startswith("start quiz"):
#         topic = user_input.replace("start quiz", "").strip()

#         if not topic:
#             await cl.Message(
#                 content="❌ Please specify a topic.\nExample: `start quiz python loops`"
#             ).send()
#             return

#         cl.user_session.set("quiz_active", True)
#         cl.user_session.set("quiz_topic", topic)

#         await cl.Message(
#             content=f"🎯 Quiz started on **{topic}**!\nAnswer the questions one by one."
#         ).send()

#         await ask_quiz_question(topic)
#         return

#     # IF QUIZ ACTIVE → CHECK ANSWER
#     if cl.user_session.get("quiz_active"):
#         feedback = await check_answer(message.content)

#         await cl.Message(
#             content=f"📝 **Result**\n{feedback}"
#         ).send()

#         topic = cl.user_session.get("quiz_topic")
#         await ask_quiz_question(topic)
#         return

#     # NORMAL CHAT
#     result = await Runner.run(
#         agent,
#         input=message.content,
#         run_config=config
#     )

#     await cl.Message(content=result.final_output).send()





from agents import Agent, Runner, OpenAIChatCompletionsModel, AsyncOpenAI, RunConfig
import os
import chainlit as cl
from dotenv import load_dotenv

load_dotenv()

# =====================
# Gemini Setup
# =====================
gemini_api_key = os.getenv("GEMINI_API_KEY")

external_client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

model = OpenAIChatCompletionsModel(
    model="gemini-2.5-flash",
    openai_client=external_client,
)

config = RunConfig(
    model=model,
    model_provider=external_client,
    tracing_disabled=True
)

# =====================
# Agent
# =====================
agent = Agent(
    name="StudyBuddy AI",
    instructions="""
You are StudyBuddy AI, a friendly tutor.

For quizzes:
- Ask ONE question at a time
- Do NOT reveal the answer
- Keep difficulty beginner-friendly
"""
)

# =====================
# Helper Functions
# =====================
async def ask_quiz_question(topic):
    prompt = f"""
Create ONE quiz question on topic: {topic}
Do NOT give the answer.
Only output the question.
"""
    result = await Runner.run(agent, input=prompt, run_config=config)
    question = result.final_output.strip()

    cl.user_session.set("last_question", question)

    await cl.Message(
        content=f"🧠 **Question**\n{question}"
    ).send()


async def check_answer(user_answer):
    question = cl.user_session.get("last_question")

    prompt = f"""
Question:
{question}

User Answer:
{user_answer}

Check correctness.
Reply strictly in this format:

Correct or Incorrect
Short explanation (2 lines max)
"""
    result = await Runner.run(agent, input=prompt, run_config=config)
    return result.final_output


# =====================
# Main Handler
# =====================
@cl.on_message
async def handle_message(message: cl.Message):
    user_input = message.content.strip().lower()

    # =====================
    # START QUIZ
    # =====================
    if user_input.startswith("start quiz"):
        topic = user_input.replace("start quiz", "").strip()

        if not topic:
            await cl.Message(
                content="❌ Example: `start quiz python loops`"
            ).send()
            return

        cl.user_session.set("quiz_active", True)
        cl.user_session.set("quiz_topic", topic)
        cl.user_session.set("score", 0)
        cl.user_session.set("total", 0)

        await cl.Message(
            content=f"""
🎯 **Quiz Started**
📘 Topic: {topic}

Commands:
• `/score` → check score
• `/end quiz` → finish quiz
"""
        ).send()

        await ask_quiz_question(topic)
        return

    # =====================
    # SHOW SCORE
    # =====================
    if user_input == "/score":
        score = cl.user_session.get("score", 0)
        total = cl.user_session.get("total", 0)

        await cl.Message(
            content=f"📊 **Your Score:** {score}/{total}"
        ).send()
        return

    # =====================
    # END QUIZ
    # =====================
    if user_input == "/end quiz":
        score = cl.user_session.get("score", 0)
        total = cl.user_session.get("total", 0)

        cl.user_session.set("quiz_active", False)

        await cl.Message(
            content=f"""
🏁 **Quiz Finished**
Final Score: **{score}/{total}**

Great job! 🎉
"""
        ).send()
        return

    # =====================
    # CHECK ANSWER
    # =====================
    if cl.user_session.get("quiz_active"):
        feedback = await check_answer(message.content)

        cl.user_session.set(
            "total",
            cl.user_session.get("total") + 1
        )

        if feedback.lower().startswith("correct"):
            cl.user_session.set(
                "score",
                cl.user_session.get("score") + 1
            )
            emoji = "✅"
        else:
            emoji = "❌"

        score = cl.user_session.get("score")
        total = cl.user_session.get("total")

        await cl.Message(
            content=f"""
{emoji} **Result**
{feedback}

📊 Score: {score}/{total}
"""
        ).send()

        await ask_quiz_question(cl.user_session.get("quiz_topic"))
        return

    # =====================
    # NORMAL CHAT
    # =====================
    result = await Runner.run(
        agent,
        input=message.content,
        run_config=config
    )

    await cl.Message(content=result.final_output).send()
