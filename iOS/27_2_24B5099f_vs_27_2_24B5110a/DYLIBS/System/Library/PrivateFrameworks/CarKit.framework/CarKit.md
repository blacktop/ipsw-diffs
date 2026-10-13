## CarKit

> `/System/Library/PrivateFrameworks/CarKit.framework/CarKit`

```diff

-807.4.0.0.0
-  __TEXT.__text: 0x602a0
-  __TEXT.__objc_methlist: 0x63ec
+807.4.1.0.0
+  __TEXT.__text: 0x60544
+  __TEXT.__objc_methlist: 0x6404
   __TEXT.__const: 0x558
   __TEXT.__gcc_except_tab: 0xa1c
-  __TEXT.__oslogstring: 0x6c26
+  __TEXT.__oslogstring: 0x6c96
   __TEXT.__cstring: 0x5b6d
   __TEXT.__dlopen_cstrs: 0x15e
   __TEXT.__constg_swiftt: 0x1a0

   __TEXT.__swift5_builtin: 0x50
   __TEXT.__swift5_assocty: 0x30
   __TEXT.__swift5_proto: 0x10
-  __TEXT.__unwind_info: 0x2610
+  __TEXT.__unwind_info: 0x2618
   __TEXT.__eh_frame: 0x80
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x20a0
+  __DATA_CONST.__const: 0x20c8
   __DATA_CONST.__objc_classlist: 0x278
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x170
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3750
+  __DATA_CONST.__objc_selrefs: 0x3770
   __DATA_CONST.__objc_protorefs: 0x108
   __DATA_CONST.__objc_superrefs: 0x1e0
   __DATA_CONST.__objc_arraydata: 0xc0
-  __DATA_CONST.__got: 0x880
+  __DATA_CONST.__got: 0x888
   __AUTH_CONST.__const: 0x1bc0
   __AUTH_CONST.__cfstring: 0x5d80
   __AUTH_CONST.__objc_const: 0x10370

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 3058
-  Symbols:   4757
-  CStrings:  1434
+  Functions: 3060
+  Symbols:   4761
+  CStrings:  1436
 
Symbols:
+ +[CRVehicleVideoSettings _analyticsEntriesFromData:]
+ _OBJC_CLASS_$_NSJSONSerialization
+ __OBJC_$_CLASS_METHODS_CRVehicleVideoSettings
+ ___block_descriptor_48_e8_32s40bs_e28_v24?0"NSData"8"NSError"16ls40l8s32l8
Functions:
~ ___59-[CRVehicleVideoSettings fetchAnalyticsDataWithCompletion:]_block_invoke : 188 -> 192
~ ___59-[CRVehicleVideoSettings fetchAnalyticsDataWithCompletion:]_block_invoke_2 : 320 -> 236
+ +[CRVehicleVideoSettings _analyticsEntriesFromData:]
+ +[CRVehicleVideoSettings _analyticsEntriesFromData:].cold.1
CStrings:
+ "couldn't expand analytics into entries, returning single blob: %{public}@"
+ "couldn't serialize analytics entry: %{public}@"
```
