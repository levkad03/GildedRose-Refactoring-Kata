# -*- coding: utf-8 -*-
SELL_IN_0 = 0
ADJUSTMENT_MINUS = -1
ADJUSTMENT_1 = 1
SELL_IN_6 = 6
SELL_IN_11 = 11
QUALITY_0 = 0
QUALITY_50 = 50
SULFURAS = "Sulfuras, Hand of Ragnaros"
BACKSTAGE = "Backstage passes to a TAFKAL80ETC concert"
BRIE = "Aged Brie"


class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def adjust_sell_in(self, item):
        item.sell_in = item.sell_in - 1

    def adjust_quality(self, adjustment, item):
        new_quality = item.quality + adjustment
        if QUALITY_50 >= new_quality >= QUALITY_0:
            item.quality = new_quality

    def update_brie(self, item):
        self.adjust_quality(ADJUSTMENT_1, item)
        self.adjust_sell_in(item)
        if item.sell_in < SELL_IN_0:
            self.adjust_quality(ADJUSTMENT_1, item)

    def update_pass(self, item):
        self.adjust_quality(ADJUSTMENT_1, item)
        if item.sell_in < SELL_IN_11:
            self.adjust_quality(ADJUSTMENT_1, item)
        if item.sell_in < SELL_IN_6:
            self.adjust_quality(ADJUSTMENT_1, item)
        self.adjust_sell_in(item)
        if item.sell_in < SELL_IN_0:
            item.quality = item.quality - item.quality

    def update_sulfuras(self, item):
        pass

    def update_default(self, item):
        self.adjust_quality(ADJUSTMENT_MINUS, item)
        self.adjust_sell_in(item)
        if item.sell_in < SELL_IN_0:
            self.adjust_quality(ADJUSTMENT_MINUS, item)

    def update_quality(self):
        for item in self.items:
            self.update_item_quality(item)

    def update_item_quality(self, item):
        if item.name == BRIE:
            self.update_brie(item)
        elif item.name == BACKSTAGE:
            self.update_pass(item)
        elif item.name == SULFURAS:
            self.update_sulfuras(item)
        else:
            self.update_default(item)


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
