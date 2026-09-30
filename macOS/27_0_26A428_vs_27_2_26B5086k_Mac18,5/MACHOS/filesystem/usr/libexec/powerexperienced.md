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
-  __TEXT.__text: 0x169dc
-  __TEXT.__auth_stubs: 0x580
-  __TEXT.__objc_stubs: 0x2f00
-  __TEXT.__objc_methlist: 0x1f2c
-  __TEXT.__const: 0x140
-  __TEXT.__cstring: 0x11fa
-  __TEXT.__objc_methname: 0x372c
-  __TEXT.__oslogstring: 0x26b2
+180.0.0.0.0
+  __TEXT.__text: 0x1654c
+  __TEXT.__auth_stubs: 0x520
+  __TEXT.__objc_stubs: 0x2e60
+  __TEXT.__objc_methlist: 0x1f14
+  __TEXT.__const: 0x138
+  __TEXT.__cstring: 0x10f1
+  __TEXT.__objc_methname: 0x3670
+  __TEXT.__oslogstring: 0x25e6
   __TEXT.__objc_classname: 0x347
-  __TEXT.__objc_methtype: 0x6cb
-  __TEXT.__gcc_except_tab: 0x48
-  __TEXT.__dlopen_cstrs: 0x8d
-  __TEXT.__unwind_info: 0x7f0
-  __DATA_CONST.__const: 0x8c0
-  __DATA_CONST.__cfstring: 0x11a0
+  __TEXT.__objc_methtype: 0x6b3
+  __TEXT.__gcc_except_tab: 0x38
+  __TEXT.__unwind_info: 0x7d0
+  __DATA_CONST.__const: 0x878
+  __DATA_CONST.__cfstring: 0x11c0
   __DATA_CONST.__objc_classlist: 0xd0
   __DATA_CONST.__objc_protolist: 0x58
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x38
   __DATA_CONST.__objc_superrefs: 0xc0
   __DATA_CONST.__objc_intobj: 0xc0
-  __DATA_CONST.__auth_got: 0x2d0
+  __DATA_CONST.__auth_got: 0x2a0
   __DATA_CONST.__got: 0xd0
-  __DATA.__objc_const: 0x47c0
-  __DATA.__objc_selrefs: 0xeb8
-  __DATA.__objc_ivar: 0x220
+  __DATA.__objc_const: 0x4760
+  __DATA.__objc_selrefs: 0xe98
+  __DATA.__objc_ivar: 0x218
   __DATA.__objc_data: 0x820
   __DATA.__data: 0x420
   __DATA.__common: 0x80

   - /System/Library/PrivateFrameworks/PerformanceControlKit.framework/Versions/A/PerformanceControlKit
   - /System/Library/PrivateFrameworks/PowerExperience.framework/Versions/A/PowerExperience
   - /System/Library/PrivateFrameworks/PowerLog.framework/Versions/A/PowerLog
-  - /System/Library/PrivateFrameworks/SoftLinking.framework/Versions/A/SoftLinking
   - /System/Library/PrivateFrameworks/Trial.framework/Versions/A/Trial
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 744
-  Symbols:   125
-  CStrings:  1221
+  Functions: 733
+  Symbols:   119
+  CStrings:  1203
 
Symbols:
- __Block_object_dispose
- __sl_dlopen
- _abort_report_np
- _dlopen_preflight
- _free
- _objc_getClass
CStrings:
+ "HardwarePlatform"
+ "Trial: Setting TrialID: %lld with CLPC"
+ "Trial:Error setting clpc trial value %@"
+ "kHardwarePlatformContext"
+ "resetForTesting"
+ "waitForPendingEvaluation"
- "%s"
- "/AppleInternal/Library/Frameworks/PerformanceControlKitInternal.framework/PerformanceControlKitInternal"
- "/System/Library/../../AppleInternal/Library/Frameworks/PerformanceControlKitInternal.framework/Contents/MacOS/PerformanceControlKitInternal"
- "@\"<CLPCInternalAccess>\""
- "CLPCInternalInterface"
- "Error creating CLPC Internal User Client %@"
- "Error setting clpc trial value %@"
- "Initialized internal CLPC Policy Interface"
- "InternalBuild"
- "PerformanceControlKitInternal not available"
- "T@\"<CLPCInternalAccess>\",&,V_clpcInternalAccessClient"
- "TB,V_isInternal"
- "Trial:No trial value for CLPC tuning option. Resetting to default"
- "Unable to find class %s"
- "Updating CLPCInternal client RPC buffer size to 16k"
- "_clpcInternalAccessClient"
- "_isInternal"
- "clpcInternalAccessClient"
- "isInternal"
- "numberWithUnsignedInt:"
- "setClpcInternalAccessClient:"
- "setIsInternal:"
- "setRPCBufferSize:"
- "softlink:o:path:/System/Library/../../AppleInternal/Library/Frameworks/PerformanceControlKitInternal.framework/PerformanceControlKitInternal"
```
