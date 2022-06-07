from dash import Input, Output, callback, State

@callback(
    Output('html-dash-output', 'children'),
    [Input('content-html', 'value')],
    [Input('submit-html-convert', 'n_clicks')])
def display_convert(value, n_clicks):
    if n_clicks > 0:
        # print("value: ", value)
        convert_content = convert_html_to_dash(value)
        print("convert_content: ", str(convert_content))
        # return str(convert_content)
    return "Entrer du html"


def convert_html_to_dash(html_code):
    """Convert standard html to Dash components"""
    from xml.etree import ElementTree
    from dash import html

    def parse_css(css):
        """Convert a style in ccs format to dictionary accepted by Dash"""
        return {k: v for style in css.strip(";").split(";") for k, v in [style.split(":")]}

    def _convert(elem):
        comp = getattr(html, elem.tag.capitalize())
        children = [_convert(child) for child in elem]
        if not children:
            children = elem.text
        attribs = elem.attrib.copy()
        if "class" in attribs:
            attribs["className"] = attribs.pop("class")
        attribs = {k: (parse_css(v) if k == "style" else v) for k, v in attribs.items()}

        return comp(children=children, **attribs)

    et = ElementTree.fromstring(html_code)

    return _convert(et)