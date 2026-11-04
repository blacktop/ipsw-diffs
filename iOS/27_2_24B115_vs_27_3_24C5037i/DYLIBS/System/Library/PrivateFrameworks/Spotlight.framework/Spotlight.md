## Spotlight

> `/System/Library/PrivateFrameworks/Spotlight.framework/Spotlight`

```diff

-2465.1.9.0.0
-  __TEXT.__text: 0xa07ec
-  __TEXT.__objc_methlist: 0x2d7c
-  __TEXT.__const: 0xe74
-  __TEXT.__oslogstring: 0x57d2
-  __TEXT.__cstring: 0x36cc
-  __TEXT.__gcc_except_tab: 0x5834
+2465.2.7.101.0
+  __TEXT.__text: 0xa218c
+  __TEXT.__objc_methlist: 0x2ebc
+  __TEXT.__const: 0xe84
+  __TEXT.__oslogstring: 0x5822
+  __TEXT.__cstring: 0x37fc
+  __TEXT.__gcc_except_tab: 0x5938
   __TEXT.__ustring: 0x6
   __TEXT.__swift5_typeref: 0x7da
   __TEXT.__swift5_fieldmd: 0x28c

   __TEXT.__swift5_capture: 0x3f4
   __TEXT.__swift5_assocty: 0x60
   __TEXT.__swift5_builtin: 0x3c
-  __TEXT.__unwind_info: 0x1b80
+  __TEXT.__unwind_info: 0x1bf0
   __TEXT.__eh_frame: 0x1200
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0xe30
-  __DATA_CONST.__objc_classlist: 0x158
+  __DATA_CONST.__const: 0xf18
+  __DATA_CONST.__objc_classlist: 0x170
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x8
-  __DATA_CONST.__objc_selrefs: 0x30a8
+  __DATA_CONST.__objc_selrefs: 0x3150
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0xa8
+  __DATA_CONST.__objc_superrefs: 0xc0
   __DATA_CONST.__objc_arraydata: 0x3e8
-  __DATA_CONST.__got: 0x1948
-  __AUTH_CONST.__const: 0x14e8
-  __AUTH_CONST.__cfstring: 0x30a0
-  __AUTH_CONST.__objc_const: 0x4ea0
+  __DATA_CONST.__got: 0x1978
+  __AUTH_CONST.__const: 0x1528
+  __AUTH_CONST.__cfstring: 0x3140
+  __AUTH_CONST.__objc_const: 0x5278
   __AUTH_CONST.__weak_auth_got: 0x10
   __AUTH_CONST.__objc_intobj: 0x240
   __AUTH_CONST.__objc_arrayobj: 0xc0
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__objc_doubleobj: 0x10
-  __AUTH_CONST.__auth_got: 0x13a8
-  __AUTH.__objc_data: 0x558
+  __AUTH_CONST.__auth_got: 0x13b0
+  __AUTH.__objc_data: 0x648
   __AUTH.__data: 0x50
-  __DATA.__objc_ivar: 0x440
+  __DATA.__objc_ivar: 0x46c
   __DATA.__data: 0x6d8
   __DATA_DIRTY.__objc_data: 0xad0
   __DATA_DIRTY.__data: 0x360

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 1812
-  Symbols:   3338
-  CStrings:  945
+  Functions: 1850
+  Symbols:   3420
+  CStrings:  953
 
Symbols:
+ +[SPBundleFilter applyFiltering:context:completionHandler:]
+ +[SPBundleFilter currentQueryFilters]
+ -[SPBundleFilterQueryFilters .cxx_destruct]
+ -[SPBundleFilterQueryFilters disabledBundleIdentifiers]
+ -[SPBundleFilterQueryFilters disabledFileProviderFilePaths]
+ -[SPBundleFilterQueryFilters filterQueries]
+ -[SPBundleFilterQueryFilters initWithFilterQueries:disabledBundleIdentifiers:disabledFileProviderFilePaths:]
+ -[SPBundleFilterResolvedDimensions blockedSet]
+ -[SPBundleFilterResolvedDimensions disableSearchInSpotlightExemptions]
+ -[SPBundleFilterResolvedDimensions verdicts]
+ -[SPBundleFilterVerdictStore .cxx_destruct]
+ -[SPBundleFilterVerdictStore init]
+ -[SPBundleFilterVerdictStore resultForItem:]
+ -[SPBundleFilterVerdictStore setResult:forItem:]
+ -[SPBundleFilteringContext blockedAppBundleIDs]
+ -[SPBundleFilteringContext disableSearchInSpotlightExemptions]
+ -[SPBundleFilteringContext setBlockedAppBundleIDs:]
+ -[SPBundleFilteringContext setDisableSearchInSpotlightExemptions:]
+ -[SPBundleFilteringContext setTimeout:]
+ -[SPBundleFilteringContext timeout]
+ -[SPBundleFilteringResult .cxx_destruct]
+ -[SPBundleFilteringResult initWithVerdicts:]
+ -[SPBundleFilteringResult verdictAtIndex:]
+ -[SPBundleFilteringResult verdicts]
+ GCC_except_table103
+ GCC_except_table79
+ _MCAppWhitelistDidChangeNotification
+ _MCEffectiveSettingsChangedNotification
+ _OBJC_CLASS_$_SPBundleFilterQueryFilters
+ _OBJC_CLASS_$_SPBundleFilterVerdictStore
+ _OBJC_CLASS_$_SPBundleFilteringResult
+ _OBJC_IVAR_$_SPBundleFilterQueryFilters._disabledBundleIdentifiers
+ _OBJC_IVAR_$_SPBundleFilterQueryFilters._disabledFileProviderFilePaths
+ _OBJC_IVAR_$_SPBundleFilterQueryFilters._filterQueries
+ _OBJC_IVAR_$_SPBundleFilterResolvedDimensions._blockedSet
+ _OBJC_IVAR_$_SPBundleFilterResolvedDimensions._disableSearchInSpotlightExemptions
+ _OBJC_IVAR_$_SPBundleFilterResolvedDimensions._verdicts
+ _OBJC_IVAR_$_SPBundleFilterVerdictStore._results
+ _OBJC_IVAR_$_SPBundleFilteringContext._blockedAppBundleIDs
+ _OBJC_IVAR_$_SPBundleFilteringContext._disableSearchInSpotlightExemptions
+ _OBJC_IVAR_$_SPBundleFilteringContext._timeout
+ _OBJC_IVAR_$_SPBundleFilteringResult._verdicts
+ _OBJC_METACLASS_$_SPBundleFilterQueryFilters
+ _OBJC_METACLASS_$_SPBundleFilterVerdictStore
+ _OBJC_METACLASS_$_SPBundleFilteringResult
+ _SPBundleFilterAllowedSetForOwnBundleID
+ _SPBundleFilterEvaluateApplicationItem
+ _SPBundleFilterFinalizeUnevaluated
+ _SPBundleFilterObserveMDMRestrictionChanges.onceToken
+ _SPBundleFilterRun
+ _SPBundleFilterUnionBlockedSet
+ _SSApplicationBundleIdGeneralApplication
+ __OBJC_$_INSTANCE_METHODS_SPBundleFilterQueryFilters
+ __OBJC_$_INSTANCE_METHODS_SPBundleFilterVerdictStore
+ __OBJC_$_INSTANCE_METHODS_SPBundleFilteringResult
+ __OBJC_$_INSTANCE_VARIABLES_SPBundleFilterQueryFilters
+ __OBJC_$_INSTANCE_VARIABLES_SPBundleFilterVerdictStore
+ __OBJC_$_INSTANCE_VARIABLES_SPBundleFilteringResult
+ __OBJC_$_PROP_LIST_SPBundleFilterQueryFilters
+ __OBJC_$_PROP_LIST_SPBundleFilteringResult
+ __OBJC_CLASS_RO_$_SPBundleFilterQueryFilters
+ __OBJC_CLASS_RO_$_SPBundleFilterVerdictStore
+ __OBJC_CLASS_RO_$_SPBundleFilteringResult
+ __OBJC_METACLASS_RO_$_SPBundleFilterQueryFilters
+ __OBJC_METACLASS_RO_$_SPBundleFilterVerdictStore
+ __OBJC_METACLASS_RO_$_SPBundleFilteringResult
+ ___41+[SPBundleFilter applyFiltering:context:]_block_invoke
+ ___59+[SPBundleFilter applyFiltering:context:completionHandler:]_block_invoke
+ ___SPBundleFilterObserveMDMRestrictionChanges_block_invoke
+ ___SPBundleFilterObserveMDMRestrictionChanges_block_invoke_2
+ ___SPBundleFilterRunServerXPCStep_block_invoke
+ ___SPBundleFilterRun_block_invoke
+ ___SPBundleFilterSendServerXPCRequest_block_invoke
+ ___SPBundleFilterSendServerXPCRequest_block_invoke_2
+ ___SPBundleFilterSendServerXPCRequest_block_invoke_3
+ ___block_descriptor_32_e24_v16?0"NSNotification"8l
+ ___block_descriptor_40_e8_32bs_e51_v24?0"CSBundleFilterEvaluationReply"8"NSError"16ls32l8
+ ___block_descriptor_48_e8_32s40bs_e48_v24?0"SPBundleFilterVerdictStore"8"NSError"16ls40l8s32l8
+ ___block_descriptor_56_e8_32bs40r48r_e39_v16?0"CSBundleFilterEvaluationReply"8lr40l8r48l8s32l8
+ ___block_descriptor_56_e8_32s40r48r_e48_v24?0"SPBundleFilterVerdictStore"8"NSError"16lr40l8r48l8s32l8
+ ___block_descriptor_56_e8_32s40s48bs_e39_v16?0"CSBundleFilterEvaluationReply"8ls48l8s32l8s40l8
+ ___block_descriptor_56_e8_32s40s48bs_e8_v12?0B8ls32l8s40l8s48l8
+ _dispatch_after
+ _sMDMRestrictedCache
+ _sMDMRestrictedGeneration
+ _sMDMRestrictedLock
- GCC_except_table63
- _SPBundleFilterRunServerXPCStep
- ___SPBundleFilterAwaitServerXPCReply_block_invoke
- ___block_descriptor_64_e8_32s40r48r56r_e51_v24?0"CSBundleFilterEvaluationReply"8"NSError"16lr40l8r48l8r56l8s32l8
CStrings:
+ "%\""
+ "[App Exclusions] Client-supplied disabledApps %@ is not a subset of disabledBundles %@"
+ "com.apple.CloudDocs.MobileDocumentsFileProvider"
+ "com.apple.CloudDocs.iCloudDriveFileProvider"
+ "com.apple.CloudDocs.iCloudDriveFileProviderManaged"
+ "com.apple.FileProvider.LocalStorage"
+ "tpbck"
+ "v16@?0@\"CSBundleFilterEvaluationReply\"8"
+ "v16@?0@\"NSNotification\"8"
+ "v24@?0@\"SPBundleFilterVerdictStore\"8@\"NSError\"16"
- "$\""
- ")"
```
