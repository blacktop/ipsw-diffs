## DisplayTransportServices

> `/System/Library/PrivateFrameworks/DisplayTransportServices.framework/Versions/A/DisplayTransportServices`

```diff

 1.4.0.0.0
-  __TEXT.__text: 0x4790
+  __TEXT.__text: 0x4768
   __TEXT.__auth_stubs: 0x270
-  __TEXT.__objc_methlist: 0x570
+  __TEXT.__objc_methlist: 0x8e4
   __TEXT.__const: 0x88
   __TEXT.__gcc_except_tab: 0x394
   __TEXT.__cstring: 0x382

   __DATA_CONST.__objc_classlist: 0x58
   __DATA_CONST.__objc_protolist: 0x60
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x488
+  __DATA_CONST.__objc_selrefs: 0x528
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x30
   __AUTH_CONST.__auth_got: 0x148
   __AUTH_CONST.__const: 0x1f0
   __AUTH_CONST.__cfstring: 0x4a0
-  __AUTH_CONST.__objc_const: 0x1e70
+  __AUTH_CONST.__objc_const: 0x1820
   __AUTH_CONST.__objc_intobj: 0x30
   __AUTH.__objc_data: 0x370
   __DATA.__objc_ivar: 0x70

   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/Versions/A/CoreAnalytics
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 65AB07DF-9FB9-354E-A3D5-3CFBD870249E
-  Functions: 136
-  Symbols:   538
+  UUID: 4F8BD0EB-6AA6-3D8B-82FE-BFB5023B3DD8
+  Functions: 138
+  Symbols:   540
   CStrings:  427
 
Symbols:
+ +[DTSAgentConnection sharedConnection].cold.1
+ -[DTSDPDeviceProxy initWithDescription:].cold.1
Functions:
~ -[DTSDPDeviceProxy initWithDescription:] : 300 -> 284
~ -[DTSDPDeviceProxy _assertPortState:] : 560 -> 552
~ -[DTSDPDeviceDPCDInfo description] : 324 -> 308
~ -[DTSDisplayPortDeviceAnalyticsData deviceLockedWithInfo:] : 484 -> 468
~ -[DTSDisplayPortDeviceAnalyticsData deviceUnlocked:] : 212 -> 204
~ +[DTSAgentConnection sharedConnection] : 84 -> 68

```
