import streamlit as st

st.set_page_config(
    page_title="Generative AI Learning Roadmap",
    page_icon="🚀",
    layout="wide",
)

# ============================================================
# 1. ROADMAP DATA
# ============================================================
ROADMAP = {
    "Beginner": {
        "summary": (
            "The basics of Prompt Engineering and Generative AI to "
            "get started with foundation models."
        ),
        "time": "2-3 hours",
        "topics": [
            [
                "Introduction to Generative AI",
                [
                    "What is Generative AI?",
                    "Traditional AI vs. Generative AI",
                    "Applications of Generative AI (text, image, code, etc.)",
                ],
                "Read 'What is Generative AI?' article.",
                "Summarize the key differences between traditional and Generative AI in 3 sentences.",
            ],
            [
                "Foundation Models",
                [
                    "What are Foundation Models?",
                    "Key characteristics (pre-trained, adaptable, multimodal)",
                    "Examples of Foundation Models (BERT, GPT, Imagen, etc.)",
                ],
                "Explore the concept of transfer learning in the context of foundation models.",
                "Identify 3 foundation models and their primary use cases.",
            ],
            [
                "Introduction to Large Language Models (LLMs)",
                [
                    "What are LLMs?",
                    "How do LLMs work (brief overview of transformer architecture)?",
                    "Key capabilities and limitations",
                ],
                "Watch a video explaining transformer architecture.",
                "List 3 common applications and 3 limitations of LLMs.",
            ],
            [
                "Basic Prompt Engineering",
                [
                    "What is prompt engineering?",
                    "Role of effective prompts",
                    "Components of a good prompt (persona, format, context, tone, task)",
                ],
                "Practice writing prompts for a simple task (e.g., summarizing a text).",
                "Write a prompt to generate a 3-paragraph story about a robot and a cat.",
            ],
            [
                "Prompting Techniques - Zero-shot, Few-shot, Chain-of-Thought",
                [
                    "Zero-shot prompting",
                    "Few-shot prompting",
                    "Chain-of-Thought prompting for complex tasks",
                ],
                "Experiment with few-shot prompting using different examples.",
                "Compare the output of zero-shot vs. few-shot prompting for a factual question.",
            ],
        ],
    },
    "Intermediate": {
        "summary": (
            "Advanced Prompt Engineering, fine-tuning, and practical "
            "applications for building GenAI solutions."
        ),
        "time": "4-6 hours",
        "topics": [
            [
                "Advanced Prompt Engineering - Role-Playing and Delimiters",
                [
                    "Using delimiters to structure prompts",
                    "Assigning personas/roles to the LLM",
                    "Iterative prompting for refinement",
                ],
                "Design a prompt where the LLM acts as a specific historical figure.",
                "Develop a prompt using delimiters to extract structured data from unstructured text.",
            ],
            [
                "Evaluation of LLM Outputs",
                [
                    "Metrics for evaluating generated text (fluency, coherence, relevance)",
                    "Human evaluation vs. automated metrics",
                    "Identifying and mitigating biases",
                ],
                "Evaluate 5 generated text samples based on coherence and relevance.",
                "Describe a scenario where automated metrics might fail in evaluating LLM output.",
            ],
            [
                "Retrieval Augmented Generation (RAG)",
                [
                    "Introduction to RAG architecture",
                    "Components: retriever, generator",
                    "Benefits of RAG for factual accuracy and reduced hallucinations",
                ],
                "Research a RAG framework (e.g., Haystack, LlamaIndex).",
                "Explain how RAG improves upon standalone LLMs for question answering.",
            ],
            [
                "Fine-tuning Foundation Models (Concepts)",
                [
                    "When and why to fine-tune",
                    "Approaches to fine-tuning (full fine-tuning, LoRA, etc.)",
                    "Data preparation for fine-tuning",
                ],
                "Understand the difference between pre-training and fine-tuning.",
                "Propose a dataset for fine-tuning an LLM for a specific industry.",
            ],
            [
                "Introduction to Multimodal Models",
                [
                    "What are multimodal models?",
                    "Examples: text-to-image (DALL-E, Midjourney), image-to-text, text-to-video",
                    "Challenges and opportunities",
                ],
                "Experiment with a text-to-image generator (e.g., DALL-E mini).",
                "Describe a potential multimodal AI application not yet widely available.",
            ],
        ],
    },
    "Advanced": {
        "summary": (
            "Building and deploying Generative AI applications, "
            "ethical considerations, and future trends."
        ),
        "time": "5-7 hours",
        "topics": [
            [
                "Building with Generative AI APIs",
                [
                    "Integrating LLMs into applications (e.g., OpenAI API, Google Gemini API)",
                    "Handling API keys and rate limits",
                    "Error handling and response parsing",
                ],
                "Develop a simple application that uses an LLM API to answer questions.",
                "Implement a basic error handling mechanism for API calls.",
            ],
            [
                "Deploying Generative AI Models",
                [
                    "Deployment strategies (cloud platforms, on-premise)",
                    "Containerization (Docker) and orchestration (Kubernetes)",
                    "Monitoring and maintaining deployed models",
                ],
                "Explore a cloud provider's GenAI deployment options.",
                "Outline the steps to deploy a simple LLM-powered chatbot.",
            ],
            [
                "Ethical AI and Responsible Development",
                [
                    "Bias and fairness in Generative AI",
                    "Transparency and interpretability",
                    "Privacy and data security",
                    "Mitigation strategies and best practices",
                ],
                "Analyze a case study of AI bias in a real-world application.",
                "Propose 3 ethical guidelines for developing a new GenAI product.",
            ],
            [
                "Generative AI in Production - MLOps for GenAI",
                [
                    "Data versioning for fine-tuning",
                    "Model versioning and lineage",
                    "Continuous integration/continuous deployment (CI/CD) for GenAI",
                    "Monitoring model performance and drift",
                ],
                "Identify tools used for MLOps in GenAI (e.g., MLflow, Weights & Biases).",
                "Describe how model drift could impact a deployed GenAI application.",
            ],
            [
                "Future Trends in Generative AI",
                [
                    "Longer context windows",
                    "More efficient models (smaller, faster)",
                    "Advanced multimodal capabilities",
                    "Agentic AI systems",
                ],
                "Research a recent breakthrough in Generative AI.",
                "Speculate on how agentic AI systems might change software development.",
            ],
        ],
    },
}

