from model import Image, Product, BaseModel
from parsing_client import ClientAParser
import pytest
import unittest


class ParserTest(unittest.TestCase):

    def setUp(self):
        xml_filename = 'feed.gz'
        self.parser = ClientAParser(xml_filename)

    @pytest.mark.order1
    def test_image_type(self):
        image_url = """https://images.asos-media.com/products/"""
        """vestido-largo-y-plisado-de-dama-de-honor-en-rosa-exclusivo-de-tfnc/"""
        """13955198-2?$XXL$&wid=513&fit=constrain"""
        for etag in ["xx", None]:
                image = Image(url=image_url, etag=etag)
                self.assertTrue(hasattr(image, "etag"))
                self.assertIsInstance(image.etag, (str, type(None)))
    @pytest.mark.order2
    def test_product_type(self):
        image_url = """https://images.asos-media.com/products/"""
        """vestido-largo-y-plisado-de-dama-de-honor-en-rosa-exclusivo-de-tfnc/"""
        """13955198-2?$XXL$&wid=513&fit=constrain"""
        product_url = """https://www.asos.com/es/tfnc/"""
        """vestido-largo-y-plisado-de-dama-de-honor-en-rosa-exclusivo-de-tfnc/"""
        """prd/13955198?clr=rosa&colourWayId=16579390&SearchQuery=&cid=17245"""
        description = "Vestido largo y plisado de dama de honor en rosa exclusivo de TFNC"
        images = [Image(url=image_url) for x in range(5)]  # 5 fake images
        product = Product(uid="sku1000", images=images, gender="female",
                          url=product_url, price=82.99,
                          category="dress", size="M", description=description)

        self.assertTrue(hasattr(product, "uid"))
        self.assertTrue(hasattr(product, "images"))
        self.assertTrue(hasattr(product, "gender"))
        self.assertTrue(hasattr(product, "url"))
        self.assertTrue(hasattr(product, "price"))
        self.assertTrue(hasattr(product, "size"))
        self.assertTrue(hasattr(product, "category"))
        self.assertTrue(hasattr(product, "description"))

        self.assertIsInstance(product.uid, str)
        self.assertIsInstance(product.images, list)
        self.assertIsInstance(product.gender, str)
        self.assertIsInstance(product.url, str)
        self.assertIsInstance(product.price, float)
        self.assertIsInstance(product.size, str)
        self.assertIsInstance(product.category, str)
        self.assertIsInstance(product.description, str)

    @pytest.mark.order3
    def test_parser_length(self):
        n_products = len(self.parser)
        self.assertIsInstance(n_products, int)
        self.assertEqual(n_products, 53878)

    @pytest.mark.order4
    def test_parser_getitem(self):
        # compare that the Product at index 2 is the same as below.
        idx = 2
        product = self.parser[idx]

        self.assertIsInstance(product, Product)
        # we expect the price of the product at index 2 is 329
        self.assertEqual(product.price, 329.00)
        # we expect the uid of the product at index 2 is "1000046"
        self.assertEqual(product.uid, "1000046")
        # and so on ...
        self.assertEqual(product.description, "Dsquared2 Siyah İpek Papyon")
        self.assertEqual(product.url,
                         "https://www.beymen.com/p_dsquared2-siyah-ipek-papyon_303527")
        
    

    def tearDown(self):
        pass

if __name__ == '__main__':

    unittest.main()
