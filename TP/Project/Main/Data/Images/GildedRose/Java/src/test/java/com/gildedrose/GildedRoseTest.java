package com.gildedrose;

import static org.junit.Assert.*;

import org.junit.Test;

public class GildedRoseTest {

	@Test
    public void SulfurasQualitySellInNegative() {
        Item[] items = new Item[] { new Item("Sulfuras, Hand of Ragnaros",-1, 80) };
        GildedRose app = new GildedRose(items);
        app.updateQuality();
        assertEquals(80, app.items[0].quality);
    }
    @Test
    public void SulfurasQualitySellInPositive() {
        Item[] items = new Item[] { new Item("Sulfuras, Hand of Ragnaros",1, 80) };
        GildedRose app = new GildedRose(items);
        app.updateQuality();
        assertEquals(80, app.items[0].quality);
    }
    @Test
    public void SulfurasSellInNegative() {
        Item[] items = new Item[] { new Item("Sulfuras, Hand of Ragnaros",-1, 80) };
        GildedRose app = new GildedRose(items);
        app.updateQuality();
        assertEquals(-1, app.items[0].sellIn);
    }
    @Test
    public void SulfurasSellInPositive() {
        Item[] items = new Item[] { new Item("Sulfuras, Hand of Ragnaros",1, 80) };
        GildedRose app = new GildedRose(items);
        app.updateQuality();
        assertEquals(1, app.items[0].sellIn);
    }
    
    
    @Test
    public void AgedBrieQualitySellInEquals_0() {
        Item[] items = new Item[] { new Item("Aged Brie",0, 40) };
        GildedRose app = new GildedRose(items);
        app.updateQuality();
        assertEquals(42, app.items[0].quality);
    }

    @Test
    public void AgedBrieQualitySellInEquals_1() {
        Item[] items = new Item[] { new Item("Aged Brie",1, 40) };
        GildedRose app = new GildedRose(items);
        app.updateQuality();
        assertEquals(41, app.items[0].quality);
    }
    @Test
    public void AgedBrieQualityMaxSellInEquals_0() {
        Item[] items = new Item[] { new Item("Aged Brie",0, 49) };
        GildedRose app = new GildedRose(items);
        app.updateQuality();
        assertEquals(50, app.items[0].quality);
    }
    
    
    @Test
    public void BackstageQualitySellInEquals_5() {
        Item[] items = new Item[] { new Item("Backstage passes to a TAFKAL80ETC concert",5, 40) };
        GildedRose app = new GildedRose(items);
        app.updateQuality();
        assertEquals(43, app.items[0].quality);
    }
    @Test
    public void BackstageQualityMaxSellInEquals_6() {
        Item[] items = new Item[] { new Item("Backstage passes to a TAFKAL80ETC concert",6, 40) };
        GildedRose app = new GildedRose(items);
        app.updateQuality();
        assertEquals(42, app.items[0].quality);
    }
    @Test
    public void BackstageQualitySellInEquals_10() {
        Item[] items = new Item[] { new Item("Backstage passes to a TAFKAL80ETC concert",10, 40) };
        GildedRose app = new GildedRose(items);
        app.updateQuality();
        assertEquals(42, app.items[0].quality);
    }
    @Test
    public void BackstageQualitySellInEquals_11() {
        Item[] items = new Item[] { new Item("Backstage passes to a TAFKAL80ETC concert",11, 40) };
        GildedRose app = new GildedRose(items);
        app.updateQuality();
        assertEquals(41, app.items[0].quality);
    }
    @Test
    public void BackstageQualityMaxSellInEquals_0() {
        Item[] items = new Item[] { new Item("Backstage passes to a TAFKAL80ETC concert",0, 40) };
        GildedRose app = new GildedRose(items);
        app.updateQuality();
        assertEquals(0, app.items[0].quality);
    }
    @Test
    public void BackstageQualityMaxSellInEquals_5() {
        Item[] items = new Item[] { new Item("Backstage passes to a TAFKAL80ETC concert",5, 49) };
        GildedRose app = new GildedRose(items);
        app.updateQuality();
        assertEquals(50, app.items[0].quality);
    }
    
    
    @Test
    public void fooBeerQualitySellInEquals_1() {
        Item[] items = new Item[] { new Item("foo", 1, 30) };
        GildedRose app = new GildedRose(items);
        app.updateQuality();
        assertEquals(29, app.items[0].quality);
    }
    @Test
    public void fooBeerQuality0SellInEquals_0() {
        Item[] items = new Item[] { new Item("foo", 0, 30) };
        GildedRose app = new GildedRose(items);
        app.updateQuality();
        assertEquals(28, app.items[0].quality);
    }

    @Test
    public void fooBeerQualityMinSellInEquals_0() {
        Item[] items = new Item[] { new Item("foo", 0, 1) };
        GildedRose app = new GildedRose(items);
        app.updateQuality();
        assertEquals(0, app.items[0].quality);
    }
    @Test
    public void sellIn() {
        Item[] items = new Item[] { new Item("foo", 0, 0) };
        GildedRose app = new GildedRose(items);
        app.updateQuality();
        assertEquals(-1, app.items[0].sellIn);
    }
   
    
    @Test
    public void ConjuredQualitySellInEquals_1() {
        Item[] items = new Item[] { new Item("Conjured Mana Cake",1, 49) };
        GildedRose app = new GildedRose(items);
        app.updateQuality();
        assertEquals(47, app.items[0].quality);
    }
    @Test
    public void ConjuredQualitySellInEquals_0() {
        Item[] items = new Item[] { new Item("Conjured Mana Cake",0, 49) };
        GildedRose app = new GildedRose(items);
        app.updateQuality();
        assertEquals(45, app.items[0].quality);
    }
    @Test
    public void ConjuredQualityMinSellInEquals_0() {
        Item[] items = new Item[] { new Item("Conjured Mana Cake",0, 2) };
        GildedRose app = new GildedRose(items);
        app.updateQuality();
        assertEquals(0, app.items[0].quality);
    }
}
