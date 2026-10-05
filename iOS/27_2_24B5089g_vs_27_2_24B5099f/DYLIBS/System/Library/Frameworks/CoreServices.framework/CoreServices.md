## CoreServices

> `/System/Library/Frameworks/CoreServices.framework/CoreServices`

```diff

-1517.1.9.0.0
-  __TEXT.__text: 0x1c7a88
+1517.1.11.0.0
+  __TEXT.__text: 0x1c6d54
   __TEXT.__delay_helper: 0x1b8
   __TEXT.__lazy_helpers: 0xa8
-  __TEXT.__objc_methlist: 0xe334
+  __TEXT.__objc_methlist: 0xe304
   __TEXT.__const: 0x9c0
-  __TEXT.__cstring: 0x29633
-  __TEXT.__oslogstring: 0x16d55
-  __TEXT.__gcc_except_tab: 0x2a3dc
+  __TEXT.__cstring: 0x2944b
+  __TEXT.__oslogstring: 0x16d87
+  __TEXT.__gcc_except_tab: 0x2a28c
   __TEXT.__ustring: 0x23c
-  __TEXT.__unwind_info: 0xdce0
+  __TEXT.__unwind_info: 0xdc80
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x75d8
+  __DATA_CONST.__const: 0x7588
   __DATA_CONST.__objc_classlist: 0x7b0
   __DATA_CONST.__objc_catlist: 0x78
   __DATA_CONST.__objc_protolist: 0x180
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x6608
+  __DATA_CONST.__objc_selrefs: 0x65f8
   __DATA_CONST.__objc_protorefs: 0x90
   __DATA_CONST.__objc_superrefs: 0x640
   __DATA_CONST.__objc_arraydata: 0x990
   __DATA_CONST.__got: 0xbb8
   __AUTH_CONST.__const: 0x3be8
-  __AUTH_CONST.__cfstring: 0x17d60
-  __AUTH_CONST.__objc_const: 0x15760
+  __AUTH_CONST.__cfstring: 0x17d20
+  __AUTH_CONST.__objc_const: 0x15750
   __AUTH_CONST.__weak_auth_got: 0x18
   __AUTH_CONST.__lazy_load_got: 0x10
   __AUTH_CONST.__objc_intobj: 0x7e0
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__objc_arrayobj: 0x150
   __AUTH_CONST.__auth_got: 0x1968
-  __AUTH.__objc_data: 0x33b8
+  __AUTH.__objc_data: 0x3368
   __AUTH.__data: 0x318
   __DATA.__objc_ivar: 0xbf8
-  __DATA.__data: 0x15c4
+  __DATA.__data: 0x15bc
   __DATA.__common: 0x40
-  __DATA_DIRTY.__objc_data: 0x1928
+  __DATA_DIRTY.__objc_data: 0x1978
   __DATA_DIRTY.__data: 0x58
   __DATA_DIRTY.__crash_info: 0x148
-  __DATA_DIRTY.__bss: 0x948
+  __DATA_DIRTY.__bss: 0x970
   __DATA_DIRTY.__common: 0x8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 9619
-  Symbols:   14321
-  CStrings:  6119
+  Functions: 9609
+  Symbols:   14307
+  CStrings:  6114
 
Symbols:
- -[_LSDModifyClient registerExtensionPoint:platform:declaringURL:withInfo:completionHandler:]
- -[_LSDModifyClient unregisterExtensionPoint:platform:withVersion:parentBundleUnit:completionHandler:]
- GCC_except_table132
- __LSRegisterExtensionPointClient
- __LSUnregisterExtensionPoint
- __LSUnregisterExtensionPointClient
- ___101-[_LSDModifyClient unregisterExtensionPoint:platform:withVersion:parentBundleUnit:completionHandler:]_block_invoke
- ___92-[_LSDModifyClient registerExtensionPoint:platform:declaringURL:withInfo:completionHandler:]_block_invoke
- ____LSRegisterExtensionPointClient_block_invoke
- ____LSRegisterExtensionPointClient_block_invoke_2
- ____LSUnregisterExtensionPointClient_block_invoke
- ____LSUnregisterExtensionPointClient_block_invoke_2
- ___block_descriptor_64_ea8_32s40s48bs_e42_v24?0"LSDBExecutionContext"8"NSError"16ls32l8s40l8s48l8
- ___block_descriptor_68_ea8_32s40s48s56bs_e42_v24?0"LSDBExecutionContext"8"NSError"16ls32l8s40l8s48l8s56l8
CStrings:
+ "cannot register extension points from a LS client"
- "-[_LSDModifyClient registerExtensionPoint:platform:declaringURL:withInfo:completionHandler:]"
- "-[_LSDModifyClient registerExtensionPoint:platform:declaringURL:withInfo:completionHandler:]_block_invoke"
- "-[_LSDModifyClient unregisterExtensionPoint:platform:withVersion:parentBundleUnit:completionHandler:]"
- "-[_LSDModifyClient unregisterExtensionPoint:platform:withVersion:parentBundleUnit:completionHandler:]_block_invoke"
- "invalid extensionPoint SDK dictionary"
- "invalid extensionPoint identifier"
```
