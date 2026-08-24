## LaunchServices

> `/System/Library/Frameworks/CoreServices.framework/Versions/A/Frameworks/LaunchServices.framework/Versions/A/LaunchServices`

```diff

-1510.400.0.0.0
-  __TEXT.__text: 0x252f9c
+1517.0.1.401.0
+  __TEXT.__text: 0x253fb4
   __TEXT.__lazy_helpers: 0xa8
-  __TEXT.__objc_methlist: 0xedbc
-  __TEXT.__const: 0xab0
-  __TEXT.__cstring: 0x33486
-  __TEXT.__oslogstring: 0x222b0
-  __TEXT.__gcc_except_tab: 0x3444c
+  __TEXT.__objc_methlist: 0xede4
+  __TEXT.__const: 0xab8
+  __TEXT.__cstring: 0x3364f
+  __TEXT.__oslogstring: 0x224d3
+  __TEXT.__gcc_except_tab: 0x345d4
   __TEXT.__ustring: 0x1be
   __TEXT.__dof_LSFSNode: 0x2b6
-  __TEXT.__unwind_info: 0xeaf0
+  __TEXT.__unwind_info: 0xeb60
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x3e98
+  __DATA_CONST.__const: 0x3ed8
   __DATA_CONST.__objc_classlist: 0x7a8
   __DATA_CONST.__objc_catlist: 0x88
   __DATA_CONST.__objc_protolist: 0x190
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x6e60
+  __DATA_CONST.__objc_selrefs: 0x6e70
   __DATA_CONST.__objc_protorefs: 0x98
   __DATA_CONST.__objc_superrefs: 0x638
   __DATA_CONST.__objc_arraydata: 0xa10
   __DATA_CONST.__got: 0xe40
-  __AUTH_CONST.__const: 0xaaa8
-  __AUTH_CONST.__cfstring: 0x1df00
-  __AUTH_CONST.__objc_const: 0x16668
+  __AUTH_CONST.__const: 0xab58
+  __AUTH_CONST.__cfstring: 0x1df60
+  __AUTH_CONST.__objc_const: 0x16680
   __AUTH_CONST.__weak_auth_got: 0x30
   __AUTH_CONST.__lazy_load_got: 0x10
   __AUTH_CONST.__objc_intobj: 0x750

   __AUTH.__data: 0x248
   __DATA.__objc_ivar: 0xc68
   __DATA.__data: 0x15ec
-  __DATA.__bss: 0x1a70
+  __DATA.__bss: 0x1a80
   __DATA.__common: 0x5
   __DATA_DIRTY.__objc_data: 0x1130
   __DATA_DIRTY.__data: 0x250

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/system/libxpc.dylib
-  Functions: 11147
-  Symbols:   19519
-  CStrings:  7906
+  Functions: 11169
+  Symbols:   19543
+  CStrings:  7933
 
Symbols:
+ -[FSMimic bundleInfoDictionaryWithError:]
+ -[FSMimicPopulator populateBundleInfoDictionaryWithError:]
+ -[LSApplicationRecord(MobileInstall) originalInstallDate]
+ GCC_except_table301
+ GCC_except_table318
+ GCC_except_table323
+ GCC_except_table326
+ GCC_except_table335
+ GCC_except_table338
+ GCC_except_table352
+ _ZL25_LSBundleApplyCheckUpdate24LSBundleCheckUpdateStylePKcU13block_pointerFvP9LSContextE
+ __LSBundleCopyNodeWithCheckStyle
+ __Z21CFTypeGetAsDictionaryPKv
+ __ZL19_LSBundleCreateNodeP11_LSDatabasej24LSBundleCheckUpdateStylePbPU15__autoreleasingP7NSError
+ __ZL24_LSBundleCopyOrCheckNodeP11_LSDatabasejj24LSBundleCheckUpdateStylePU8__strongP6FSNode
+ __ZL25_LSBundleApplyCheckUpdate24LSBundleCheckUpdateStylePKcU13block_pointerFvP9LSContextE
+ __ZZL31_LSBundleCheckUpdateClientQueuevE5queue
+ __ZZL31_LSBundleCheckUpdateClientQueuevE9onceToken
+ ___ZL24_LSBundleCopyOrCheckNodeP11_LSDatabasejj24LSBundleCheckUpdateStylePU8__strongP6FSNode_block_invoke
+ ___ZL25_LSBundleApplyCheckUpdate24LSBundleCheckUpdateStylePKcU13block_pointerFvP9LSContextE_block_invoke
+ ____ZL19_LSBundleCreateNodeP11_LSDatabasej24LSBundleCheckUpdateStylePbPU15__autoreleasingP7NSError_block_invoke
+ ____ZL24_LSBundleCopyOrCheckNodeP11_LSDatabasejj24LSBundleCheckUpdateStylePU8__strongP6FSNode_block_invoke
+ ____ZL25_LSBundleApplyCheckUpdate24LSBundleCheckUpdateStylePKcU13block_pointerFvP9LSContextE_block_invoke
+ ____ZL31_LSBundleCheckUpdateClientQueuev_block_invoke
+ ____ZN14LaunchServices10ContainersL7displayEP9LSContextjjP29CSStoreAttributedStringWriter_block_invoke
+ ___block_descriptor_36_e21_v16?0^{LSContext=}8l
+ ___block_descriptor_40_ea8_32s_e21_v16?0^{LSContext=}8l
+ ___block_descriptor_48_ea8_32bs_e9_v16?0r*8l
+ ___block_descriptor_64_ea8_32r40r_e14_v24?0I8I12*16l
+ __kLSApplicationDisclaimAsParentApplicationKey
+ __kLSApplicationHasReExecedItselfKey
+ __kLSApplicationPossibleForegroundOwnerApplicationsASNsArrayKey
+ __kLSURLIsHiddenBySystemChangedNotificationsKey
+ __kLSURLIsHiddenBySystemKey
+ _objc_msgSend$populateBundleInfoDictionaryWithError:
- GCC_except_table300
- GCC_except_table317
- GCC_except_table320
- GCC_except_table324
- GCC_except_table332
- GCC_except_table336
- _ZL24_LSBundleCopyOrCheckNodeP11_LSDatabasejjhPU8__strongP6FSNode
- __ZL19_LSBundleCreateNodeP11_LSDatabasejbPbPU15__autoreleasingP7NSError
- __ZL24_LSBundleCopyOrCheckNodeP11_LSDatabasejjhPU8__strongP6FSNode
- ____ZL24_LSBundleCopyOrCheckNodeP11_LSDatabasejjhPU8__strongP6FSNode_block_invoke
- __kLSApplicationHasAVisibleOwnerApplicationASNsArrayKey
CStrings:
+ "%{public}s: finished %{public}s database update (%{public}s)"
+ "%{public}s: performing synchronous (client) database update (%{public}s)"
+ "%{public}s: performing synchronous (server) database update (%{public}s)"
+ "%{public}s: scheduling asynchronous (client) database update (%{public}s)"
+ "%{public}s: scheduling asynchronous (server) database update (%{public}s)"
+ "-[FSMimic bundleInfoDictionaryWithError:]"
+ "184173499"
+ "HWLOC_DARWIN_CPUKINDS_FROM_SYSCTL"
+ "LAUNCH: Setting HWLOC_DARWIN_CPUKINDS_FROM_SYSCTL workaround."
+ "LSApplicationDisclaimAsParentApplicationKey"
+ "LSApplicationHasReExecedItselfKey"
+ "LSApplicationPossibleForegroundOwnerApplicationsASNsArrayKey"
+ "OSStatus _LSBundleCopyOrCheckNode(__strong LSDatabaseRef, LSBundleID, CSStringID, LSBundleCheckUpdateStyle, FSNodeHandle)"
+ "_LSBundleApplyCheckUpdate"
+ "_LSBundleCopyOrCheckNode_block_invoke"
+ "asynchronous (client)"
+ "asynchronous (server)"
+ "bundleInfoDictionary"
+ "com.apple.LaunchServices.bundle-check-update"
+ "failed to get node for %@ but had no error"
+ "failed to prepare value for %@ but had no error"
+ "kLSNotificationApplicationReExeced"
+ "kLSNotifyApplicationRebirth"
+ "mimic selector %{public}@ returned false without setting an error"
+ "mimic selector %{public}@ returned nil without setting an error"
+ "re-registering changed bundle"
+ "registering changed bundle"
+ "synchronous (client)"
+ "synchronous (server)"
+ "unregistering bundle missing from disk"
+ "unregistering changed bundle"
+ "v16@?0r*8"
- "LAUNCH: Disclaiming parent relationship for launch of %{public}@ by application %{public}s"
- "LSApplicationHasAVisibleOwnerApplicationASNsArrayKey"
- "OSStatus _LSBundleCopyOrCheckNode(__strong LSDatabaseRef, LSBundleID, CSStringID, Boolean, FSNodeHandle)"
- "node had unregistered bundle type but can't issue IO to localize its name"
- "node had unregistered personality but cannot do IO to localize its name"
```
