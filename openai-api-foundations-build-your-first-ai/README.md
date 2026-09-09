# OpenAI API Foundations: Build Your First AI Application
This is the repository for the LinkedIn Learning course `OpenAI API Foundations: Build Your First AI Application`. The full course is available from [LinkedIn Learning][lil-course-url].

![course-name-alt-text][lil-thumbnail-url] 

_See the readme file in the main branch for updated instructions and information._
## About This Course

The OpenAI platform gives developers four core APIs that cover text, images, audio, and search. This course teaches all four by building a real project: an Internal Knowledge Search Tool that answers employee questions using text generation, vision, voice, structured output, and semantic search.
- Use the Responses API to generate text, analyze images, process documents, call functions, and return structured output from a single endpoint.
- Connect the Responses API to external data sources using built-in web search, custom function calling, and the Model Context Protocol (MCP).
- Use the Audio API to transcribe speech to text and convert text to speech within an application.
- Use the Images API to generate images from text prompts.
- Use the Embeddings API to build semantic search that retrieves documents from natural language questions.

## Project

Throughout this course you build an **Internal Knowledge Search Tool**. Employees ask questions in plain language and get structured answers sourced from company documents. The tool handles text, images, PDFs, voice input, audio output, visual diagrams, and semantic search across a knowledge base.

## APIs Covered

1. **Responses API** - Text generation, vision, PDF input, structured outputs, function calling, web search, MCP, streaming
2. **Audio API** - Speech-to-text (Whisper), text-to-speech (gpt-4o-mini-tts)
3. **Images API** - Image generation with gpt-image-1
4. **Embeddings API** - Vector creation with text-embedding-3-small, semantic search

## Requirements

- Python 3.12+
- An [OpenAI API key](https://platform.openai.com/api-keys)
- A [Context7 API key](https://context7.com/dashboard) 
- GitHub Codespaces (recommended) or a local Python environment

## Getting Started

1. Open this repository in GitHub Codespaces by clicking the green **Code** button and selecting **Create codespace on main**. The devcontainer will automatically install all dependencies.

2. Copy the environment file and add your API keys:

```
cp .env.example .env
```

3. Open `.env` and paste in your keys:

```
OPENAI_API_KEY=sk-proj-your-key-here
CONTEXT7_API_KEY=your-context7-key-here
```

## Structure

Each video has its own folder. Inside each folder you'll find two versions of every lesson:

- **begin** files have TODO comments for you to complete as you follow along
- **end** files have the finished code you can reference or run directly

```
├── .env.example
├── requirements.txt
├── CH01/
│   ├── data/
│   │   ├── error.png
│   │   └── company_vpn_policy.pdf
│   ├── 01_01_begin.py
│   ├── 01_01_end.py
│   ├── 01_02_begin.py
│   └── 01_02_end.py
├── CH02/
│   ├── 02_01_begin.py
│   ├── 02_01_end.py
│   ├── 02_02_begin.py
│   ├── 02_02_end.py
│   ├── 02_03_begin.py
│   ├── 02_03_end.py
│   ├── 02_04_begin.py
│   └── 02_04_end.py
├── CH03/
│   ├── data/
│   │   └── employee_question.wav
│   ├── output/
│   ├── 03_01_begin.py
│   ├── 03_01_end.py
│   ├── 03_02_begin.py
│   ├── 03_02_end.py
│   ├── 03_03_begin.py
│   └── 03_03_end.py
└── CH04/
    ├── data/
    │   └── knowledge_base.json (generated in 04_01)
    ├── output/
    ├── 04_01_begin.py
    ├── 04_01_end.py
    ├── 04_02_begin.py
    ├── 04_02_end.py
    ├── 04_03_begin.py
    └── 04_03_end.py
```

## Running the Code

Navigate to the chapter folder before running any script:

```
cd CH01
python 01_01_end.py
```

## Author
Kesha Williams is a distinguished tech leader and innovator specializing in AI and machine learning (ML).

Kesha works at the intersection of AI architecture, engineering, and strategy, with 25+ years of experience designing and delivering complex software and AI systems. She is the founder and managing partner of Keysoft, where she leads AI advisory, engineering, and enablement services that help organizations turn AI ambition into operational reality. An AWS Artificial Intelligence (AI) Hero, Kesha partners with enterprises and technology leaders to adopt AI responsibly, modernize engineering practices, and build AI systems developers can trust and sustain.

Visit her other courses at: https://www.linkedin.com/learning/instructors/kesha-williams

[0]: # (Replace these placeholder URLs with actual course URLs)

[lil-course-url]: https://www.linkedin.com/learning/openai-api-foundations-build-your-first-ai-application
[lil-thumbnail-url]: https://media.licdn.com/dms/image/v2/D560DAQFTn3CCZcFvcg/learning-public-crop_675_1200/B56Z7MYwUtKYAY-/0/1781545502301?e=2147483647&v=beta&t=ym8y9QNOIipF5Jt4sC0LZ55Sxzs-nDk6moYalpNxYY4

