## hangreporter

> `filesystem/usr/libexec/hangreporter`

```diff

-398.1.0.0.0
-  __TEXT.__text: 0x3fc98
+398.2.0.0.0
+  __TEXT.__text: 0x40014
   __TEXT.__auth_stubs: 0xee0
   __TEXT.__objc_stubs: 0x2d40
   __TEXT.__objc_methlist: 0xfa4
   __TEXT.__const: 0x298
-  __TEXT.__cstring: 0x30ca4
+  __TEXT.__cstring: 0x31063
   __TEXT.__oslogstring: 0x4b03
   __TEXT.__gcc_except_tab: 0xc00
   __TEXT.__objc_methname: 0x530d

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libtailspin.dylib
   - /usr/lib/libz.1.dylib
-  UUID: AB8A7594-022D-37AA-939F-ADB0EA9B95E6
+  UUID: C9A2D666-F17E-3909-B795-2231621C3E8C
   Functions: 701
   Symbols:   329
-  CStrings:  5728
+  CStrings:  5745
 
Functions:
~ sub_100023e50 : 22696 -> 22972
~ sub_1000299e8 -> sub_100029afc : 51780 -> 52212
~ sub_1000366c0 -> sub_100036984 : 26380 -> 26564
CStrings:
+ "ASPFTLParseBufferToCxt: assertHistory(948): (#5) cfg elements != (%d) buffer elements"
+ "ASPFTLParseBufferToCxt: assertHistory(948): Cannot add 5 elements to context"
+ "ASPFTLParseBufferToCxt: assertHistoryUpdates(1754) cannot add 1 element to context"
+ "ASPFTLParseBufferToCxt: massScanCleanBootsDuringScan(1757) cannot add 1 element to context"
+ "ASPFTLParseBufferToCxt: massScanUncleanBootsDuringScan(1756) cannot add 1 element to context"
+ "ASPFTLParseBufferToCxt: numPerfOptionalRefreshes(1274) cannot add 1 element to context"
+ "ASPFTLParseBufferToCxt: pgHappyBandRelease(1200) cannot add 1 element to context"
+ "ASPFTLParseBufferToCxt: unCleanBootBlankCheck(1755) cannot add 1 element to context"
+ "ASPFTLParseBufferToCxt: unCleanBootClog(1763) cannot add 1 element to context"
+ "ASPMSPParseBufferToCxt: program_switch(16400): Error adding 16 elements to context"
+ "ASPMSPParseBufferToCxt: program_switch(16400): cfg 16 elements; (16*8) cfg bytes != (%d) buffer bytes"
+ "assertHistoryUpdates"
+ "massScanCleanBootsDuringScan"
+ "massScanUncleanBootsDuringScan"
+ "numPerfOptionalRefreshes"
+ "pgHappyBandRelease"
+ "program_switch_"
+ "unCleanBootBlankCheck"
+ "unCleanBootClog"
- "ASPFTLParseBufferToCxt: assertHistory(948): (#40) cfg elements != (%d) buffer elements"
- "ASPFTLParseBufferToCxt: assertHistory(948): Cannot add 40 elements to context"

```
