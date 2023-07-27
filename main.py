""" Main Module for starting the application.
"""


from app import App


if __name__ == "__main__":
    """ Here starts the application.
    """
    try:
        app = App()
        app.mainloop()
    except Exception as e:
        print(f"An {type(e).__name__} occurred: {str(e)}.")
