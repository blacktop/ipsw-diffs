## WPDaemon

> `/System/Library/PrivateFrameworks/WPDaemon.framework/WPDaemon`

```diff

-2701.7.1.0.0
-  __TEXT.__text: 0x5edfc
+2702.3.1.0.0
+  __TEXT.__text: 0x5efec
   __TEXT.__objc_methlist: 0x4654
-  __TEXT.__cstring: 0x4b8f
+  __TEXT.__cstring: 0x4c15
   __TEXT.__const: 0x290
-  __TEXT.__oslogstring: 0xafe0
+  __TEXT.__oslogstring: 0xb031
   __TEXT.__gcc_except_tab: 0x12cc
   __TEXT.__unwind_info: 0x2838
   __TEXT.__objc_stubs: 0x0

   __DATA_CONST.__objc_classlist: 0xf8
   __DATA_CONST.__objc_protolist: 0x80
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2938
+  __DATA_CONST.__objc_selrefs: 0x2940
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0xe0
   __DATA_CONST.__objc_arraydata: 0x2d8
-  __DATA_CONST.__got: 0x4c8
-  __AUTH_CONST.__const: 0x6f08
-  __AUTH_CONST.__cfstring: 0x3a20
+  __DATA_CONST.__got: 0x4d0
+  __AUTH_CONST.__const: 0x6f28
+  __AUTH_CONST.__cfstring: 0x3a60
   __AUTH_CONST.__objc_const: 0x8b98
   __AUTH_CONST.__weak_auth_got: 0x18
   __AUTH_CONST.__objc_intobj: 0x198

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 3636
-  Symbols:   3011
-  CStrings:  1578
+  Functions: 3637
+  Symbols:   3013
+  CStrings:  1582
 
Symbols:
+ GCC_except_table110
+ GCC_except_table120
+ GCC_except_table140
+ _NSCocoaErrorDomain
- GCC_except_table109
- GCC_except_table139
Functions:
~ -[WPScanRequest initWithCoder:] : 1036 -> 1276
~ -[WPScanRequest convertUseCaseToString:] : 3628 -> 3680
~ -[WPDScanManager addScanRequest:forClient:] : 1496 -> 1488
- ___41-[WPDAdvertisingManager updateAdvertiser]_block_invoke.399
~ ___50-[WPDZoneManager centralManager:didLoseZone:mask:]_block_invoke.209 : 928 -> 984
~ ___31-[WPDZoneManager updateScanner]_block_invoke.242 : 112 -> 88
~ -[WPDAdvertisingManager refreshHeySiriAuthTagInActiveRequests] : 740 -> 1012
+ ___62-[WPDAdvertisingManager refreshHeySiriAuthTagInActiveRequests]_block_invoke.241
~ ___41-[WPDAdvertisingManager updateAdvertiser]_block_invoke.402 : 8 -> 4
+ ___41-[WPDAdvertisingManager updateAdvertiser]_block_invoke.405
~ -[WPDAdvertisingManager refreshHeySiriAuthTagInActiveRequests].cold.4 : 132 -> 36
CStrings:
+ "ProximityServiceThirdPartyHomeSetup"
+ "RPIdentity: skipping refresh, HeySiri adv missing auth tag flag"
+ "RPIdentity: skipping refresh, unexpected HeySiri adv length %lu (expected %lu)"
+ "WPDaemon iOS 27.3 (24C5037g) (WirelessProximity-2702.3.1) (Release) built on 2026-10-29 22:13:33"
+ "WPScanRequest blob value exceeds maximum length"
+ "WPScanRequest mask value exceeds maximum length"
- "RPIdentity: skipping refresh, unexpected HeySiri adv length %lu"
- "WPDaemon iOS 27.2 (24B112) (WirelessProximity-2701.7.1) (Release) built on 2026-10-13 21:05:02"
```
