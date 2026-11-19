## DMCTools

> `/System/Library/PrivateFrameworks/DMCTools.framework/Versions/A/DMCTools`

```diff

-113.1.9.0.0
-  __TEXT.__text: 0x22760
-  __TEXT.__objc_methlist: 0x718
-  __TEXT.__const: 0xde0
-  __TEXT.__oslogstring: 0xe16
+113.40.20.0.0
+  __TEXT.__text: 0x235cc
+  __TEXT.__objc_methlist: 0x778
+  __TEXT.__const: 0xdf8
+  __TEXT.__oslogstring: 0xfa6
   __TEXT.__swift5_typeref: 0x3db
   __TEXT.__cstring: 0x571
-  __TEXT.__swift5_capture: 0x114
+  __TEXT.__swift5_capture: 0x124
   __TEXT.__constg_swiftt: 0x1f4
   __TEXT.__swift5_builtin: 0x78
   __TEXT.__swift5_reflstr: 0x150

   __TEXT.__swift5_fieldmd: 0x1d4
   __TEXT.__swift5_proto: 0xa4
   __TEXT.__swift5_types: 0x2c
-  __TEXT.__unwind_info: 0x6f8
-  __TEXT.__eh_frame: 0x790
+  __TEXT.__unwind_info: 0x740
+  __TEXT.__eh_frame: 0x7f0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__const: 0x50
   __DATA_CONST.__objc_classlist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x548
-  __DATA_CONST.__got: 0x230
-  __AUTH_CONST.__const: 0x6f8
-  __AUTH_CONST.__objc_const: 0xfb0
+  __DATA_CONST.__objc_selrefs: 0x598
+  __DATA_CONST.__got: 0x238
+  __AUTH_CONST.__const: 0x748
+  __AUTH_CONST.__objc_const: 0xfe0
   __AUTH_CONST.__auth_got: 0x730
   __AUTH_CONST.__auth_ptr: 0x2f0
   __AUTH.__objc_data: 0x2e0
   __AUTH.__data: 0x258
-  __DATA.__data: 0x4b0
+  __DATA.__data: 0x4b8
   __DATA.__bss: 0x1480
   __DATA_DIRTY.__objc_data: 0xa0
   __DATA_DIRTY.__data: 0xf0

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 651
-  Symbols:   446
-  CStrings:  83
+  Functions: 669
+  Symbols:   455
+  CStrings:  87
 
Symbols:
+ _OBJC_CLASS_$_BGRepeatingSystemTaskRequest
+ _objc_msgSend$_activeInterval
+ _objc_msgSend$cancelExistingTaskIfNeeded
+ _objc_msgSend$infuseBaseRequest:requirements:
+ _objc_msgSend$recordScheduledInterval:
+ _objc_msgSend$setInterval:
+ _objc_msgSend$setMinDurationBetweenInstances:
+ _objc_msgSend$set_activeInterval:
+ _objc_msgSend$submitNewRepeatingRequestWithInterval:requirements:
+ _objc_msgSend$updateExistingRepeatingRequest:interval:requirements:
- _objc_msgSend$infuseRequest:interval:tolerance:requirements:
CStrings:
+ "DMCBackgroundTask failed to submit repeating task '%{public}s' with error: %{public}@"
+ "DMCBackgroundTask failed to update repeating task '%{public}s' with error: %{public}@. Falling back to submit."
+ "DMCBackgroundTask submitted repeating task '%{public}s' with interval %{public}f seconds"
+ "DMCBackgroundTask task with name %s exists, attempting to cancel before submitting"
+ "DMCBackgroundTask updated repeating task '%{public}s' with interval %{public}f seconds"
- "DMCBackgroundTask task with name %s exists, attempting to cancel before submitting again"
```
