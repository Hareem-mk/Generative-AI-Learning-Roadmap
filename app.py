# 1. Imports
import streamlit as st

level_selector = st.selectbox(
    "Level", ["Beginner", "Intermediate", "Advanced"]
)

# Update displayed sections directly based on level_selector
st.markdown(f"Showing roadmap for: **{level_selector}**")

# 2. ROADMAP dictionary
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
                    "Applications of Generative AI (text, image, code, etc.)"
                ],
                "Read 'What is Generative AI?' article.",
                "Summarize the key differences between traditional and Generative AI in 3 sentences."
            ],
            [
                "Foundation Models",
                [
                    "What are Foundation Models?",
                    "Key characteristics (pre-trained, adaptable, multimodal)",
                    "Examples of Foundation Models (BERT, GPT, Imagen, etc.)"
                ],
                "Explore the concept of transfer learning in the context of foundation models.",
                "Identify 3 foundation models and their primary use cases."
            ],
            [
                "Introduction to Large Language Models (LLMs)",
                [
                    "What are LLMs?",
                    "How do LLMs work (brief overview of transformer architecture)?",
                    "Key capabilities and limitations"
                ],
                "Watch a video explaining transformer architecture.",
                "List 3 common applications and 3 limitations of LLMs."
            ],
            [
                "Basic Prompt Engineering",
                [
                    "What is prompt engineering?",
                    "Role of effective prompts",
                    "Components of a good prompt (persona, format, context, tone, task)"
                ],
                "Practice writing prompts for a simple task (e.g., summarizing a text).",
                "Write a prompt to generate a 3-paragraph story about a robot and a cat."
            ],
            [
                "Prompting Techniques - Zero-shot, Few-shot, Chain-of-Thought",
                [
                    "Zero-shot prompting",
                    "Few-shot prompting",
                    "Chain-of-Thought prompting for complex tasks"
                ],
                "Experiment with few-shot prompting using different examples.",
                "Compare the output of zero-shot vs. few-shot prompting for a factual question."
            ]
        ]
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
                    "Iterative prompting for refinement"
                ],
                "Design a prompt where the LLM acts as a specific historical figure.",
                "Develop a prompt using delimiters to extract structured data from unstructured text."
            ],
            [
                "Evaluation of LLM Outputs",
                [
                    "Metrics for evaluating generated text (fluency, coherence, relevance)",
                    "Human evaluation vs. automated metrics",
                    "Identifying and mitigating biases"
                ],
                "Evaluate 5 generated text samples based on coherence and relevance.",
                "Describe a scenario where automated metrics might fail in evaluating LLM output."
            ],
            [
                "Retrieval Augmented Generation (RAG)",
                [
                    "Introduction to RAG architecture",
                    "Components: retriever, generator",
                    "Benefits of RAG for factual accuracy and reduced hallucinations"
                ],
                "Research a RAG framework (e.g., Haystack, LlamaIndex).",
                "Explain how RAG improves upon standalone LLMs for question answering."
            ],
            [
                "Fine-tuning Foundation Models (Concepts)",
                [
                    "When and why to fine-tune",
                    "Approaches to fine-tuning (full fine-tuning, LoRA, etc.)",
                    "Data preparation for fine-tuning"
                ],
                "Understand the difference between pre-training and fine-tuning.",
                "Propose a dataset for fine-tuning an LLM for a specific industry."
            ],
            [
                "Introduction to Multimodal Models",
                [
                    "What are multimodal models?",
                    "Examples: text-to-image (DALL-E, Midjourney), image-to-text, text-to-video",
                    "Challenges and opportunities"
                ],
                "Experiment with a text-to-image generator (e.g., DALL-E mini).",
                "Describe a potential multimodal AI application not yet widely available."
            ]
        ]
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
                    "Error handling and response parsing"
                ],
                "Develop a simple application that uses an LLM API to answer questions.",
                "Implement a basic error handling mechanism for API calls."
            ],
            [
                "Deploying Generative AI Models",
                [
                    "Deployment strategies (cloud platforms, on-premise)",
                    "Containerization (Docker) and orchestration (Kubernetes)",
                    "Monitoring and maintaining deployed models"
                ],
                "Explore a cloud provider's GenAI deployment options.",
                "Outline the steps to deploy a simple LLM-powered chatbot."
            ],
            [
                "Ethical AI and Responsible Development",
                [
                    "Bias and fairness in Generative AI",
                    "Transparency and interpretability",
                    "Privacy and data security",
                    "Mitigation strategies and best practices"
                ],
                "Analyze a case study of AI bias in a real-world application.",
                "Propose 3 ethical guidelines for developing a new GenAI product."
            ],
            [
                "Generative AI in Production - MLOps for GenAI",
                [
                    "Data versioning for fine-tuning",
                    "Model versioning and lineage",
                    "Continuous integration/continuous deployment (CI/CD) for GenAI",
                    "Monitoring model performance and drift"
                ],
                "Identify tools used for MLOps in GenAI (e.g., MLflow, Weights & Biases).",
                "Describe how model drift could impact a deployed GenAI application."
            ],
            [
                "Future Trends in Generative AI",
                [
                    "Longer context windows",
                    "More efficient models (smaller, faster)",
                    "Advanced multimodal capabilities",
                    "Agentic AI systems"
                ],
                "Research a recent breakthrough in Generative AI.",
                "Speculate on how agentic AI systems might change software development."
            ]
        ]
    }
}

