class DictionariesBuilder:

    def __init__(self):
        pass

    def build_move_method_dict(self, refactoring_description, r):
        source_class, source_method, target_class = self.build_move_refactorings_dict(refactoring_description, r, "move_method")
        refactoring_dict = {
            "type": "move_method",
            "source_class": source_class,
            "source_method": source_method,
            "target_class": target_class
        }

        return refactoring_dict

    def build_pull_up_method_dict(self, refactoring_description, r):
        source_class, source_method, target_class = self.build_move_refactorings_dict(refactoring_description, r, "pull_up_method")
        refactoring_dict = {
            "type": "pull_up_method",
            "source_class": source_class,
            "source_method": source_method,
            "target_class": target_class
        }

        return refactoring_dict

    @staticmethod
    def build_move_refactorings_dict(refactoring_description, r, type):
        split = refactoring_description.strip().split()
        split_len = len(split)
        source_class = split[split_len - 1]
        source_method = ""
        target_class = ""
        for j in range(split_len):
            if split[j] != "from":
                source_method += split[j] + " "
            else:
                j = j + 2  # skip unnecessary words
                break

        source_class = split[j] + " "

        while j in range(split_len):
            if split[j] != "from":
                j = j + 1
            else:
                j = j + 2
                target_class = split[j] + " "
                break

        source_class = source_class.strip()
        target_class = target_class.strip()
        source_method = source_method.strip()

        r.append(type, "source_class", source_class)
        r.append(type, "source_method", source_method)
        r.append(type, "target_class", target_class)

        return source_class, source_method, target_class

    def build_push_down_method_dict(self, refactoring_description, r):
        source_class, source_method, target_class = self.build_move_refactorings_dict(refactoring_description, r, "push_down_method")
        refactoring_dict = {
            "type": "push_down_method",
            "source_class": source_class,
            "source_method": source_method,
            "target_class": target_class
        }

        return refactoring_dict

    def build_extract_superclass_dict(self, refactoring_description, r):
        split = refactoring_description.strip().split()
        split_len = len(split)
        target_class = split[0]
        source_classes = []
        j = 3
        while j in range(split_len):
            source_classes.append(split[j].strip("#[],"))
            j = j + 1

        target_class = target_class.strip()
        refactoring_dict = {
            "type": "extract_superclass",
            "target_class": target_class,
            "source_class": source_classes
        }

        r.append("extract_superclass", "source_class", source_classes)

        return refactoring_dict

    def build_inline_method_dict(self, refactoring_description, r):
        split = refactoring_description.strip().split()
        split_len = len(split)
        source_class = split[split_len - 1]
        method1 = ""
        method2 = ""
        for j in range(split_len):
            if split[j] != "inlined":
                method1 += split[j] + " "
            else:
                j = j + 2  # skip unnecessary words
                break

        while j in range(split_len):
            if split[j] != "in":
                method2 += split[j] + " "
                j = j + 1
            else:
                break

        source_class = source_class.strip()
        method1 = method1.strip()
        method2 = method2.strip()

        refactoring_dict = {
            "type": "inline_method",
            "source_class": source_class,
            "method1": method1,
            "method2": method2
        }

        r.append("inline_method", "source_class", source_class)
        r.append("inline_method", "source_method", method1)
        r.append("inline_method", "source_method", method2)

        return refactoring_dict

    def build_extract_method_dict(self, refactoring_description, r):
        new_method, source_class, source_method = self.get_extract_method_elements(refactoring_description)

        source_class = source_class.strip()
        new_method = new_method.strip()
        source_method = source_method.strip()

        refactoring_dict = {
            "type": "extract_method",
            "source_class": source_class,
            "source_method": source_method,
            "new_method": new_method
        }

        r.append("extract_method", "source_class", source_class)
        r.append("extract_method", "source_method", source_method)

        return refactoring_dict

    @staticmethod
    def get_extract_method_elements(refactoring_description):
        split = refactoring_description.strip().split()
        split_len = len(split)
        source_class = split[split_len - 1]
        new_method = ""
        source_method = ""
        for j in range(split_len):
            if split[j] != "extracted":
                new_method += split[j] + " "
            else:
                j = j + 2  # skip unnecessary words
                break
        while j in range(split_len):
            if split[j] != "in":
                source_method += split[j] + " "
            else:
                break
            j = j + 1
        return new_method, source_class, source_method

    def build_extract_class_dict(self, refactoring_description, r):
        pass

    def build_extract_subclass_dict(self, refactoring_description, r):
        pass

    def build_inline_class_dict(self, refactoring_description, r):
        pass
