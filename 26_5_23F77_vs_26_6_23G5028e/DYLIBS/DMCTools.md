## DMCTools

> `/System/Library/PrivateFrameworks/DMCTools.framework/DMCTools`

```diff

-59.120.4.0.0
-  __TEXT.__text: 0x21480
-  __TEXT.__auth_stubs: 0xf10
+59.160.4.0.0
+  __TEXT.__text: 0x21510
+  __TEXT.__auth_stubs: 0xf00
   __TEXT.__objc_methlist: 0x718
   __TEXT.__const: 0xe08
-  __TEXT.__oslogstring: 0xe16
+  __TEXT.__oslogstring: 0xe56
   __TEXT.__swift5_typeref: 0x3ef
   __TEXT.__cstring: 0x5b1
   __TEXT.__swift5_capture: 0x104

   __DATA_CONST.__objc_classlist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x550
-  __AUTH_CONST.__auth_got: 0x790
+  __AUTH_CONST.__auth_got: 0x788
   __AUTH_CONST.__const: 0x6d0
   __AUTH_CONST.__objc_const: 0xfb0
   __AUTH.__objc_data: 0x380

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: FF364AC3-6394-328C-8159-C8F93CB02C92
+  UUID: E56230DB-5549-3B4B-92BF-8DF3AE415816
   Functions: 632
-  Symbols:   548
+  Symbols:   547
   CStrings:  332
 
Symbols:
- _objc_retain_x26
Functions:
~ sub_24f785698 -> sub_2508a4698 : 1536 -> 1664
~ sub_24f786c0c -> sub_2508a5c8c : 1752 -> 1768
CStrings:
+ "DMCBackgroundTask failed to cancel task: %{public}s, error: %{public}@. Aborting submit."
+ "DMCBackgroundTask failed to update task '%{public}s' with error: %{public}@. Falling back to submit."
- "DMCBackgroundTask failed to cancel task task: %s"
- "DMCBackgroundTask failed to update task '%{public}s' with error: %{public}@"

```
