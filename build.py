import os
import json
import markdown
from datetime import datetime


ROOT = os.path.dirname(__file__)
RAW_DATA_DIRECTORY = os.path.join(ROOT, 'raw')
DATA_FILE_NAME = 'data.json'
ABSTRACT_FILE_NAME = 'abstract.md'
BODY_FILE_NAME = 'body.md'
TEMPLATE_POST_DIRECTORY = os.path.join(ROOT, 'template_post.html')
TEMPLATE_INDEX_DIRECTORY = os.path.join(ROOT, 'template_index.html')
TEMPLATE_ARCHIVE_DIRECTORY = os.path.join(ROOT, 'template_archive.html')
TEMPLATE_TRUNCATED_POST_DIRECTORY = os.path.join(
    ROOT,
    'template_truncated_post.html'
)
OUTPUT_DIRECTORY = ROOT
NUMBER_OF_POSTS_ON_INDEX = 5
HOME_TITLE = 'Right. Why?'
HOME_ABSTRACT = 'Just some words about some things. A blog by James Wright, \
    a member of the species homo-sapiens, who happens to call Sol 3 home.'


def build():
    """
    Builds the site.
    """
    posts = _get_posts()

    build_pages(posts)
    build_index(posts)
    build_archive(posts)


def _get_posts():
    posts = []

    for folder in os.listdir(RAW_DATA_DIRECTORY):
        folder_directory = os.path.join(RAW_DATA_DIRECTORY, folder)

        data_directory = os.path.join(folder_directory, DATA_FILE_NAME)
        abstract_directory = os.path.join(folder_directory, ABSTRACT_FILE_NAME)
        body_directory = os.path.join(folder_directory, BODY_FILE_NAME)

        with open(data_directory) as post_data_json_file:
            post_data = json.load(post_data_json_file)
            post_name = post_data['name']
            post_is_new = post_data['is_new']
            post_time = decimal_time() if post_is_new else post_data['time']

        if post_is_new:
            with open(data_directory, 'w') as post_data_json_file:
                post_data['is_new'] = False
                post_data['time'] = post_time
                json.dump(post_data, post_data_json_file)

        with open(abstract_directory) as abstract_markdown_file:
            abstract_html = markdown.markdown(abstract_markdown_file.read())

        with open(body_directory) as body_markdown_file:
            body_html = markdown.markdown(body_markdown_file.read())

        posts.append(
            {
                'post_name': post_name,
                'post_time': post_time,
                'abstract_html': abstract_html,
                'body_html': body_html
            }
        )

    return posts


def build_pages(posts):
    """
    Parses all the pages, and places the output in the correct directory.
    """
    for post in posts:
        with open(TEMPLATE_POST_DIRECTORY) as template_file:

            whole_post = template_file.read().format(
                post['post_name'],
                post['post_name'],
                post['post_time'],
                post['abstract_html'],
                post['body_html']
            )

        post_output_directory = os.path.join(
            OUTPUT_DIRECTORY,
            post['post_name'].lower().replace(' ', '-'),
            'index.html'
        )
        os.makedirs(os.path.dirname(post_output_directory), exist_ok=True)
        with open(post_output_directory, 'w') as post_output_file:
            post_output_file.write(whole_post)


def build_index(posts):
    """
    Constructs an index page, containing links to the most recent posts.
    """
    with open(TEMPLATE_INDEX_DIRECTORY) as template_file:
        index_template = template_file.read()
    with open(TEMPLATE_TRUNCATED_POST_DIRECTORY) as template_file:
        truncated_post_template = template_file.read()

    truncated_posts_html = ''
    for post in sorted(posts, key=lambda post: post['post_time'], \
            reverse=True)[:NUMBER_OF_POSTS_ON_INDEX]:
        truncated_posts_html += truncated_post_template.format(
            link=post['post_name'].lower().replace(' ', '-'),
            title=post['post_name'],
            time=post['post_time'],
            abstract=post['abstract_html']
        )

    whole_index = index_template.format(
        HOME_TITLE,
        HOME_ABSTRACT,
        truncated_posts_html
    )

    index_output_directory = os.path.join(
        OUTPUT_DIRECTORY,
        'index.html'
    )
    with open(index_output_directory, 'w') as index_output_file:
        index_output_file.write(whole_index)


def build_archive(posts):
    """
    Constructs an archive page, containing links to all posts ever made.
    """
    with open(TEMPLATE_ARCHIVE_DIRECTORY) as template_file:
        archive_template = template_file.read()
    with open(TEMPLATE_TRUNCATED_POST_DIRECTORY) as template_file:
        truncated_post_template = template_file.read()

    truncated_posts_html = ''
    for post in sorted(posts, key=lambda post: post['post_time'], reverse=True):
        truncated_posts_html += truncated_post_template.format(
            link=post['post_name'].lower().replace(' ', '-'),
            title=post['post_name'],
            time=post['post_time'],
            abstract=post['abstract_html']
        )

    whole_archive = archive_template.format(truncated_posts_html)

    archive_output_directory = os.path.join(
        OUTPUT_DIRECTORY,
        'archive.html'
    )
    with open(archive_output_directory, 'w') as archive_output_file:
        archive_output_file.write(whole_archive)


def decimal_time():
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
