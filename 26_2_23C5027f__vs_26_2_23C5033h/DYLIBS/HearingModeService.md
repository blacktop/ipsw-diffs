## HearingModeService

> `/System/Library/PrivateFrameworks/HearingModeService.framework/HearingModeService`

```diff

-32.2.0.0.0
-  __TEXT.__text: 0x14cf4
+32.3.0.0.0
+  __TEXT.__text: 0x14d04
   __TEXT.__auth_stubs: 0x4a0
   __TEXT.__objc_methlist: 0x16ec
   __TEXT.__const: 0x70

   - /System/Library/PrivateFrameworks/MediaExperience.framework/MediaExperience
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 0D0BD7D7-BD76-3784-A45A-1536901F85AB
-  Functions: 593
-  Symbols:   1947
+  UUID: E167C7C4-F4FF-35E4-BB32-86CD700D862D
+  Functions: 592
+  Symbols:   1943
   CStrings:  1767
 
Symbols:
+ ___69+[HMAudiogramUtility frequencyToHearingDecibelLevelMapFromAudiogram:]_block_invoke.461
- ___69+[HMAudiogramUtility frequencyToHearingDecibelLevelMapFromAudiogram:]_block_invoke.452
Functions:
- _OUTLINED_FUNCTION_1
~ -[HMAccessoryManager _writeHearingModeSetting:].cold.1 : 96 -> 116
~ -[HMAccessoryManager _discoveryAccessory].cold.1 : 28 -> 32
~ -[HMAccessoryManager peripheral:didDiscoverCharacteristicsForService:error:].cold.4 : 104 -> 100
~ -[HMDeviceDiagnosticRecord computeOcclusionResultForHearingTest] : 488 -> 484
~ -[HMEnrollmentService _getHearingModeSettings:fromAudiogram:].cold.1 : 96 -> 116

```
