## CoreServices

> `/System/Library/Frameworks/CoreServices.framework/CoreServices`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__weak_auth_got`
- `__AUTH_CONST.__lazy_load_got`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH.__objc_data`
- `__AUTH.__data`
- `__DATA.__objc_ivar`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`
- `__DATA_DIRTY.__data`

```diff

-1512.0.0.0.0
-  __TEXT.__text: 0x1c6f38
+1517.0.1.0.0
+  __TEXT.__text: 0x1c7980
   __TEXT.__delay_helper: 0x1b8
   __TEXT.__lazy_helpers: 0xa8
-  __TEXT.__objc_methlist: 0xe1d4
+  __TEXT.__objc_methlist: 0xe1fc
   __TEXT.__const: 0x990
-  __TEXT.__cstring: 0x28cce
-  __TEXT.__oslogstring: 0x1650f
-  __TEXT.__gcc_except_tab: 0x2955c
+  __TEXT.__cstring: 0x28c7d
+  __TEXT.__oslogstring: 0x1667b
+  __TEXT.__gcc_except_tab: 0x29618
   __TEXT.__ustring: 0x23c
-  __TEXT.__unwind_info: 0xc5d0
+  __TEXT.__unwind_info: 0xc628
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x7418
+  __DATA_CONST.__const: 0x7478
   __DATA_CONST.__objc_classlist: 0x7b0
   __DATA_CONST.__objc_catlist: 0x78
   __DATA_CONST.__objc_protolist: 0x180
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x6540
+  __DATA_CONST.__objc_selrefs: 0x6548
   __DATA_CONST.__objc_protorefs: 0x90
   __DATA_CONST.__objc_superrefs: 0x640
   __DATA_CONST.__objc_arraydata: 0x990
   __DATA_CONST.__got: 0xbb8
-  __AUTH_CONST.__const: 0x3b90
-  __AUTH_CONST.__cfstring: 0x17a00
-  __AUTH_CONST.__objc_const: 0x156e0
+  __AUTH_CONST.__const: 0x3bb0
+  __AUTH_CONST.__cfstring: 0x17a20
+  __AUTH_CONST.__objc_const: 0x156e8
   __AUTH_CONST.__weak_auth_got: 0x18
   __AUTH_CONST.__lazy_load_got: 0x10
   __AUTH_CONST.__objc_intobj: 0x7f8

   __AUTH.__data: 0x318
   __DATA.__objc_ivar: 0xbf0
   __DATA.__data: 0x15c4
-  __DATA.__bss: 0xf30
+  __DATA.__bss: 0xf40
   __DATA.__common: 0x40
   __DATA_DIRTY.__objc_data: 0x1928
   __DATA_DIRTY.__data: 0x58

   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 9533
-  Symbols:   16473
-  CStrings:  6034
+  Functions: 9545
+  Symbols:   16488
+  CStrings:  6048
 
Symbols:
+ -[FSMimic bundleInfoDictionaryWithError:]
+ -[FSMimicPopulator populateBundleInfoDictionaryWithError:]
+ __LSBundleCopyNodeWithCheckStyle
+ __ZL19_LSBundleCreateNodeP11_LSDatabasej24LSBundleCheckUpdateStylePbPU15__autoreleasingP7NSError
+ __ZL24_LSBundleCopyOrCheckNodeP11_LSDatabasejj24LSBundleCheckUpdateStylePU8__strongP6FSNode
+ __ZL25_LSBundleApplyCheckUpdate24LSBundleCheckUpdateStylePKcU13block_pointerFvP9LSContextE
+ __ZZL31_LSBundleCheckUpdateClientQueuevE5queue
+ __ZZL31_LSBundleCheckUpdateClientQueuevE9onceToken
+ ____ZL24_LSBundleCopyOrCheckNodeP11_LSDatabasejj24LSBundleCheckUpdateStylePU8__strongP6FSNode_block_invoke
+ ____ZL25_LSBundleApplyCheckUpdate24LSBundleCheckUpdateStylePKcU13block_pointerFvP9LSContextE_block_invoke
+ ____ZL31_LSBundleCheckUpdateClientQueuev_block_invoke
+ ____ZN14LaunchServices10ContainersL7displayEP9LSContextjjP29CSStoreAttributedStringWriter_block_invoke
+ ___block_descriptor_40_ea8_32s_e21_v16?0^{LSContext=}8ls32l8
+ ___block_descriptor_48_ea8_32bs_e9_v16?0r*8ls32l8
+ __kLSURLIsHiddenBySystemChangedNotificationsKey
+ __kLSURLIsHiddenBySystemKey
+ _objc_msgSend$populateBundleInfoDictionaryWithError:
- __ZL19_LSBundleCreateNodeP11_LSDatabasejbPbPU15__autoreleasingP7NSError
- __ZL24_LSBundleCopyOrCheckNodeP11_LSDatabasejjhPU8__strongP6FSNode
CStrings:
+ "%{public}s: finished %{public}s database update (%{public}s)"
+ "%{public}s: performing synchronous (client) database update (%{public}s)"
+ "%{public}s: performing synchronous (server) database update (%{public}s)"
+ "%{public}s: scheduling asynchronous (client) database update (%{public}s)"
+ "%{public}s: scheduling asynchronous (server) database update (%{public}s)"
+ "-[FSMimic bundleInfoDictionaryWithError:]"
+ "Failed to get keys remotely, but keeping original error. Remote error info: %@ %ld"
+ "InstallBuildVersion"
+ "OriginalInstallDate"
+ "_LSBundleApplyCheckUpdate"
+ "_LSBundleCopyOrCheckNode_block_invoke"
+ "asynchronous (client)"
+ "asynchronous (server)"
+ "bundleInfoDictionary"
+ "com.apple.LaunchServices.bundle-check-update"
+ "registering changed bundle"
+ "synchronous (client)"
+ "synchronous (server)"
+ "v16@?0r*8"
- "+[_LSDisplayNameConstructor(ConstructForAnyFile) displayNameConstructorWithContextIfNeeded:bundle:bundleClass:node:preferredLocalizations:error:]"
- "+[_LSDisplayNameConstructor(ConstructForAnyFile) displayNameConstructorsWithContextIfNeeded:bundle:bundleClass:node:error:]"
- "Failed to get keys remotely, but keeping original error. Remote error: %@"
- "node had unregistered bundle type but can't issue IO to localize its name"
- "node had unregistered personality but cannot do IO to localize its name"
```
