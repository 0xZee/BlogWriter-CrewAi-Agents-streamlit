from crewai_tools import tool
from duckduckgo_search import DDGS


class DuckSearchTool:
    def __init__(self):
        self.ddgs = DDGS()

    @tool("web search")
    def web_search(query):
        """
        Perform a web search using DuckDuckGo based on query.
        Useful for searching for information and articles.
        Args: query (str): The search query.
        Returns: list: List of search results with content and url sources.
        """
        return DDGS().text(query, max_results=10, timelimit="y")

    @tool("recent search")
    def recent_search(query):
        """
        Retrieve instant last and up to date answers from DuckDuckGo.
        Useful for getting up to date information for a query.
        Args: query (str): The search query.
        Returns: list: List of instant answers results.
        """
        #return DDGS().answers(query, timelimit='m')
        return DDGS().text(query, max_results=5, timelimit="d")

    @tool("summary search")
    def summary_search(query):
        """
        Retrieve summary from DuckDuckGo for a query.
        Useful for getting summarization for a query or topic.
        Args: query (str): The search query.
        Returns: list: List of instant answers results.
        """
        #return DDGS().answers(query, timelimit='m')
        return DDGS().answers(query)

    @tool("news search")
    def news_search(query):
        """
        Perform a last news search using DuckDuckGo for the last mounth.
        Args: query (str): The search query.
        Returns: list: List of news results, with news's content, date, source, url
        """
        return DDGS().news(query, timelimit="w", max_results=10)

    @tool("translate text")
    def translate_text(text):
        """
        Useful to get text translation to french.
        Can help provide last answer in user's native language if needed or asked.
        Args:
            query (str): The text to translate.
            source_language (str): Source language code. Defaults to 'auto'.
            target_language (str): Target language code. Defaults to 'fr'.

        Returns: str: Translated text.
        """
        return DDGS().translate(text, source_language='auto', target_language='fr')

    @tool("ai chat")
    def ai_chat(query, model='gpt-3.5'):
        """
        Initiate a chat session with DuckDuckGo AI.

        Args:
            query (str): The initial message or question to send to the AI.
            model (str): The model to use ('gpt-3.5', 'claude-3-haiku', 'llama-3-70b', 'mixtral-8x7b'). Defaults to 'gpt-3.5'.

        Returns:
            str: The response from the AI.
        """
        return DDGS().chat(query, model=model)

    @tool("image search")
    def image_search(query, region='wt-wt', safesearch='moderate', timelimit='y', size=None, color=None, type_image=None, layout=None, license_image=None, max_results=10):
        """
        Perform an image search using DuckDuckGo.

        Args:
            query (str): The search query.
            region (str): Region code. Defaults to 'wt-wt'.
            safesearch (str): Safesearch level. Defaults to 'moderate'.
            timelimit (str): Time limit for search. Defaults to None.
            size (str): Image size. Defaults to None.
            color (str): Image color. Defaults to None.
            type_image (str): Image type. Defaults to None.
            layout (str): Image layout. Defaults to None.
            license_image (str): Image license type. Defaults to None.
            max_results (int): Maximum number of results to return. Defaults to 10.

        Returns:
            list: List of image search results.
        """
        return DDGS().images(query, region=region, safesearch=safesearch, timelimit=timelimit, size=size, color=color, type_image=type_image, layout=layout, license_image=license_image, max_results=max_results)

    def video_search(query, region='wt-wt', safesearch='moderate', timelimit=None, duration=None, resolution=None, max_results=10):
        """
        Perform a video search using DuckDuckGo.

        Args:
            query (str): The search query.
            region (str): Region code. Defaults to 'wt-wt'.
            safesearch (str): Safesearch level. Defaults to 'moderate'.
            timelimit (str): Time limit for search. Defaults to None.
            duration (str): Video duration. Defaults to None.
            resolution (str): Video resolution. Defaults to None.
            max_results (int): Maximum number of results to return. Defaults to 10.

        Returns:
            list: List of video search results.
        """
        return DDGS().videos(query, region=region, safesearch=safesearch, timelimit=timelimit, duration=duration, resolution=resolution, max_results=max_results)

    def map_search(query, region='wt-wt', max_results=10):
        """
        Perform a map search using DuckDuckGo.

        Args:
            query (str): The search query.
            region (str): Region code. Defaults to 'wt-wt'.
            max_results (int): Maximum number of results to return. Defaults to 10.

        Returns:
            list: List of map search results.
        """
        return DDGS().maps(query, region=region, max_results=max_results)



