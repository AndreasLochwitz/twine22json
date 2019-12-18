
class TextBuffer:

    def __init__(self, text):
        self.text_content = text
        self.search_pos = 0

    def get_text_part(self, start_part, end_part):
        start_pos = self.text_content.find(start_part, self.search_pos)
        if start_pos > -1:
            end_pos = self.text_content.find(end_part, start_pos + len(start_part))
            if end_pos > -1:
                self.search_pos = end_pos + 1
                return self.text_content[start_pos + len(start_part):end_pos]
        return False
