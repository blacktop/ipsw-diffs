## HearingModeService_Private

> `/System/Library/PrivateFrameworks/HearingModeService_Private.framework/HearingModeService_Private`

```diff

-21.5.0.0.0
-  __TEXT.__text: 0x79f0
-  __TEXT.__auth_stubs: 0x370
-  __TEXT.__objc_methlist: 0x504
+21.9.1.0.0
+  __TEXT.__text: 0x7d50
+  __TEXT.__auth_stubs: 0x380
+  __TEXT.__objc_methlist: 0x514
   __TEXT.__const: 0x60
-  __TEXT.__gcc_except_tab: 0x1fc
-  __TEXT.__cstring: 0x2208
+  __TEXT.__gcc_except_tab: 0x21c
+  __TEXT.__cstring: 0x235b
   __TEXT.__unwind_info: 0x288
   __TEXT.__objc_classname: 0xfc
-  __TEXT.__objc_methname: 0x1819
+  __TEXT.__objc_methname: 0x18a0
   __TEXT.__objc_methtype: 0x678
-  __TEXT.__objc_stubs: 0x12c0
+  __TEXT.__objc_stubs: 0x1380
   __DATA_CONST.__got: 0xf0
-  __DATA_CONST.__const: 0x368
+  __DATA_CONST.__const: 0x380
   __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x568
+  __DATA_CONST.__objc_selrefs: 0x598
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x20
-  __AUTH_CONST.__auth_got: 0x1c8
+  __AUTH_CONST.__auth_got: 0x1d0
   __AUTH_CONST.__const: 0xe0
-  __AUTH_CONST.__cfstring: 0x100
+  __AUTH_CONST.__cfstring: 0x120
   __AUTH_CONST.__objc_const: 0x1228
   __AUTH.__objc_data: 0x50
   __DATA.__objc_ivar: 0x74

   - /System/Library/PrivateFrameworks/CoreUtils.framework/CoreUtils
   - /System/Library/PrivateFrameworks/HearingModeService.framework/HearingModeService
   - /System/Library/PrivateFrameworks/PersonalAudio.framework/PersonalAudio
+  - /System/Library/PrivateFrameworks/ToneLibrary.framework/ToneLibrary
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 149
-  Symbols:   245
-  CStrings:  513
+  Functions: 151
+  Symbols:   248
+  CStrings:  529
 
Symbols:
+ _objc_retainAutorelease
CStrings:
+ "currentNoiseLevel"
+ "setCurrentNoiseLevel:"
+ "Multimodal context updated for unknown identifier: %!@(MISSING)"
+ "-[HMDeviceManager _aaControllerEnsureStarted]_block_invoke_4"
+ "HMDeviceRecord UUID %!@(MISSING), SPL level changed: %!s(MISSING) --> %!s(MISSING)"
+ "lowNoise"
+ "Unknown"
+ "Multimodal context message dimension: %!d(MISSING), not supported"
+ "setMultimodalContextMessageHandler:"
+ "length"
+ "_multimodalContextMessageReceived:identifier:"
+ "highNoise"
+ "bytes"
+ "Multimodal context message type: %!d(MISSING), not supported"
+ "-[HMDeviceManager _multimodalContextMessageReceived:identifier:]"
+ "override-bud-to-source-context"
+ "?"
- "-[HMDeviceManager _aaControllerEnsureStarted]_block_invoke_3"

```
