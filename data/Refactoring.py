from collections import Counter

class Refactoring(object):

    def __init__(self, repository, commit):
        self.repository = repository
        self.commit = commit
        self.extract_method_source_class = []
        self.extract_superclass_source_class = []
        self.move_method_target_class = []
        self.move_method_source_class = []
        self.push_down_method_target_class = []
        self.push_down_method_source_class = []
        self.pull_up_method_target_class = []
        self.pull_up_method_source_class = []
        self.inline_method_source_class = []

        self.extract_method_source_method = []
        self.move_method_source_method = []
        self.push_down_method_source_method = []
        self.pull_up_method_source_method = []
        self.inline_method_source_method = []

    def append(self, refactoring_name, key, value):
        method_name = refactoring_name + "_" + key
        attribute = getattr(self, method_name, lambda: "Invalid call")
        if type(value) is list:
            for x in value:
                attribute.append(x)
        else:
            attribute.append(value)

    def show_information(self):
        #print(self.repository)
        #print(self.commit)
        c = dict(Counter(self.extract_method_source_class))
        #commits with more than 10 refactored elements
        if len(c.values()) > 5:
            print("Extract Method")
            print(c.values())

        c = dict(Counter(self.extract_superclass_source_class))
        #commits with more than 10 refactored elements
        if len(c.values()) > 5:
            print("Extract Superclass")
            print(c.values())

        c = dict(Counter(self.move_method_source_class))
        #commits with more than 10 refactored elements
        if len(c.values()) > 5:
            print("Move Method")
            print(c.values())

        c = dict(Counter(self.inline_method_source_class))
        #commits with more than 10 refactored elements
        if len(c.values()) > 5:
            print("Inline Method")
            print(c.values())

        c = dict(Counter(self.pull_up_method_source_class))
        #commits with more than 10 refactored elements
        if len(c.values()) > 5:
            print("Pull Up Method")
            print(c.values())

        c = dict(Counter(self.push_down_method_source_class))
        #commits with more than 10 refactored elements
        if len(c.values()) > 5:
            print("Push Down Method")
            print(c.values())