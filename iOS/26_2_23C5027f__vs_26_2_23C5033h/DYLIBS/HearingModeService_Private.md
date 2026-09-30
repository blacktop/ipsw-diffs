## HearingModeService_Private

> `/System/Library/PrivateFrameworks/HearingModeService_Private.framework/HearingModeService_Private`

```diff

-32.2.0.0.0
-  __TEXT.__text: 0x13040
+32.3.0.0.0
+  __TEXT.__text: 0x130c4
   __TEXT.__auth_stubs: 0x4b0
   __TEXT.__objc_methlist: 0xc6c
   __TEXT.__const: 0x86
   __TEXT.__gcc_except_tab: 0x514
-  __TEXT.__cstring: 0x51ad
-  __TEXT.__unwind_info: 0x5f8
+  __TEXT.__cstring: 0x51cf
+  __TEXT.__unwind_info: 0x5f0
   __TEXT.__objc_classname: 0x14d
   __TEXT.__objc_methname: 0x36e2
   __TEXT.__objc_methtype: 0x8ef

   __DATA_CONST.__objc_superrefs: 0x30
   __AUTH_CONST.__auth_got: 0x268
   __AUTH_CONST.__const: 0x160
-  __AUTH_CONST.__cfstring: 0x700
+  __AUTH_CONST.__cfstring: 0x740
   __AUTH_CONST.__objc_const: 0x1498
   __AUTH_CONST.__objc_doubleobj: 0x80
   __AUTH_CONST.__objc_intobj: 0x18

   - /System/Library/PrivateFrameworks/ToneLibrary.framework/ToneLibrary
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 4881F956-8C72-3980-81BC-5FA698ED98F8
-  Functions: 438
-  Symbols:   1670
-  CStrings:  1140
+  UUID: 2C595D55-F3DA-379C-A1B8-9CD01AAF0F5B
+  Functions: 437
+  Symbols:   1666
+  CStrings:  1143
 
Symbols:
+ ___71+[HMHealthKitUtilities frequencyToHearingDecibelLevelMapFromAudiogram:]_block_invoke.319
+ ___block_literal_global.375
+ ___block_literal_global.378
+ ___block_literal_global.409
+ ___block_literal_global.467
+ ___block_literal_global.494
+ ___block_literal_global.511
- ___71+[HMHealthKitUtilities frequencyToHearingDecibelLevelMapFromAudiogram:]_block_invoke.310
- ___block_literal_global.360
- ___block_literal_global.363
- ___block_literal_global.394
- ___block_literal_global.452
- ___block_literal_global.479
- ___block_literal_global.496
Functions:
- _OUTLINED_FUNCTION_1
~ -[HMDeviceManager _submitHearingFeaturesMetricFor:] : 1156 -> 1268
~ -[HMDeviceAHPSConnectionManager peripheral:didDiscoverCharacteristicsForService:error:].cold.4 : 104 -> 100
~ -[HMSettingsTelemetry _sendSettingsChanges:record:].cold.1 : 112 -> 116
~ -[HMHealthKitUtilities updateHMSettingsStruct:fromAudiogram:].cold.1 : 96 -> 116
~ -[HMDeviceManager _diagnosticDataReceived:identifier:isInternal:].cold.2 : 96 -> 116
CStrings:
+ "HearingProtectionPPERegionSupport"

```
