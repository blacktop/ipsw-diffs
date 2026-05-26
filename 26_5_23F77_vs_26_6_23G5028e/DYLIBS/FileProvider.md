## FileProvider

> `/System/Library/Frameworks/FileProvider.framework/FileProvider`

```diff

-4018.120.24.0.0
-  __TEXT.__text: 0x13a60c
+4018.160.4.0.0
+  __TEXT.__text: 0x13a668
   __TEXT.__auth_stubs: 0x1ce0
   __TEXT.__objc_methlist: 0xe714
   __TEXT.__const: 0x88a
   __TEXT.__gcc_except_tab: 0x9cf8
-  __TEXT.__cstring: 0x14bd9
+  __TEXT.__cstring: 0x14c1c
   __TEXT.__oslogstring: 0xdea1
   __TEXT.__dlopen_cstrs: 0x793
   __TEXT.__ustring: 0x21e

   __TEXT.__swift5_types: 0x8
   __TEXT.__swift_as_entry: 0x4
   __TEXT.__swift_as_ret: 0x4
-  __TEXT.__unwind_info: 0x5d40
+  __TEXT.__unwind_info: 0x5d48
   __TEXT.__eh_frame: 0xa0
   __TEXT.__objc_classname: 0x2048
   __TEXT.__objc_methname: 0x24512

   __DATA_CONST.__objc_arraydata: 0xab0
   __AUTH_CONST.__auth_got: 0xe80
   __AUTH_CONST.__const: 0x1cc8
-  __AUTH_CONST.__cfstring: 0x11400
+  __AUTH_CONST.__cfstring: 0x11420
   __AUTH_CONST.__objc_const: 0x24a90
   __AUTH_CONST.__objc_intobj: 0x108
   __AUTH_CONST.__objc_arrayobj: 0x198

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
-  UUID: 9E1989CB-ECC7-39DE-9B4B-3E18C5531946
+  UUID: 5AF9DAED-E98C-3840-A54D-1907D59F4F91
   Functions: 7383
-  Symbols:   24082
-  CStrings:  12396
+  Symbols:   24083
+  CStrings:  12397
 
Symbols:
+ ___block_literal_global.130
+ ___block_literal_global.77
+ _fpfs_is_seed_build.is_seed_build
- ___block_literal_global.128
- ___block_literal_global.75
Functions:
~ -[NSURL(FPAdditions) fp_issueSandboxExtensionOfClass:report:error:] : 808 -> 884
~ _fpfs_is_seed_build : 52 -> 56
~ ___fpfs_is_seed_build_block_invoke : 4 -> 16
CStrings:
+ "4018.160.4"
+ "couldn't issue sandbox extension %s for '%s'; failed strdup concatenated path"
+ "couldn't issue sandbox extension %s for '%s'; failed to build path from parent"
- "%s/%s"
- "4018.120.24"
- "couldn't issue sandbox extension %s for '%s'; failed to build path from parent: %s"

```
