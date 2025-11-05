## NetworkStatistics

> `/System/Library/PrivateFrameworks/NetworkStatistics.framework/Versions/A/NetworkStatistics`

```diff

-240.60.2.0.0
-  __TEXT.__text: 0x2e8d4
-  __TEXT.__auth_stubs: 0x8e0
-  __TEXT.__objc_methlist: 0x3f64
-  __TEXT.__cstring: 0x43f4
-  __TEXT.__oslogstring: 0x1d5c
-  __TEXT.__const: 0x1f4
+249.0.0.0.0
+  __TEXT.__text: 0x2e850
+  __TEXT.__auth_stubs: 0x8d0
+  __TEXT.__objc_methlist: 0x40e8
+  __TEXT.__cstring: 0x444d
+  __TEXT.__oslogstring: 0x1e38
+  __TEXT.__const: 0x1e4
   __TEXT.__gcc_except_tab: 0x2cc
-  __TEXT.__unwind_info: 0x918
+  __TEXT.__unwind_info: 0x930
   __TEXT.__objc_classname: 0x4a5
-  __TEXT.__objc_methname: 0x755e
-  __TEXT.__objc_methtype: 0x7c6c
+  __TEXT.__objc_methname: 0x74b3
+  __TEXT.__objc_methtype: 0x7cae
   __TEXT.__objc_stubs: 0x45e0
-  __DATA_CONST.__got: 0x170
-  __DATA_CONST.__const: 0x530
+  __DATA_CONST.__got: 0x190
+  __DATA_CONST.__const: 0x568
   __DATA_CONST.__objc_classlist: 0x178
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1808
+  __DATA_CONST.__objc_selrefs: 0x18a0
   __DATA_CONST.__objc_superrefs: 0x118
-  __DATA_CONST.__objc_arraydata: 0x240
-  __AUTH_CONST.__auth_got: 0x480
+  __DATA_CONST.__objc_arraydata: 0x250
+  __AUTH_CONST.__auth_got: 0x478
   __AUTH_CONST.__const: 0x3d0
-  __AUTH_CONST.__cfstring: 0x4080
-  __AUTH_CONST.__objc_const: 0x7758
+  __AUTH_CONST.__cfstring: 0x40e0
+  __AUTH_CONST.__objc_const: 0x74b0
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH.__objc_data: 0xe10
-  __DATA.__objc_ivar: 0x71c
+  __DATA.__objc_ivar: 0x714
   __DATA.__data: 0x4b0
   __DATA.__bss: 0x80
   __DATA.__common: 0x18

   - /System/Library/Frameworks/Security.framework/Versions/A/Security
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 95C1881D-CCF4-3942-AD52-09F199DC2569
-  Functions: 1496
-  Symbols:   3265
-  CStrings:  2927
+  UUID: BE5B4C3A-BAB3-3B3E-8A90-3DD4B66FBE5C
+  Functions: 1497
+  Symbols:   3271
+  CStrings:  2928
 
Symbols:
+ -[NWStatsConnSource processExtendedUpdate:length:].cold.2
+ -[NWStatsProtocolSnapshot interfaceWiFiInfra]
+ -[NWStatsQUICSnapshot interfaceWiFiInfra]
+ -[NWStatsSource bundleNameImpliesNonAppInitiated:].cold.1
+ -[NWStatsTCPSnapshot interfaceWiFiInfra]
+ -[NWStatsUDPSnapshot interfaceWiFiInfra]
+ NStatGetLog.cold.1
+ NStatMgrVTraceF.cold.1
+ OBJC_IVAR_$_NWStatsProtocolSnapshot._interfaceWiFiInfra
+ __block_literal_global.152
+ __block_literal_global.171
+ _flowsWithAnomalies
+ _flowsWithAnomaliesLock
+ _objc_msgSend$deltaAccountingRxCompanionLinkBluetoothBytes
+ _objc_msgSend$deltaAccountingTxCompanionLinkBluetoothBytes
+ pid_to_coalitionID.cold.1
+ printf_domain.cold.1
+ stringByRemovingTrailingUUIDsAndLaunchServicesStuff.cold.1
- OBJC_IVAR_$_NWStatsProtocolSnapshot._deltaAccountingRxCompanionLinkBluetoothBytes
- OBJC_IVAR_$_NWStatsProtocolSnapshot._deltaAccountingTxCompanionLinkBluetoothBytes
- OBJC_IVAR_$_NWStatsTCPSnapshot._TCPStateNumber
- _OUTLINED_FUNCTION_6
- _OUTLINED_FUNCTION_7
- __block_literal_global.146
- __block_literal_global.165
- _flowsWithAnomalousCounts
- _flowsWithAnomalousCountsLock
- _objc_msgSend$rxCompanionLinkBluetoothBytes
- _objc_msgSend$txCompanionLinkBluetoothBytes
- _strncmp
CStrings:
+ "%@ %@ flow id %lld (%@%@) %@%@ i/f %d props 0x%x first %d pkts rx %lld tx %lld, bytes %lld %lld cell %lld %lld wifi %lld %lld wired %lld %lld deltas %lld %lld %lld %lld %lld %lld %lld %lld acct_deltas %lld %lld %lld %lld %lld %lld"
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
- "{accumulator_bytes=\"rxCellularBytes\"Q\"rxWiFiBytes\"Q\"rxWiredBytes\"Q\"txCellularBytes\"Q\"txWiFiBytes\"Q\"txWiredBytes\"Q}"
- "\xf0\xf0\xf0\xf0\xf0\xf0Rv"

```
