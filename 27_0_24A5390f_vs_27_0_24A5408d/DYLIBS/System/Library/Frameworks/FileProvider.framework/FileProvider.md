## FileProvider

> `/System/Library/Frameworks/FileProvider.framework/FileProvider`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__swift5_typeref`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_fieldmd`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift5_types`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH.__objc_data`
- `__AUTH.__data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`

```diff

-4838.0.93.0.0
-  __TEXT.__text: 0x12d45c
-  __TEXT.__objc_methlist: 0xe97c
+4838.0.125.0.0
+  __TEXT.__text: 0x12dc84
+  __TEXT.__objc_methlist: 0xe9dc
   __TEXT.__const: 0x88a
-  __TEXT.__cstring: 0x14e47
-  __TEXT.__gcc_except_tab: 0x8b04
+  __TEXT.__cstring: 0x14ea2
+  __TEXT.__gcc_except_tab: 0x8b24
   __TEXT.__oslogstring: 0xe394
   __TEXT.__dlopen_cstrs: 0x793
   __TEXT.__ustring: 0x21e

   __TEXT.__swift_as_entry: 0x4
   __TEXT.__swift_as_ret: 0x4
   __TEXT.__swift_as_cont: 0xc
-  __TEXT.__unwind_info: 0x5918
+  __TEXT.__unwind_info: 0x5948
   __TEXT.__eh_frame: 0xa0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x61f8
+  __DATA_CONST.__const: 0x6220
   __DATA_CONST.__objc_classlist: 0x698
   __DATA_CONST.__objc_catlist: 0x88
   __DATA_CONST.__objc_protolist: 0x2a8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x70a8
+  __DATA_CONST.__objc_selrefs: 0x70e0
   __DATA_CONST.__objc_protorefs: 0x158
   __DATA_CONST.__objc_superrefs: 0x550
   __DATA_CONST.__objc_arraydata: 0xab0
   __DATA_CONST.__got: 0xb18
   __AUTH_CONST.__const: 0x1da8
-  __AUTH_CONST.__cfstring: 0x115a0
-  __AUTH_CONST.__objc_const: 0x25008
+  __AUTH_CONST.__cfstring: 0x115e0
+  __AUTH_CONST.__objc_const: 0x25060
   __AUTH_CONST.__objc_intobj: 0x120
   __AUTH_CONST.__objc_arrayobj: 0x198
   __AUTH_CONST.__auth_got: 0xeb0
   __AUTH.__objc_data: 0x25f8
   __AUTH.__data: 0x10
-  __DATA.__objc_ivar: 0x10d4
+  __DATA.__objc_ivar: 0x10d8
   __DATA.__data: 0x23f0
   __DATA.__bss: 0xc30
   __DATA.__common: 0x39

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
-  Functions: 7455
-  Symbols:   13824
-  CStrings:  4058
+  Functions: 7467
+  Symbols:   13846
+  CStrings:  4062
 
Symbols:
+ +[FPTask exec:environment:stdinHandle:stdoutString:stderrString:error:]
+ +[FPTask freePreparedEnvpArray:]
+ -[FPItemManager outOfBandIndexItemIDs:completionHandler:]
+ -[FPTask environment]
+ -[FPTask newPreparedEnvpArray]
+ -[FPTask setEnvironment:]
+ -[NSURL(FPAdditions) fp_pathOnlyRelationshipToItemAtURL:]
+ GCC_except_table104
+ GCC_except_table115
+ GCC_except_table137
+ GCC_except_table90
+ GCC_except_table95
+ _FPPrivateNormalizedPath
+ _FPURLIsFSKitStorage
+ _OBJC_IVAR_$_FPTask._environment
+ ___30-[FPTask newPreparedEnvpArray]_block_invoke
+ ___71+[FPTask exec:environment:stdinHandle:stdoutString:stderrString:error:]_block_invoke
+ ___block_descriptor_48_e8_32r_e35_v32?0"NSString"8"NSString"16^B24lr32l8
+ _fpfs_get_provider_content_version
+ _fpfs_remove_provider_content_version
+ _objc_msgSend$caseInsensitiveCompare:
+ _objc_msgSend$exec:environment:stdinHandle:stdoutString:stderrString:error:
+ _objc_msgSend$fp_pathOnlyRelationshipToItemAtURL:
+ _objc_msgSend$freePreparedEnvpArray:
+ _objc_msgSend$newPreparedEnvpArray
+ _objc_msgSend$outOfBandIndexItemIDs:completionHandler:
+ _objc_msgSend$setEnvironment:
- GCC_except_table121
- GCC_except_table136
- GCC_except_table79
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
