from itertools import groupby
from operator import itemgetter
import json
from builder.DictionariesBuilder import DictionariesBuilder
from data.Refactoring import Refactoring
from data.data_switcher import switcher

class JsonBuilder:
    #CVS methods
    #CVS class

    def create_refactoring_dict(self, refactoring_type, refactoring_description, r):
        method_name = str(switcher.get(refactoring_type.lower()))
        if method_name != "None":
            dictionaries_builder = DictionariesBuilder()
            method = getattr(dictionaries_builder, method_name, lambda: "Invalid refactoring")
            return method(refactoring_description, r)

    def create_refactoring_list(self, repository, commit, refactorings_list, r):
        new_refactorings_list = []
        for i in refactorings_list:
            new_dict = self.create_refactoring_dict(i["type"], i["description"], r)
            if new_dict is not None:
                new_refactorings_list.append(new_dict)
        return new_refactorings_list

    def main(self):
        with open("../json/github_refactorings.json", "r") as read_file:
            dataset = json.load(read_file)

        grouper = itemgetter("repository")
        result = []  # final list of json items
        all = 0
        for k, v in groupby(sorted(dataset, key=grouper), key=grouper):
            #print(k)
            r = Refactoring(k, "")
            json_dict = {"repository": k}
            commits = []  # each json item has a list of commits
            count = 0
            for i in v:
                refactorings_list = self.create_refactoring_list(k, i["sha1"], i["refactorings"], r)
                count = count + len(refactorings_list)
                if len(refactorings_list) > 0:
                    #print(len(refactorings_list))
                    sha1_dict = {
                        "sha1": i["sha1"],
                        "author": i["author"],
                        "time": i["time"],
                        # each commit has a list of refactorings
                        "refactorings": refactorings_list
                    }
                    commits.append(sha1_dict)

            if count > 100: #and len(commits) > 50: and count > 20:
                #print(k)
                r.show_information()
                #print(k)
                #for x in commits:
                #    print(len(x["refactorings"]))
                #print(len(commits))
                #print(count)
                all = all + 1
                json_dict["commits"] = commits
                result.append(json_dict)
        print(all)

        with open("../json/result.json", 'w+') as file:
            json.dump(result, file, indent=4)


if __name__ == '__main__':
    JsonBuilder().main()

