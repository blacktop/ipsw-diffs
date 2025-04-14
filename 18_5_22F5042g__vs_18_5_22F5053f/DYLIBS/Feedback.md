## Feedback

> `/System/Library/PrivateFrameworks/Feedback.framework/Feedback`

```diff

-150.10.0.0.0
-  __TEXT.__text: 0x108674
+150.12.0.0.0
+  __TEXT.__text: 0x108bdc
   __TEXT.__auth_stubs: 0x3310
   __TEXT.__objc_methlist: 0x968
   __TEXT.__const: 0x9574

   __TEXT.__swift5_capture: 0xfd8
   __TEXT.__swift5_proto: 0x540
   __TEXT.__swift5_types: 0x2ec
-  __TEXT.__oslogstring: 0x38ba
+  __TEXT.__oslogstring: 0x39ea
   __TEXT.__swift5_mpenum: 0x40
   __TEXT.__swift_as_entry: 0x94
   __TEXT.__swift_as_ret: 0xe0
   __TEXT.__swift5_protos: 0x18
-  __TEXT.__unwind_info: 0x3428
+  __TEXT.__unwind_info: 0x3420
   __TEXT.__eh_frame: 0x2da0
   __TEXT.__objc_classname: 0xc7
   __TEXT.__objc_methname: 0x2003

   __DATA_CONST.__objc_selrefs: 0xa98
   __DATA_CONST.__objc_protorefs: 0x60
   __AUTH_CONST.__auth_got: 0x1988
-  __AUTH_CONST.__auth_ptr: 0x1348
+  __AUTH_CONST.__auth_ptr: 0x1220
   __AUTH_CONST.__const: 0x67f8
   __AUTH_CONST.__objc_const: 0x3118
   __AUTH.__objc_data: 0x1520

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 5082
+  Functions: 5083
   Symbols:   568
-  CStrings:  1237
+  CStrings:  1241
 
CStrings:
+ "Should show batch UI? NO because score is zero AND failed to fetch donations"
+ "Should show batch UI? NO because score is zero AND there are no donations"
+ "Should show batch UI? Yes because score is > 0. Raw score [%ld]"
+ "Should show batch UI? Yes because score is zero but there are donations"

```
