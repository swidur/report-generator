class HtmlGenerator:
    def __init__(self):
        pass

    def generate_document(self, config, results):
        document = []
        row_count = 0

        # Append title
        if config.title is not None:
            document.append(f'<h1 class="repo-title">{config.title}</h1>')

        document.append("<table>\n")

        # Append headers if present in config
        if config.headers is not None:
            document.append("\t<tr>\n")
            if config.row_numbering:
                document.append(f"\t\t<th>No.</th>\n")
            for header in config.headers:
                document.append(f"\t\t<th>{header}</th>\n")
            document.append("\t</tr>\n")

        # Append rows
        for row in results:
            row_count += 1
            if row_count % 2 == 0:
                document.append('\t<tr class="even">\n')
            else:
                document.append('\t<tr class="odd">\n')
            if config.row_numbering:
                document.append(f"\t\t<td>{row_count}</td>\n")
            for col in row:
                document.append(f"\t\t<td>{col}</td>\n")
            document.append("\t</tr>\n")

        document.append("</table>\n")

        # append default style to the HTML or style string provided by config
        if config.style == "default":
            document.append(
                "<style>"
                "table {border-collapse: collapse;}"
                "th {border: 1px solid black;background-color: #b3b3b3;font-weight: bold;}"
                "td {border: 1px solid black;padding: 2 5 2 5}"
                ".repo-title {font-size: 1.5em}"
                ".odd {background-color: #e3e3e3}"
                ".even {background-color: #ffffff}"
                "</style>")
        else:
            document.append(config.style)

        return document
