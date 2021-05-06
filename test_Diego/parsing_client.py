"""Implement one particular client parser."""
import xml.etree.ElementTree as ET
from model import Product, Image


class ClientParser:
    """Client parser abstract class."""

    def __len__(self):
        """Get number of products.

        Return:
            int, number of products

        """
        root = self.tree.getroot()
        number_of_poducts = 0
        for child in root:
            number_of_poducts += 1
        return number_of_poducts


        raise NotImplementedError

    def __getitem__(self, idx):
        """Get the product of index `idx`.

        Iterate over the feed and extract needed information for the product
        at `idx` index.

        Return:
            Product, one product

        """
        root = self.tree.getroot()
        for child in root[idx]:
            if str(child.tag)=='price':
                price = child.text
            if str(child.tag)=='productid':
                uid = child.text
            if str(child.tag)=='title':
                description = child.text
            if str(child.tag)=='url':
                url = child.text
            if str(child.tag)=='gender':
                gender = child.text
            if str(child.tag)=='image':
                images = [child.text]
            if str(child.tag)=='sizes':
                size = str(child.text[0]).upper()
            if str(child.tag)=='categories':
                categories = child.text
        product = Product(uid=uid, images=images, gender=gender,
                          url=url, price=price,
                          category=categories, size=size, description=description)
        return product

        raise NotImplementedError


class ClientAParser(ClientParser):
    """Client A parser."""

    def __init__(self, filename):
        """Client parser constructor."""
        if filename.endswith("xml"):
            self.tree = ET.parse(filename)
        elif filename.endswith(".gz"):
            import gzip
            self.tree = ET.parse(gzip.open(filename))
        else:
            raise NotImplementedError

    def __len__(self):
        return super().__len__()
        #TODO, implement "how to get number of products"


    def __getitem__(self, idx):
        #TODO, implement the parsing product at `idx`
        # For instance, get the following information and others from the XML:
        # category = 'Papyon'
        # price = 329.00
        # gender = "male"
        return super().__getitem__(idx)

    # auto generated doc from super class
    __len__.__doc__ = ClientParser.__len__.__doc__
    __getitem__.__doc__ = ClientParser.__getitem__.__doc__


if __name__ == '__main__':

    import time

    xml_filename = 'feed.gz'
    parser = ClientAParser(xml_filename)
    
    
    tic = time.time()
    # optimize and speed up the whole xml parsing
    # you could use threading, multi processing and etc
    for idx in range(len(parser)):
        product = parser[idx]
    toc = time.time() - tic
    print('Elapsed {} secs'.format(toc))
