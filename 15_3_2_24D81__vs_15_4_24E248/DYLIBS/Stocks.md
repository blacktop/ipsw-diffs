## Stocks

> `/System/iOSSupport/System/Library/PrivateFrameworks/Stocks.framework/Versions/A/Stocks`

```diff

-1216.1.0.0.0
-  __TEXT.__text: 0x46a0c
+1555.1.0.0.0
+  __TEXT.__text: 0x46930
   __TEXT.__auth_stubs: 0xb60
-  __TEXT.__objc_methlist: 0x4990
+  __TEXT.__objc_methlist: 0x54a8
   __TEXT.__const: 0x2f8
   __TEXT.__cstring: 0x23be
   __TEXT.__oslogstring: 0x1cb3
-  __TEXT.__gcc_except_tab: 0x5ac
+  __TEXT.__gcc_except_tab: 0x594
   __TEXT.__ustring: 0x28
-  __TEXT.__unwind_info: 0x1198
+  __TEXT.__unwind_info: 0x1200
   __TEXT.__objc_classname: 0x88e
   __TEXT.__objc_methname: 0xe9b4
   __TEXT.__objc_methtype: 0x26e4
   __TEXT.__objc_stubs: 0xaa60
   __DATA_CONST.__got: 0x690
-  __DATA_CONST.__const: 0x1660
+  __DATA_CONST.__const: 0x16a0
   __DATA_CONST.__objc_classlist: 0x278
   __DATA_CONST.__objc_catlist: 0x38
   __DATA_CONST.__objc_protolist: 0xe8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x33c0
+  __DATA_CONST.__objc_selrefs: 0x37b8
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x200
   __DATA_CONST.__objc_arraydata: 0x1198
   __AUTH_CONST.__auth_got: 0x5c0
   __AUTH_CONST.__const: 0x420
   __AUTH_CONST.__cfstring: 0x3b60
-  __AUTH_CONST.__objc_const: 0xa878
+  __AUTH_CONST.__objc_const: 0x9408
   __AUTH_CONST.__objc_intobj: 0x1c8
   __AUTH_CONST.__objc_dictobj: 0xf0
   __AUTH_CONST.__objc_arrayobj: 0x708

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 76A93644-F0DE-357C-BB61-25363FB30490
-  Functions: 1804
-  Symbols:   5136
+  UUID: BF4883A0-3017-326E-9D19-CA06A9F9BD06
+  Functions: 1825
+  Symbols:   5160
   CStrings:  4210
 
Symbols:
+ +[Exchange formattedExchangeNameForName:].cold.1
+ +[ExchangeManager sharedManager].cold.1
+ +[Stock listNameOverridesBySymbol].cold.1
+ +[StockUpdateManager sharedManager].cold.1
+ +[YQLConstants YQLDataSourceToStocksKeyMap].cold.1
+ +[YQLConstants YQLExchangeToStocksKeyMap].cold.1
+ +[YQLConstants YQLQuoteToStocksKeyMap].cold.1
+ +[YahooResponseParser parseExchangeDictionaries:parsedExchangeResult:].cold.1
+ -[NetPreferences _cacheDirectoryPath].cold.1
+ -[NetPreferences _stocksUserAgent].cold.1
+ -[NetPreferences serviceDebuggingPath].cold.1
+ -[NewsUpdater fetchNewsForStock:withCompletion:].cold.1
+ -[SCKZoneModificationSilo _shouldAssertRecordValidity].cold.1
+ -[SCKZoneModificationSilo initWithZoneSchema:contents:].cold.1
+ -[SCKZoneSnapshot initWithZoneSchema:records:].cold.1
+ -[StockChartView enumerateGraphsAndDisplayModesUsingBlock:].cold.1
+ -[StockPlatterViewController initWithStockTicker:].cold.1
+ ClientInfo.cold.1
+ DeviceInfo.cold.1
+ ProductVersion.cold.1
+ SCKDatabaseLog.cold.1
+ ShouldSwapColorsForLocale.cold.1
+ StocksLogForCategory.cold.1
+ _ConsumerSecret.cold.1
+ __70+[YahooResponseParser parseExchangeDictionaries:parsedExchangeResult:]_block_invoke_2.cold.3

```
