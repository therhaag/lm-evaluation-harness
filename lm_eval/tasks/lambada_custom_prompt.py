from lm_eval.tasks.lambada import LAMBADA


class LAMBADA_CP(LAMBADA):
    VERSION = 0
    def doc_to_text(self, doc):
        return "###\nParagraph:\n" + doc['text'].rsplit(' ', 1)[0] + "\nCompletion:"

    def doc_to_target(self, doc):
        return " " + doc['text'].rsplit(' ', 1)[1]
    
    def fewshot_description(self):
        return "A bot completes paragraphs of text with a single word that best completes the last sentence."