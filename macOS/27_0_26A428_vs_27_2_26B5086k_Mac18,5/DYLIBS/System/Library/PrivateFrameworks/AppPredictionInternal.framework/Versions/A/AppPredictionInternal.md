## AppPredictionInternal

> `/System/Library/PrivateFrameworks/AppPredictionInternal.framework/Versions/A/AppPredictionInternal`

```diff

-671.0.1.0.1
-  __TEXT.__text: 0x4fb500
-  __TEXT.__objc_methlist: 0x38ab4
+674.0.1.0.0
+  __TEXT.__text: 0x4fbf80
+  __TEXT.__objc_methlist: 0x38b2c
   __TEXT.__const: 0x5ef0
-  __TEXT.__cstring: 0x59ec4
-  __TEXT.__oslogstring: 0x3aeb9
+  __TEXT.__cstring: 0x59f34
+  __TEXT.__oslogstring: 0x3b029
   __TEXT.__gcc_except_tab: 0x1073c
   __TEXT.__dlopen_cstrs: 0x10a
   __TEXT.__ustring: 0x90

   __TEXT.__swift5_assocty: 0x228
   __TEXT.__swift5_protos: 0x24
   __TEXT.__swift5_mpenum: 0x10
-  __TEXT.__unwind_info: 0x13c50
+  __TEXT.__unwind_info: 0x13c78
   __TEXT.__eh_frame: 0x5fb4
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__objc_protolist: 0x4b0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x10
-  __DATA_CONST.__objc_selrefs: 0x1be08
+  __DATA_CONST.__objc_selrefs: 0x1be68
   __DATA_CONST.__objc_protorefs: 0xb0
   __DATA_CONST.__objc_superrefs: 0x1488
   __DATA_CONST.__objc_arraydata: 0x1330
   __DATA_CONST.__got: 0x3b40
   __AUTH_CONST.__const: 0x137e8
-  __AUTH_CONST.__cfstring: 0x3b2c0
-  __AUTH_CONST.__objc_const: 0x82858
+  __AUTH_CONST.__cfstring: 0x3b340
+  __AUTH_CONST.__objc_const: 0x828a0
   __AUTH_CONST.__weak_auth_got: 0x20
   __AUTH_CONST.__objc_intobj: 0x3450
   __AUTH_CONST.__objc_arrayobj: 0x1128
   __AUTH_CONST.__objc_dictobj: 0xf0
   __AUTH_CONST.__objc_floatobj: 0x30
   __AUTH_CONST.__objc_doubleobj: 0x40
-  __AUTH_CONST.__auth_got: 0x23d0
+  __AUTH_CONST.__auth_got: 0x23d8
   __AUTH.__objc_data: 0x3a08
   __AUTH.__data: 0x1e20
   __DATA.__objc_ivar: 0x4a10

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 26731
-  Symbols:   47193
-  CStrings:  12441
+  Functions: 26741
+  Symbols:   47218
+  CStrings:  12448
 
Symbols:
+ +[ATXHeroDataServerHelper anyHeroPredictionsAreEligibleGivenIsMoving:isNearKnownTypeLOI:isNearKnownTypeLOIExcludingGym:isNearFrequentLOI:]
+ +[ATXHeroDataServerHelper canPredictClipsGivenRecentMotionWithContext:]
+ +[ATXHeroDataServerHelper heroAppAndClipPredictionsAreEligibleGivenIsMoving:isNearKnownTypeLOI:isNearFrequentLOI:]
+ +[ATXHeroDataServerHelper heroPoiPredictionsAreEligibleGivenIsMoving:isNearKnownTypeLOIExcludingGym:]
+ +[ATXHeroDataServerHelper isNearKnownTypeLocationOfInterest:]
+ +[ATXHeroDataServerHelper isNearKnownTypeLocationOfInterestExcludingGym:]
+ +[_ATXDataStore histogramTypeForString:found:]
+ -[ATXCDNDownloaderTriggerManager _anyHeroPredictionsAreEligible]
+ -[ATXStackStateTracker internalStateFromDisk]
+ -[_ATXInspectionClient launchCountForBundleId:inHistogramNamed:reply:]
+ -[_ATXInspectionServer launchCountForBundleId:inHistogramNamed:reply:]
+ _ATXLanguageChangeIsAwaitingRestart
+ __ATXLanguageChangeObservedTime
+ ___70-[_ATXInspectionClient launchCountForBundleId:inHistogramNamed:reply:]_block_invoke
+ _clock_gettime_nsec_np
+ _objc_msgSend$_anyHeroPredictionsAreEligible
+ _objc_msgSend$anyHeroPredictionsAreEligibleGivenIsMoving:isNearKnownTypeLOI:isNearKnownTypeLOIExcludingGym:isNearFrequentLOI:
+ _objc_msgSend$canPredictClipsGivenRecentMotionWithContext:
+ _objc_msgSend$heroPoiPredictionsAreEligibleGivenIsMoving:isNearKnownTypeLOIExcludingGym:
+ _objc_msgSend$histogramTypeForString:found:
+ _objc_msgSend$internalStateFromDisk
+ _objc_msgSend$isNearKnownTypeLocationOfInterest:
+ _objc_msgSend$isNearKnownTypeLocationOfInterestExcludingGym:
+ _objc_msgSend$languageCode
+ _objc_msgSend$launchCountForBundleId:inHistogramNamed:reply:
+ _objc_msgSend$localeWithLocaleIdentifier:
+ _objc_msgSend$preferredLanguages
+ _objc_msgSend$preferredLocalizations
- -[ATXHeroDataServer heroAppAndClipPredictionsAreEligibleGivenIsMoving:isNearKnownTypeLOI:isNearFrequentLOI:]
- -[ATXHeroDataServer heroPoiPredictionsAreEligibleGivenIsMoving:isNearKnownTypeLOIExcludingGym:isNearFrequentLOI:]
- _objc_msgSend$heroPoiPredictionsAreEligibleGivenIsMoving:isNearKnownTypeLOIExcludingGym:isNearFrequentLOI:
CStrings:
+ "%@ is deprecated and no longer records launches."
+ "%@ is not a known _ATXHistogramType. Use `atxtool histograms show-all-by-size` to see the valid names."
+ "%s: [role=%lu] deferring generation: awaiting restart after language change"
+ "%s: [role=%lu] localization mismatch: section titles resolve in '%{public}@' but the configuration is stamped '%{public}@'; gallery strings are stale"
+ "%s: [role=%lu] using locale: %{public}@ (bundle localization: %{public}@, preferred language: %{public}@)"
+ "%{public}s: Could not unarchive internal state (unarchiveErr %@, internalState %@)"
+ "%{public}s: No internal state read from disk (dataFromDisk is nil)"
+ "-[ATXStackStateTracker internalStateFromDisk]"
+ "Could not instantiate a histogram of type %@."
+ "Defaults for OverrideHeroAppPredictionEligibility set to True: treating hero predictions as eligible."
+ "FaceSuggestionAssetParametersAmbient_iOS"
+ "Skipping CDN download since no hero prediction type is eligible here. Clearing predictions."
+ "launchCountForBundleId"
- "%s: no section order provided in ambient asset parameters, or asset parameters missing!"
- "%s: using locale: %@"
- "%{public}s: Using empty internal state because loadInternalState failed (dataFromDisk is nil)"
- "%{public}s: Using empty internal state because loadInternalState failed (unarchiveErr %@, internalState %@)"
- "-[ATXFaceGalleryLayoutGenerator _ambientFaceGallerySectionsWithWidgetDescriptorsAdditionalData:aggregatedAppLaunchData:bundleIdToCompanionBundleId:ambientParameters:]"
- "FaceSuggestionAssetParametersAmbient"
```
