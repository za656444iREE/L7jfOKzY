# 代码生成时间: 2025-09-21 01:45:16
import scrapy
def get_ui_component(library_name, component_name, url):
    """
    Fetches a specific UI component from a user interface component library.
    
    Args:
        library_name (str): The name of the UI component library.
        component_name (str): The name of the UI component to fetch.
        url (str): The URL of the UI component library.
    
    Returns:
        str or None: The HTML code of the UI component if found, otherwise None.
    """
    try:
        # Initialize Scrapy Selector
        component_selector = scrapy.Selector(text='')
        
        # Fetch the component from the library
        response = scrapy.Request(url, callback=lambda r: component_selector.replace_with(r.body_as_unicode()))
        
        # Wait for the response and get the component
        component = response.get()
        
        # Extract the component based on its name
        component_html = component_selector.css(f'div#{component_name}::text').get()
        
        # Return the component HTML if found
        if component_html:
            return component_html
        else:
            return None
    except Exception as e:
        # Handle any exceptions that occur during the process
        print(f"An error occurred: {e}")
        return None

if __name__ == '__main__':
    # Example usage of the get_ui_component function
    LIBRARY_NAME = "Bootstrap"
    COMPONENT_NAME = "alert"
    URL = "https://getbootstrap.com/docs/5.3/components/alerts/"
    
    component_html = get_ui_component(LIBRARY_NAME, COMPONENT_NAME, URL)
    if component_html:
        print(f"Fetched UI component: {LIBRARY_NAME} - {COMPONENT_NAME}")
        print(component_html)
    else:
        print("UI component not found.")