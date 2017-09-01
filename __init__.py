import os
import json
import markdown
from datetime import datetime


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

        with open(abstract_directory) as abstract_markdown_file:
            abstract_html = markdown.markdown(abstract_markdown_file.read())

        with open(body_directory) as body_markdown_file:
            body_html = markdown.markdown(body_markdown_file.read())

        with open(TEMPLATE_DIRECTORY) as template_file:
            whole_post = template_file.read().format(
                post_name,
                post_name,
                post_time,
                abstract_html,
                body_html
            )

        post_output_directory = os.path.join(
            OUTPUT_DIRECTORY,
            post_name.lower().replace(' ', '-'),
            'index.html'
        )
        os.makedirs(os.path.dirname(post_output_directory), exist_ok=True)
        with open(post_output_directory, 'w') as post_output_file:
            post_output_file.write(whole_post)


def build_index():
    """
    Constructs and index page.
    """
    pass


def get_year_decimal_time():
    """
    Gets the current time as a decimal of the year.
    """
    now = datetime.now()
    year, month, day, hour, minute, second, microsecond = now.year, now.month, \
        now.day, now.hour, now.minute, now.second, now.microsecond
    is_leap_year = year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
    days_in_months = [
        None,
        31,
        29 if is_leap_year else 28,
        31,
        30,
        31,
        30,
        31,
        31,
        30,
        31,
        30,
        31
    ]

    # 24 * 60 * 60 * 1000000 = 86400000000
    # Also below is just for show really.
    microseconds_in_this_year = (366 if is_leap_year else 365) * 86400000000
    days_into_this_year = day + sum(days_in_months[1:month])
    hours_into_this_year = days_into_this_year * 24 + hour
    minutes_into_this_year = hours_into_this_year * 60 + minute
    seconds_into_this_year = minutes_into_this_year * 60 + second
    microseconds_into_this_year = seconds_into_this_year * 1000000 + microsecond

    return year + microseconds_into_this_year / microseconds_in_this_year


if __name__ == '__main__':
    build()
