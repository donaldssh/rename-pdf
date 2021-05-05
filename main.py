import PyPDF2
import argparse
import os


def rename_single_pdf(file_name, dir_name):
    pdf_file = open(file_name, "rb")
    pdf_reader = PyPDF2.PdfFileReader(pdf_file)
    title = pdf_reader.getDocumentInfo().title

    if title:
        print("Renaming with the title")
        new_file_name = title

    else:
        print("Title not found, renaming with the first line")
        first_page_text = pdf_reader.getPage(0).extractText()
        first_line = first_page_text.split("\n")[0]
        new_file_name = first_line

    if new_file_name:
        new_file_name += ".pdf"
        os.rename(
            os.path.join(dir_name, file_name), (os.path.join(dir_name, new_file_name))
        )

        print(f"{file_name} --> {new_file_name}\n")

    else:
        print(f"Not possible to rename {file_name}\n")

    pdf_reader.stream.close()


def rename_pdfs(args):

    if args.file_name:
        file_name = args.file_name
        dir_name = os.path.split(os.path.abspath(file_name))[0]
        rename_single_pdf(file_name, dir_name)

    elif args.dir:
        dir_name = os.path.abspath(args.dir)
        for entry in os.scandir(args.dir):
            if entry.path.endswith(".pdf"):
                file_name = entry.path.replace("./", "")
                rename_single_pdf(file_name, dir_name)


if __name__ == "__main__":
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument(
        "--file_name",
        type=str,
        help="Path to the pdf file to be renamed",
        required=False,
    )
    arg_parser.add_argument(
        "--dir",
        type=str,
        help="Path to the directory containing all the pdfs to be renamed",
        required=False,
    )
    args = arg_parser.parse_args()
    rename_pdfs(args)
