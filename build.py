import os
import json
import markdown
import time
from datetime import datetime


ROOT = os.path.dirname(__file__)
RAW_DATA_DIRECTORY = os.path.join(ROOT, 'raw')
DATA_FILE_NAME = 'data.json'
ABSTRACT_FILE_NAME = 'abstract.md'
BODY_FILE_NAME = 'body.md'
TEMPLATE_POST_CONTENT_DIRECTORY = os.path.join(
    ROOT,
    'template_post_content.html'
)
TEMPLATE_INDEX_CONTENT_DIRECTORY = os.path.join(
    ROOT,
    'template_index_content.html'
)
TEMPLATE_PAGE_DIRECTORY = os.path.join(ROOT, 'template_page.html')
TEMPLATE_TRUNCATED_POST_DIRECTORY = os.path.join(
    ROOT,
    'template_truncated_post.html'
)
OUTPUT_DIRECTORY = ROOT
NUMBER_OF_POSTS_ON_INDEX = 5
HOME_TITLE = 'Right. Why?'
HOME_ABSTRACT = 'Just some words about some things. A blog by James Wright, \
    a member of the species homo-sapiens, who happens to call Sol 3 home.'
MATHJAX_SCRIPTS = '''
    <script type='text/x-mathjax-config'>
        MathJax.Hub.Config({tex2jax: {inlineMath: [['\\(','\\)']]}});
    </script>
    <script
        type='text/javascript'
        async
        src='https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.2/MathJax.js?config=TeX-AMS_CHTML'>
    </script>
    '''
INDEX_STATIC_DIRECTORY = 'static'
POST_STATIC_DIRECTORY = '../static'
# The above to variables are not for file paths, but web links, so, don't need
# to be joined with os.path.join.


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
            requires_maths_scripts = post_data['requires_maths_scripts']
            requires_maths_scripts_for_abstract = post_data[
                'requires_maths_scripts_for_abstract'
            ]

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
                'body_html': body_html,
                'requires_maths_scripts': requires_maths_scripts,
                'requires_maths_scripts_for_abstract': \
                    requires_maths_scripts_for_abstract
            }
        )

    return posts


def build_pages(posts):
    """
    Parses all the pages, and places the output in the correct directory.
    """
    for post in posts:
        with open(TEMPLATE_POST_CONTENT_DIRECTORY) as template_file:
            post_content = template_file.read().format(
                title=post['post_name'],
                time=post['post_time'],
                abstract=post['abstract_html'],
                post_body=post['body_html']
            )

        with open(TEMPLATE_PAGE_DIRECTORY) as template_file:
            whole_post = template_file.read().format(
                title=post['post_name'] + ' | ',
                static_directory=POST_STATIC_DIRECTORY,
                extra_scripts=MATHJAX_SCRIPTS if \
                    post['requires_maths_scripts'] else '',
                content=post_content
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
    with open(TEMPLATE_PAGE_DIRECTORY) as template_file:
        page_template = template_file.read()
    with open(TEMPLATE_INDEX_CONTENT_DIRECTORY) as template_file:
        index_template = template_file.read()
    with open(TEMPLATE_TRUNCATED_POST_DIRECTORY) as template_file:
        truncated_post_template = template_file.read()

    truncated_posts_html = ''
    requires_maths_scripts_for_abstract = False
    for post in sorted(posts, key=lambda post: post['post_time'], \
            reverse=True)[:NUMBER_OF_POSTS_ON_INDEX]:
        truncated_posts_html += truncated_post_template.format(
            link=post['post_name'].lower().replace(' ', '-'),
            title=post['post_name'],
            time=post['post_time'],
            abstract=post['abstract_html']
        )
        if post['requires_maths_scripts_for_abstract']:
            requires_maths_scripts_for_abstract = True

    index_content = index_template.format(
        title=HOME_TITLE,
        description=HOME_ABSTRACT,
        post_list=truncated_posts_html
    )

    whole_index = page_template.format(
        title='',
        static_directory=INDEX_STATIC_DIRECTORY,
        extra_scripts=MATHJAX_SCRIPTS if requires_maths_scripts_for_abstract \
            else '',
        content=index_content
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
    with open(TEMPLATE_PAGE_DIRECTORY) as template_file:
        page_template = template_file.read()
    with open(TEMPLATE_TRUNCATED_POST_DIRECTORY) as template_file:
        truncated_post_template = template_file.read()

    truncated_posts_html = ''
    requires_maths_scripts_for_abstract = False
    for post in sorted(posts, key=lambda post: post['post_time'], reverse=True):
        truncated_posts_html += truncated_post_template.format(
            link=post['post_name'].lower().replace(' ', '-'),
            title=post['post_name'],
            time=post['post_time'],
            abstract=post['abstract_html']
        )
        if post['requires_maths_scripts_for_abstract']:
            requires_maths_scripts_for_abstract = True

    whole_archive = page_template.format(
        title='ARCHIVE | ',
        static_directory=INDEX_STATIC_DIRECTORY,
        extra_scripts=MATHJAX_SCRIPTS if requires_maths_scripts_for_abstract \
            else '',
        content=truncated_posts_html
    )

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

    time_string = str(
        year + microseconds_into_this_year / microseconds_in_this_year
    )

    # Offsets due to timezone.
    if time.localtime().tm_isdst == 0:
        # If not in daylight savings.
        microseconds_offset = time.timezone * -1000000
    else:
        # If daylight savings.
        microseconds_offset = time.altzone * -1000000
    year_offset = microseconds_offset / microseconds_in_this_year

    offset_string = ('+' if year_offset >= 0 else '') + str(year_offset)

    return time_string[:16].ljust(16) + offset_string[:16].ljust(16)


if __name__ == '__main__':
    build()
