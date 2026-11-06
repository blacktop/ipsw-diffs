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
+182.40.2.0.0
+  __TEXT.__text: 0x167b8
+  __TEXT.__auth_stubs: 0x520
+  __TEXT.__objc_stubs: 0x2ee0
+  __TEXT.__objc_methlist: 0x1f44
+  __TEXT.__const: 0x138
+  __TEXT.__cstring: 0x1143
+  __TEXT.__objc_methname: 0x36a1
+  __TEXT.__oslogstring: 0x262b
   __TEXT.__objc_classname: 0x347
-  __TEXT.__objc_methtype: 0x6cb
-  __TEXT.__gcc_except_tab: 0x48
-  __TEXT.__dlopen_cstrs: 0x8d
-  __TEXT.__unwind_info: 0x7f0
-  __DATA_CONST.__const: 0x8c0
-  __DATA_CONST.__cfstring: 0x11a0
+  __TEXT.__objc_methtype: 0x6bb
+  __TEXT.__gcc_except_tab: 0x38
+  __TEXT.__unwind_info: 0x7d8
+  __DATA_CONST.__const: 0x878
+  __DATA_CONST.__cfstring: 0x1240
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
+  __DATA.__objc_const: 0x4790
+  __DATA.__objc_selrefs: 0xeb0
+  __DATA.__objc_ivar: 0x21c
   __DATA.__objc_data: 0x820
   __DATA.__data: 0x420
-  __DATA.__bss: 0x250
+  __DATA.__bss: 0x238
   __DATA.__common: 0x80
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation

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
+  Functions: 737
+  Symbols:   119
+  CStrings:  1212
 
Symbols:
- __Block_object_dispose
- __sl_dlopen
- _abort_report_np
- _dlopen_preflight
- _free
- _objc_getClass
CStrings:
+ "AssertionTimeout"
+ "AssistantMode changing from %@ to %@ (siriRemoteSession=%d, siriLocalSession=%d, assistantUI=%d, nanoSiriX=%d)"
+ "HardwarePlatform"
+ "HomeAcc"
+ "HomeAccessory"
+ "Overriding InBoxUpdateMode Assertion with defaults timeout value %ld"
+ "Trial: Setting TrialID: %lld with CLPC"
+ "Trial:Error setting clpc trial value %@"
+ "assertionTimeout"
+ "com.apple.powerexperienced.inboxupdatemode"
+ "integerValue"
+ "kHardwarePlatformContext"
+ "numberWithInteger:"
+ "q16@0:8"
+ "resetForTesting"
+ "waitForPendingEvaluation"
- "%s"
- "/AppleInternal/Library/Frameworks/PerformanceControlKitInternal.framework/PerformanceControlKitInternal"
- "/System/Library/../../AppleInternal/Library/Frameworks/PerformanceControlKitInternal.framework/Contents/MacOS/PerformanceControlKitInternal"
- "@\"<CLPCInternalAccess>\""
- "AssistantMode changing from %@ to %@ (siriRemoteSession=%d, siriLocalSession=%d, assistantUI=%d, siriAudio=%d)"
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
