## PosterUIFoundation

> `/System/Library/PrivateFrameworks/PosterUIFoundation.framework/PosterUIFoundation`

```diff

-289.103.0.0.0
-  __TEXT.__text: 0x8dbc8
-  __TEXT.__auth_stubs: 0x1c30
-  __TEXT.__objc_methlist: 0xa3b4
-  __TEXT.__const: 0xa94
-  __TEXT.__oslogstring: 0x3581
-  __TEXT.__cstring: 0x5cd2
-  __TEXT.__gcc_except_tab: 0x16b0
+290.105.0.0.0
+  __TEXT.__text: 0x8e5a4
+  __TEXT.__auth_stubs: 0x1c40
+  __TEXT.__objc_methlist: 0xa47c
+  __TEXT.__const: 0xa84
+  __TEXT.__oslogstring: 0x35d1
+  __TEXT.__cstring: 0x5d42
+  __TEXT.__gcc_except_tab: 0x16dc
   __TEXT.__dlopen_cstrs: 0x1a8
   __TEXT.__swift5_typeref: 0x502
   __TEXT.__constg_swiftt: 0x1d4

   __TEXT.__swift5_proto: 0x24
   __TEXT.__swift5_types: 0x24
   __TEXT.__swift5_capture: 0x10
-  __TEXT.__unwind_info: 0x2690
+  __TEXT.__unwind_info: 0x26c0
   __TEXT.__objc_classname: 0x1713
-  __TEXT.__objc_methname: 0x187df
-  __TEXT.__objc_methtype: 0x3e41
-  __TEXT.__objc_stubs: 0x10c80
+  __TEXT.__objc_methname: 0x189fc
+  __TEXT.__objc_methtype: 0x3e4a
+  __TEXT.__objc_stubs: 0x10d80
   __DATA_CONST.__got: 0xe28
-  __DATA_CONST.__const: 0x2588
+  __DATA_CONST.__const: 0x25c0
   __DATA_CONST.__objc_classlist: 0x4b0
   __DATA_CONST.__objc_catlist: 0xc0
   __DATA_CONST.__objc_protolist: 0x1b8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x5520
+  __DATA_CONST.__objc_selrefs: 0x5598
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x3d8
   __DATA_CONST.__objc_arraydata: 0x1b0
-  __AUTH_CONST.__auth_got: 0xe28
-  __AUTH_CONST.__const: 0xf80
-  __AUTH_CONST.__cfstring: 0x66c0
-  __AUTH_CONST.__objc_const: 0x1db68
+  __AUTH_CONST.__auth_got: 0xe30
+  __AUTH_CONST.__const: 0xf60
+  __AUTH_CONST.__cfstring: 0x6700
+  __AUTH_CONST.__objc_const: 0x1dca0
   __AUTH_CONST.__objc_dictobj: 0x28
-  __AUTH_CONST.__objc_intobj: 0x2e8
+  __AUTH_CONST.__objc_intobj: 0x318
   __AUTH_CONST.__objc_doubleobj: 0x2b0
   __AUTH_CONST.__objc_arrayobj: 0xa8
   __AUTH_CONST.__objc_floatobj: 0x20
   __AUTH.__objc_data: 0x21e0
   __AUTH.__data: 0x110
-  __DATA.__objc_ivar: 0xb70
+  __DATA.__objc_ivar: 0xb78
   __DATA.__data: 0x16c0
   __DATA.__bss: 0x7e0
   __DATA.__common: 0x18

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 08880029-EAFB-318C-83BA-53F15CFBD0EF
-  Functions: 3851
-  Symbols:   13797
-  CStrings:  6671
+  UUID: 84D22F7D-DC62-31C9-B86F-98CE101EF71B
+  Functions: 3860
+  Symbols:   13831
+  CStrings:  6698
 
Symbols:
+ -[FBSMutableSceneClientSettings(PosterUIFoundation) pui_setAdaptiveTimeMode:]
+ -[FBSMutableSceneSettings(PosterUIFoundation) pui_setAdaptiveTimeDisabled:]
+ -[FBSSceneClientSettings(PosterUIFoundation) pui_adaptiveTimeMode]
+ -[FBSSceneClientSettingsDiff(PosterUIFoundation) pui_adaptiveTimeModeDidChange]
+ -[FBSSceneSettings(PosterUIFoundation) pui_isAdaptiveTimeDisabled]
+ -[PUIPosterSnapshotBundle fileResourceIdentifier]
+ -[PUIPosterSnapshotFilesystemCache reachableCacheFuture]
+ -[PUIPosterSnapshotFilesystemCache snapshotDestinationFutureForPath:clientAuditToken:]
+ -[PUIPosterSnapshotSQLiteCache reachableCacheFuture]
+ -[PUIPosterSnapshotSQLiteCache snapshotDestinationFutureForPath:clientAuditToken:]
+ -[PUIStylePickerHomeScreenItemView _effectiveStyleTypeOption]
+ -[PUIStylePickerHomeScreenTintSourceControl _updateSelectionViewMask]
+ GCC_except_table28
+ GCC_except_table40
+ GCC_except_table48
+ GCC_except_table49
+ _OBJC_IVAR_$_PUIPosterSnapshotBundle._fileResourceIdentifier
+ _OBJC_IVAR_$_PUIStylePickerHomeScreenTintSourceControl._unreleasedBanner
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_PUIPosterSnapshotDestinationProviding
+ __OBJC_$_PROTOCOL_REFS_PUIPosterSnapshotDestinationProviding
+ ___52-[PUIPosterSnapshotSQLiteCache reachableCacheFuture]_block_invoke
+ ___56-[PUIPosterSnapshotFilesystemCache reachableCacheFuture]_block_invoke
+ ___60-[PUIPosterSnapshotSQLiteCache cacheSnapshotBundle:options:]_block_invoke.55
+ ___65-[PUIPosterSceneSnapshotter _mainQueue_captureSnapshotWithScene:]_block_invoke.37
+ ___65-[PUIPosterSceneSnapshotter _mainQueue_captureSnapshotWithScene:]_block_invoke_2.39
+ ___65-[PUIPosterSceneSnapshotter _mainQueue_captureSnapshotWithScene:]_block_invoke_3
+ ___68-[PUIPosterSnapshotBundlePredicate(SQLiteAdditions) SQLitePredicate]_block_invoke.503
+ ___69-[_PUIPosterSnapshotSQLiteCacheImplementation prepareCacheWithError:]_block_invoke.560
+ ___75-[PUIPosterSnapshotSQLiteCache discardSnapshotBundlesMatchingSQLPredicate:]_block_invoke.46
+ ___75-[_PUIPosterSnapshotSQLiteCacheImplementation cacheSnapshotBundle:options:]_block_invoke.589
+ ___77-[PUIPosterSceneSnapshotter _teardownSceneSynchronously:sceneWasDeactivated:]_block_invoke.47
+ ___77-[PUIPosterSceneSnapshotter _teardownSceneSynchronously:sceneWasDeactivated:]_block_invoke_2.48
+ ___81-[PUIPosterSnapshotSQLiteCache snapshotBundlesMatchingPredicate:orderedBy:limit:]_block_invoke.58
+ ___81-[PUIPosterSnapshotSQLiteCache snapshotBundlesMatchingPredicate:orderedBy:limit:]_block_invoke.58.cold.1
+ ___81-[PUIPosterSnapshotSQLiteCache snapshotBundlesMatchingPredicate:orderedBy:limit:]_block_invoke.59
+ ___81-[PUIPosterSnapshotSQLiteCache snapshotBundlesMatchingPredicate:orderedBy:limit:]_block_invoke.59.cold.1
+ ___81-[PUIPosterSnapshotSQLiteCache snapshotBundlesMatchingPredicate:orderedBy:limit:]_block_invoke.60
+ ___86-[PUIPosterSnapshotFilesystemCache cacheSnapshotBundle:forRequest:options:completion:]_block_invoke.103
+ ___86-[PUIPosterSnapshotFilesystemCache cacheSnapshotBundle:forRequest:options:completion:]_block_invoke.99
+ ___86-[PUIPosterSnapshotFilesystemCache cacheSnapshotBundle:forRequest:options:completion:]_block_invoke_2.109
+ ___90-[_PUIPosterSnapshotSQLiteCacheImplementation discardSnapshotBundlesMatchingSQLPredicate:]_block_invoke.571
+ ___90-[_PUIPosterSnapshotSQLiteCacheImplementation discardSnapshotBundlesMatchingSQLPredicate:]_block_invoke.573
+ ___99-[_PUIPosterSnapshotSQLiteCacheImplementation snapshotBundlesMatchingSQLPredicate:orderedBy:limit:]_block_invoke.581
+ ___99-[_PUIPosterSnapshotSQLiteCacheImplementation snapshotBundlesMatchingSQLPredicate:orderedBy:limit:]_block_invoke.583
+ ___block_descriptor_105_e8_32s40s48s56s64s72s80s88s96r_e5_v8?0ls32l8s40l8s48l8r96l8s56l8s64l8s72l8s80l8s88l8
+ ___block_descriptor_40_e8_32w_e60_"<PFTFuture>"16?0"_PUIPosterSnapshotSQLiteCacheInstance"8lw32l8
+ ___block_descriptor_40_e8_32w_e9_16?0^8lw32l8
+ ___block_descriptor_48_e8_32s40s_e51_"<PFTFuture>"16?0"PUIPosterSnapshotDestination"8ls32l8s40l8
+ ___block_literal_global.134
+ ___block_literal_global.271
+ ___block_literal_global.286
+ ___block_literal_global.294
+ ___block_literal_global.298
+ ___block_literal_global.311
+ ___block_literal_global.316
+ ___block_literal_global.563
+ _objc_msgSend$_effectiveStyleTypeOption
+ _objc_msgSend$_updateSelectionViewMask
+ _objc_msgSend$appendPath:
+ _objc_msgSend$bezierPathWithRect:
+ _objc_msgSend$createFileAtPath:contents:attributes:
+ _objc_msgSend$fileResourceIdentifier
+ _objc_msgSend$flatMap:continuationScheduler:
+ _objc_msgSend$isEnabled
+ _objc_msgSend$pui_adaptiveTimeMode
+ _objc_msgSend$reachableCacheFuture
+ _objc_msgSend$setUsesEvenOddFillRule:
+ _objc_msgSend$snapshotDestinationFutureForPath:clientAuditToken:
+ _objc_release_x2
- -[PUIPosterSnapshotFilesystemCache checkCacheIsReachableAsync]
- -[PUIPosterSnapshotFilesystemCache snapshotDestinationForPath:clientAuditToken:error:]
- -[PUIPosterSnapshotSQLiteCache checkCacheIsReachableAsync]
- -[PUIPosterSnapshotSQLiteCache snapshotDestinationForPath:clientAuditToken:error:]
- GCC_except_table47
- GCC_except_table7
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_PUIPosterSnapshotDestinationProviding
- ___58-[PUIPosterSnapshotSQLiteCache checkCacheIsReachableAsync]_block_invoke
- ___60-[PUIPosterSnapshotSQLiteCache cacheSnapshotBundle:options:]_block_invoke.58
- ___62-[PUIPosterSnapshotFilesystemCache checkCacheIsReachableAsync]_block_invoke
- ___65-[PUIPosterSceneSnapshotter _mainQueue_captureSnapshotWithScene:]_block_invoke.34
- ___68-[PUIPosterSnapshotBundlePredicate(SQLiteAdditions) SQLitePredicate]_block_invoke.500
- ___69-[_PUIPosterSnapshotSQLiteCacheImplementation prepareCacheWithError:]_block_invoke.556
- ___69-[_PUIPosterSnapshotSQLiteCacheImplementation prepareCacheWithError:]_block_invoke.cold.2
- ___75-[PUIPosterSnapshotSQLiteCache discardSnapshotBundlesMatchingSQLPredicate:]_block_invoke.49
- ___75-[_PUIPosterSnapshotSQLiteCacheImplementation cacheSnapshotBundle:options:]_block_invoke.585
- ___77-[PUIPosterSceneSnapshotter _teardownSceneSynchronously:sceneWasDeactivated:]_block_invoke.43
- ___77-[PUIPosterSceneSnapshotter _teardownSceneSynchronously:sceneWasDeactivated:]_block_invoke_2.44
- ___81-[PUIPosterSnapshotSQLiteCache snapshotBundlesMatchingPredicate:orderedBy:limit:]_block_invoke.61
- ___81-[PUIPosterSnapshotSQLiteCache snapshotBundlesMatchingPredicate:orderedBy:limit:]_block_invoke.61.cold.1
- ___81-[PUIPosterSnapshotSQLiteCache snapshotBundlesMatchingPredicate:orderedBy:limit:]_block_invoke.62
- ___81-[PUIPosterSnapshotSQLiteCache snapshotBundlesMatchingPredicate:orderedBy:limit:]_block_invoke.62.cold.1
- ___81-[PUIPosterSnapshotSQLiteCache snapshotBundlesMatchingPredicate:orderedBy:limit:]_block_invoke.63
- ___86-[PUIPosterSnapshotFilesystemCache cacheSnapshotBundle:forRequest:options:completion:]_block_invoke.90
- ___86-[PUIPosterSnapshotFilesystemCache cacheSnapshotBundle:forRequest:options:completion:]_block_invoke.97
- ___86-[PUIPosterSnapshotFilesystemCache cacheSnapshotBundle:forRequest:options:completion:]_block_invoke_2.103
- ___90-[_PUIPosterSnapshotSQLiteCacheImplementation discardSnapshotBundlesMatchingSQLPredicate:]_block_invoke.567
- ___90-[_PUIPosterSnapshotSQLiteCacheImplementation discardSnapshotBundlesMatchingSQLPredicate:]_block_invoke.569
- ___99-[_PUIPosterSnapshotSQLiteCacheImplementation snapshotBundlesMatchingSQLPredicate:orderedBy:limit:]_block_invoke.577
- ___99-[_PUIPosterSnapshotSQLiteCacheImplementation snapshotBundlesMatchingSQLPredicate:orderedBy:limit:]_block_invoke.579
- ___block_descriptor_32_e60_"<PFTFuture>"16?0"_PUIPosterSnapshotSQLiteCacheInstance"8l
- ___block_descriptor_65_e8_32s40s48s_e17_v16?0"NSError"8ls32l8s40l8s48l8
- ___block_descriptor_97_e8_32s40s48s56s64s72s80s88r_e5_v8?0ls32l8s40l8r88l8s48l8s56l8s64l8s72l8s80l8
- ___block_literal_global.132
- ___block_literal_global.268
- ___block_literal_global.280
- ___block_literal_global.288
- ___block_literal_global.295
- ___block_literal_global.299
- ___block_literal_global.37
- ___block_literal_global.42
- ___block_literal_global.559
- _objc_msgSend$assetView
- _objc_msgSend$checkCacheIsReachableAsync
- _objc_msgSend$configureAssetPackageView:withColorStops:accentColor:
- _objc_msgSend$snapshotDestinationForPath:clientAuditToken:error:
CStrings:
+ "<%{public}@> Changed allow-suspend-with-open-file-handle for sqlite database url %{public}@: %{public}@"
+ "<_PUIPosterSnapshotSQLiteCacheImplementation init> Unable to change allow-suspend-with-open-file-handle for sqlite database url %{public}@: %{public}@"
+ "@"
+ "@\"<PFTFuture>\"16@?0@\"PUIPosterSnapshotDestination\"8"
+ "@\"PFTFuture\"32@0:8@\"PFPosterPath\"16@\"BSAuditToken\"24"
+ "A required weak reference became nil"
+ "Captured preferred salient content rect '%{public}@'"
+ "TB,N,Gpui_isAdaptiveTimeDisabled,Spui_setAdaptiveTimeDisabled:"
+ "TB,R,N,Gpui_isAdaptiveTimeDisabled"
+ "TQ,N,Spui_setAdaptiveTimeMode:"
+ "_effectiveStyleTypeOption"
+ "_fileResourceIdentifier"
+ "_unreleasedBanner"
+ "_updateSelectionViewMask"
+ "appendPath:"
+ "backdropLayer:didSampleProtectedLuma:"
+ "bezierPathWithRect:"
+ "createFileAtPath:contents:attributes:"
+ "fileResourceIdentifier"
+ "flatMap:continuationScheduler:"
+ "isEnabled"
+ "pui_adaptiveTimeDisabled"
+ "pui_adaptiveTimeMode"
+ "pui_adaptiveTimeModeDidChange"
+ "pui_isAdaptiveTimeDisabled"
+ "pui_setAdaptiveTimeDisabled:"
+ "pui_setAdaptiveTimeMode:"
+ "reachableCacheFuture"
+ "setUsesEvenOddFillRule:"
+ "snapshotDestinationFutureForPath:clientAuditToken:"
+ "unknown destination creation error"
+ "v28@0:8@\"CABackdropLayer\"16B24"
- "(%{public}@) Error generating destination: %{public}@"
- "<%{public}@> Skipping marking database for allow suspend with open handles (opened readonly?)"
- "<%{public}@> Validated sqlite database URL %{public}@ allowed open while suspend"
- "@\"PUIPosterSnapshotDestination\"40@0:8@\"PFPosterPath\"16@\"BSAuditToken\"24o^@32"
- "T@\"UIColor\",C,N,V_tintColor"
- "checkCacheIsReachableAsync"
- "snapshotDestinationForPath:clientAuditToken:error:"

```
