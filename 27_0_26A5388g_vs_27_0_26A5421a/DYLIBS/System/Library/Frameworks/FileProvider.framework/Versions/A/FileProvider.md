## FileProvider

> `/System/Library/Frameworks/FileProvider.framework/Versions/A/FileProvider`

```diff

-4838.0.93.0.0
-  __TEXT.__text: 0x13fb04
-  __TEXT.__objc_methlist: 0xe89c
+4838.0.125.0.0
+  __TEXT.__text: 0x1402e8
+  __TEXT.__objc_methlist: 0xe90c
   __TEXT.__const: 0x8aa
-  __TEXT.__cstring: 0x14ff4
-  __TEXT.__gcc_except_tab: 0x8938
+  __TEXT.__cstring: 0x1504f
+  __TEXT.__gcc_except_tab: 0x8958
   __TEXT.__oslogstring: 0xe0ea
   __TEXT.__dlopen_cstrs: 0x6ba
   __TEXT.__ustring: 0x21e

   __TEXT.__swift_as_entry: 0x4
   __TEXT.__swift_as_ret: 0x4
   __TEXT.__swift_as_cont: 0xc
-  __TEXT.__unwind_info: 0x5818
+  __TEXT.__unwind_info: 0x5848
   __TEXT.__eh_frame: 0xa0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__objc_catlist: 0x90
   __DATA_CONST.__objc_protolist: 0x2a8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x6fe8
+  __DATA_CONST.__objc_selrefs: 0x7020
   __DATA_CONST.__objc_protorefs: 0x158
   __DATA_CONST.__objc_superrefs: 0x548
   __DATA_CONST.__objc_arraydata: 0xab0
   __DATA_CONST.__got: 0xb50
-  __AUTH_CONST.__const: 0x6f88
-  __AUTH_CONST.__cfstring: 0x11920
-  __AUTH_CONST.__objc_const: 0x24fd0
+  __AUTH_CONST.__const: 0x6fb8
+  __AUTH_CONST.__cfstring: 0x11960
+  __AUTH_CONST.__objc_const: 0x25028
   __AUTH_CONST.__objc_intobj: 0x120
   __AUTH_CONST.__objc_arrayobj: 0x198
   __AUTH_CONST.__auth_got: 0xf18
   __AUTH.__objc_data: 0x2490
   __AUTH.__data: 0x10
-  __DATA.__objc_ivar: 0x10c8
+  __DATA.__objc_ivar: 0x10cc
   __DATA.__data: 0x23f0
   __DATA.__bss: 0xbc0
   __DATA.__common: 0x2b

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
-  Functions: 7516
-  Symbols:   14244
-  CStrings:  4081
+  Functions: 7528
+  Symbols:   14263
+  CStrings:  4085
 
Symbols:
+ +[FPTask exec:environment:stdinHandle:stdoutString:stderrString:error:]
+ +[FPTask freePreparedEnvpArray:]
+ -[FPItemManager outOfBandIndexItemIDs:completionHandler:]
+ -[FPTask environment]
+ -[FPTask newPreparedEnvpArray]
+ -[FPTask setEnvironment:]
+ -[NSURL(FPAdditions) fp_pathOnlyRelationshipToItemAtURL:]
+ GCC_except_table115
+ GCC_except_table53
+ OBJC_IVAR_$_FPTask._environment
+ _FPPrivateNormalizedPath
+ _FPURLIsFSKitStorage
+ __71+[FPTask exec:environment:stdinHandle:stdoutString:stderrString:error:]_block_invoke
+ ___30-[FPTask newPreparedEnvpArray]_block_invoke
+ ___71+[FPTask exec:environment:stdinHandle:stdoutString:stderrString:error:]_block_invoke
+ ___block_descriptor_48_e8_32r_e35_v32?0"NSString"8"NSString"16^B24l
+ _fpfs_get_provider_content_version
+ _fpfs_remove_provider_content_version
+ _objc_msgSend$caseInsensitiveCompare:
+ _objc_msgSend$exec:environment:stdinHandle:stdoutString:stderrString:error:
+ _objc_msgSend$freePreparedEnvpArray:
+ _objc_msgSend$newPreparedEnvpArray
+ _objc_msgSend$outOfBandIndexItemIDs:completionHandler:
+ _objc_msgSend$setEnvironment:
- GCC_except_table146
- GCC_except_table82
- __59+[FPTask exec:stdinHandle:stdoutString:stderrString:error:]_block_invoke
- ___59+[FPTask exec:stdinHandle:stdoutString:stderrString:error:]_block_invoke
- _objc_msgSend$exec:stdinHandle:stdoutString:stderrString:error:
CStrings:
+ "%@=%@"
+ "/private/"
+ "4838.0.125"
+ "com.apple.genstore.fp_provider_cver#C"
+ "v32@?0@\"NSString\"8@\"NSString\"16^B24"
- "4838.0.93"
```
