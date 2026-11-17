## momentsd

> `/usr/libexec/momentsd`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__swift5_typeref`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_fieldmd`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_types`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__swift5_protos`
- `__TEXT.__swift5_mpenum`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-504.0.7.0.0
-  __TEXT.__text: 0x2762d0
-  __TEXT.__auth_stubs: 0x2410
-  __TEXT.__objc_stubs: 0x1f700
-  __TEXT.__objc_methlist: 0xf86c
-  __TEXT.__cstring: 0x25ece
+504.0.8.0.0
+  __TEXT.__text: 0x276928
+  __TEXT.__auth_stubs: 0x2420
+  __TEXT.__objc_stubs: 0x1f7e0
+  __TEXT.__objc_methlist: 0xf8a4
+  __TEXT.__cstring: 0x25f3e
   __TEXT.__objc_classname: 0x2035
-  __TEXT.__objc_methtype: 0x34fe
-  __TEXT.__objc_methname: 0x37e35
-  __TEXT.__oslogstring: 0x3554b
+  __TEXT.__objc_methtype: 0x350e
+  __TEXT.__objc_methname: 0x37f05
+  __TEXT.__oslogstring: 0x3558b
   __TEXT.__const: 0x1e90
-  __TEXT.__gcc_except_tab: 0x87b4
+  __TEXT.__gcc_except_tab: 0x87c0
   __TEXT.__ustring: 0x4
   __TEXT.__dlopen_cstrs: 0x51
   __TEXT.__swift5_typeref: 0x80e

   __TEXT.__swift_as_cont: 0x78
   __TEXT.__swift5_protos: 0x4
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0x7388
+  __TEXT.__unwind_info: 0x73a0
   __TEXT.__eh_frame: 0x1820
-  __DATA_CONST.__const: 0xc6a8
-  __DATA_CONST.__cfstring: 0x236c0
+  __DATA_CONST.__const: 0xc750
+  __DATA_CONST.__cfstring: 0x236e0
   __DATA_CONST.__objc_classlist: 0x7e0
   __DATA_CONST.__objc_catlist: 0xc8
   __DATA_CONST.__objc_protolist: 0x158

   __DATA_CONST.__objc_dictobj: 0x118
   __DATA_CONST.__objc_doubleobj: 0x5d0
   __DATA_CONST.__objc_floatobj: 0x260
-  __DATA_CONST.__auth_got: 0x1220
-  __DATA_CONST.__got: 0x12b8
+  __DATA_CONST.__auth_got: 0x1228
+  __DATA_CONST.__got: 0x12c8
   __DATA_CONST.__auth_ptr: 0x338
   __DATA.__objc_const: 0x1b028
-  __DATA.__objc_selrefs: 0x9cc8
+  __DATA.__objc_selrefs: 0x9d00
   __DATA.__objc_ivar: 0x1450
   __DATA.__objc_data: 0x5d30
   __DATA.__data: 0x2188

   - /System/Library/PrivateFrameworks/ProactiveSupport.framework/ProactiveSupport
   - /System/Library/PrivateFrameworks/RunningBoardServices.framework/RunningBoardServices
   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
+  - /System/Library/PrivateFrameworks/TCC.framework/TCC
   - /System/Library/PrivateFrameworks/ToolKit.framework/ToolKit
   - /System/Library/PrivateFrameworks/Trial.framework/Trial
   - /usr/lib/libMobileGestalt.dylib

   - /usr/lib/swift/libswift_DarwinFoundation1.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 8749
-  Symbols:   19955
-  CStrings:  15574
+  Functions: 8758
+  Symbols:   19976
+  CStrings:  15588
 
Symbols:
+ +[MOEventBundleProcessor(LearnFromThisApp) _bundleIds:inDenyList:]
+ +[MOEventBundleProcessor(LearnFromThisApp) _learningFromAppDenyListWithAppExclusionsEnabled:tccReader:legacyReader:]
+ +[MOEventBundleProcessor(LearnFromThisApp) _normalizedBundleIdSet:]
+ +[MOEventBundleProcessor(LearnFromThisApp) _readLegacyLFTABlocklist]
+ +[MOEventBundleProcessor(LearnFromThisApp) _readTCCExclusionList]
+ _RTErrorDomain
+ _TCCAccessCopyBundleIdentifiersDisabledForService
+ ___66+[MOEventBundleProcessor(LearnFromThisApp) _bundleIds:inDenyList:]_block_invoke
+ ___68+[MOEventBundleProcessor(LearnFromThisApp) _learningFromAppDenyList]_block_invoke
+ ___68+[MOEventBundleProcessor(LearnFromThisApp) _learningFromAppDenyList]_block_invoke_2
+ ___68+[MOEventBundleProcessor(LearnFromThisApp) _learningFromAppDenyList]_block_invoke_3
+ ___block_descriptor_32_e14_"NSArray"8?0l
+ ___block_descriptor_40_e8_32s_e22_B24?0"NSString"8^B16ls32l8
+ _kTCCServiceSiriAccess
+ _objc_msgSend$_bundleIds:inDenyList:
+ _objc_msgSend$_learningFromAppDenyListWithAppExclusionsEnabled:tccReader:legacyReader:
+ _objc_msgSend$_normalizedBundleIdSet:
+ _objc_msgSend$_readLegacyLFTABlocklist
+ _objc_msgSend$_readTCCExclusionList
+ _objc_msgSend$objectsPassingTest:
+ _objc_msgSend$setWithCapacity:
CStrings:
+ "@\"NSArray\"8@?0"
+ "@40@0:8@?16@?24@?32"
+ "AppExclusions"
+ "B24@?0@\"NSString\"8^B16"
+ "IntelligenceFlow"
+ "_bundleIds:inDenyList:"
+ "_learningFromAppDenyListWithAppExclusionsEnabled:tccReader:legacyReader:"
+ "_normalizedBundleIdSet:"
+ "_readLegacyLFTABlocklist"
+ "_readTCCExclusionList"
+ "approvedForLearnFromThisApp,failed to read deny list, useTCC=%d"
+ "bundleSuperType in %@ AND interfaceType != %lu"
+ "fetch oldest visit denied, routine disabled, purging all visits"
+ "objectsPassingTest:"
+ "setWithCapacity:"
- "approvedForLearnFromThisApp,failed to read deny list"
```