# ============================================================
# 2. TOOLS LANDSCAPE DATA
# ============================================================
TOOLS = {
    "Large Language Models (LLMs)": [
        ["OpenAI GPT-3.5/GPT-4", "API (paid)"],
        ["Google Gemini Pro/Ultra", "API (free tier available)"],
        ["Anthropic Claude 3", "API (free tier available)"],
        ["Meta Llama 2/3", "Open-source (self-host)"],
        ["Mistral AI models", "Open-source / API (paid)"],
    ],
    "Text-to-Image Generators": [
        ["Midjourney", "Subscription (paid)"],
        ["DALL-E 3 (via ChatGPT Plus/API)", "Subscription / API (paid)"],
        ["Stable Diffusion", "Open-source (self-host) / API (paid)"],
        ["Imagen (Google)", "API (paid)"],
    ],
    "Code Generation/Completion": [
        ["GitHub Copilot", "Subscription (paid)"],
        ["Amazon CodeWhisperer", "Free / Enterprise (paid)"],
        ["Google Gemini Code Assist", "API (paid)"],
    ],
    "Vector Databases & Embeddings": [
        ["Pinecone", "Free tier / Paid"],
        ["Weaviate", "Open-source / Cloud (paid)"],
        ["Chroma", "Open-source (self-host)"],
        ["FAISS", "Open-source (self-host)"],
        ["Voyage AI (Embeddings)", "API (free tier available)"],
        ["OpenAI Embeddings", "API (paid)"],
        ["Cohere Embeddings", "API (free tier available)"],
    ],
    "Frameworks & Libraries": [
        ["LangChain", "Open-source (Python/JS)"],
        ["LlamaIndex", "Open-source (Python)"],
        ["Hugging Face Transformers", "Open-source (Python)"],
        ["Gradio", "Open-source (Python)"],
        ["Streamlit", "Open-source (Python)"],
    ],
    "Cloud Platforms (GenAI Services)": [
        ["Google Cloud Vertex AI", "Pay-as-you-go"],
        ["AWS SageMaker", "Pay-as-you-go"],
        ["Azure AI Studio", "Pay-as-you-go"],
    ],
}

