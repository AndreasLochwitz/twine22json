
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

    def reset(self):
        self.search_pos = 0

    def set_text(self, text):
        self.text_content = text

    def get_text(self):
        return self.text_content

    @staticmethod
    def get_parameter_data(text, parametername):
        start_pos = text.find(parametername + "=\"")
        if start_pos > -1:
            end_pos = text.find("\"", start_pos + len(parametername) +2)
            if end_pos > -1:
                return text[start_pos + len(parametername) + 2:end_pos]
        return False

    @staticmethod
    def get_text_til_end(text, parameter_name):
        start_pos = text.find(parameter_name)
        if start_pos > -1:
            return text[start_pos + len(parameter_name):]
        return False

    def replace_string(self, old_string, new_string):
        self.text_content = self.text_content.replace(old_string, new_string, 1)
        self.reset()
