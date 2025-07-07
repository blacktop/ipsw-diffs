## PosterUIFoundation

> `/System/Library/PrivateFrameworks/PosterUIFoundation.framework/PosterUIFoundation`

```diff

-280.101.0.0.0
-  __TEXT.__text: 0x8b370
-  __TEXT.__auth_stubs: 0x1c90
-  __TEXT.__objc_methlist: 0xa214
-  __TEXT.__const: 0xaa4
-  __TEXT.__oslogstring: 0x32d1
-  __TEXT.__cstring: 0x5c42
-  __TEXT.__gcc_except_tab: 0x1350
+283.101.0.0.0
+  __TEXT.__text: 0x8d6d8
+  __TEXT.__auth_stubs: 0x1cc0
+  __TEXT.__objc_methlist: 0xa314
+  __TEXT.__const: 0xab4
+  __TEXT.__oslogstring: 0x3511
+  __TEXT.__cstring: 0x5d02
+  __TEXT.__gcc_except_tab: 0x1524
   __TEXT.__dlopen_cstrs: 0x1a8
   __TEXT.__swift5_typeref: 0x502
   __TEXT.__constg_swiftt: 0x1d4

   __TEXT.__swift5_proto: 0x24
   __TEXT.__swift5_types: 0x24
   __TEXT.__swift5_capture: 0x10
-  __TEXT.__unwind_info: 0x25e0
-  __TEXT.__objc_classname: 0x16c6
-  __TEXT.__objc_methname: 0x180d9
-  __TEXT.__objc_methtype: 0x3f3a
-  __TEXT.__objc_stubs: 0x10a80
-  __DATA_CONST.__got: 0xe28
-  __DATA_CONST.__const: 0x24d8
-  __DATA_CONST.__objc_classlist: 0x4a8
+  __TEXT.__unwind_info: 0x2640
+  __TEXT.__objc_classname: 0x1728
+  __TEXT.__objc_methname: 0x18365
+  __TEXT.__objc_methtype: 0x3f4e
+  __TEXT.__objc_stubs: 0x10b80
+  __DATA_CONST.__got: 0xe38
+  __DATA_CONST.__const: 0x24e0
+  __DATA_CONST.__objc_classlist: 0x4b8
   __DATA_CONST.__objc_catlist: 0xc0
   __DATA_CONST.__objc_protolist: 0x1c0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x5410
+  __DATA_CONST.__objc_selrefs: 0x5470
   __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__objc_superrefs: 0x3c8
+  __DATA_CONST.__objc_superrefs: 0x3d8
   __DATA_CONST.__objc_arraydata: 0x1b0
-  __AUTH_CONST.__auth_got: 0xe58
+  __AUTH_CONST.__auth_got: 0xe70
   __AUTH_CONST.__const: 0xf80
-  __AUTH_CONST.__cfstring: 0x6680
-  __AUTH_CONST.__objc_const: 0x1dd88
+  __AUTH_CONST.__cfstring: 0x6740
+  __AUTH_CONST.__objc_const: 0x1df50
   __AUTH_CONST.__objc_dictobj: 0x28
-  __AUTH_CONST.__objc_intobj: 0x2b8
+  __AUTH_CONST.__objc_intobj: 0x318
   __AUTH_CONST.__objc_doubleobj: 0x2b0
   __AUTH_CONST.__objc_arrayobj: 0xa8
   __AUTH_CONST.__objc_floatobj: 0x20
-  __AUTH.__objc_data: 0x2230
+  __AUTH.__objc_data: 0x22d0
   __AUTH.__data: 0x110
-  __DATA.__objc_ivar: 0xb64
+  __DATA.__objc_ivar: 0xb74
   __DATA.__data: 0x1720
   __DATA.__bss: 0x7e0
   __DATA.__common: 0x18

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 249F7154-319C-3175-9271-F8DDFD9556C5
-  Functions: 3797
-  Symbols:   13691
-  CStrings:  6624
+  UUID: 1C60126E-33A7-3227-919E-F8A79AA061D1
+  Functions: 3835
+  Symbols:   13790
+  CStrings:  6667
 
Symbols:
+ +[UIFont(PosterUIFoundation) pui_UIFontWithName:forRole:includingFallbackFonts:attributes:]
+ -[PUIPosterSnapshotFilesystemCache checkCacheIsReachableAsync]
+ -[PUIPosterSnapshotSQLiteCache _accessCacheImplementationSyncWithReason:outError:]
+ -[PUIPosterSnapshotSQLiteCache cacheSnapshotBundle:options:outError:]
+ -[PUIPosterSnapshotSQLiteCache checkCacheIsReachableAsync]
+ -[PUIPosterSnapshotSQLiteCache cleanupWithError:]
+ -[PUIPosterSnapshotSQLiteCache discardSnapshotBundlesMatchingPredicate:outError:]
+ -[PUIPosterSnapshotSQLiteCache discardSnapshotBundlesMatchingSQLPredicate:outError:]
+ -[PUIPosterSnapshotSQLiteCache latestSnapshotBundleMatchingPredicate:outError:]
+ -[PUIPosterSnapshotSQLiteCache snapshotBundlesMatchingPredicate:orderedBy:limit:outError:]
+ -[PUIPosterSnapshotSQLiteCache snapshotBundlesMatchingPredicate:orderedBy:limit:outError:].cold.1
+ -[PUIPosterSnapshotSQLiteCache snapshotBundlesMatchingPredicate:outError:]
+ -[PUIStylePickerHomeScreenItemView _setStyleVariantOption:updatingLayout:]
+ -[UIFont(PosterUIFoundation) pui_fontWithAttributes:options:]
+ -[_PUIPosterSnapshotCapture _cleanup].cold.1
+ -[_PUIPosterSnapshotCapture _cleanup].cold.2
+ -[_PUIPosterSnapshotCapture _finishCaptureWithError:]
+ -[_PUIPosterSnapshotCapture _finishCaptureWithError:].cold.1
+ -[_PUIPosterSnapshotCapture _fire].cold.2
+ -[_PUIPosterSnapshotSQLiteCacheAsyncImplementation cacheSnapshotBundle:options:]
+ -[_PUIPosterSnapshotSQLiteCacheAsyncImplementation discardSnapshotBundlesMatchingSQLPredicate:]
+ -[_PUIPosterSnapshotSQLiteCacheAsyncImplementation invalidate]
+ -[_PUIPosterSnapshotSQLiteCacheAsyncImplementation prepareCacheWithError:]
+ -[_PUIPosterSnapshotSQLiteCacheAsyncImplementation snapshotBundlesMatchingSQLPredicate:orderedBy:limit:]
+ -[_PUIPosterSnapshotSQLiteCacheSyncImplementation cacheSnapshotBundle:options:outError:]
+ -[_PUIPosterSnapshotSQLiteCacheSyncImplementation discardSnapshotBundlesMatchingSQLPredicate:outError:]
+ -[_PUIPosterSnapshotSQLiteCacheSyncImplementation initWithURL:fileManager:options:error:]
+ -[_PUIPosterSnapshotSQLiteCacheSyncImplementation snapshotBundlesMatchingSQLPredicate:orderedBy:limit:outError:]
+ GCC_except_table174
+ GCC_except_table30
+ GCC_except_table43
+ _CTFontCreateWithFontDescriptorAndOptions
+ _CTFontDescriptorCreateCopyWithAttributes
+ _OBJC_CLASS_$__PUIPosterSnapshotSQLiteCacheAsyncImplementation
+ _OBJC_CLASS_$__PUIPosterSnapshotSQLiteCacheSyncImplementation
+ _OBJC_IVAR_$_PUIPosterSnapshotCaptureController._captureQueueHighWaterMark
+ _OBJC_IVAR_$__PUIPosterSnapshotCapture._cleanedUpSignal
+ _OBJC_IVAR_$__PUIPosterSnapshotCapture._finished
+ _OBJC_IVAR_$__PUIPosterSnapshotCapture._sceneIsReadyToSnapshot
+ _OBJC_IVAR_$__PUIPosterSnapshotCapture._startTime
+ _OBJC_METACLASS_$__PUIPosterSnapshotSQLiteCacheAsyncImplementation
+ _OBJC_METACLASS_$__PUIPosterSnapshotSQLiteCacheSyncImplementation
+ _OUTLINED_FUNCTION_10
+ _OUTLINED_FUNCTION_11
+ _PUIFontAttributesForPUIFontIdentifier
+ __OBJC_$_INSTANCE_METHODS__PUIPosterSnapshotSQLiteCacheAsyncImplementation
+ __OBJC_$_INSTANCE_METHODS__PUIPosterSnapshotSQLiteCacheSyncImplementation
+ __OBJC_CLASS_RO_$__PUIPosterSnapshotSQLiteCacheAsyncImplementation
+ __OBJC_CLASS_RO_$__PUIPosterSnapshotSQLiteCacheSyncImplementation
+ __OBJC_METACLASS_RO_$__PUIPosterSnapshotSQLiteCacheAsyncImplementation
+ __OBJC_METACLASS_RO_$__PUIPosterSnapshotSQLiteCacheSyncImplementation
+ ___34-[_PUIPosterSnapshotCapture _fire]_block_invoke.cold.1
+ ___46-[_PUIPosterSnapshotCapture _attemptSnapshot:]_block_invoke.48
+ ___46-[_PUIPosterSnapshotCapture _attemptSnapshot:]_block_invoke.52
+ ___46-[_PUIPosterSnapshotCapture _attemptSnapshot:]_block_invoke.52.cold.1
+ ___52-[_PUIPosterSnapshotCapture _captureLevelSet:error:]_block_invoke.79
+ ___53-[_PUIPosterSnapshotCapture _finishCaptureWithError:]_block_invoke
+ ___53-[_PUIPosterSnapshotCapture _finishCaptureWithError:]_block_invoke.83
+ ___53-[_PUIPosterSnapshotCapture _finishCaptureWithError:]_block_invoke_2
+ ___53-[_PUIPosterSnapshotCapture _finishCaptureWithError:]_block_invoke_2.cold.1
+ ___58-[PUIPosterSnapshotSQLiteCache checkCacheIsReachableAsync]_block_invoke
+ ___60-[PUIPosterSnapshotCaptureController _lock_kickCaptureQueue]_block_invoke.207
+ ___60-[PUIPosterSnapshotCaptureController _lock_kickCaptureQueue]_block_invoke.207.cold.1
+ ___60-[PUIPosterSnapshotCaptureController _lock_kickCaptureQueue]_block_invoke.210
+ ___60-[PUIPosterSnapshotSQLiteCache cacheSnapshotBundle:options:]_block_invoke.58
+ ___60-[PUIPosterSnapshotSQLiteCache cacheSnapshotBundle:options:]_block_invoke.cold.1
+ ___62-[PUIPosterSnapshotFilesystemCache checkCacheIsReachableAsync]_block_invoke
+ ___68-[PUIPosterSnapshotBundlePredicate(SQLiteAdditions) SQLitePredicate]_block_invoke.500
+ ___69-[_PUIPosterSnapshotSQLiteCacheImplementation prepareCacheWithError:]_block_invoke.556
+ ___75-[PUIPosterSnapshotSQLiteCache discardSnapshotBundlesMatchingSQLPredicate:]_block_invoke.49
+ ___75-[PUIPosterSnapshotSQLiteCache discardSnapshotBundlesMatchingSQLPredicate:]_block_invoke.cold.1
+ ___75-[_PUIPosterSnapshotSQLiteCacheImplementation cacheSnapshotBundle:options:]_block_invoke.585
+ ___81-[PUIPosterSnapshotSQLiteCache snapshotBundlesMatchingPredicate:orderedBy:limit:]_block_invoke.61
+ ___81-[PUIPosterSnapshotSQLiteCache snapshotBundlesMatchingPredicate:orderedBy:limit:]_block_invoke.61.cold.1
+ ___81-[PUIPosterSnapshotSQLiteCache snapshotBundlesMatchingPredicate:orderedBy:limit:]_block_invoke.62
+ ___81-[PUIPosterSnapshotSQLiteCache snapshotBundlesMatchingPredicate:orderedBy:limit:]_block_invoke.62.cold.1
+ ___81-[PUIPosterSnapshotSQLiteCache snapshotBundlesMatchingPredicate:orderedBy:limit:]_block_invoke.63
+ ___81-[PUIPosterSnapshotSQLiteCache snapshotBundlesMatchingPredicate:orderedBy:limit:]_block_invoke.cold.1
+ ___82-[PUIPosterSnapshotSQLiteCache _accessCacheImplementationSyncWithReason:outError:]_block_invoke
+ ___86-[PUIPosterSnapshotFilesystemCache cacheSnapshotBundle:forRequest:options:completion:]_block_invoke.105
+ ___86-[PUIPosterSnapshotFilesystemCache cacheSnapshotBundle:forRequest:options:completion:]_block_invoke.90
+ ___90-[_PUIPosterSnapshotSQLiteCacheImplementation discardSnapshotBundlesMatchingSQLPredicate:]_block_invoke.567
+ ___90-[_PUIPosterSnapshotSQLiteCacheImplementation discardSnapshotBundlesMatchingSQLPredicate:]_block_invoke.569
+ ___99-[_PUIPosterSnapshotSQLiteCacheImplementation snapshotBundlesMatchingSQLPredicate:orderedBy:limit:]_block_invoke.577
+ ___99-[_PUIPosterSnapshotSQLiteCacheImplementation snapshotBundlesMatchingSQLPredicate:orderedBy:limit:]_block_invoke.579
+ ___block_descriptor_105_e8_32s40s48s56s64s72s80s_e5_v8?0ls32l8s40l8s48l8s56l8s64l8s72l8s80l8
+ ___block_descriptor_48_e8_32s40s_e27_v16?0"BSSimpleAssertion"8ls32l8s40l8
+ ___block_descriptor_56_e8_32s40r48w_e5_v8?0lr40l8w48l8s32l8
+ ___block_descriptor_56_e8_32s40s_e60_"<PFTFuture>"16?0"_PUIPosterSnapshotSQLiteCacheInstance"8ls32l8s40l8
+ ___block_descriptor_64_e8_32s40bs48r56w_e8_B12?0B8lw56l8r48l8s32l8s40l8
+ ___block_descriptor_64_e8_32s40s48s_e60_"<PFTFuture>"16?0"_PUIPosterSnapshotSQLiteCacheInstance"8ls32l8s40l8s48l8
+ ___block_descriptor_72_e8_32s40s48s56s_e60_"<PFTFuture>"16?0"_PUIPosterSnapshotSQLiteCacheInstance"8ls32l8s40l8s48l8s56l8
+ ___block_descriptor_81_e8_32s40s48s56s64w_e5_v8?0ls32l8s40l8s48l8w64l8s56l8
+ ___block_literal_global.268
+ ___block_literal_global.280
+ ___block_literal_global.283
+ ___block_literal_global.288
+ ___block_literal_global.291
+ ___block_literal_global.295
+ ___block_literal_global.299
+ ___block_literal_global.302
+ ___block_literal_global.305
+ ___block_literal_global.308
+ ___block_literal_global.559
+ _kCTFontTrackAttribute
+ _objc_msgSend$_finishCaptureWithError:
+ _objc_msgSend$_setStyleVariantOption:updatingLayout:
+ _objc_msgSend$cacheQueue
+ _objc_msgSend$cacheSnapshotBundle:options:outError:
+ _objc_msgSend$checkCacheIsReachableAsync
+ _objc_msgSend$discardSnapshotBundlesMatchingSQLPredicate:outError:
+ _objc_msgSend$immediateScheduler
+ _objc_msgSend$pui_UIFontWithName:forRole:includingFallbackFonts:attributes:
+ _objc_msgSend$pui_fontWithAttributes:options:
+ _objc_msgSend$removeTrait:
+ _objc_msgSend$setOverrideUserInterfaceStyle:
+ _objc_msgSend$setSupportsEyedropper:
+ _objc_msgSend$snapshotBundlesMatchingSQLPredicate:orderedBy:limit:outError:
+ _objc_msgSend$traitOverrides
+ _objc_terminate
- +[UIFont(PosterUIFoundation) pui_UIFontWithName:forRole:includingFallbackFonts:]
- -[_PUIPosterSnapshotCapture _attemptSnapshot:].cold.4
- -[_PUIPosterSnapshotCapture _finalizeBundle]
- GCC_except_table155
- GCC_except_table29
- GCC_except_table31
- GCC_except_table34
- _OBJC_CLASS_$_PFDefer
- _OBJC_IVAR_$__PUIPosterSnapshotCapture._snapshotReadinessObserver
- ___44-[_PUIPosterSnapshotCapture _finalizeBundle]_block_invoke
- ___44-[_PUIPosterSnapshotCapture _finalizeBundle]_block_invoke_2
- ___46-[_PUIPosterSnapshotCapture _attemptSnapshot:]_block_invoke.44
- ___46-[_PUIPosterSnapshotCapture _attemptSnapshot:]_block_invoke.cold.3
- ___52-[_PUIPosterSnapshotCapture _captureLevelSet:error:]_block_invoke.73
- ___60-[PUIPosterSnapshotCaptureController _lock_kickCaptureQueue]_block_invoke.196
- ___60-[PUIPosterSnapshotCaptureController _lock_kickCaptureQueue]_block_invoke.196.cold.1
- ___60-[PUIPosterSnapshotCaptureController _lock_kickCaptureQueue]_block_invoke.199
- ___60-[PUIPosterSnapshotSQLiteCache cacheSnapshotBundle:options:]_block_invoke_4
- ___63-[PUIPosterSnapshotSQLiteCache checkCacheIsReachableWithError:]_block_invoke
- ___67-[PUIStylePickerHomeScreenItemVariantPicker initWithFrame:actions:]_block_invoke
- ___68-[PUIPosterSnapshotBundlePredicate(SQLiteAdditions) SQLitePredicate]_block_invoke.479
- ___69-[_PUIPosterSnapshotSQLiteCacheImplementation prepareCacheWithError:]_block_invoke.534
- ___75-[PUIPosterSnapshotSQLiteCache discardSnapshotBundlesMatchingSQLPredicate:]_block_invoke_4
- ___75-[_PUIPosterSnapshotSQLiteCacheImplementation cacheSnapshotBundle:options:]_block_invoke.563
- ___81-[PUIPosterSnapshotSQLiteCache snapshotBundlesMatchingPredicate:orderedBy:limit:]_block_invoke.55
- ___81-[PUIPosterSnapshotSQLiteCache snapshotBundlesMatchingPredicate:orderedBy:limit:]_block_invoke.55.cold.1
- ___81-[PUIPosterSnapshotSQLiteCache snapshotBundlesMatchingPredicate:orderedBy:limit:]_block_invoke.56
- ___81-[PUIPosterSnapshotSQLiteCache snapshotBundlesMatchingPredicate:orderedBy:limit:]_block_invoke_2
- ___81-[PUIPosterSnapshotSQLiteCache snapshotBundlesMatchingPredicate:orderedBy:limit:]_block_invoke_2.cold.1
- ___86-[PUIPosterSnapshotFilesystemCache cacheSnapshotBundle:forRequest:options:completion:]_block_invoke.106
- ___86-[PUIPosterSnapshotFilesystemCache cacheSnapshotBundle:forRequest:options:completion:]_block_invoke.91
- ___90-[_PUIPosterSnapshotSQLiteCacheImplementation discardSnapshotBundlesMatchingSQLPredicate:]_block_invoke.545
- ___90-[_PUIPosterSnapshotSQLiteCacheImplementation discardSnapshotBundlesMatchingSQLPredicate:]_block_invoke.547
- ___99-[_PUIPosterSnapshotSQLiteCacheImplementation snapshotBundlesMatchingSQLPredicate:orderedBy:limit:]_block_invoke.555
- ___99-[_PUIPosterSnapshotSQLiteCacheImplementation snapshotBundlesMatchingSQLPredicate:orderedBy:limit:]_block_invoke.557
- ___block_descriptor_113_e8_32s40s48s56s64s72s80s88s_e5_v8?0ls32l8s40l8s48l8s56l8s64l8s72l8s80l8s88l8
- ___block_descriptor_40_e36_"UIColor"16?0"UITraitCollection"8l
- ___block_descriptor_40_e8_32s_e60_"<PFTFuture>"16?0"_PUIPosterSnapshotSQLiteCacheInstance"8ls32l8
- ___block_descriptor_48_e8_32s40s_e60_"<PFTFuture>"16?0"_PUIPosterSnapshotSQLiteCacheInstance"8ls32l8s40l8
- ___block_descriptor_56_e8_32s40s48w_e5_v8?0ls32l8w48l8s40l8
- ___block_descriptor_56_e8_32s40s48w_e8_B12?0B8lw48l8s32l8s40l8
- ___block_descriptor_64_e8_32s40s48s56s_e60_"<PFTFuture>"16?0"_PUIPosterSnapshotSQLiteCacheInstance"8ls32l8s40l8s48l8s56l8
- ___block_descriptor_73_e8_32s40s48s56s64w_e5_v8?0ls32l8s40l8s48l8s56l8w64l8
- ___block_literal_global.247
- ___block_literal_global.259
- ___block_literal_global.262
- ___block_literal_global.267
- ___block_literal_global.270
- ___block_literal_global.274
- ___block_literal_global.278
- ___block_literal_global.281
- ___block_literal_global.284
- ___block_literal_global.287
- ___block_literal_global.292
- ___block_literal_global.537
- _objc_msgSend$_finalizeBundle
- _objc_msgSend$block:
- _objc_msgSend$cancelAllOperations
- _objc_msgSend$colorWithDynamicProvider:
- _objc_msgSend$isFinished
- _objc_msgSend$setSuspended:
CStrings:
+ "(%@) Enqueued capture %p; %lu snapshots pending; high water mark: %lu"
+ "(%p) Abort Cleaning up; capture is not completed..."
+ "(%p) Clean up skip; already ran."
+ "(%p) Cleaned up complete"
+ "(%p) Cleaning up..."
+ "(%p) Invalidating _PUIPosterSnapshotCapture..."
+ "(%p) Snapshot Finalized; much success; capture time %f"
+ "(%p) Snapshot bundle failed: %{public}@; capture time %f"
+ "(%p) Snapshot failed to capture: %{public}@; capture time %f"
+ "(%p) abort finish; already finished!"
+ "(%p) attempting snapshot after CA commit"
+ "(%p) scene is ready to snapshot..."
+ "(%p) scene isn't ready yet for reason (%{public}@); setting up snapshot readiness observer..."
+ "(capture %p) capturing snapshot for interface orientation %lu user interface style %lu"
+ "(wait %p) waiting to attempt snapshot until after CA commit"
+ ".ADTSlabSoftNumeric-Heavy"
+ ".ADTSlabSoftNumeric-Medium"
+ ".ADTSlabSoftNumeric-Semibold"
+ ".NewYorkSoftNumeric-Heavy"
+ ".NewYorkSoftNumeric-Medium"
+ ".NewYorkSoftNumeric-Semibold"
+ ".SFRailRoundedNumeric-Heavy"
+ "@44@0:8@16@24B32@36"
+ "Invalidating PUIPosterSnapshotCaptureController: %p"
+ "_PUIPosterSnapshotSQLiteCacheAsyncImplementation"
+ "_PUIPosterSnapshotSQLiteCacheSyncImplementation"
+ "__obj"
+ "_captureQueueHighWaterMark"
+ "_cleanedUpSignal"
+ "_finishCaptureWithError:"
+ "_finished"
+ "_sceneIsReadyToSnapshot"
+ "_setStyleVariantOption:updatingLayout:"
+ "_startTime"
+ "b"
+ "cacheSnapshotBundle:options:outError:"
+ "capture failed without error"
+ "checkCacheIsReachableAsync"
+ "cleanupWithError:"
+ "discardSnapshotBundlesMatchingPredicate:outError:"
+ "discardSnapshotBundlesMatchingSQLPredicate:outError:"
+ "finish sqlite cache operation synchronously"
+ "immediateScheduler"
+ "latestSnapshotBundleMatchingPredicate:outError:"
+ "pui_UIFontWithName:forRole:includingFallbackFonts:attributes:"
+ "pui_fontWithAttributes:options:"
+ "removeTrait:"
+ "setOverrideUserInterfaceStyle:"
+ "setSupportsEyedropper:"
+ "snapshotBundlesMatchingPredicate:orderedBy:limit:outError:"
+ "snapshotBundlesMatchingPredicate:outError:"
+ "snapshotBundlesMatchingSQLPredicate:orderedBy:limit:outError:"
+ "timed out waiting for scene readiness"
+ "traitOverrides"
- "(%@) Enqueued capture %p"
- "(%p) setup snapshot readiness observer..."
- "(wait %p) capture of levelset %{public}@ failed: %{public}@"
- "(wait %p) capture succeeded of levelset %{public}@..."
- "(wait %p) scene is ready, attempting capture of levelset %{public}@..."
- ".ADTSlabNumeric-Heavy"
- ".ADTSlabNumeric-Medium"
- ".NewYorkNumeric-Heavy"
- ".NewYorkNumeric-Medium"
- "_finalizeBundle"
- "block:"
- "cancelAllOperations"
- "colorWithDynamicProvider:"
- "exceeded frame render timeout"
- "isFinished"
- "setSuspended:"

```
