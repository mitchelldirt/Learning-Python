def banner_text(text: str =" ", screen_width: int =80) -> None:
    """
    Text is centered and screen width is reduced by 4 to account for
    **{string}** the asterisks on either side of your string.

    :param text: The input that the user will give. Defaults to a space
        if no input is provided.
    :param screen_width: The default width of the screen (80).
    :raises ValueError: if the supplied string is too long to fit.
    """
    if len(text) > screen_width -4:
        raise ValueError("String {0} is larger than specified width {1}"
                         .format(text, screen_width))

    if text == "*":
        print("*" * screen_width)
    else:
        output_string = "**{0}**".format(text.center(screen_width - 4))
        print(output_string)


banner_text("*", 60)
banner_text("YEET", 60)
banner_text("SKRRRRRRT", 60)
banner_text(screen_width=60)
banner_text("YUH YUH YUH", 60)
banner_text("AYYYYYEEEEE", 60)
banner_text("*", 60)
