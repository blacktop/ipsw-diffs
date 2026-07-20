## batteryintelligenced

> `/usr/libexec/batteryintelligenced`

### Sections with Same Size but Changed Content

- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-215.0.0.0.0
-  __TEXT.__text: 0x41c70
+218.0.0.0.0
+  __TEXT.__text: 0x42004
   __TEXT.__auth_stubs: 0xa80
-  __TEXT.__objc_stubs: 0x4920
-  __TEXT.__objc_methlist: 0x314c
+  __TEXT.__objc_stubs: 0x4940
+  __TEXT.__objc_methlist: 0x317c
   __TEXT.__cstring: 0x354b
   __TEXT.__objc_classname: 0x855
+  __TEXT.__objc_methname: 0x643c
   __TEXT.__objc_methtype: 0x1537
   __TEXT.__const: 0x338
-  __TEXT.__objc_methname: 0x62e3
-  __TEXT.__oslogstring: 0x7924
+  __TEXT.__oslogstring: 0x7a54
   __TEXT.__gcc_except_tab: 0x340
   __TEXT.__unwind_info: 0xc78
   __DATA_CONST.__const: 0xcf8

   __DATA_CONST.__objc_doubleobj: 0x70
   __DATA_CONST.__objc_dictobj: 0x28
   __DATA_CONST.__auth_got: 0x550
-  __DATA_CONST.__got: 0x2a8
+  __DATA_CONST.__got: 0x338
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA.__objc_const: 0x79f0
-  __DATA.__objc_selrefs: 0x1778
-  __DATA.__objc_ivar: 0x330
+  __DATA.__objc_const: 0x7a50
+  __DATA.__objc_selrefs: 0x17a8
+  __DATA.__objc_ivar: 0x338
   __DATA.__objc_data: 0x1400
   __DATA.__data: 0x528
   __DATA.__bss: 0x248

   - /System/Library/PrivateFrameworks/CoreDuetContext.framework/CoreDuetContext
   - /System/Library/PrivateFrameworks/IDS.framework/IDS
   - /System/Library/PrivateFrameworks/IDSFoundation.framework/IDSFoundation
+  - /System/Library/PrivateFrameworks/MobileStoreDemoKit.framework/MobileStoreDemoKit
   - /System/Library/PrivateFrameworks/PerfPowerServicesReader.framework/PerfPowerServicesReader
   - /System/Library/PrivateFrameworks/PowerLog.framework/PowerLog
   - /System/Library/PrivateFrameworks/PowerUI.framework/PowerUI

   - /usr/lib/libSMC.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1492
-  Symbols:   271
-  CStrings:  2426
+  Functions: 1499
+  Symbols:   272
+  CStrings:  2440
 
Symbols:
+ _OBJC_CLASS_$_MSDKDemoState
CStrings:
+ "Not a supported device for BatteryAnalysis (isDemoDevice=%d, isVirtualDevice=%d). Skipping manager setup."
+ "Rejected new connection from pid %d. Not a supported device for BatteryAnalysis."
+ "TB,N,V_isBatteryAnalysisSupportedDevice"
+ "TB,N,V_shouldRunBatteryAnalysisEstimator"
+ "_isBatteryAnalysisSupportedDevice"
+ "_shouldRunBatteryAnalysisEstimator"
+ "isBatteryAnalysisSupportedDevice"
+ "isDemoDevice: isDeviceEnrolledWithDeKOTA returned error: %@"
+ "isDemoDevice: isSecureDemoModeEnabled returned error: %@"
+ "isDeviceEnrolledWithDeKOTA:"
+ "isSecureDemoModeEnabled:"
+ "setIsBatteryAnalysisSupportedDevice:"
+ "setShouldRunBatteryAnalysisEstimator:"
+ "shouldRunBatteryAnalysisEstimator"
```
