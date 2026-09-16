## powerexperienced

> `/usr/libexec/powerexperienced`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__got`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-176.0.0.0.0
-  __TEXT.__text: 0x1bbc4
-  __TEXT.__auth_stubs: 0x730
-  __TEXT.__objc_stubs: 0x3ca0
-  __TEXT.__objc_methlist: 0x25c4
-  __TEXT.__const: 0x158
-  __TEXT.__cstring: 0x13e4
-  __TEXT.__objc_methname: 0x4508
-  __TEXT.__oslogstring: 0x3455
+180.0.0.0.0
+  __TEXT.__text: 0x1b650
+  __TEXT.__auth_stubs: 0x6c0
+  __TEXT.__objc_stubs: 0x3c00
+  __TEXT.__objc_methlist: 0x259c
+  __TEXT.__const: 0x150
+  __TEXT.__cstring: 0x1375
+  __TEXT.__objc_methname: 0x443b
+  __TEXT.__oslogstring: 0x3356
   __TEXT.__objc_classname: 0x442
-  __TEXT.__objc_methtype: 0x8eb
-  __TEXT.__gcc_except_tab: 0x5c
-  __TEXT.__dlopen_cstrs: 0x8d
-  __TEXT.__unwind_info: 0xa08
-  __DATA_CONST.__const: 0x940
-  __DATA_CONST.__cfstring: 0x1400
+  __TEXT.__objc_methtype: 0x8d3
+  __TEXT.__gcc_except_tab: 0x4c
+  __TEXT.__unwind_info: 0x9e8
+  __DATA_CONST.__const: 0x900
+  __DATA_CONST.__cfstring: 0x1440
   __DATA_CONST.__objc_classlist: 0xf0
   __DATA_CONST.__objc_protolist: 0x88
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_superrefs: 0xe0
   __DATA_CONST.__objc_intobj: 0x108
   __DATA_CONST.__objc_floatobj: 0x10
-  __DATA_CONST.__auth_got: 0x3a8
+  __DATA_CONST.__auth_got: 0x370
   __DATA_CONST.__got: 0x1a0
-  __DATA.__objc_const: 0x5a40
-  __DATA.__objc_selrefs: 0x1260
-  __DATA.__objc_ivar: 0x290
+  __DATA.__objc_const: 0x59e0
+  __DATA.__objc_selrefs: 0x1238
+  __DATA.__objc_ivar: 0x288
   __DATA.__objc_data: 0x960
   __DATA.__data: 0x660
   __DATA.__common: 0x80

   - /System/Library/PrivateFrameworks/PerformanceControlKit.framework/PerformanceControlKit
   - /System/Library/PrivateFrameworks/PowerExperience.framework/PowerExperience
   - /System/Library/PrivateFrameworks/PowerLog.framework/PowerLog
-  - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /System/Library/PrivateFrameworks/Trial.framework/Trial
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 889
-  Symbols:   178
-  CStrings:  1502
+  Functions: 878
+  Symbols:   171
+  CStrings:  1484
 
Symbols:
- __Block_object_dispose
- __sl_dlopen
- _abort_report_np
- _dlopen_preflight
- _free
- _objc_getClass
- _objc_retain_x9
CStrings:
+ "HardwarePlatform"
+ "Trial: Setting TrialID: %lld with CLPC"
+ "Trial:Error setting clpc trial value %@"
+ "kHardwarePlatformContext"
+ "resetForTesting"
+ "waitForPendingEvaluation"
- "%s"
- "/AppleInternal/Library/Frameworks/PerformanceControlKitInternal.framework/PerformanceControlKitInternal"
- "@\"<CLPCInternalAccess>\""
- "CLPCInternalInterface"
- "Charging, not in use and TP Light. ChargingTPLight"
- "Error creating CLPC Internal User Client %@"
- "Error setting clpc trial value %@"
- "Initialized internal CLPC Policy Interface"
- "PerformanceControlKitInternal not available"
- "T@\"<CLPCInternalAccess>\",&,V_clpcInternalAccessClient"
- "TB,V_isInternal"
- "Trial:No trial value for CLPC tuning option. Resetting to default"
- "Unable to find class %s"
- "Updating CLPCInternal client RPC buffer size to 16k"
- "_clpcInternalAccessClient"
- "_isInternal"
- "clpcInternalAccessClient"
- "isChargingTPLite"
- "isInternal"
- "numberWithUnsignedInt:"
- "setClpcInternalAccessClient:"
- "setIsInternal:"
- "setRPCBufferSize:"
- "softlink:o:path:/System/Library/../../AppleInternal/Library/Frameworks/PerformanceControlKitInternal.framework/PerformanceControlKitInternal"
```
