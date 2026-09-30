## lockdownd

> `filesystem/usr/libexec/lockdownd`

```diff

 1365.100.8.0.0
-  __TEXT.__text: 0xaa930
+  __TEXT.__text: 0xaacac
   __TEXT.__auth_stubs: 0x1db0
   __TEXT.__objc_stubs: 0x15c0
   __TEXT.__objc_methlist: 0x180
-  __TEXT.__cstring: 0x3bd14
+  __TEXT.__cstring: 0x3c0d3
   __TEXT.__const: 0x10fc0
   __TEXT.__gcc_except_tab: 0xaf0
   __TEXT.__objc_methname: 0xf22

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libramrod.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 0F227822-1D0F-3D77-A65C-44E598884702
+  UUID: A9183D5D-9AF6-3A1E-848E-0A27158F3992
   Functions: 918
   Symbols:   637
-  CStrings:  7471
+  CStrings:  7488
 
Functions:
~ sub_10008f5e8 : 22696 -> 22972
~ sub_100096520 -> sub_100096634 : 51780 -> 52212
~ sub_1000a4598 -> sub_1000a485c : 26380 -> 26564
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
