from docx import Document


def getopts(argv):
    opts = {}
    while argv:
        if argv[0][0] == '-':
            opts[argv[0]] = argv[1]
        argv = argv[1:]
    return opts


def add_para(document, text):
    p = document.add_paragraph(text)
    document.save('demo.docx')


if __name__ == '__main__':
    from sys import argv

    myargs = getopts(argv)
    document = Document()
    add_para(document, myargs['-t'])
