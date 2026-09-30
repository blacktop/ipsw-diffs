## NetworkStatistics

> `/System/Library/PrivateFrameworks/NetworkStatistics.framework/NetworkStatistics`

```diff

-240.60.2.0.0
-  __TEXT.__text: 0x2cd28
-  __TEXT.__auth_stubs: 0xaa0
-  __TEXT.__objc_methlist: 0x40a4
-  __TEXT.__cstring: 0x5068
-  __TEXT.__oslogstring: 0x1f37
-  __TEXT.__const: 0x1ec
+249.0.0.0.0
+  __TEXT.__text: 0x2cd0c
+  __TEXT.__auth_stubs: 0xa90
+  __TEXT.__objc_methlist: 0x4248
+  __TEXT.__cstring: 0x50f4
+  __TEXT.__oslogstring: 0x2013
+  __TEXT.__const: 0x1dc
   __TEXT.__gcc_except_tab: 0x404
   __TEXT.__unwind_info: 0xab0
   __TEXT.__objc_classname: 0x4f2
-  __TEXT.__objc_methname: 0x7979
-  __TEXT.__objc_methtype: 0x7d21
-  __TEXT.__objc_stubs: 0x4b20
-  __DATA_CONST.__got: 0x170
-  __DATA_CONST.__const: 0x830
+  __TEXT.__objc_methname: 0x78ce
+  __TEXT.__objc_methtype: 0x7d63
+  __TEXT.__objc_stubs: 0x4b60
+  __DATA_CONST.__got: 0x190
+  __DATA_CONST.__const: 0x868
   __DATA_CONST.__objc_classlist: 0x188
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1920
+  __DATA_CONST.__objc_selrefs: 0x19b0
   __DATA_CONST.__objc_superrefs: 0x120
-  __DATA_CONST.__objc_arraydata: 0x898
-  __AUTH_CONST.__auth_got: 0x560
+  __DATA_CONST.__objc_arraydata: 0x8a8
+  __AUTH_CONST.__auth_got: 0x558
   __AUTH_CONST.__const: 0x120
-  __AUTH_CONST.__cfstring: 0x5600
-  __AUTH_CONST.__objc_const: 0x7df8
+  __AUTH_CONST.__cfstring: 0x5660
+  __AUTH_CONST.__objc_const: 0x7b30
   __AUTH_CONST.__objc_arrayobj: 0x78
   __AUTH_CONST.__objc_dictobj: 0x50
-  __DATA.__objc_ivar: 0x750
+  __DATA.__objc_ivar: 0x748
   __DATA.__data: 0x508
   __DATA.__common: 0x18
   __DATA.__bss: 0x30

   - /System/Library/Frameworks/Security.framework/Security
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1519
-  Symbols:   1938
-  CStrings:  2682
+  Functions: 1521
+  Symbols:   1947
+  CStrings:  2680
 
Symbols:
- _strncmp
CStrings:
+ "%@ %@ flow id %lld (%@%@) %@%@ i/f %d props 0x%x first %d pkts rx %lld tx %lld, bytes %lld %lld cell %lld %lld wifi %lld %lld wired %lld %lld comp_bt %lld %lld deltas %lld %lld %lld %lld %lld %lld %lld %lld %lld %lld acct_deltas %lld %lld %lld %lld %lld %lld %lld %lld"
+ "5C5BCB61-2C52-4D1F-9C1B-A5049F4998E8"
+ "Noted multiple interface usage for TCP/QUIC flow"
+ "TB,R,N,V_interfaceWiFiInfra"
+ "T^{accumulator_bytes=QQQQQQQQ},R,N"
+ "^{accumulator_bytes=QQQQQQQQ}16@0:8"
+ "_interfaceWiFiInfra"
+ "adjustment bytecounts > actual deltas in the snapshot. deltaRxCompanionLinkBluetoothBytes = %llu, adjustmentRxCompanionLinkBluetoothBytes = %llu"
+ "adjustment bytecounts > actual deltas in the snapshot. deltaTxCompanionLinkBluetoothBytes = %llu, adjustmentTxCompanionLinkBluetoothBytes = %llu"
+ "com.apple.mobileassetd.client.asutili"
+ "interfaceWiFiInfra"
+ "saved rx/tx cell %lld %lld wifi %lld %lld wired %lld %lld bt %lld %lld"
+ "{accumulator_bytes=\"rxCellularBytes\"Q\"rxWiFiBytes\"Q\"rxWiredBytes\"Q\"rxCompanionLinkBluetoothBytes\"Q\"txCellularBytes\"Q\"txWiFiBytes\"Q\"txWiredBytes\"Q\"txCompanionLinkBluetoothBytes\"Q}"
+ "\xf0\xf0\xf0\xf0\xf0\xf0rV"
- "%@ %@ flow id %lld (%@%@) %@%@ i/f %d props 0x%x first %d pkts rx %lld tx %lld, bytes %lld %lld cell %lld %lld wifi %lld %lld wired %lld %lld comp_bt %lld %lld deltas %lld %lld %lld %lld %lld %lld %lld %lld %lld %lld acct_deltas %lld %lld %lld %lld %lld %lld"
- "Flow details %@"
- "TI,R,N,V_TCPStateNumber"
- "TQ,R,N,V_deltaAccountingRxCompanionLinkBluetoothBytes"
- "TQ,R,N,V_deltaAccountingTxCompanionLinkBluetoothBytes"
- "T^{accumulator_bytes=QQQQQQ},R,N"
- "Unexpected multiple interface usage for TCP flow %lld"
- "^{accumulator_bytes=QQQQQQ}16@0:8"
- "_TCPStateNumber"
- "_deltaAccountingRxCompanionLinkBluetoothBytes"
- "_deltaAccountingTxCompanionLinkBluetoothBytes"
- "en"
- "pdp"
- "saved rx/tx cell %lld %lld wifi %lld %lld wired %lld %lld"
- "{accumulator_bytes=\"rxCellularBytes\"Q\"rxWiFiBytes\"Q\"rxWiredBytes\"Q\"txCellularBytes\"Q\"txWiFiBytes\"Q\"txWiredBytes\"Q}"
- "\xf0\xf0\xf0\xf0\xf0\xf0Rv"

```
