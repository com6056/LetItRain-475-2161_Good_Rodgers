# Contains report generation code

import os
from FileObject import FileObject

# Create report folder and report file (report+folder_name)
def create_folder(folder_name):
    if not os.path.exists("{}/report_let_it_rain".format(folder_name)):
        os.makedirs("{}/report_let_it_rain".format(folder_name))
        print("Folder created!")
        return
    print("Folder already exists.")


# Write to the txt file the hashing results
def write_to_report_file(results, folder_name, args):
    file1 = open("{}/report_let_it_rain/report.txt".format(folder_name), 'wb')
    file1.write("Folder name: {}\n\n".format(folder_name))
    if args.positive:
        file1.write("Positive matching requested, displaying matching files and their hashes.\n\n")
    else:
        file1.write("Negative hashing requested, displaying non-matching files and their hashes.\n\n")
    if not results[0] == [] and not args.md5file == "None":
        file1.write("\n\nMD5:\n")
        for res in results[0]:
            file1.write("{} - {}\n".format(res.get_name().strip(), res.get_md5()))
    if not results[1] == [] and not args.sha1file == "None":
        file1.write("\n\nSHA1:\n")
        for res in results[1]:
            file1.write("{} - {}\n".format(res.get_name().strip(), res.get_sha1()))
    if not results[2] == [] and not args.sha256file == "None":
        file1.write("\n\nSHA256:\n")
        for res in results[2]:
            file1.write("{} - {}\n".format(res.get_name().strip(), res.get_sha256()))

# Main function for generating the report
def generate_report(results, folder_name, args):
    print("Creating report folder...")
    create_folder(folder_name)
    print("Writing report. This may take a few moments...")
    write_to_report_file(results, folder_name, args)
