class Processor:
    def __init__(self,reader,writer):
        self.reader = reader
        self.writer = writer

    def process(self):
        while 1 :
            data = self.reader.readline()
            if not data : break
            data = self.converter(data)
            self.writer.write(data)

    def converter(self,data):
        assert False, "Converter must be defined"



class UpperCase(Processor):
    def converter(self,data):
        return str(data).upper()

class HTMLize:
    def write(self,line):
        print("<PRE>%s</PRE>"%line.strip())

if __name__ == "__main__" :
    import sys
    # obj = UpperCase(open("spam"),sys.stdout)
    obj = UpperCase(open("spam"),HTMLize())

    obj.process()