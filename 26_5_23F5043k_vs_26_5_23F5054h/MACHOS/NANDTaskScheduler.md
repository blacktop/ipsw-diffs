## NANDTaskScheduler

> `filesystem/usr/libexec/NANDTaskScheduler`

```diff

-659.120.8.0.0
-  __TEXT.__text: 0x21dfc
+659.120.9.0.0
+  __TEXT.__text: 0x22178
   __TEXT.__auth_stubs: 0x530
   __TEXT.__objc_stubs: 0x7e0
   __TEXT.__objc_methlist: 0xc4
-  __TEXT.__cstring: 0x2d7af
+  __TEXT.__cstring: 0x2db6e
   __TEXT.__const: 0x108
   __TEXT.__gcc_except_tab: 0x80
   __TEXT.__oslogstring: 0x130b

   - /System/Library/PrivateFrameworks/SidebarFileDispatcher.framework/SidebarFileDispatcher
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 22A45B1A-0298-373A-8A9E-DDFEA38C946F
+  UUID: 4BFAE4DF-A604-3219-8918-D85B0609CC4B
   Functions: 158
   Symbols:   123
-  CStrings:  3499
+  CStrings:  3516
 
Functions:
~ sub_1000018fc : 22696 -> 22972
~ sub_100008834 -> sub_100008948 : 51780 -> 52212
~ sub_1000168ac -> sub_100016b70 : 26380 -> 26564
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
