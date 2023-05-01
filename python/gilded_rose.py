# -*- coding: utf-8 -*-
SULFURAS = "Sulfuras, Hand of Ragnaros"
BACKSTAGE = "Backstage passes to a TAFKAL80ETC concert"
BRIE = "Aged Brie"


class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_brie(self, item):
        if item.quality < 50:
            item.quality = item.quality + 1
        item.sell_in = item.sell_in - 1
        if item.sell_in < 0 and item.quality < 50:
            item.quality = item.quality + 1

    def update_pass(self, item):
        if item.quality < 50:
            item.quality = item.quality + 1
        if item.sell_in < 11 and item.quality < 50:
            item.quality = item.quality + 1
        if item.sell_in < 6 and item.quality < 50:
            item.quality = item.quality + 1
        item.sell_in = item.sell_in - 1
        if item.sell_in < 0:
            item.quality = item.quality - item.quality

    def update_sulfuras(self, item):
        pass

    def update_default(self, item):
        if item.quality > 0:
            item.quality = item.quality - 1
        item.sell_in = item.sell_in - 1
        if item.sell_in < 0 < item.quality:
            item.quality = item.quality - 1

    def update_quality(self):
        for item in self.items:
            if item.name == BRIE:
                self.update_brie(item)
            elif item.name == BACKSTAGE:
                self.update_pass(item)
            elif item.name == SULFURAS:
                self.update_sulfuras(item)
            else:
                self.update_default(item)
            #self.update_item_quality(item)

    def update_item_quality(self, item):
        condition = item.name != BRIE and item.name != BACKSTAGE and item.name != SULFURAS
        if condition:
            self.adjust_quality(-1, item)
        else:
            self.adjust_quality(1, item)
        if item.name == BACKSTAGE:
            if item.sell_in < 11 or item.sell_in < 6:
                self.adjust_quality(1, item)
        if item.name != SULFURAS:
            item.sell_in = item.sell_in - 1
        if item.sell_in < 0:
            if condition:
                self.adjust_quality(-1, item)
            if item.name == BRIE:
                self.adjust_quality(1, item)
            elif item.name == BACKSTAGE:
                item.quality = item.quality - item.quality

    def adjust_quality(self, adjustment, item):
        new_quality = item.quality + adjustment
        if 50 >= new_quality >= 0:
            item.quality = new_quality


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
