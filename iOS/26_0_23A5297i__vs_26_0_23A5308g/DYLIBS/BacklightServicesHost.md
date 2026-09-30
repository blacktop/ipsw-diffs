## BacklightServicesHost

> `/System/Library/PrivateFrameworks/BacklightServicesHost.framework/BacklightServicesHost`

```diff

-5.0.59.0.0
-  __TEXT.__text: 0x88a40
+5.0.62.0.0
+  __TEXT.__text: 0x88d04
   __TEXT.__auth_stubs: 0xb10
   __TEXT.__objc_methlist: 0x7bcc
   __TEXT.__const: 0x3b8
   __TEXT.__gcc_except_tab: 0x1090
   __TEXT.__cstring: 0x69db
-  __TEXT.__oslogstring: 0xfac9
+  __TEXT.__oslogstring: 0xfc1f
   __TEXT.__ustring: 0x328
-  __TEXT.__unwind_info: 0x2288
+  __TEXT.__unwind_info: 0x2280
   __TEXT.__objc_classname: 0x2004
   __TEXT.__objc_methname: 0x11d05
   __TEXT.__objc_methtype: 0x43e9

   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__objc_floatobj: 0x10
-  __AUTH.__objc_data: 0xf00
+  __AUTH.__objc_data: 0xeb0
   __DATA.__objc_ivar: 0xe60
   __DATA.__data: 0x1f80
   __DATA.__bss: 0x98
-  __DATA_DIRTY.__objc_data: 0x26c0
+  __DATA_DIRTY.__objc_data: 0x2710
   __DATA_DIRTY.__bss: 0xf8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreMotion.framework/CoreMotion

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libtailspin.dylib
-  UUID: 1C99A166-5E6B-3620-BFC0-B7774F8C6E8B
-  Functions: 3355
-  Symbols:   11635
-  CStrings:  5851
+  UUID: 808106BC-7779-3707-9626-4A845636A0A7
+  Functions: 3354
+  Symbols:   11629
+  CStrings:  5856
 
Symbols:
+ -[BLSHWatchdogProvider fireWatchdogWithTimer:delegate:timeout:elapsedTime:].cold.1
+ GCC_except_table107
+ ___118-[BLSHWatchdogProvider _fireWatchdogWithTimer:delegate:timeout:elapsedTime:abortContext:explanation:remainingRetries:]_block_invoke.137
+ ___118-[BLSHWatchdogProvider _fireWatchdogWithTimer:delegate:timeout:elapsedTime:abortContext:explanation:remainingRetries:]_block_invoke.137.cold.1
+ ___118-[BLSHWatchdogProvider _fireWatchdogWithTimer:delegate:timeout:elapsedTime:abortContext:explanation:remainingRetries:]_block_invoke.137.cold.2
+ ___118-[BLSHWatchdogProvider _fireWatchdogWithTimer:delegate:timeout:elapsedTime:abortContext:explanation:remainingRetries:]_block_invoke.137.cold.3
+ ___block_descriptor_48_e8_32s40s_e74_v24?0"BLSAlwaysOnDateSpecifier"8"<BLSHBacklightSceneHostEnvironment>"16ls32l8s40l8
- -[BLSHBacklightEnvironmentStateMachine onMain_setPresentation:withTargetBacklightState:].cold.5
- -[BLSHBacklightEnvironmentStateMachine onMain_setPresentation:withTargetBacklightState:].cold.6
- GCC_except_table106
- ___118-[BLSHWatchdogProvider _fireWatchdogWithTimer:delegate:timeout:elapsedTime:abortContext:explanation:remainingRetries:]_block_invoke.131
- ___118-[BLSHWatchdogProvider _fireWatchdogWithTimer:delegate:timeout:elapsedTime:abortContext:explanation:remainingRetries:]_block_invoke.131.cold.1
- ___118-[BLSHWatchdogProvider _fireWatchdogWithTimer:delegate:timeout:elapsedTime:abortContext:explanation:remainingRetries:]_block_invoke.131.cold.2
- ___118-[BLSHWatchdogProvider _fireWatchdogWithTimer:delegate:timeout:elapsedTime:abortContext:explanation:remainingRetries:]_block_invoke.131.cold.3
- ___block_descriptor_40_e8_32s_e74_v24?0"BLSAlwaysOnDateSpecifier"8"<BLSHBacklightSceneHostEnvironment>"16ls32l8
CStrings:
+ "%p charge rendered specifier:%{public}@ environment:%{public}@"
+ "ESM:%p didUpdateToDateSpecifier:%{public}@ expectedDate:%{BOOL}u transitionState:%{public}@"
+ "ESM:%p removal— no longer active transitionState:%{public}@"
+ "ESM:%p transitionComplete:%{BOOL}u for transitionStateComplete:%{public}@ "
+ "Failed to generate tailspin for watchdog hang: %@"

```
