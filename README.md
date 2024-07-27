# NSAHHOA

## Introduction
Welcome to the North San Antonio Hills Homeowners Association (NSAHHOA) website repository. This project is built using [Streamlit](https://streamlit.io/) to provide a user-friendly interface for our community members. We appreciate your interest in contributing to this project!

## Table of Contents
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
- [Contributing](#contributing)
- [License](#license)


### Key Files and Directories
- **Home.py**: The main entry point for the Streamlit app.
- **pages/**: Contains individual pages for the website.
  - `00_Community_News.py`: Community news page.
  - `01_Events.py`: Events page.
  - `02_Contacts.py`: Contacts page.
  - `03_Documents.py`: Documents page.
  - `04_Committees.py`: Committees page.
- **assets/**: Contains images and other static assets.
- **.streamlit/config.toml**: Configuration file for Streamlit.
- **requirements.txt**: Lists the Python dependencies for the project.
- **LICENSE**: The MIT license for the project.

## Getting Started
To get started with development, follow these steps:

1. **Clone the repository**:
    ```sh
    git clone https://github.com/yourusername/NSAHHOA.git
    cd NSAHHOA
    ```

2. **Create a virtual environment**:
    ```sh
    python -m venv .venv
    source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`
    ```

3. **Install dependencies**:
    ```sh
    pip install -r requirements.txt
    ```

4. **Run the Streamlit app**:
    ```sh
    streamlit run Home.py
    ```

## Contributing
We welcome contributions to improve the NSAHHOA website. Here are some ways you can contribute:

1. **Fork the repository** and create your branch from `main`.
2. **Make your changes** and ensure that the app runs correctly.
3. **Commit your changes** with clear commit messages.
4. **Push to your branch** and create a Pull Request.

### Code Style
- Follow PEP 8 guidelines for Python code.
- Use meaningful variable and function names.
- Keep your code DRY (Don't Repeat Yourself).

### Adding New Pages
To add a new page:
1. Create a new Python file in the `pages/` directory.
2. Use the existing pages as a template for setting up the Streamlit configuration and layout.
3. Add your content and ensure it integrates well with the rest of the app.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact
For any questions or suggestions, feel free to reach out to the HOA board at [assistantsecretary@nsah-hoa.org](mailto:assistantsecretary@nsah-hoa.org).

Thank you for your contributions!