COLORS = {
    "Beginner": "#10B981",
    "Intermediate": "#3B82F6",
    "Advanced": "#F97316",
    "Tools Landscape": "#6B7280",
}

# Build deterministic keys for every topic checkbox upfront
ALL_CHECKBOX_KEYS: list[str] = []
for level_number, level_name in enumerate(["Beginner", "Intermediate", "Advanced"], start=1):
    for topic_number, _ in enumerate(ROADMAP[level_name]["topics"], start=1):
        ALL_CHECKBOX_KEYS.append(f"completed_{level_number}_{topic_number}")

for key in ALL_CHECKBOX_KEYS:
    st.session_state.setdefault(key, False)


# ============================================================
# 3. HELPERS & CALLBACKS
# ============================================================
def render_topic_body(number: str, title: str, concepts: list[str], practice: str, deliverable: str) -> None:
    concept_list = "\n".join(f"- {concept}" for concept in concepts)
    st.markdown(
        f"""
## {number} — {title}

### Core Topics
{concept_list}

---

### Hands-on Practice
{practice}

### Expected Deliverable
**{deliverable}**
"""
    )


def build_progress_markdown(checkbox_values: list[bool]) -> str:
    total_topics = len(checkbox_values)
    completed_topics = sum(1 for val in checkbox_values if val)
    percentage = 0 if total_topics == 0 else round(completed_topics / total_topics * 100)

    completed_blocks = round(percentage / 5)
    remaining_blocks = 20 - completed_blocks
    progress_bar = "🟩" * completed_blocks + "⬜" * remaining_blocks

    if percentage == 100:
        status = "Roadmap completed. Continue building real Generative AI projects."
    elif percentage >= 65:
        status = "Excellent progress. You are approaching the advanced stage."
    elif percentage >= 35:
        status = "Good progress. Continue building practical applications."
    elif percentage > 0:
        status = "You have started. Complete one topic at a time."
    else:
        status = "Select your learning level and begin with the first topic."

    return (
        f"### Your Progress\n\n"
        f"{progress_bar}\n\n"
        f"**Completed:** {completed_topics} of {total_topics} topics\n\n"
        f"**Overall progress:** {percentage}%\n\n"
        f"{status}"
    )


def reset_all_progress() -> None:
    for key in ALL_CHECKBOX_KEYS:
        st.session_state[key] = False


# ============================================================
# 4. HEADER, NAVIGATION & PROGRESS OVERVIEW
# ============================================================
st.markdown(
    """
<div style="padding: 28px; margin-bottom: 18px; border-radius: 16px; color: #ffffff; background: linear-gradient(135deg, #10251c, #166534);">
    <h1 style="margin: 0 0 10px 0; color: #ffffff; font-size: 34px;">Generative AI Learning Roadmap</h1>
    <p style="margin: 4px 0; color: #e1f5e8; font-size: 16px;">A continuous path from AI fundamentals to building and deploying real Generative AI applications.</p>
    <p style="margin: 4px 0; color: #e1f5e8; font-size: 15px;">Select your current learning level from the menu below.</p>
</div>
""",
    unsafe_allow_html=True,
)

level_selector = st.selectbox(
    label="Select Learning Level",
    options=["Beginner", "Intermediate", "Advanced", "Tools Landscape"],
    help="You can start from Beginner or jump to your current level.",
)