# 3. TOOLS dictionary
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

# 4. COLORS dictionary
COLORS = {
    "Beginner": "#10B981",      # Emerald green
    "Intermediate": "#3B82F6",  # Royal blue
    "Advanced": "#F97316",      # Orange
    "Tools Landscape": "#6B7280", # Gray
}

# 5. topic_markdown() function
def topic_markdown(
    number,
    title,
    concepts,
    practice,
    deliverable,
    color
):
    """
    Creates the learning content shown inside each topic.
    Pure Markdown is used to avoid dark or black HTML boxes.
    """

    concept_list = "\n".join(
        f"- {concept}"
        for concept in concepts
    )

    return f"""
## {number} — {title}

### Core Topics

{concept_list}

---

### Hands-on Practice

{practice}

### Expected Deliverable

**{deliverable}**
"""

# 6. tools_markdown() function
# You may keep or delete this function because it is no longer used.

# 7. update_progress() function
def update_progress(*checkbox_values):
    """
    Calculates the total learning progress.
    Returns ordinary Markdown for maximum compatibility.
    """

    total_topics = len(checkbox_values)

    completed_topics = sum(
        1 for value in checkbox_values
        if value is True
    )

    if total_topics == 0:
        percentage = 0
    else:
        percentage = round(
            completed_topics / total_topics * 100
        )

    # Create a 20-block visual progress bar
    completed_blocks = round(
        percentage / 5
    )

    remaining_blocks = (
        20 - completed_blocks
    )

    progress_bar = (
        "🟩" * completed_blocks
        + "⬜" * remaining_blocks
    )

    if percentage == 100:
        status = (
            "Roadmap completed. Continue building "
            "real Generative AI projects."
        )

    elif percentage >= 65:
        status = (
            "Excellent progress. You are approaching "
            "the advanced stage."
        )

    elif percentage >= 35:
        status = (
            "Good progress. Continue building "
            "practical applications."
        )

    elif percentage > 0:
        status = (
            "You have started. Complete one topic "
            "at a time."
        )

    else:
        status = (
            "Select your learning level and begin "
            "with the first topic."
        )

    return f"""
### Your Progress

{progress_bar}

**Completed:** {completed_topics} of {total_topics} topics

**Overall progress:** {percentage}%

{status}
"""


# ============================================================
# APPLICATION THEME AND STYLING
# ============================================================

[theme]
base = "light"
primaryColor = "#6366f1"
backgroundColor = "#ffffff"
secondaryBackgroundColor = "#f3f4f6"
textColor = "#111827"
    primary_hue="green",
    secondary_hue="blue",
    neutral_hue="slate",
).set(
    body_background_fill="#f4f7f5",
    body_background_fill_dark="#f4f7f5",

    body_text_color="#17201a",
    body_text_color_dark="#17201a",

    block_background_fill="#ffffff",
    block_background_fill_dark="#ffffff",

    block_border_color="#cbd5ce",
    block_border_color_dark="#cbd5ce",

    input_background_fill="#ffffff",
    input_background_fill_dark="#ffffff",

    input_border_color="#9ca9a0",
    input_border_color_dark="#9ca9a0",

    button_primary_background_fill="#166534",
    button_primary_background_fill_hover="#14532d",

    button_secondary_background_fill="#ffffff",
    button_secondary_background_fill_hover="#edf5f0",
)


