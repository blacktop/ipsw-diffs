## BacklightServicesHost

> `/System/Library/PrivateFrameworks/BacklightServicesHost.framework/BacklightServicesHost`

```diff

-5.0.66.0.0
-  __TEXT.__text: 0x892f0
+5.1.3.0.0
+  __TEXT.__text: 0x89568
   __TEXT.__auth_stubs: 0xb10
   __TEXT.__objc_methlist: 0x7bcc
   __TEXT.__const: 0x3b8
   __TEXT.__gcc_except_tab: 0x1090
-  __TEXT.__cstring: 0x69f2
-  __TEXT.__oslogstring: 0xfd87
+  __TEXT.__cstring: 0x69fb
+  __TEXT.__oslogstring: 0xfdd7
   __TEXT.__ustring: 0x328
-  __TEXT.__unwind_info: 0x2290
+  __TEXT.__unwind_info: 0x2298
   __TEXT.__objc_classname: 0x2005
-  __TEXT.__objc_methname: 0x11d6e
+  __TEXT.__objc_methname: 0x11d7c
   __TEXT.__objc_methtype: 0x43e9
-  __TEXT.__objc_stubs: 0xa2a0
+  __TEXT.__objc_stubs: 0xa2c0
   __DATA_CONST.__got: 0x758
   __DATA_CONST.__const: 0x2600
   __DATA_CONST.__objc_classlist: 0x560
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x2a0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x31a0
+  __DATA_CONST.__objc_selrefs: 0x31a8
   __DATA_CONST.__objc_superrefs: 0x460
   __DATA_CONST.__objc_arraydata: 0x78
   __AUTH_CONST.__auth_got: 0x598

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libtailspin.dylib
-  UUID: 42AF9684-885A-3208-A20A-94C0C82BB65B
-  Functions: 3375
-  Symbols:   11674
-  CStrings:  5865
+  UUID: 2D96E732-084B-373B-8B4E-8723C82738AC
+  Functions: 3376
+  Symbols:   11677
+  CStrings:  5868
 
Symbols:
+ -[BLSHBacklightFBSceneHostEnvironment synchronizePropertiesWithSettings:]
+ GCC_except_table76
+ ___102-[BLSHBacklightEnvironmentStateMachine transitionState:didCompleteUpdateToBacklightState:visualState:]_block_invoke.202
+ ___block_literal_global.177
+ ___block_literal_global.204
+ ___block_literal_global.70
+ _objc_msgSend$isHostProcess
- GCC_except_table75
- ___102-[BLSHBacklightEnvironmentStateMachine transitionState:didCompleteUpdateToBacklightState:visualState:]_block_invoke.199
- ___block_literal_global.176
- ___block_literal_global.180
- ___block_literal_global.198
- ___block_literal_global.64
Functions:
~ _OUTLINED_FUNCTION_8 : 16 -> 20
~ _OUTLINED_FUNCTION_2 : 16 -> 20
~ _OUTLINED_FUNCTION_2 : 28 -> 16
~ _OUTLINED_FUNCTION_2 : 20 -> 28
+ _OUTLINED_FUNCTION_2
- _OUTLINED_FUNCTION_3
~ _OUTLINED_FUNCTION_30 : 24 -> 12
~ _OUTLINED_FUNCTION_7 : 20 -> 16
~ _OUTLINED_FUNCTION_19 : 36 -> 12
~ _OUTLINED_FUNCTION_20 : 12 -> 36
+ _OUTLINED_FUNCTION_22
- _OUTLINED_FUNCTION_29
~ _OUTLINED_FUNCTION_32 : 28 -> 24
~ _OUTLINED_FUNCTION_36 : 12 -> 20
~ _OUTLINED_FUNCTION_37 : 20 -> 12
~ -[BLSHBacklightEnvironmentStateMachine onMain_setPresentation:withTargetBacklightState:] : 2816 -> 2872
~ -[BLSHBacklightEnvironmentStateMachine transitionState:didUpdateToDateSpecifier:] : 612 -> 640
~ -[BLSHAlwaysOnPresentationEngine main_performNextStep] : 608 -> 904
~ -[BLSHAlwaysOnPresentationEngine main_performUpdateIfNeeded] : 236 -> 248
~ -[BLSHBacklightEnvironmentStateMachine onMain_performEvent:withInitialSpecifier:performBacklightRamp:] : 1156 -> 1192
~ -[BLSHBacklightEnvironmentStateMachine transitionCompleteAfterCompletingTransitionState:] : 300 -> 336
~ -[BLSHBacklightEnvironmentStateMachine _lock_ifPossibleStopTrackingTransitionState:] : 356 -> 384
+ -[BLSHBacklightFBSceneHostEnvironment synchronizePropertiesWithSettings:]
CStrings:
+ "%p:%{public}@ will notify current, sleeping but have %.2lfs worth of flipbook frames"
+ "ESM:%p (finishing - %s) performEvent:%{public}@ transitionStates:%{public}@ "
+ "isHostProcess"
+ "obsolete"
- "ESM:%p (finishing - waiting) performEvent:%{public}@ transitionStates:%{public}@ "

```
