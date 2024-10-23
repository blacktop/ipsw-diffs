## WPDaemon

> `/System/Library/PrivateFrameworks/WPDaemon.framework/WPDaemon`

```diff

-181.8.1.5.0
-  __TEXT.__text: 0x57f2c
-  __TEXT.__auth_stubs: 0x8c0
-  __TEXT.__objc_methlist: 0x378c
-  __TEXT.__cstring: 0x3e91
+182.17.6.1.1
+  __TEXT.__text: 0x58448
+  __TEXT.__auth_stubs: 0x8d0
+  __TEXT.__objc_methlist: 0x37dc
+  __TEXT.__cstring: 0x3ec1
   __TEXT.__const: 0x220
-  __TEXT.__oslogstring: 0xa795
+  __TEXT.__oslogstring: 0xa6ed
   __TEXT.__gcc_except_tab: 0x16a4
-  __TEXT.__unwind_info: 0x16d8
+  __TEXT.__unwind_info: 0x16f0
   __TEXT.__objc_classname: 0x377
-  __TEXT.__objc_methname: 0x975c
+  __TEXT.__objc_methname: 0x9967
   __TEXT.__objc_methtype: 0x162d
-  __TEXT.__objc_stubs: 0x79e0
-  __DATA_CONST.__got: 0x468
+  __TEXT.__objc_stubs: 0x7a80
+  __DATA_CONST.__got: 0x470
   __DATA_CONST.__const: 0x10d8
   __DATA_CONST.__objc_classlist: 0xe8
   __DATA_CONST.__objc_protolist: 0x80
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2438
+  __DATA_CONST.__objc_selrefs: 0x2470
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0xd0
   __DATA_CONST.__objc_arraydata: 0x2b8
-  __AUTH_CONST.__auth_got: 0x470
+  __AUTH_CONST.__auth_got: 0x478
   __AUTH_CONST.__auth_ptr: 0x8
   __AUTH_CONST.__const: 0x66e0
-  __AUTH_CONST.__cfstring: 0x3340
-  __AUTH_CONST.__objc_const: 0x9490
+  __AUTH_CONST.__cfstring: 0x33a0
+  __AUTH_CONST.__objc_const: 0x94f0
   __AUTH_CONST.__objc_intobj: 0x108
   __AUTH_CONST.__objc_arrayobj: 0x48
   __AUTH.__objc_data: 0xf0
-  __DATA.__objc_ivar: 0x4ec
+  __DATA.__objc_ivar: 0x4f4
   __DATA.__data: 0x600
-  __DATA.__bss: 0x4
+  __DATA.__bss: 0x14
   __DATA_DIRTY.__objc_data: 0x820
   __DATA_DIRTY.__bss: 0xe8
   __DATA_DIRTY.__common: 0x10

   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/Security.framework/Security
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
+  - /System/Library/PrivateFrameworks/CoreUtils.framework/CoreUtils
   - /System/Library/PrivateFrameworks/FrontBoardServices.framework/FrontBoardServices
   - /System/Library/PrivateFrameworks/MobileKeyBag.framework/MobileKeyBag
   - /System/Library/PrivateFrameworks/PowerLog.framework/PowerLog

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2533
-  Symbols:   2926
-  CStrings:  3467
+  Functions: 2540
+  Symbols:   2935
+  CStrings:  3480
 
Symbols:
+ _CBAdvertisementDataIsNonConnectableSecondary
+ _GestaltGetDeviceClass
CStrings:
+ "\x1eA"
+ "@28@0:8q16B24"
+ "Platform supports NonConnectable Secondary AdvertisingInstance: %!s(MISSING)"
+ "ProxControlDeviceClose"
+ "T@\"CBPeripheralManager\",&,N,V_nonConnectableSecondaryPeripheralManager"
+ "T@\"WPDAdvertisingData\",&,N,V_currentNonConnectableSecondaryAdvertisingData"
+ "WPDaemon iOS 18.2 (22C5109o) (WirelessProximity-182.17.6.1.1) (Release) built on 2024-10-20 21:00:20"
+ "[Privacy] AdvertisingRulesiOS: current %!@(MISSING) advertisers: %!@(MISSING), current clients for address change notification: %!@(MISSING)"
+ "[Privacy] AdvertisingRulesiOS: remaining %!@(MISSING) advertisers: %!@(MISSING), notification clients: %!@(MISSING)"
+ "_currentNonConnectableSecondaryAdvertisingData"
+ "_nonConnectableSecondaryPeripheralManager"
+ "addressChangeNotificationNeeded:advertiserTypeString:"
+ "currentNonConnectableSecondaryAdvertisingData"
+ "maxAdvertisingRules"
+ "non-connectable"
+ "non-connectable secondary"
+ "nonConnectableSecondaryPeripheralManager"
+ "requestFromAdvertisingDataFromInstance:AddressChangeNotificationNeeded:"
+ "setCurrentNonConnectableSecondaryAdvertisingData:"
+ "setNonConnectableSecondaryPeripheralManager:"
+ "supportsNC2AdvertisingInstance"
- "\x1cA"
- "@24@0:8B16B20"
- "PrecisionFindingFindeeHighPriority"
- "WPDaemon iOS 18.1 (22B81) (WirelessProximity-181.8.1.5) (Release) built on 2024-10-18 14:55:59"
- "[Privacy] AdvertisingRulesiOS: current connectable advertisers: %!@(MISSING), current clients for address change notification: %!@(MISSING)"
- "[Privacy] AdvertisingRulesiOS: current non-connectable advertisers: %!@(MISSING), current clients for address change notification: %!@(MISSING)"
- "[Privacy] AdvertisingRulesiOS: remaining connectable advertisers: %!@(MISSING), notification clients: %!@(MISSING)"
- "[Privacy] AdvertisingRulesiOS: remaining non-connectable advertisers: %!@(MISSING), notification clients: %!@(MISSING)"
- "requestFromAdvertisingDataConnectable:AddressChangeNotificationNeeded:"

```
