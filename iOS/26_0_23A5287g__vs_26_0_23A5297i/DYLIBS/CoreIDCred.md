## CoreIDCred

> `/System/Library/PrivateFrameworks/CoreIDCred.framework/CoreIDCred`

```diff

-8.38.3.0.0
-  __TEXT.__text: 0x48270
-  __TEXT.__auth_stubs: 0xda0
-  __TEXT.__objc_methlist: 0x2054
+8.40.1.0.0
+  __TEXT.__text: 0x48454
+  __TEXT.__auth_stubs: 0xdf0
+  __TEXT.__objc_methlist: 0x206c
   __TEXT.__const: 0x3708
   __TEXT.__cstring: 0x2046
-  __TEXT.__oslogstring: 0x39fc
+  __TEXT.__oslogstring: 0x3a3c
+  __TEXT.__gcc_except_tab: 0x14
   __TEXT.__constg_swiftt: 0x900
   __TEXT.__swift5_typeref: 0xe52
   __TEXT.__swift5_builtin: 0x1b8

   __TEXT.__swift5_capture: 0x590
   __TEXT.__swift_as_entry: 0xd8
   __TEXT.__swift_as_ret: 0xf0
-  __TEXT.__unwind_info: 0x18d8
+  __TEXT.__unwind_info: 0x18f0
   __TEXT.__eh_frame: 0x2380
   __TEXT.__objc_classname: 0x2be
-  __TEXT.__objc_methname: 0x41cc
-  __TEXT.__objc_methtype: 0xec6
-  __TEXT.__objc_stubs: 0x19e0
+  __TEXT.__objc_methname: 0x41d2
+  __TEXT.__objc_methtype: 0xecf
+  __TEXT.__objc_stubs: 0x1a20
   __DATA_CONST.__got: 0x288
-  __DATA_CONST.__const: 0x9d0
+  __DATA_CONST.__const: 0x9f8
   __DATA_CONST.__objc_classlist: 0xe8
   __DATA_CONST.__objc_protolist: 0x58
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0xc40
   __DATA_CONST.__objc_protorefs: 0x30
   __DATA_CONST.__objc_superrefs: 0xb8
-  __AUTH_CONST.__auth_got: 0x6d8
+  __AUTH_CONST.__auth_got: 0x708
   __AUTH_CONST.__const: 0x23a8
   __AUTH_CONST.__cfstring: 0x16e0
-  __AUTH_CONST.__objc_const: 0x3758
+  __AUTH_CONST.__objc_const: 0x3768
   __AUTH.__objc_data: 0x2a8
   __AUTH.__data: 0x1b8
   __DATA.__objc_ivar: 0x244

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 64B3A9FA-D83D-36C7-B978-68F192054742
-  Functions: 2382
-  Symbols:   3321
-  CStrings:  1453
+  UUID: 0F13CB25-ECA0-3F40-A932-8756578D06FC
+  Functions: 2386
+  Symbols:   3339
+  CStrings:  1456
 
Symbols:
+ -[DCCredentialStoreClient interruptionHandler]
+ -[DCCredentialStoreClient setInterruptionHandler:]
+ GCC_except_table0
+ __Unwind_Resume
+ ___40-[DCCredentialStore initWithPartitions:]_block_invoke
+ ___40-[DCCredentialStore initWithPartitions:]_block_invoke.cold.1
+ ___block_descriptor_40_e8_32w_e5_v8?0lw32l8
+ ___objc_personality_v0
+ _objc_copyWeak
+ _objc_destroyWeak
+ _objc_initWeak
+ _objc_loadWeakRetained
+ _objc_msgSend$interruptionHandler
+ _objc_msgSend$setInterruptionHandler:
CStrings:
+ "@?16@0:8"
+ "DCCredentialStore server interrupted, resetting configured flag"
+ "T@?,C"

```
