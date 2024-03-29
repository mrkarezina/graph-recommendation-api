import newspaper
import requests
from article_downloader import Article

from config import natural_language_function_base_url, retry_article_parse_tokens


def download(url, clean_doc=True):
    """
    Tries to download + parse the article using newspaper
    :param url:
    :return:
    """

    article = Article(url)
    is_valid = True

    try:
        article.download()
        article.parse(clean_doc=clean_doc)
    except newspaper.article.ArticleException:
        print("Download error")
        is_valid = False

    return article, is_valid


def fetch_article(url):
    """
    Downloads the article from URL
    :param url:
    :return:
    """

    article, is_valid = download(url)

    if is_valid:

        # Retry downloading article without cleaning
        if len(article.text.split()) < retry_article_parse_tokens:
            article, is_valid = download(url, clean_doc=False)

        title = article.title
        text = article.text
        date = article.publish_date
        img = article.top_image

        return {
            'text': text,
            'title': title,
            'date': str(date),
            'img_url': img,
            'url': url,
        }


def process_language(text, processor_id):
    """
    Fetch from language processing API (cloud function)
    :param text:
    :return:
    """

    # The language processing seems to fail without acsii decoding, ie remove emoji and chinese characters
    request = {
        'text': text.encode("ascii", errors="ignore").decode()
    }

    response = requests.post(natural_language_function_base_url.format(processor_id),
                             json=request)

    return response.json()


def article_processor(url, processor_id):
    """
    Used to process and enrich text to be suitable for knowledge graph
    :param text:
    :return:
        Returns dict containing enritched entites dict, document embedding, and summary
    """

    is_valid = True

    article_dict = fetch_article(url)

    try:
        if len(article_dict['text'].split()) < 100:
            is_valid = False

        processed_language = process_language(
            article_dict['text'], processor_id)

        article_dict['summary'] = processed_language['summary']
        article_dict['embedding'] = processed_language['embedding']
    except Exception as e:
        print(e)
        is_valid = False

    if not is_valid:
        print("Failed processing URL: {0}".format(url))

    return article_dict, is_valid
