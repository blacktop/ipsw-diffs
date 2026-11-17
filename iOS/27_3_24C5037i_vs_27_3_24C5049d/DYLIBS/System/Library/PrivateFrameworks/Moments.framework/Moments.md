## Moments

> `/System/Library/PrivateFrameworks/Moments.framework/Moments`

```diff

-504.0.7.0.0
-  __TEXT.__text: 0x76c10
-  __TEXT.__objc_methlist: 0x6d74
-  __TEXT.__cstring: 0xe67e
+504.0.8.0.0
+  __TEXT.__text: 0x77128
+  __TEXT.__objc_methlist: 0x6dac
+  __TEXT.__cstring: 0xe6be
   __TEXT.__const: 0x1048
-  __TEXT.__oslogstring: 0x54ef
+  __TEXT.__oslogstring: 0x54fa
   __TEXT.__gcc_except_tab: 0x41c
   __TEXT.__swift5_typeref: 0x2fd
   __TEXT.__constg_swiftt: 0x410

   __TEXT.__swift5_types: 0x50
   __TEXT.__swift5_mpenum: 0x8
   __TEXT.__swift5_protos: 0x4
-  __TEXT.__unwind_info: 0x22d0
+  __TEXT.__unwind_info: 0x22e8
   __TEXT.__eh_frame: 0xb48
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x34a0
+  __DATA_CONST.__const: 0x3508
   __DATA_CONST.__objc_classlist: 0x320
   __DATA_CONST.__objc_catlist: 0x38
   __DATA_CONST.__objc_protolist: 0x78
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x34c0
+  __DATA_CONST.__objc_selrefs: 0x34f0
   __DATA_CONST.__objc_protorefs: 0x50
   __DATA_CONST.__objc_superrefs: 0x280
   __DATA_CONST.__objc_arraydata: 0x470
-  __DATA_CONST.__got: 0x848
-  __AUTH_CONST.__const: 0x820
+  __DATA_CONST.__got: 0x850
+  __AUTH_CONST.__const: 0x880
   __AUTH_CONST.__cfstring: 0x10c40
   __AUTH_CONST.__objc_const: 0xb7d0
   __AUTH_CONST.__objc_arrayobj: 0xd8
   __AUTH_CONST.__objc_intobj: 0x540
   __AUTH_CONST.__objc_dictobj: 0x28
-  __AUTH_CONST.__auth_got: 0x930
+  __AUTH_CONST.__auth_got: 0x940
   __AUTH.__objc_data: 0x1a18
   __AUTH.__data: 0x2e0
   __DATA.__objc_ivar: 0x830

   - /System/Library/PrivateFrameworks/HealthUI.framework/HealthUI
   - /System/Library/PrivateFrameworks/PersonalizationPortrait.framework/PersonalizationPortrait
   - /System/Library/PrivateFrameworks/RunningBoardServices.framework/RunningBoardServices
+  - /System/Library/PrivateFrameworks/TCC.framework/TCC
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib

   - /usr/lib/swift/libswift_DarwinFoundation1.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 3059
-  Symbols:   6732
-  CStrings:  2673
+  Functions: 3068
+  Symbols:   6747
+  CStrings:  2677
 
Symbols:
+ +[MOEventBundleProcessor(LearnFromThisApp) _bundleIds:inDenyList:]
+ +[MOEventBundleProcessor(LearnFromThisApp) _learningFromAppDenyListWithAppExclusionsEnabled:tccReader:legacyReader:]
+ +[MOEventBundleProcessor(LearnFromThisApp) _normalizedBundleIdSet:]
+ +[MOEventBundleProcessor(LearnFromThisApp) _readLegacyLFTABlocklist]
+ +[MOEventBundleProcessor(LearnFromThisApp) _readTCCExclusionList]
+ _TCCAccessCopyBundleIdentifiersDisabledForService
+ ___66+[MOEventBundleProcessor(LearnFromThisApp) _bundleIds:inDenyList:]_block_invoke
+ ___68+[MOEventBundleProcessor(LearnFromThisApp) _learningFromAppDenyList]_block_invoke
+ ___68+[MOEventBundleProcessor(LearnFromThisApp) _learningFromAppDenyList]_block_invoke_2
+ ___68+[MOEventBundleProcessor(LearnFromThisApp) _learningFromAppDenyList]_block_invoke_3
+ ___block_descriptor_32_e14_"NSArray"8?0l
+ ___block_descriptor_32_e5_B8?0l
+ ___block_descriptor_40_e8_32s_e22_B24?0"NSString"8^B16ls32l8
+ __os_feature_enabled_impl
+ _kTCCServiceSiriAccess
CStrings:
+ "@\"NSArray\"8@?0"
+ "AppExclusions"
+ "B24@?0@\"NSString\"8^B16"
+ "IntelligenceFlow"
+ "approvedForLearnFromThisApp,failed to read deny list, useTCC=%d"
- "approvedForLearnFromThisApp,failed to read deny list"
```