custom_css = """
/* Force a clear light appearance */
:root {
    color-scheme: light;
}

body,
.gradio-container {
    background: #f4f7f5 !important;
    color: #17201a !important;
}

.gradio-container {
    max-width: 1200px !important;
    margin: auto !important;
}

/* Main heading */
.hero {
    padding: 30px;
    margin-bottom: 18px;
    border-radius: 18px;
    color: #ffffff !important;
    background: linear-gradient(
        135deg,
        #10251c,
        #166534
    );
}

.hero h1 {
    margin: 0 0 12px 0;
    color: #ffffff !important;
    font-size: 38px;
}

.hero p {
    margin: 6px 0;
    color: #e1f5e8 !important;
    font-size: 16px;
}

/* Level information */
.level-summary {
    padding: 18px;
    margin-bottom: 14px;
    border: 1px solid #b9c8be;
    border-radius: 12px;
    background: #ffffff !important;
    color: #17201a !important;
}

.level-summary h2,
.level-summary p {
    color: #17201a !important;
}

/* Topic cards */
.topic {
    padding: 20px 22px;
    margin: 8px 0 12px 0;
    border: 1px solid #c6d1ca;
    border-left: 5px solid;
    border-radius: 12px;
    background: #ffffff !important;
    color: #17201a !important;
}

.topic h3,
.topic h4,
.topic p,
.topic li,
.topic strong {
    color: #17201a !important;
}

/* Hands-on exercise */
.practice {
    padding: 16px;
    margin-top: 16px;
    border: 1px solid #9fc4ac;
    border-radius: 10px;
    background: #eaf6ee !important;
    color: #173d25 !important;
}

/* Progress area */
.progress {
    padding: 18px;
    border: 1px solid #b9c8be;
    border-radius: 12px;
    background: #ffffff !important;
    color: #17201a !important;
}

.progress-title {
    display: flex;
    justify-content: space-between;
    margin-bottom: 10px;
}

.progress-track {
    width: 100%;
    height: 14px;
    overflow: hidden;
    border-radius: 20px;
    background: #d9e1dc;
}

.progress-fill {
    height: 100%;
    border-radius: 20px;
    background: linear-gradient(
        90deg,
        #16a34a,
        #0284c7,
        #ea580c
    );
    transition: width 0.4s ease;
}

/* Dropdown */
.level-dropdown {
    padding: 14px;
    border: 1px solid #b9c8be;
    border-radius: 12px;
    background: #ffffff !important;
}

/* Improve accordion visibility */
.gradio-container .label-wrap {
    color: #17201a !important;
    font-weight: 700 !important;
}

.gradio-container button {
    color: #17201a;
}

/* Checkbox labels */
.gradio-container label {
    color: #17201a !important;
}

/* Markdown text */
.gradio-container .prose {
    color: #17201a !important;
}

.gradio-container .prose p,
.gradio-container .prose li,
.gradio-container .prose h1,
.gradio-container .prose h2,
.gradio-container .prose h3,
.gradio-container .prose h4 {
    color: #17201a !important;
}

/* Mobile layout */
@media screen and (max-width: 600px) {
    .hero {
        padding: 22px;
    }

    .hero h1 {
        font-size: 29px;
    }

    .topic {
        padding: 16px;
    }
}
/* Dropdown main field */
.level-dropdown,
.level-dropdown > div,
.level-dropdown input,
.level-dropdown [role="combobox"] {
    background: #ffffff !important;
    color: #17201a !important;
    border-color: #8fa097 !important;
}

/* Dropdown options box */
[role="listbox"] {
    background: #ffffff !important;
    color: #17201a !important;
    border: 1px solid #8fa097 !important;
}

/* Individual dropdown options */
[role="option"] {
    background: #ffffff !important;
    color: #17201a !important;
    opacity: 1 !important;
}

/* Option when cursor moves over it */
[role="option"]:hover {
    background: #dff3e6 !important;
    color: #14532d !important;
}

/* Selected option */
[role="option"][aria-selected="true"] {
    background: #ccebd7 !important;
    color: #14532d !important;
    font-weight: 700 !important;
}

/* Dropdown label and information */
.level-dropdown label,
.level-dropdown span,
.level-dropdown p {
    color: #17201a !important;
    opacity: 1 !important;
}
/* ==========================================================
   ACCORDION / TOPIC HEADER COLOURS
   ========================================================== */

/* Complete accordion container */
.gradio-container .accordion {
    background: #ffffff !important;
    color: #17201a !important;
    border: 1px solid #b9c8be !important;
    border-radius: 10px !important;
}

/* Accordion clickable heading */
.gradio-container .accordion button,
.gradio-container button[aria-expanded="true"],
.gradio-container button[aria-expanded="false"] {
    background: #ffffff !important;
    color: #17201a !important;
    border-color: #b9c8be !important;
    opacity: 1 !important;
}

/* Accordion heading text */
.gradio-container .accordion button span,
.gradio-container button[aria-expanded="true"] span,
.gradio-container button[aria-expanded="false"] span {
    color: #17201a !important;
    opacity: 1 !important;
    font-weight: 700 !important;
}

/* Accordion arrow icon */
.gradio-container .accordion button svg,
.gradio-container button[aria-expanded="true"] svg,
.gradio-container button[aria-expanded="false"] svg {
    color: #166534 !important;
    stroke: #166534 !important;
}

/* Mouse-over effect */
.gradio-container .accordion button:hover,
.gradio-container button[aria-expanded="true"]:hover,
.gradio-container button[aria-expanded="false"]:hover {
    background: #eaf6ee !important;
    color: #14532d !important;
}

/* Open accordion heading */
.gradio-container button[aria-expanded="true"] {
    background: #dff3e6 !important;
    color: #14532d !important;
    border-bottom-color: #9fc4ac !important;
}

/* Area inside the accordion */
.gradio-container .accordion > div {
    background: #ffffff !important;
    color: #17201a !important;
}

/* Accordion labels used by some Gradio versions */
.gradio-container .label-wrap {
    background: #ffffff !important;
    color: #17201a !important;
    opacity: 1 !important;
}

.gradio-container .label-wrap:hover {
    background: #eaf6ee !important;
}
/* Learning topic accordions */
.learning-topic {
    background: #ffffff !important;
    color: #17201a !important;
    border: 1px solid #aebdb3 !important;
    border-radius: 10px !important;
    margin-bottom: 10px !important;

    --block-background-fill: #ffffff;
    --block-background-fill-dark: #ffffff;
    --block-label-background-fill: #ffffff;
    --block-label-background-fill-dark: #ffffff;
    --block-label-text-color: #17201a;
    --block-label-text-color-dark: #17201a;
}

/* Learning topic heading */
.learning-topic button,
.learning-topic .label-wrap {
    background: #ffffff !important;
    color: #17201a !important;
    opacity: 1 !important;
}

/* Heading text */
.learning-topic button span,
.learning-topic .label-wrap span {
    color: #17201a !important;
    opacity: 1 !important;
    font-weight: 700 !important;
}

/* Open topic */
.learning-topic button[aria-expanded="true"] {
    background: #dff3e6 !important;
    color: #14532d !important;
}

/* Hover */
.learning-topic button:hover,
.learning-topic .label-wrap:hover {
    background: #eaf6ee !important;
    color: #14532d !important;
}

/* Content inside an open topic */
.learning-topic .prose,
.learning-topic .prose h2,
.learning-topic .prose h3,
.learning-topic .prose p,
.learning-topic .prose li,
.learning-topic .prose strong {
    background: #ffffff !important;
    color: #17201a !important;
    opacity: 1 !important;
}
"""
# ============================================================
# DROPDOWN SELECTION FUNCTION
# ============================================================

