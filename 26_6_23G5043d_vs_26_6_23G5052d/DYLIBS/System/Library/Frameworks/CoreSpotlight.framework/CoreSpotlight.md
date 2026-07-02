## CoreSpotlight

> `/System/Library/Frameworks/CoreSpotlight.framework/CoreSpotlight`

```diff

-  __TEXT.__text: 0xe9978
+  __TEXT.__text: 0xe9d34
   __TEXT.__auth_stubs: 0x1d70
   __TEXT.__objc_methlist: 0xd850
   __TEXT.__const: 0xd10
-  __TEXT.__cstring: 0x1468c
-  __TEXT.__oslogstring: 0x84be
-  __TEXT.__gcc_except_tab: 0x2f94
+  __TEXT.__cstring: 0x146ca
+  __TEXT.__oslogstring: 0x8527
+  __TEXT.__gcc_except_tab: 0x3008
   __TEXT.__dlopen_cstrs: 0x49b
   __TEXT.__ustring: 0x3c
   __TEXT.__swift5_typeref: 0x2a0

   __TEXT.__swift_as_ret: 0x24
   __TEXT.__swift5_builtin: 0x14
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0x3d58
+  __TEXT.__unwind_info: 0x3d70
   __TEXT.__eh_frame: 0x210
   __TEXT.__objc_classname: 0x1180
-  __TEXT.__objc_methname: 0x207ab
+  __TEXT.__objc_methname: 0x207b7
   __TEXT.__objc_methtype: 0x2682
   __TEXT.__objc_stubs: 0x10ca0
   __DATA_CONST.__got: 0x858
-  __DATA_CONST.__const: 0x54b8
+  __DATA_CONST.__const: 0x5508
   __DATA_CONST.__objc_classlist: 0x4b0
   __DATA_CONST.__objc_catlist: 0x48
   __DATA_CONST.__objc_protolist: 0x90

   __DATA_CONST.__objc_arraydata: 0xd90
   __AUTH_CONST.__auth_got: 0xed0
   __AUTH_CONST.__const: 0x1a70
-  __AUTH_CONST.__cfstring: 0x13e60
+  __AUTH_CONST.__cfstring: 0x13ec0
   __AUTH_CONST.__objc_const: 0x11fd8
   __AUTH_CONST.__objc_arrayobj: 0xa80
   __AUTH_CONST.__objc_intobj: 0x7c8

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 5910
-  Symbols:   18701
-  CStrings:  12944
+  Functions: 5914
+  Symbols:   18711
+  CStrings:  12954
 
Sections:
~ __TEXT.__objc_methlist : content changed
~ __TEXT.__const : content changed
~ __TEXT.__swift5_typeref : content changed
~ __TEXT.__constg_swiftt : content changed
~ __TEXT.__swift5_proto : content changed
~ __TEXT.__swift_as_entry : content changed
~ __TEXT.__swift_as_ret : content changed
~ __TEXT.__eh_frame : content changed
~ __TEXT.__objc_methtype : content changed
~ __DATA_CONST.__got : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_catlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_selrefs : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__objc_arraydata : content changed
~ __AUTH_CONST.__const : content changed
~ __AUTH_CONST.__objc_const : content changed
~ __AUTH_CONST.__objc_arrayobj : content changed
~ __AUTH_CONST.__objc_intobj : content changed
~ __AUTH_CONST.__objc_dictobj : content changed
~ __AUTH_CONST.__objc_doubleobj : content changed
~ __AUTH.__objc_data : content changed
~ __AUTH.__data : content changed
~ __DATA.__data : content changed
~ __DATA_DIRTY.__objc_data : content changed
~ __DATA_DIRTY.__data : content changed
Symbols:
+ -[CSFileProviderContainerCache filterForDisabledBundles:logForQuery:]
+ ___69-[CSFileProviderContainerCache filterForDisabledBundles:logForQuery:]_block_invoke
+ ___69-[CSFileProviderContainerCache filterForDisabledBundles:logForQuery:]_block_invoke_2
+ ___69-[CSFileProviderContainerCache filterForDisabledBundles:logForQuery:]_block_invoke_3
+ ___69-[CSFileProviderContainerCache filterForDisabledBundles:logForQuery:]_block_invoke_4
+ ___block_descriptor_40_e8_32s_e22_v24?0"NSNumber"8^B16ls32l8
+ ___block_descriptor_40_e8_32s_e22_v24?0"NSString"8^B16ls32l8
+ ___block_descriptor_56_e8_32s40r48r_e35_v32?0"NSString"8"NSNumber"16^B24ls32l8r40l8r48l8
+ ___block_descriptor_57_e8_32s40r_e46_v32?0"NSString"8"NSMutableDictionary"16^B24ls32l8r40l8
- -[CSFileProviderContainerCache filterForDisabledBundles:]
- ___57-[CSFileProviderContainerCache filterForDisabledBundles:]_block_invoke
- ___57-[CSFileProviderContainerCache filterForDisabledBundles:]_block_invoke_2
- ___57-[CSFileProviderContainerCache filterForDisabledBundles:]_block_invoke_3
- ___block_descriptor_48_e8_32s40r_e35_v32?0"NSString"8"NSNumber"16^B24ls32l8r40l8
- ___block_descriptor_49_e8_32s40r_e46_v32?0"NSString"8"NSMutableDictionary"16^B24ls32l8r40l8
CStrings:
+ " && (FPAppContainerBundleID != %@)"
+ " && (_kMDItemQueryPathOID != %@)"
+ " || (FPAppContainerBundleID = %@)"
+ " || (_kMDItemQueryPathOID = %@)"
+ "((%@ = %@)"
+ "((%@ = %@) && %@)"
+ "(false"
+ "[ProtectedApps][qid=%ld] filtering in paths with %@"
+ "[ProtectedApps][qid=%ld] filtering out paths with %@"
+ "filterForDisabledBundles:logForQuery:"
+ "v24@?0@\"NSNumber\"8^B16"
+ "v24@?0@\"NSString\"8^B16"
- "(%@ = %@)"
- "((%@ = %@) && (%@))"
- "(_kMDItemQueryPathOID != %@) && (FPAppContainerBundleID != %@)"
- "(_kMDItemQueryPathOID = %@) || (FPAppContainerBundleID = %@)"
- "filterForDisabledBundles:"

```
