## HearingModeService_Private

> `/System/Library/PrivateFrameworks/HearingModeService_Private.framework/HearingModeService_Private`

```diff

-30.45.3.0.0
-  __TEXT.__text: 0x12368
+30.48.2.1.2
+  __TEXT.__text: 0x123a4
   __TEXT.__auth_stubs: 0x4b0
   __TEXT.__objc_methlist: 0xc34
   __TEXT.__const: 0x86
   __TEXT.__gcc_except_tab: 0x514
-  __TEXT.__cstring: 0x4dd9
+  __TEXT.__cstring: 0x4dd8
   __TEXT.__unwind_info: 0x5c8
   __TEXT.__objc_classname: 0x14d
-  __TEXT.__objc_methname: 0x33f8
+  __TEXT.__objc_methname: 0x3416
   __TEXT.__objc_methtype: 0x8af
-  __TEXT.__objc_stubs: 0x2f20
+  __TEXT.__objc_stubs: 0x2f60
   __DATA_CONST.__got: 0x1e0
   __DATA_CONST.__const: 0x858
   __DATA_CONST.__objc_classlist: 0x38
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xde8
+  __DATA_CONST.__objc_selrefs: 0xdf8
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x30
   __AUTH_CONST.__auth_got: 0x268

   - /System/Library/PrivateFrameworks/ToneLibrary.framework/ToneLibrary
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 717ACE5A-8994-3EF5-B66A-158CDF3B9040
-  Functions: 423
+  UUID: 4D7C0AE9-8AF1-3B6E-8F4A-37B82A5D0A8E
+  Functions: 422
   Symbols:   1609
-  CStrings:  1091
+  CStrings:  1093
 
Symbols:
+ ___71+[HMHealthKitUtilities frequencyToHearingDecibelLevelMapFromAudiogram:]_block_invoke.310
+ ___block_literal_global.360
+ ___block_literal_global.384
+ ___block_literal_global.440
+ ___block_literal_global.467
+ ___block_literal_global.484
+ _objc_msgSend$getSafetyInformation:
+ _objc_msgSend$version
- -[HMDeviceManager _populateV1Struct:identifier:deviceRecord:hmSettingsStruct:].cold.8
- ___71+[HMHealthKitUtilities frequencyToHearingDecibelLevelMapFromAudiogram:]_block_invoke.307
- ___block_literal_global.354
- ___block_literal_global.381
- ___block_literal_global.437
- ___block_literal_global.464
- ___block_literal_global.481
Functions:
~ -[HMDeviceManager _deviceFound:] : 356 -> 396
~ -[HMDeviceManager _populateV1Struct:identifier:deviceRecord:hmSettingsStruct:] : 1532 -> 1620
~ -[HMDeviceManager _populateV1Struct:identifier:deviceRecord:hmSettingsStruct:].cold.3 : 68 -> 120
- -[HMDeviceManager _populateV1Struct:identifier:deviceRecord:hmSettingsStruct:].cold.8
CStrings:
+ "HearingAid config data not found, created new config with version %d"
+ "getSafetyInformation:"
+ "version"
- "HearingAid config data not found, creating new config with version %d"

```
