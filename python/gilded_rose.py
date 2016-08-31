# -*- coding: utf-8 -*-


class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            delta_quality = lambda x: (
                -1 if x.sell_in > 0 else
                -2)
            delta_quality_backstage = lambda x: (
                -x.quality if x.sell_in <= 0 else
                3 if x.sell_in <= 5 else
                2 if x.sell_in <= 10 else
                1)

            ops = dict(
                delta_quality=delta_quality,
                delta_sell_in=lambda x: -1,
                limit_quality=lambda q: max(0, min(q, 50)))

            ops.update({
                'Aged Brie': dict(
                    delta_quality=lambda x: -delta_quality(x)),
                'Backstage passes to a TAFKAL80ETC concert': dict(
                    delta_quality=delta_quality_backstage),
                'Sulfuras, Hand of Ragnaros': dict(
                    delta_quality=lambda x: 0,
                    delta_sell_in=lambda x: 0,
                    limit_quality=lambda q: q),
                'Conjured Mana Cake': dict(
                    delta_quality=lambda x: 2 * delta_quality(x))
            }.get(item.name, {}))

            item.quality += ops.get('delta_quality')(item)
            item.sell_in += ops.get('delta_sell_in')(item)
            item.quality = ops.get('limit_quality')(item.quality)


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
