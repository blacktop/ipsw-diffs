## FileProvider

> `/System/Library/Frameworks/FileProvider.framework/FileProvider`

```diff

-4018.100.242.0.0
-  __TEXT.__text: 0x13a42c
+4018.120.13.0.0
+  __TEXT.__text: 0x13a5e4
   __TEXT.__auth_stubs: 0x1ce0
-  __TEXT.__objc_methlist: 0xe6f4
+  __TEXT.__objc_methlist: 0xe6fc
   __TEXT.__const: 0x88a
   __TEXT.__gcc_except_tab: 0x9cf8
-  __TEXT.__cstring: 0x14ac4
+  __TEXT.__cstring: 0x14bc1
   __TEXT.__oslogstring: 0xdea1
   __TEXT.__dlopen_cstrs: 0x793
   __TEXT.__ustring: 0x21e

   __TEXT.__unwind_info: 0x5d40
   __TEXT.__eh_frame: 0xa0
   __TEXT.__objc_classname: 0x2045
-  __TEXT.__objc_methname: 0x24475
+  __TEXT.__objc_methname: 0x244aa
   __TEXT.__objc_methtype: 0x69e2
   __TEXT.__objc_stubs: 0x14240
   __DATA_CONST.__got: 0xac0
-  __DATA_CONST.__const: 0x6100
+  __DATA_CONST.__const: 0x6108
   __DATA_CONST.__objc_classlist: 0x690
   __DATA_CONST.__objc_catlist: 0x88
   __DATA_CONST.__objc_protolist: 0x2a0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x6ea0
+  __DATA_CONST.__objc_selrefs: 0x6ea8
   __DATA_CONST.__objc_protorefs: 0x158
   __DATA_CONST.__objc_superrefs: 0x550
   __DATA_CONST.__objc_arraydata: 0xab0
   __AUTH_CONST.__auth_got: 0xe80
   __AUTH_CONST.__const: 0x1cc8
-  __AUTH_CONST.__cfstring: 0x11360
-  __AUTH_CONST.__objc_const: 0x24a38
+  __AUTH_CONST.__cfstring: 0x113e0
+  __AUTH_CONST.__objc_const: 0x24a60
   __AUTH_CONST.__objc_intobj: 0x108
   __AUTH_CONST.__objc_arrayobj: 0x198
   __AUTH.__objc_data: 0x4b0

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
-  UUID: AE43681F-807D-3554-B2A6-6860D9F82716
+  UUID: 427508AE-626C-3D6D-9A4A-A96DD520F65A
   Functions: 7381
-  Symbols:   24076
-  CStrings:  12380
+  Symbols:   24078
+  CStrings:  12390
 
Symbols:
+ _NSFileProviderErrorWasTimeoutKey
+ ___block_descriptor_102_e8_32s40s48s56s64s72r_e17_v16?0"NSError"8ls32l8r72l8s40l8s48l8s56l8s64l8
+ ___block_literal_global.128
+ ___block_literal_global.264
+ ___block_literal_global.437
+ ___block_literal_global.510
+ ___block_literal_global.592
+ ___block_literal_global.594
+ ___block_literal_global.75
+ _fpfs_is_seed_build.is_seed_build
- ___block_descriptor_102_e8_32s40s48s56s64s72r_e17_v16?0"NSError"8lr72l8s32l8s40l8s48l8s56l8s64l8
- ___block_literal_global.263
- ___block_literal_global.436
- ___block_literal_global.445
- ___block_literal_global.509
- ___block_literal_global.591
- ___block_literal_global.593
Functions:
~ -[FPXPCAutomaticErrorProxy forwardInvocation:] : 2532 -> 2504
~ -[NSURL(FPAdditions) fp_issueSandboxExtensionOfClass:report:error:] : 428 -> 808
~ _fpfs_is_seed_build : 52 -> 56
~ ___fpfs_is_seed_build_block_invoke : 4 -> 16
~ ___46-[FPXPCAutomaticErrorProxy forwardInvocation:]_block_invoke.19 : 852 -> 924
CStrings:
+ "%s/%s"
+ "4018.120.13"
+ "_test_removeUnOwnedDirectoryAtURL:completionHandler:"
+ "couldn't issue sandbox extension %s for '%s': %s"
+ "couldn't issue sandbox extension %s for '%s'; failed to build path from parent: %s"
+ "couldn't issue sandbox extension %s for '%s'; failed to get realpath for parent: %s"
+ "couldn't issue sandbox extension %s for '%s'; failed to get realpath: %s"
+ "timeout"
- "4018.100.242"
- "couldn't issue sandbox extension %s for '%@': %s"

```
