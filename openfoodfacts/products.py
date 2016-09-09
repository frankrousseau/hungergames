import utils


"""
Return information of a given product.
"""
def get_product(barcode):
    return utils.fetch('api/v0/product/%s' % barcode)
