from argparse import ArgumentParser

from pdf2image import convert_from_path

parser = ArgumentParser()
parser.add_argument("file", help="分割したいPDFファイル")
args = parser.parse_args()

file = args.file

pages = convert_from_path(file)
for i, page in enumerate(pages):
    filename = f"{i+1:02}.jpg"
    page.save(filename)
