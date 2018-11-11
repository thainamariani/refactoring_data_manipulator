from git import Repo
from distutils.dir_util import copy_tree
import subprocess
import json
import os
import shutil

with open("../json/result.json", "r") as read_file:
    repositories = json.load(read_file)

f = open("../repositories/log.txt", "w+")

print(len(repositories))
count_commits = 0

for repository in repositories:
    url = repository["repository"]
    name = url
    name = name.split('/')
    name = name[3] + '-' + name[4].strip('.git')
    print(name)
    f.write(name + "\n")
    count_commits = count_commits + len(repository["commits"])

    # for commit in repository["commits"]:
    #     sha1 = commit["sha1"]
    #     time = str(commit["time"])
    #     time = time.replace(" ", "_")
    #     #ar_dir = '/mnt/NAS/tmariani/Repositories/' + name + sha1 + '/_AR'
    #     ar_dir = "../repositories/" + name + "/" + time + "/AR_" + sha1
    #     try:
    #         ar_repo = Repo.clone_from(url, ar_dir)
    #         ar_head = ar_repo.create_head("ar_head", sha1)
    #         ar_repo.heads.ar_head.checkout()
    #         br_head = ar_repo.create_head("br_head", "HEAD~1")
    #         ar_repo.heads.br_head.checkout()
    #         br_dir = "../repositories/" + name + "/" + time + "/BR_" + str(br_head.commit)
    #         shutil.copytree(ar_dir, br_dir)
    #         ar_repo.heads.ar_head.checkout()
    #         shutil.rmtree(ar_dir + '/.git')
    #         shutil.rmtree(br_dir + '/.git')
    #         root, dirs, files = os.walk(ar_dir)
    #         if "src" not in dirs:
    #             f.write("Error: no src directory\n")
    #         if ".java" not in files:
    #             f.write("Error: no java files\n")
    #         else:
    #             f.write("Success!\n")
    #     except Exception as e:
    #         f.write("Error: " + str(e) + "\n")

print(count_commits)

