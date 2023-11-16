from waifuc.action import PersonSplitAction
from waifuc.export import SaveExporter
from waifuc.source import LocalSource

if __name__ == '__main__':
    source = LocalSource('/data/raw')
    source = source.attach(
        PersonSplitAction(),
    )

    source.export(SaveExporter('/data/dstdataset'))