def change_section(selected_section):
    """
    Shows only the level selected in the dropdown.

    The function returns visibility instructions for:
    1. Beginner
    2. Intermediate
    3. Advanced
    4. Tools Landscape
    """

    section_names = [
        "Beginner",
        "Intermediate",
        "Advanced",
        "Tools Landscape"
    ]

    return [
        gr.update(
            visible=(selected_section == section)
        )
        for section in section_names
    ]


# ============================================================
# BUILD THE GRADIO APPLICATION
# ============================================================

TOTAL_TOPICS = sum(
    len(level_data["topics"])
    for level_data in ROADMAP.values()
)

with gr.Blocks(
    title="Generative AI Learning Roadmap",
    theme=custom_theme,
    css=custom_css
) as app:

    gr.HTML("""
    <div class="hero">

        <h1>Generative AI Learning Roadmap</h1>

        <p>
            A continuous path from AI fundamentals to building
            and deploying real Generative AI applications.
        </p>

        <p>
            Select your current learning level from the menu below.
        </p>

    </div>
    """)

    # --------------------------------------------------------
    # LEVEL DROPDOWN
    # --------------------------------------------------------

    level_selector = gr.Dropdown(
        choices=[
            "Beginner",
            "Intermediate",
            "Advanced",
            "Tools Landscape"
        ],
        value="Beginner",
        label="Select Learning Level",
        info="You can start from Beginner or jump to your current level.",
        interactive=True,
        elem_classes=["level-dropdown"]
    )

    # List used to store every completion checkbox
    checkbox_components = []

    # List used to store the four display sections
    display_sections = []

    with gr.Row():

        with gr.Column(scale=2):

            gr.Markdown("""
### How to use this roadmap

1. Select your learning level.
2. Open the topics in sequence.
3. Study the core concepts.
4. Complete the practical exercise.
5. Mark the topic as completed.
6. Keep each deliverable for your portfolio.
            """)

        with gr.Column(scale=1):
          progress_output = gr.Markdown(
    value=update_progress(
        *([False] * TOTAL_TOPICS)
    )
)


    # ========================================================
    # BEGINNER, INTERMEDIATE AND ADVANCED SECTIONS
    # ========================================================

    for level_number, level in enumerate(
        ["Beginner", "Intermediate", "Advanced"],
        start=1
    ):

        level_data = ROADMAP[level]
        level_color = COLORS[level]

        # Only Beginner is visible when the app starts
        with gr.Column(
            visible=(level == "Beginner")
        ) as level_section:

            display_sections.append(level_section)

            gr.HTML(f"""
            <div
                class="level-summary"
                style="border-top: 6px solid {level_color};"
            >

                <h2>
                    Level {level_number}: {level}
                </h2>

                <p>
                    {level_data["summary"]}
                </p>

                <p>
                    <strong>Estimated completion time:</strong>
                    {level_data["time"]}
                </p>

            </div>
            """
            )

            for topic_number, topic in enumerate(
                level_data["topics"],
                start=1
            ):

                topic_id = (
                    f"{level_number}.{topic_number}"
                )

                topic_title = topic[0]
                concepts = topic[1]
                practice = topic[2]
                deliverable = topic[3]

                with gr.Accordion(
                    label=f"{topic_id} — {topic_title}",
                    open=(
                        level == "Beginner"
                        and topic_number == 1
              ),
              elem_classes=["learning-topic"]
          ):


                    gr.Markdown(
                        topic_markdown(
                            topic_id,
                            topic_title,
                            concepts,
                            practice,
                            deliverable,
                            level_color
                        )
                    )

                    completed_checkbox = gr.Checkbox(
                        label=(
                            "I completed this topic "
                            "and its practical exercise"
                        ),
                        value=False
                    )

                    checkbox_components.append(
                        completed_checkbox
                    )


    # ========================================================
    # TOOLS LANDSCAPE SECTION
    # ========================================================

    with gr.Column(
        visible=False
    ) as tools_section:

        display_sections.append(tools_section)

        gr.Markdown("""
# Generative AI Tools Landscape

Select a category to view the available tools.

**Note:** Prices and free plans may change. Always verify the
latest information on the official platform website.
        """)

        for category, items in TOOLS.items():

            with gr.Accordion(
                label=category,
                open=False
            ):

                tools_text = ""

                for tool_name, access_type in items:

                    tools_text += (
                        f"### {tool_name}\n\n"
                        f"**Access:** {access_type}\n\n"
                        "---\n\n"
                    )

                gr.Markdown(tools_text)


    # ========================================================
# DROPDOWN EVENT
# ========================================================
level_selector.change(
    fn=change_section,
    inputs=level_selector,
    outputs=display_sections,
)

# ========================================================
# PROGRESS EVENTS
# ========================================================
print("Total checkboxes created:", len(checkbox_components))

for checkbox in checkbox_components:
    checkbox.change(
        fn=update_progress,
        inputs=checkbox_components,
        outputs=progress_output,
    )

# ========================================================
# RESET BUTTON
# ========================================================
reset_button = gr.Button("Reset All Progress", variant="secondary")


def reset_all():
    """Clears every checkbox and resets progress."""
    num_boxes = len(checkbox_components)
    empty_values = [False] * num_boxes
    # If your update_progress function takes N booleans and returns a string/markdown:
    reset_progress_text = update_progress(*empty_values)
    return tuple(empty_values) + (reset_progress_text,)


reset_button.click(
    fn=reset_all,
    inputs=None,
    outputs=checkbox_components + [progress_output],
)

# ============================================================
# LAUNCH APPLICATION
# ============================================================
if __name__ == "__main__":
    # Use this for Google Colab testing:
    app.launch()
