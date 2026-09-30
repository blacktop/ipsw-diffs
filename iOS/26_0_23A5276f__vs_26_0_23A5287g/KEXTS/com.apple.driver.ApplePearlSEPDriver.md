## com.apple.driver.ApplePearlSEPDriver

> `com.apple.driver.ApplePearlSEPDriver`

```diff

-867.0.0.0.0
+870.0.0.0.0
   __TEXT.__const: 0x318
-  __TEXT.__cstring: 0x9edf
-  __TEXT.__os_log: 0x470b
-  __TEXT_EXEC.__text: 0x3da4c
+  __TEXT.__cstring: 0x9f66
+  __TEXT.__os_log: 0x46ec
+  __TEXT_EXEC.__text: 0x3dacc
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xcd
   __DATA.__common: 0x1d8

   __DATA_CONST.__const: 0x2030
   __DATA_CONST.__kalloc_type: 0x580
   __DATA_CONST.__kalloc_var: 0x1e0
-  UUID: AF4D56B9-6E6E-34FA-A799-D97A317C6E49
+  UUID: CBEEA3B8-163F-3281-82AB-AAECD2E536EF
   Functions: 614
   Symbols:   0
-  CStrings:  1591
+  CStrings:  1596
 
Functions:
~ sub_fffffff00994bc3c -> sub_fffffff009960fbc : 1960 -> 1956
~ sub_fffffff009951540 -> sub_fffffff0099668bc : 1412 -> 1408
~ sub_fffffff009958360 -> sub_fffffff00996d6d8 : 296 -> 420
~ sub_fffffff00995a5e0 -> sub_fffffff00996f9d4 : 524 -> 564
~ sub_fffffff00996075c -> sub_fffffff009975b78 : 10588 -> 10584
~ sub_fffffff00996572c -> sub_fffffff00997ab44 : 680 -> 676
~ sub_fffffff0099668a8 -> sub_fffffff00997bcbc : 3588 -> 3572
~ sub_fffffff0099704c4 -> sub_fffffff0099858c8 : 1040 -> 1036
CStrings:
+ "%s <- sequenceType:%s (%d) overrideIsPearlDisabled:%d\n"
+ "%s: newMatchAttempt:%u params->trigger:%u params->unsupportedOrientation:%u triggerOverride:%d secureFaceDetectForcedMode:%d -> useSecureFD:%u\n"
+ "pearl-SFDModeForLiftToWake"
+ "pearl-SFDModeForPowerButton"
+ "pearl-SFDModeForSwipeUp"
+ "pearl-SFDModeForTapToWake"
+ "pearl-SFDModeForUserInitiated"
- "%s <- sequenceType:%s (%d) overrideIsPearlDisabled:%d loadingFDR:%d\n"
- "%s: newMatchAttempt:%u params->trigger:%u params->unsupportedOrientation:%u prewarmRunning:%u prewarmTrigger:%u secureFaceDetectForcedMode:%d -> useSecureFD:%u\n"

```
