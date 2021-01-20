from page.models import Block, Element


def create_block(**param):
    block = Block.objects.create(**param)
    block.save()
    return block


def create_element(**param):
    elem = Element.objects.create(**param)
    elem.save()
    return elem
