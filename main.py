import PyPDF2
import argparse
import os


def rename_pdf(args):
    file_name = args.file_name
    pdf_file = open(file_name, "rb")
    pdf_reader = PyPDF2.PdfFileReader(pdf_file)

    dir_name = os.path.split(os.path.abspath(file_name))[0]

    title = pdf_reader.getDocumentInfo().title

    if title:
        print("Renaming with the title")

        new_file_name = title

    else:
        print("Title not found, renaming with the first line")

        first_page_text = pdf_reader.getPage(0).extractText()
        first_line = first_page_text.split("\n")[0]
        new_file_name = first_line

    os.rename(
        os.path.join(dir_name, file_name), (os.path.join(dir_name, new_file_name))
    )

    print(f"Renamed {file_name} --> {new_file_name}")

    pdf_reader.stream.close()


if __name__ == "__main__":
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument(
        "--file_name", type=str, help="Path to the pdf file to be renamed"
    )
    args = arg_parser.parse_args()
    rename_pdf(args)
