## HearingMLHelperService

> `/System/Library/PrivateFrameworks/HearingMLHelper.framework/XPCServices/HearingMLHelperService.xpc/HearingMLHelperService`

```diff

-485.3.0.0.0
-  __TEXT.__text: 0x101c
-  __TEXT.__auth_stubs: 0x310
-  __TEXT.__objc_stubs: 0x380
+488.0.0.0.0
+  __TEXT.__text: 0x1438
+  __TEXT.__auth_stubs: 0x320
+  __TEXT.__objc_stubs: 0x3a0
   __TEXT.__objc_methlist: 0x20c
   __TEXT.__const: 0x60
   __TEXT.__gcc_except_tab: 0x64
-  __TEXT.__objc_methname: 0x484
-  __TEXT.__oslogstring: 0x2b7
+  __TEXT.__objc_methname: 0x489
+  __TEXT.__oslogstring: 0x4ac
   __TEXT.__cstring: 0xa1
   __TEXT.__objc_classname: 0xd3
   __TEXT.__objc_methtype: 0x1d8
   __TEXT.__unwind_info: 0xc0
-  __DATA_CONST.__auth_got: 0x198
+  __DATA_CONST.__auth_got: 0x1a0
   __DATA_CONST.__got: 0x48
   __DATA_CONST.__const: 0x90
   __DATA_CONST.__cfstring: 0x80

   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x8
   __DATA.__objc_const: 0x408
-  __DATA.__objc_selrefs: 0x198
+  __DATA.__objc_selrefs: 0x1a0
   __DATA.__objc_ivar: 0x10
   __DATA.__objc_data: 0xa0
   __DATA.__data: 0x1e0

   - /System/Library/PrivateFrameworks/HearingMLHelper.framework/HearingMLHelper
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 464E2915-B485-3A5A-8F6B-6BD946C96370
-  Functions: 27
-  Symbols:   75
-  CStrings:  117
+  UUID: 630F407C-ECF2-3AE1-B669-AE2B287F687A
+  Functions: 31
+  Symbols:   76
+  CStrings:  127
 
Symbols:
+ _objc_release_x26
+ _objc_release_x27
- _objc_release
CStrings:
+ "Failed to train detector: invalid hPath"
+ "Failed to train detector: invalid pretrainedWeightsPath"
+ "Invoking train method for detector ID: %@"
+ "Training Detector with ID: %@ started"
+ "Training completed for detector ID: %@ but returned nil model URL with no error"
+ "Training completed successfully for detector ID: %@, model saved at: %@"
+ "Training failed for detector ID: %@ with error: %@"
+ "Using hPath: %@"
+ "Using pretrained weights at path: %@"
+ "XPC Server - forwarding training request to delegate for detector ID: %@"
+ "XPC Server - trainWithDetectorID: %@ received training request"
+ "path"
- "Training Detector with ID: %@"
- "XPC Server - trainWithDetectorID: %@"

```
