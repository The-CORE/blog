import os
import json
import markdown


ROOT = os.path.dirname(__file__)
RAW_DATA_DIRECTORY = os.path.join(ROOT, 'raw')
DATA_FILE_NAME = 'data.json'
ABSTRACT_FILE_NAME = 'abstract.md'
BODY_FILE_NAME = 'body.md'
TEMPLATE_DIRECTORY = os.path.join(ROOT, 'template.html')
OUTPUT_DIRECTORY = ROOT


def build():
    """
    Builds the site.
    """
    build_pages()
    build_index()


def build_pages():
    """
    Parses all the pages, and places the output in the correct directory.
    """
    for folder in os.listdir(RAW_DATA_DIRECTORY):
        folder_directory = os.path.join(RAW_DATA_DIRECTORY, folder)

        data_directory = os.path.join(folder_directory, DATA_FILE_NAME)
        abstract_directory = os.path.join(folder_directory, ABSTRACT_FILE_NAME)
        body_directory = os.path.join(folder_directory, BODY_FILE_NAME)

        with open(data_directory) as post_data_json_file:
            post_data = json.load(post_data_json_file)
            post_name = post_data['name']
            post_time = post_data['time']

        with open(abstract_directory) as post_abstract_markdown_file:
            abstract_html = markdown.markdown(post_abstract_markdown_file.read())

        with open(body_directory) as post_body_markdown_file:
            body_html = markdown.markdown(post_body_markdown_file.read())

        with open(TEMPLATE_DIRECTORY) as post_template_file:
            whole_post = post_template_file.read().format(
                post_name,
                post_name,
                post_time,
                abstract_html,
                body_html
            )

        post_output_directory = os.path.join(
            OUTPUT_DIRECTORY,
            post_name,
            'index.html'
        )
        os.makedirs(os.path.dirname(post_output_directory), exist_ok=True)
        with open(post_output_directory, 'w') as post_output_file:
            post_output_file.write(whole_post)


def build_index():
    """
    Build pages should be called first. Based on all the already built pages,
    this constructs an index page.
    """
    pass


if __name__ == '__main__':
    build()
