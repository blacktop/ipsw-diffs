## HearingUtilities

> `/System/Library/PrivateFrameworks/HearingUtilities.framework/HearingUtilities`

```diff

-496.4.6.0.0
-  __TEXT.__text: 0x9a0cc
+496.4.7.0.0
+  __TEXT.__text: 0x9a1a4
   __TEXT.__auth_stubs: 0x1140
-  __TEXT.__objc_methlist: 0x7d9c
+  __TEXT.__objc_methlist: 0x7dac
   __TEXT.__const: 0x412
   __TEXT.__gcc_except_tab: 0x2930
   __TEXT.__cstring: 0x4efb
-  __TEXT.__oslogstring: 0xa2d3
+  __TEXT.__oslogstring: 0xa34c
   __TEXT.__dlopen_cstrs: 0x7a7
   __TEXT.__swift5_typeref: 0x46
   __TEXT.__swift5_capture: 0x30

   __TEXT.__unwind_info: 0x25e8
   __TEXT.__eh_frame: 0x48
   __TEXT.__objc_classname: 0x843
-  __TEXT.__objc_methname: 0x14308
-  __TEXT.__objc_methtype: 0x21ee
+  __TEXT.__objc_methname: 0x14348
+  __TEXT.__objc_methtype: 0x2246
   __TEXT.__objc_stubs: 0xeda0
   __DATA_CONST.__got: 0x620
   __DATA_CONST.__const: 0x3470

   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0xe8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4998
+  __DATA_CONST.__objc_selrefs: 0x49a0
   __DATA_CONST.__objc_superrefs: 0x180
   __DATA_CONST.__objc_arraydata: 0x430
   __AUTH_CONST.__auth_got: 0x8b0
   __AUTH_CONST.__const: 0xd98
   __AUTH_CONST.__cfstring: 0x5220
-  __AUTH_CONST.__objc_const: 0xa610
+  __AUTH_CONST.__objc_const: 0xa618
   __AUTH_CONST.__objc_intobj: 0xa80
   __AUTH_CONST.__objc_arrayobj: 0x1f8
   __AUTH_CONST.__objc_dictobj: 0x410

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: B5A15DE8-FB7C-3C2F-88DD-CDE554C58A9F
-  Functions: 3589
-  Symbols:   11552
-  CStrings:  6069
+  UUID: F3B7A288-F29C-3292-A165-9860298D6588
+  Functions: 3591
+  Symbols:   11560
+  CStrings:  6074
 
Symbols:
+ -[AXHearingAidDevice peripheral:didUpdateCharacteristic:].cold.1
+ -[AXHearingAidDevice peripheral:didUpdateCharacteristic:].cold.2
+ ___107-[HUNoiseController checkToSurfaceAnalyticsNotificationForSPL:withDuration:andBuffer:forTime:andThreshold:]_block_invoke.438
+ ___107-[HUNoiseController checkToSurfaceAnalyticsNotificationForSPL:withDuration:andBuffer:forTime:andThreshold:]_block_invoke.442
+ ___107-[HUNoiseController checkToSurfaceAnalyticsNotificationForSPL:withDuration:andBuffer:forTime:andThreshold:]_block_invoke.459
+ ___25-[HUNoiseController init]_block_invoke.321
+ ___37-[HUNoiseController restartADAMTimer]_block_invoke.401
+ ___51-[HUNoiseController subscribeToSharedNotifications]_block_invoke.494
+ ___51-[HUNoiseController subscribeToSharedNotifications]_block_invoke.494.cold.1
+ ___53-[HUNoiseController readEnvironmentalDosimetryLevels]_block_invoke.412
+ ___57-[AXHearingAidDevice peripheral:didUpdateCharacteristic:]_block_invoke.285
+ ___57-[AXHearingAidDevice peripheral:didUpdateCharacteristic:]_block_invoke.286
+ ___57-[AXHearingAidDevice peripheral:didUpdateCharacteristic:]_block_invoke.292
+ ___57-[AXHearingAidDevice peripheral:didUpdateCharacteristic:]_block_invoke.295
+ ___57-[AXHearingAidDevice peripheral:didUpdateCharacteristic:]_block_invoke.300
+ ___57-[AXHearingAidDevice peripheral:didUpdateCharacteristic:]_block_invoke_2.293
+ ___57-[AXHearingAidDevice peripheral:didUpdateCharacteristic:]_block_invoke_2.296
+ ___85-[HUNoiseController checkToSurfaceNotificationForSPL:withDuration:andBuffer:forTime:]_block_invoke.421
+ ___85-[HUNoiseController checkToSurfaceNotificationForSPL:withDuration:andBuffer:forTime:]_block_invoke.426
+ ___block_literal_global.306
+ ___block_literal_global.347
+ ___block_literal_global.400
+ ___block_literal_global.444
+ ___block_literal_global.470
+ ___block_literal_global.474
+ ___block_literal_global.510
- ___107-[HUNoiseController checkToSurfaceAnalyticsNotificationForSPL:withDuration:andBuffer:forTime:andThreshold:]_block_invoke.429
- ___107-[HUNoiseController checkToSurfaceAnalyticsNotificationForSPL:withDuration:andBuffer:forTime:andThreshold:]_block_invoke.433
- ___107-[HUNoiseController checkToSurfaceAnalyticsNotificationForSPL:withDuration:andBuffer:forTime:andThreshold:]_block_invoke.441
- ___25-[HUNoiseController init]_block_invoke.312
- ___37-[HUNoiseController restartADAMTimer]_block_invoke.392
- ___51-[HUNoiseController subscribeToSharedNotifications]_block_invoke.485
- ___51-[HUNoiseController subscribeToSharedNotifications]_block_invoke.485.cold.1
- ___53-[HUNoiseController readEnvironmentalDosimetryLevels]_block_invoke.403
- ___57-[AXHearingAidDevice peripheral:didUpdateCharacteristic:]_block_invoke.290
- ___57-[AXHearingAidDevice peripheral:didUpdateCharacteristic:]_block_invoke.294
- ___57-[AXHearingAidDevice peripheral:didUpdateCharacteristic:]_block_invoke.299
- ___57-[AXHearingAidDevice peripheral:didUpdateCharacteristic:]_block_invoke_2.291
- ___57-[AXHearingAidDevice peripheral:didUpdateCharacteristic:]_block_invoke_2.295
- ___57-[AXHearingAidDevice peripheral:didUpdateCharacteristic:]_block_invoke_3.292
- ___57-[AXHearingAidDevice peripheral:didUpdateCharacteristic:]_block_invoke_4
- ___85-[HUNoiseController checkToSurfaceNotificationForSPL:withDuration:andBuffer:forTime:]_block_invoke.412
- ___85-[HUNoiseController checkToSurfaceNotificationForSPL:withDuration:andBuffer:forTime:]_block_invoke.417
- ___block_literal_global.297
- ___block_literal_global.346
- ___block_literal_global.391
- ___block_literal_global.435
- ___block_literal_global.443
- ___block_literal_global.465
- ___block_literal_global.501
CStrings:
+ "HearingAidDevice: Error in reading HIID, got empty string"
+ "HearingAidDevice: Error in reading HIIDOther, got empty string"
+ "service:account:didReceiveLocalNetworkHandshake:fromID:context:"
+ "v52@0:8@\"IDSService\"16@\"IDSAccount\"24B32@\"NSString\"36@\"NSData\"44"
+ "v52@0:8@16@24B32@36@44"

```
