![LLMScraping_cropped](https://github.com/user-attachments/assets/94391e37-6d54-4e26-b865-996c6a227128)

<p align="center">
    <img src="https://img.shields.io/github/license/ShubhranshuArya/LLM-based-web-scraping?style=flat&logo=opensourceinitiative&logoColor=white&color=FFD21E" alt="license">
    <img src="https://img.shields.io/github/last-commit/ShubhranshuArya/LLM-based-web-scraping?style=flat&logo=git&logoColor=white&color=FFD21E" alt="last-commit">
    <img src="https://img.shields.io/github/languages/top/ShubhranshuArya/LLM-based-web-scraping?style=flat&color=FFD21E" alt="repo-top-language">
    <img src="https://img.shields.io/github/languages/count/ShubhranshuArya/LLM-based-web-scraping?style=flat&color=FFD21E" alt="repo-language-count">
</p>

## Table of Contents

- [ What Does This App Do?](#-overview)
- [ App Features](#-app-features)
- [ Project Structure](#-project-structure)
  - [ Project Index](#-project-index)
- [ Run The Project](#-run-the-project)
  - [ Prerequisites](#-prerequisites)
  - [ Installation](#-installation)
  - [ Usage](#-usage)
  - [ Testing](#-testing)
- [ Future Work](#-future-work)
- [ Contributing](#-contributing)

</details>
<hr>

## What Does This App Do?

Large Language Models(LLMs) are revolutionizing the way users interact with the internet. As data is an integral part of any company/project, why not leverage the power of LLMs to collect publicly available data in a fraction of a second? That's exactly what this project does, it utilizes the Ollama 3.1 language model (by Meta) along with Selenium for precise data extraction from Chrome. Its core features include efficient HTML content processing and accurate information retrieval. Ideal for developers seeking streamlined web scraping and content parsing, this project enhances user experience and boosts productivity.

---

## App Features

|     |      Feature      | Summary                                                                                                                                                                                                                                                                                                                                                                                          |
| :-- | :---------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ⚙️  | **Architecture**  | <ul><li>Utilizes **Scraping Browser** for web scraping, extracting and cleaning HTML body content efficiently.</li><li>Integrates **Ollama language model** for accurate information extraction from text content.</li><li>Enables content parsing within a **Streamlit app** for interactive exploration of scraped content sections.</li></ul>                                                 |
| 🔩  | **Code Quality**  | <ul><li>Well-structured codebase with clear separation of concerns between scraping, parsing, and app functionality.</li><li>Follows PEP 8 guidelines for Python code formatting.</li><li>Includes comprehensive unit tests using **pytest** for code reliability.</li></ul>                                                                                                                     |
| 📄  | **Documentation** | <ul><li>Primary language: **Python** with detailed documentation in Python and text files.</li><li>Package management using **pip** and **requirements.txt** for easy dependency installation.</li><li>Clear installation and usage commands are provided for easy setup and execution.</li></ul>                                                                                                    |
| 🔌  | **Integrations**  | <ul><li>Integrates with **Scraping Browser**, **Ollama language model**, and **Streamlit app** for seamless web scraping, content extraction, and user interaction.</li><li>Uses **html5lib**, **beautifulsoup4**, **selenium**, and other libraries for efficient web scraping.</li><li>Integration with **langchain** and **langchain_ollama** for language processing capabilities.</li></ul> |
| 🧩  |  **Modularity**   | <ul><li>Modular design allowing easy extension and maintenance of scraping, parsing, and app components.</li><li>Separate files like `scraper.py`, `parse.py`, and `main.py` for distinct functionalities.</li><li>Encourages code reusability and scalability through modular architecture.</li></ul>                                                                                           |
| ⚡️ |  **Performance**  | <ul><li>Efficient web scraping and content extraction process using **Scraping Browser** and optimized parsing with **Ollama language model**.</li><li>Streamlit app provides a responsive and interactive user experience for exploring scraped content.</li><li>Optimized codebase for faster processing and data extraction.</li></ul>                                                        |
| 🛡️  |   **Security**    | <ul><li>Follows best practices for web scraping security to prevent data breaches and unauthorized access.</li><li>Secure handling of user input URLs and content to avoid potential vulnerabilities.</li><li>Regular updates and monitoring for security vulnerabilities in dependencies.</li></ul>                                                                                             |

---

## Project Structure

```sh
└── LLM-based-web-scraping/
    ├── LICENSE
    ├── README.md
    ├── main.py
    ├── parse.py
    ├── requirements.txt
    └── scraper.py
```

---

## Run The Project

### 1. Prerequisites

This project requires Python 3.9 or higher, and one of the following installation methods:

| Requirement                          | Details                          |
|--------------------------------------|----------------------------------|
| • [python](https://www.python.org/) ≥3.9       | Core runtime                     |
| **Installation Method**              |                                  |
| • [pip](https://pip.pypa.io/en/stable/)                    | Default Python package manager   |

### 2. Clone the repository

```sh
git clone https://github.com/ShubhranshuArya/LLM-based-web-scraping
```

### 3. Install the project dependencies:
It's advised to create a virtual environment and then install all the required dependencies for the project.
Follow this to build one 👉 [venv](https://youtu.be/GZbeL5AcTgw)

```sh
pip install -r requirements.txt
```

### 4. Download Ollama:
In order to add the power of LLM in this project, you need to download Ollama in your system.
Do this by following the official docs 👉 [Ollama](https://ollama.com/download)

### 5. Install Ollama:
Once downloaded, follow the instructions to add Ollama to your system.Run this command to check if Ollama is installed successfully

```sh
ollama -v
```

If the terminal says `command not found: ollama` then you're cooked. Select the model according to your system. Check it here 👉 [Ollama](https://github.com/ollama/ollama?tab=readme-ov-file#model-library)

This project uses `Ollama 3.1` and here's how you can download it:

```sh
ollama run llama3.1
```

### 6. Proxy Skipping Tool Integration:
Almost every website these days has a proxy detection system which blocks web scraping. To overcome this, the project uses [BrightData](https://brightdata.com/), a free service to cycle around IPs to access the website content for scraping. Simply create an account and add a `Scraping Browser`. Create a project and you'll get auth details which add to the project by creating a `.env` file and connecting with `scraper.py` file.

🚨 This service is free only for 3 days.

### 7. Run Streamlit:
Once everything is in place, run the streamlit frontend to test the app.

```sh
streamlit run main.py
```
---

## Future Work

- List things that can be done in future.

---

## Contributing

- **💬 [Join the Discussions](https://github.com/ShubhranshuArya/LLM-based-web-scraping/discussions)**: Share your insights, provide feedback, or ask questions.
- **🐛 [Report Issues](https://github.com/ShubhranshuArya/LLM-based-web-scraping/issues)**: Submit bugs found or log feature requests for the `LLM-based-web-scraping` project.
- **💡 [Submit Pull Requests](https://github.com/ShubhranshuArya/LLM-based-web-scraping/blob/main/CONTRIBUTING.md)**: Review open PRs, and submit your own PRs.

### Contributing Guidelines

1. **Fork the Repository**: Start by forking the project repository to your github account.
2. **Clone Locally**: Clone the forked repository to your local machine using a git client.
   ```sh
   git clone https://github.com/ShubhranshuArya/LLM-based-web-scraping
   ```
3. **Create a New Branch**: Always work on a new branch, giving it a descriptive name.
   ```sh
   git checkout -b new-feature-x
   ```
4. **Make Your Changes**: Develop and test your changes locally.
5. **Commit Your Changes**: Commit with a clear message describing your updates.
   ```sh
   git commit -m 'Implemented new feature x.'
   ```
6. **Push to github**: Push the changes to your forked repository.
   ```sh
   git push origin new-feature-x
   ```
7. **Submit a Pull Request**: Create a PR against the original project repository. Clearly describe the changes and their motivations.
8. **Review**: Once your PR is reviewed and approved, it will be merged into the main branch. Congratulations on your contribution!


### Contributor Graph
<br>
<p align="left">
   <a href="https://github.com{/ShubhranshuArya/LLM-based-web-scraping/}graphs/contributors">
      <img src="https://contrib.rocks/image?repo=ShubhranshuArya/LLM-based-web-scraping">
   </a>
</p>

---