left_col, right_col = st.columns([2, 1])

with left_col:
    st.markdown(
        """
### How to use this roadmap
1. Select your learning level.
2. Open the topics in sequence.
3. Study the core concepts.
4. Complete the practical exercise.
5. Mark the topic as completed.
6. Keep each deliverable for your portfolio.
"""
    )

with right_col:
    current_states = [bool(st.session_state.get(key, False)) for key in ALL_CHECKBOX_KEYS]
    st.markdown(build_progress_markdown(current_states))
    st.button(
        label="Reset All Progress",
        type="secondary",
        on_click=reset_all_progress,
    )

st.divider()

# ============================================================
# 5. ACTIVE SECTION CONTENT
# ============================================================
if level_selector in ("Beginner", "Intermediate", "Advanced"):
    level_number = ["Beginner", "Intermediate", "Advanced"].index(level_selector) + 1
    level_data = ROADMAP[level_selector]
    level_color = COLORS[level_selector]

    st.markdown(
        f"""
<div style="padding: 18px; margin-bottom: 16px; border: 1px solid #b9c8be; border-top: 6px solid {level_color}; border-radius: 12px; background: #ffffff; color: #17201a;">
    <h2 style="margin: 0 0 8px 0; color: #17201a;">Level {level_number}: {level_selector}</h2>
    <p style="margin: 0 0 8px 0; color: #17201a;">{level_data["summary"]}</p>
    <p style="margin: 0; color: #17201a;"><strong>Estimated completion time:</strong> {level_data["time"]}</p>
</div>
""",
        unsafe_allow_html=True,
    )

    for topic_number, topic in enumerate(level_data["topics"], start=1):
        topic_id = f"{level_number}.{topic_number}"
        topic_title, concepts, practice, deliverable = topic
        checkbox_key = f"completed_{level_number}_{topic_number}"

        with st.expander(
            label=f"{topic_id} — {topic_title}",
            expanded=(level_selector == "Beginner" and topic_number == 1),
        ):
            render_topic_body(topic_id, topic_title, concepts, practice, deliverable)
            st.checkbox(
                label="I completed this topic and its practical exercise",
                key=checkbox_key,
            )

elif level_selector == "Tools Landscape":
    st.markdown("# Generative AI Tools Landscape")
    st.caption("Select a category to view the available tools.")
    st.info(
        "**Note:** Prices and free plans may change. Always verify the "
        "latest information on the official platform website."
    )

    for category, items in TOOLS.items():
        with st.expander(label=category, expanded=False):
            for tool_name, access_type in items:
                st.markdown(f"### {tool_name}\n\n**Access:** {access_type}\n\n---")
with right_col:
    current_states = [bool(st.session_state.get(key, False)) for key in ALL_CHECKBOX_KEYS]
    st.markdown(build_progress_markdown(current_states))

    btn_col1, btn_col2 = st.columns(2)
    with btn_col1:
        st.button(
            label="Reset All",
            type="secondary",
            on_click=reset_all_progress,
            use_container_width=True,
        )
    with btn_col2:
        st.download_button(
            label="Save JSON",
            data=build_progress_json_payload(),
            file_name="genai_roadmap_progress.json",
            mime="application/json",
            use_container_width=True,
        )

    uploader_key = f"progress_uploader_{st.session_state['import_version']}"
    uploaded_file = st.file_uploader(
        label="Restore Progress (JSON)",
        type=["json"],
        key=uploader_key,
        help="Upload a previously exported genai_roadmap_progress.json file.",
    )

    if uploaded_file is not None:
        ok, message = restore_progress_from_json(uploaded_file.getvalue())
        st.session_state["import_version"] += 1
        st.session_state["progress_status_msg"] = ("success" if ok else "error", message)
        st.rerun()

    if st.session_state.get("progress_status_msg"):
        level, msg = st.session_state["progress_status_msg"]
        if level == "success":
            st.success(msg)
        else:
            st.error(msg)
