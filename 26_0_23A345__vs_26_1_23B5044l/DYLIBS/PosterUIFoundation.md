## PosterUIFoundation

> `/System/Library/PrivateFrameworks/PosterUIFoundation.framework/PosterUIFoundation`

```diff

-290.112.0.0.0
-  __TEXT.__text: 0x8ed64
-  __TEXT.__auth_stubs: 0x1c70
-  __TEXT.__objc_methlist: 0xa4c4
+296.100.0.0.0
+  __TEXT.__text: 0x90b44
+  __TEXT.__auth_stubs: 0x1c60
+  __TEXT.__objc_methlist: 0xa624
   __TEXT.__const: 0xb04
-  __TEXT.__oslogstring: 0x35d1
-  __TEXT.__cstring: 0x5de2
-  __TEXT.__gcc_except_tab: 0x16dc
+  __TEXT.__oslogstring: 0x3711
+  __TEXT.__cstring: 0x5e52
+  __TEXT.__gcc_except_tab: 0x1684
   __TEXT.__dlopen_cstrs: 0x1a8
   __TEXT.__swift5_typeref: 0x502
   __TEXT.__constg_swiftt: 0x1d4

   __TEXT.__swift5_proto: 0x24
   __TEXT.__swift5_types: 0x24
   __TEXT.__swift5_capture: 0x10
-  __TEXT.__unwind_info: 0x26c8
-  __TEXT.__objc_classname: 0x1716
-  __TEXT.__objc_methname: 0x18b1f
-  __TEXT.__objc_methtype: 0x3e4a
-  __TEXT.__objc_stubs: 0x10ea0
-  __DATA_CONST.__got: 0xe30
-  __DATA_CONST.__const: 0x25a8
-  __DATA_CONST.__objc_classlist: 0x4b0
+  __TEXT.__unwind_info: 0x2730
+  __TEXT.__objc_classname: 0x178b
+  __TEXT.__objc_methname: 0x18f65
+  __TEXT.__objc_methtype: 0x3e94
+  __TEXT.__objc_stubs: 0x10fc0
+  __DATA_CONST.__got: 0xe38
+  __DATA_CONST.__const: 0x2670
+  __DATA_CONST.__objc_classlist: 0x4c8
   __DATA_CONST.__objc_catlist: 0xc0
   __DATA_CONST.__objc_protolist: 0x1b8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x55d8
+  __DATA_CONST.__objc_selrefs: 0x5670
   __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__objc_superrefs: 0x3d8
+  __DATA_CONST.__objc_superrefs: 0x3f0
   __DATA_CONST.__objc_arraydata: 0x1b0
-  __AUTH_CONST.__auth_got: 0xe48
+  __AUTH_CONST.__auth_got: 0xe40
   __AUTH_CONST.__const: 0xfa0
-  __AUTH_CONST.__cfstring: 0x6800
-  __AUTH_CONST.__objc_const: 0x1dd20
+  __AUTH_CONST.__cfstring: 0x6880
+  __AUTH_CONST.__objc_const: 0x1e040
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_intobj: 0x318
   __AUTH_CONST.__objc_doubleobj: 0x2b0
   __AUTH_CONST.__objc_arrayobj: 0xa8
   __AUTH_CONST.__objc_floatobj: 0x20
-  __AUTH.__objc_data: 0x21e0
+  __AUTH.__objc_data: 0x22d0
   __AUTH.__data: 0x110
-  __DATA.__objc_ivar: 0xb80
+  __DATA.__objc_ivar: 0xb88
   __DATA.__data: 0x16c0
   __DATA.__bss: 0x800
   __DATA.__common: 0x18

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: F7AF17C6-3567-3164-810E-5162544C5C13
-  Functions: 3870
-  Symbols:   13872
-  CStrings:  6727
+  UUID: 49ED3467-DB53-3913-AEC9-570D2708A2AF
+  Functions: 3902
+  Symbols:   13972
+  CStrings:  6769
 
Symbols:
+ +[PUIStylePickerSegmentedControl defaultHeight]
+ -[FBSMutableSceneClientSettings(PosterUIFoundation) pui_setWantsSuitableSnapshotChecks:]
+ -[FBSSceneClientSettings(PosterUIFoundation) pui_wantsSuitableSnapshotChecks]
+ -[FBScene(PosterUIFoundation) _pui_checkForSuitableSnapshotBundlesWithPromise:candidateBundlesFuture:descriptor:outputDestination:snapshottingAssertion:executeIfNecessary:]
+ -[FBScene(PosterUIFoundation) _pui_ensureOutputDestination:error:]
+ -[FBScene(PosterUIFoundation) _pui_executeInProcessSnapshotForDescriptor:outputDestination:snapshottingAssertion:]
+ -[FBScene(PosterUIFoundation) _pui_executeInProcessSnapshotForDescriptor:outputDestination:snapshottingAssertion:].cold.1
+ -[FBScene(PosterUIFoundation) _pui_executeOutOfProcessSnapshotWithPromise:descriptor:outputDestination:snapshottingAssertion:]
+ -[FBScene(PosterUIFoundation) _pui_finishAndCleanupSnapshottingPromise:bundle:outputDestination:snapshottingAssertion:error:]
+ -[FBScene(PosterUIFoundation) pui_executeSnapshotForDescriptor:outputDestination:candidateBundlesFutureProvider:]
+ -[PUIPosterSnapshotBundleInMemoryCache .cxx_destruct]
+ -[PUIPosterSnapshotBundleInMemoryCache cacheSnapshotBundle:forPredicate:]
+ -[PUIPosterSnapshotBundleInMemoryCache cacheSnapshotBundle:forPredicate:].cold.1
+ -[PUIPosterSnapshotBundleInMemoryCache cacheSnapshotBundle:forPredicate:].cold.2
+ -[PUIPosterSnapshotBundleInMemoryCache cachedSnapshotBundleSatisfyingPredicate:]
+ -[PUIPosterSnapshotBundleInMemoryCache clearCachedSnapshotBundlesSatisfyingPredicate:]
+ -[PUIPosterSnapshotBundleInMemoryCache init]
+ -[PUIPosterSnapshotBundlePredicate satisfiesPredicate:]
+ -[PUISceneSnapshotCandidateSnapshotContextsAction candidateSnapshotContexts]
+ -[PUISceneSnapshotCandidateSnapshotContextsAction inflightSnapshotDescriptor]
+ -[PUISceneSnapshotCandidateSnapshotContextsAction initWithCandidateSnapshotContexts:inflightSnapshotDescriptor:responder:]
+ -[PUISceneSnapshotCandidateSnapshotContextsAction respondWithError:]
+ -[PUISceneSnapshotCandidateSnapshotContextsAction respondWithSuitableURL:]
+ -[PUIStylePickerSegmentedControl .cxx_destruct]
+ -[PUIStylePickerSegmentedControl _updateSegmentWidths]
+ -[PUIStylePickerSegmentedControl calculatedWidthForAvailableWidth:]
+ -[PUIStylePickerSegmentedControl initWithFrame:actions:]
+ -[PUIStylePickerSegmentedControl layoutSubviews]
+ -[_PUIPosterSnapshotBundleInMemoryCacheEntry .cxx_destruct]
+ -[_PUIPosterSnapshotBundleInMemoryCacheEntry bundle]
+ -[_PUIPosterSnapshotBundleInMemoryCacheEntry initWithPredicate:bundle:]
+ -[_PUIPosterSnapshotBundleInMemoryCacheEntry predicate]
+ -[_PUIPosterSnapshotBundleInMemoryCacheEntry setBundle:]
+ -[_PUIPosterSnapshotBundleInMemoryCacheEntry setPredicate:]
+ GCC_except_table56
+ _CFDataGetLength
+ _OBJC_CLASS_$_PUIPosterSnapshotBundleInMemoryCache
+ _OBJC_CLASS_$_PUISceneSnapshotCandidateSnapshotContextsAction
+ _OBJC_CLASS_$_PUIStylePickerSegmentedControl
+ _OBJC_CLASS_$__PUIPosterSnapshotBundleInMemoryCacheEntry
+ _OBJC_IVAR_$_PUIPosterSnapshotBundleInMemoryCache._cacheEntries
+ _OBJC_IVAR_$_PUIStylePickerSegmentedControl._idealSegmentWidths
+ _OBJC_IVAR_$_PUIStylePickerSegmentedControl._lastKnownWidth
+ _OBJC_IVAR_$_PUIStylePickerSegmentedControl._segmentMinimumWidth
+ _OBJC_IVAR_$_PUIStylePickerSegmentedControl._totalIdealWidth
+ _OBJC_IVAR_$__PUIPosterSnapshotBundleInMemoryCacheEntry._bundle
+ _OBJC_IVAR_$__PUIPosterSnapshotBundleInMemoryCacheEntry._predicate
+ _OBJC_METACLASS_$_PUIPosterSnapshotBundleInMemoryCache
+ _OBJC_METACLASS_$_PUISceneSnapshotCandidateSnapshotContextsAction
+ _OBJC_METACLASS_$_PUIStylePickerSegmentedControl
+ _OBJC_METACLASS_$__PUIPosterSnapshotBundleInMemoryCacheEntry
+ __OBJC_$_CLASS_METHODS_PUIStylePickerSegmentedControl
+ __OBJC_$_CLASS_PROP_LIST_PUISceneSnapshotCandidateSnapshotContextsAction
+ __OBJC_$_INSTANCE_METHODS_PUIPosterSnapshotBundleInMemoryCache
+ __OBJC_$_INSTANCE_METHODS_PUISceneSnapshotCandidateSnapshotContextsAction
+ __OBJC_$_INSTANCE_METHODS_PUIStylePickerSegmentedControl
+ __OBJC_$_INSTANCE_METHODS__PUIPosterSnapshotBundleInMemoryCacheEntry
+ __OBJC_$_INSTANCE_VARIABLES_PUIPosterSnapshotBundleInMemoryCache
+ __OBJC_$_INSTANCE_VARIABLES_PUIStylePickerSegmentedControl
+ __OBJC_$_INSTANCE_VARIABLES__PUIPosterSnapshotBundleInMemoryCacheEntry
+ __OBJC_$_PROP_LIST_PUISceneSnapshotCandidateSnapshotContextsAction
+ __OBJC_$_PROP_LIST__PUIPosterSnapshotBundleInMemoryCacheEntry
+ __OBJC_CLASS_PROTOCOLS_$_PUISceneSnapshotCandidateSnapshotContextsAction
+ __OBJC_CLASS_RO_$_PUIPosterSnapshotBundleInMemoryCache
+ __OBJC_CLASS_RO_$_PUISceneSnapshotCandidateSnapshotContextsAction
+ __OBJC_CLASS_RO_$_PUIStylePickerSegmentedControl
+ __OBJC_CLASS_RO_$__PUIPosterSnapshotBundleInMemoryCacheEntry
+ __OBJC_METACLASS_RO_$_PUIPosterSnapshotBundleInMemoryCache
+ __OBJC_METACLASS_RO_$_PUISceneSnapshotCandidateSnapshotContextsAction
+ __OBJC_METACLASS_RO_$_PUIStylePickerSegmentedControl
+ __OBJC_METACLASS_RO_$__PUIPosterSnapshotBundleInMemoryCacheEntry
+ ___114-[FBScene(PosterUIFoundation) _pui_executeInProcessSnapshotForDescriptor:outputDestination:snapshottingAssertion:]_block_invoke
+ ___114-[FBScene(PosterUIFoundation) _pui_executeInProcessSnapshotForDescriptor:outputDestination:snapshottingAssertion:]_block_invoke_2
+ ___114-[FBScene(PosterUIFoundation) _pui_executeInProcessSnapshotForDescriptor:outputDestination:snapshottingAssertion:]_block_invoke_3
+ ___114-[FBScene(PosterUIFoundation) _pui_executeInProcessSnapshotForDescriptor:outputDestination:snapshottingAssertion:]_block_invoke_4
+ ___114-[FBScene(PosterUIFoundation) _pui_executeInProcessSnapshotForDescriptor:outputDestination:snapshottingAssertion:]_block_invoke_5
+ ___114-[FBScene(PosterUIFoundation) _pui_executeInProcessSnapshotForDescriptor:outputDestination:snapshottingAssertion:]_block_invoke_6
+ ___114-[FBScene(PosterUIFoundation) _pui_executeInProcessSnapshotForDescriptor:outputDestination:snapshottingAssertion:]_block_invoke_7
+ ___114-[FBScene(PosterUIFoundation) _pui_executeInProcessSnapshotForDescriptor:outputDestination:snapshottingAssertion:]_block_invoke_8
+ ___126-[FBScene(PosterUIFoundation) _pui_executeOutOfProcessSnapshotWithPromise:descriptor:outputDestination:snapshottingAssertion:]_block_invoke
+ ___126-[FBScene(PosterUIFoundation) _pui_executeOutOfProcessSnapshotWithPromise:descriptor:outputDestination:snapshottingAssertion:]_block_invoke.50
+ ___172-[FBScene(PosterUIFoundation) _pui_checkForSuitableSnapshotBundlesWithPromise:candidateBundlesFuture:descriptor:outputDestination:snapshottingAssertion:executeIfNecessary:]_block_invoke
+ ___172-[FBScene(PosterUIFoundation) _pui_checkForSuitableSnapshotBundlesWithPromise:candidateBundlesFuture:descriptor:outputDestination:snapshottingAssertion:executeIfNecessary:]_block_invoke.26
+ ___172-[FBScene(PosterUIFoundation) _pui_checkForSuitableSnapshotBundlesWithPromise:candidateBundlesFuture:descriptor:outputDestination:snapshottingAssertion:executeIfNecessary:]_block_invoke_2
+ ___172-[FBScene(PosterUIFoundation) _pui_checkForSuitableSnapshotBundlesWithPromise:candidateBundlesFuture:descriptor:outputDestination:snapshottingAssertion:executeIfNecessary:]_block_invoke_3
+ ___172-[FBScene(PosterUIFoundation) _pui_checkForSuitableSnapshotBundlesWithPromise:candidateBundlesFuture:descriptor:outputDestination:snapshottingAssertion:executeIfNecessary:]_block_invoke_4
+ ___172-[FBScene(PosterUIFoundation) _pui_checkForSuitableSnapshotBundlesWithPromise:candidateBundlesFuture:descriptor:outputDestination:snapshottingAssertion:executeIfNecessary:]_block_invoke_5
+ ___60-[FBScene(PosterUIFoundation) pui_invalidateWithCompletion:]_block_invoke.117
+ ___60-[FBScene(PosterUIFoundation) pui_invalidateWithCompletion:]_block_invoke.117.cold.1
+ ___80-[PUIPosterSnapshotBundleInMemoryCache cachedSnapshotBundleSatisfyingPredicate:]_block_invoke
+ ___block_descriptor_40_e8_32s_e52_B16?0"_PUIPosterSnapshotBundleInMemoryCacheEntry"8ls32l8
+ ___block_descriptor_64_e8_32s40s48s56r_e26_v16?0"BSActionResponse"8ls32l8s40l8r56l8s48l8
+ ___block_descriptor_72_e8_32s40s48s56s64s_e30_"<PFTFuture>"16?0"NSError"8ls32l8s40l8s48l8s56l8s64l8
+ ___block_descriptor_72_e8_32s40s48s56s64s_e5_v8?0ls32l8s40l8s48l8s56l8s64l8
+ ___block_descriptor_73_e8_32s40s48s56s64s_e45_v24?0"PUIPosterSnapshotBundle"8"NSError"16ls32l8s40l8s48l8s56l8s64l8
+ ___block_descriptor_80_e8_32s40s48s56s64s72bs_e30_"<PFTFuture>"16?0"NSArray"8ls72l8s32l8s40l8s48l8s56l8s64l8
+ ___block_literal_global.104
+ __pui_executeInProcessSnapshotForDescriptor:outputDestination:snapshottingAssertion:.fallbackQueue
+ __pui_executeInProcessSnapshotForDescriptor:outputDestination:snapshottingAssertion:.onceToken
+ _objc_msgSend$_pui_checkForSuitableSnapshotBundlesWithPromise:candidateBundlesFuture:descriptor:outputDestination:snapshottingAssertion:executeIfNecessary:
+ _objc_msgSend$_pui_ensureOutputDestination:error:
+ _objc_msgSend$_pui_executeInProcessSnapshotForDescriptor:outputDestination:snapshottingAssertion:
+ _objc_msgSend$_pui_executeOutOfProcessSnapshotWithPromise:descriptor:outputDestination:snapshottingAssertion:
+ _objc_msgSend$_pui_finishAndCleanupSnapshottingPromise:bundle:outputDestination:snapshottingAssertion:error:
+ _objc_msgSend$initWithCandidateSnapshotContexts:inflightSnapshotDescriptor:responder:
+ _objc_msgSend$initWithPredicate:bundle:
+ _objc_msgSend$pf_description
+ _objc_msgSend$predicate
+ _objc_msgSend$pui_executeSnapshotForDescriptor:outputDestination:candidateBundlesFutureProvider:
+ _objc_msgSend$pui_wantsSuitableSnapshotChecks
+ _objc_msgSend$recover:onErrorScheduler:
+ _objc_msgSend$satisfiesPredicate:
- +[PUIStylePickerHomeScreenItemVariantPicker defaultHeight]
- -[FBScene(PosterUIFoundation) pui_executeSnapshotForDescriptor:outputDestination:].cold.1
- -[PUIPosterSceneComponent _main_updateState].cold.2
- -[PUIStylePickerHomeScreenItemVariantPicker .cxx_destruct]
- -[PUIStylePickerHomeScreenItemVariantPicker _updateSegmentWidths]
- -[PUIStylePickerHomeScreenItemVariantPicker calculatedWidthForAvailableWidth:]
- -[PUIStylePickerHomeScreenItemVariantPicker initWithFrame:actions:]
- -[PUIStylePickerHomeScreenItemVariantPicker layoutSubviews]
- GCC_except_table45
- _CGAffineTransformRotate
- _OBJC_CLASS_$_PUIStylePickerHomeScreenItemVariantPicker
- _OBJC_IVAR_$_PUIStylePickerHomeScreenItemVariantPicker._idealSegmentWidths
- _OBJC_IVAR_$_PUIStylePickerHomeScreenItemVariantPicker._lastKnownWidth
- _OBJC_IVAR_$_PUIStylePickerHomeScreenItemVariantPicker._segmentMinimumWidth
- _OBJC_IVAR_$_PUIStylePickerHomeScreenItemVariantPicker._totalIdealWidth
- _OBJC_IVAR_$_PUIStylePickerHomeScreenTintSourceControl._unreleasedBanner
- _OBJC_METACLASS_$_PUIStylePickerHomeScreenItemVariantPicker
- _UIFontWeightBold
- __OBJC_$_CLASS_METHODS_PUIStylePickerHomeScreenItemVariantPicker
- __OBJC_$_INSTANCE_METHODS_PUIStylePickerHomeScreenItemVariantPicker
- __OBJC_$_INSTANCE_VARIABLES_PUIStylePickerHomeScreenItemVariantPicker
- __OBJC_CLASS_RO_$_PUIStylePickerHomeScreenItemVariantPicker
- __OBJC_METACLASS_RO_$_PUIStylePickerHomeScreenItemVariantPicker
- ___60-[FBScene(PosterUIFoundation) pui_invalidateWithCompletion:]_block_invoke.103
- ___60-[FBScene(PosterUIFoundation) pui_invalidateWithCompletion:]_block_invoke.103.cold.1
- ___82-[FBScene(PosterUIFoundation) pui_executeSnapshotForDescriptor:outputDestination:]_block_invoke
- ___82-[FBScene(PosterUIFoundation) pui_executeSnapshotForDescriptor:outputDestination:]_block_invoke_10
- ___82-[FBScene(PosterUIFoundation) pui_executeSnapshotForDescriptor:outputDestination:]_block_invoke_11
- ___82-[FBScene(PosterUIFoundation) pui_executeSnapshotForDescriptor:outputDestination:]_block_invoke_2
- ___82-[FBScene(PosterUIFoundation) pui_executeSnapshotForDescriptor:outputDestination:]_block_invoke_3
- ___82-[FBScene(PosterUIFoundation) pui_executeSnapshotForDescriptor:outputDestination:]_block_invoke_4
- ___82-[FBScene(PosterUIFoundation) pui_executeSnapshotForDescriptor:outputDestination:]_block_invoke_5
- ___82-[FBScene(PosterUIFoundation) pui_executeSnapshotForDescriptor:outputDestination:]_block_invoke_6
- ___82-[FBScene(PosterUIFoundation) pui_executeSnapshotForDescriptor:outputDestination:]_block_invoke_7
- ___82-[FBScene(PosterUIFoundation) pui_executeSnapshotForDescriptor:outputDestination:]_block_invoke_8
- ___82-[FBScene(PosterUIFoundation) pui_executeSnapshotForDescriptor:outputDestination:]_block_invoke_9
- ___block_descriptor_56_e8_32s40s48r_e45_v24?0"PUIPosterSnapshotBundle"8"NSError"16ls32l8r48l8s40l8
- ___block_literal_global.90
- _objc_msgSend$setEnabled:
- _objc_msgSend$systemBlueColor
- _objc_msgSend$systemFontOfSize:weight:
- _objc_msgSend$systemRedColor
- _os_variant_has_internal_ui
- _pui_executeSnapshotForDescriptor:outputDestination:.fallbackQueue
- _pui_executeSnapshotForDescriptor:outputDestination:.onceToken
CStrings:
+ "@\"<PFTFuture>\"16@?0@\"NSError\"8"
+ "@\"PUIPosterSnapshotBundlePredicate\""
+ "@\"PUIStylePickerSegmentedControl\""
+ "@60@0:8@16@24@32@40@48B56"
+ "B16@?0@\"_PUIPosterSnapshotBundleInMemoryCacheEntry\"8"
+ "NO"
+ "PUIPosterSnapshotBundleInMemoryCache"
+ "PUISceneSnapshotCandidateSnapshotContextsAction"
+ "PUIStylePickerSegmentedControl"
+ "Poster did not indicate that any existing snapshot was suitable for inflight snapshot descriptor: %{public}@, continue with execution? %{public}@"
+ "Poster indicated that this snapshot bundle is sufficient for inflight snapshot descriptor, bailing: %{public}@"
+ "Received response error for out of process snapshot: %@"
+ "T@\"NSDictionary\",R,N"
+ "T@\"PUIPosterSnapshotBundle\",&,N,V_bundle"
+ "T@\"PUIPosterSnapshotBundlePredicate\",&,N,V_predicate"
+ "T@\"PUIStylePickerSegmentedControl\",&,N,V_selectedVariantPicker"
+ "TB,N,Spui_setWantsSuitableSnapshotChecks:"
+ "YES"
+ "[%{public}@] Failed to acquire MLM assertion for %{public}@: %{public}@"
+ "_PUIPosterSnapshotBundleInMemoryCacheEntry"
+ "_cacheEntries"
+ "_predicate"
+ "_pui_checkForSuitableSnapshotBundlesWithPromise:candidateBundlesFuture:descriptor:outputDestination:snapshottingAssertion:executeIfNecessary:"
+ "_pui_ensureOutputDestination:error:"
+ "_pui_executeInProcessSnapshotForDescriptor:outputDestination:snapshottingAssertion:"
+ "_pui_executeOutOfProcessSnapshotWithPromise:descriptor:outputDestination:snapshottingAssertion:"
+ "_pui_finishAndCleanupSnapshottingPromise:bundle:outputDestination:snapshottingAssertion:error:"
+ "bundleURL was not reachable!"
+ "cacheSnapshotBundle:forPredicate:"
+ "cachedSnapshotBundleSatisfyingPredicate:"
+ "candidateSnapshotContexts"
+ "clearCachedSnapshotBundlesSatisfyingPredicate:"
+ "inflightSnapshotDescriptor"
+ "initWithCandidateSnapshotContexts:inflightSnapshotDescriptor:responder:"
+ "initWithPredicate:bundle:"
+ "no suitable snapshot found"
+ "pf_description"
+ "predicate"
+ "pui_executeSnapshotForDescriptor:outputDestination:candidateBundlesFutureProvider:"
+ "pui_setWantsSuitableSnapshotChecks:"
+ "pui_wantsSuitableSnapshotChecks"
+ "recover:onErrorScheduler:"
+ "respondWithSuitableURL:"
+ "satisfiesPredicate:"
+ "setBundle:"
+ "setPredicate:"
+ "v56@0:8@16@24@32@40@48"
- "@\"PUIStylePickerHomeScreenItemVariantPicker\""
- "PUIStylePickerHomeScreenItemVariantPicker"
- "T@\"PUIStylePickerHomeScreenItemVariantPicker\",&,N,V_selectedVariantPicker"
- "UNRELEASED"
- "[%{public}@] Failed to acquire MLM assertion: %{public}@"
- "_unreleasedBanner"
- "com.apple.SpringBoard"
- "systemBlueColor"
- "systemFontOfSize:weight:"
- "systemRedColor"

```
