## sysdiagnose_helper

> `filesystem/usr/libexec/sysdiagnose_helper`

```diff

 1527.100.28.0.0
-  __TEXT.__text: 0x3b510
+  __TEXT.__text: 0x3b940
   __TEXT.__auth_stubs: 0xb90
   __TEXT.__objc_stubs: 0x1640
   __TEXT.__objc_methlist: 0x58c
   __TEXT.__const: 0x3d0
   __TEXT.__gcc_except_tab: 0x85c
   __TEXT.__oslogstring: 0x2407
-  __TEXT.__cstring: 0x30c2b
+  __TEXT.__cstring: 0x30fbe
   __TEXT.__objc_classname: 0xc2
   __TEXT.__objc_methtype: 0x2a9
   __TEXT.__objc_methname: 0x15cb

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libtailspin.dylib
   - /usr/lib/libtzupdate.dylib
-  UUID: 2D7327E0-F8E5-37D4-B2C2-44FED9A3E3CA
+  UUID: B45BE93F-C045-3DB1-A8A4-5BC8590EC7F8
   Functions: 363
   Symbols:   253
-  CStrings:  4484
+  CStrings:  4499
 
Functions:
~ sub_10000e0e8 : 22696 -> 22972
~ sub_100015020 -> sub_100015134 : 51780 -> 52212
~ sub_100023098 -> sub_10002335c : 26380 -> 26564
~ sub_10002b01c -> sub_10002b398 : 53204 -> 53384
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
+ "program_switch_"
+ "unCleanBootBlankCheck"
+ "unCleanBootClog"
- "ASPFTLParseBufferToCxt: assertHistory(948): (#40) cfg elements != (%d) buffer elements"
- "ASPFTLParseBufferToCxt: assertHistory(948): Cannot add 40 elements to context"

```
