## AppPredictionInternal

> `/System/Library/PrivateFrameworks/AppPredictionInternal.framework/AppPredictionInternal`

```diff

-671.0.2.0.1
-  __TEXT.__text: 0x47c33c
-  __TEXT.__objc_methlist: 0x38eac
+674.0.1.0.0
+  __TEXT.__text: 0x47ce34
+  __TEXT.__objc_methlist: 0x38f2c
   __TEXT.__const: 0x450a
-  __TEXT.__cstring: 0x596b2
-  __TEXT.__oslogstring: 0x3bb49
+  __TEXT.__cstring: 0x59712
+  __TEXT.__oslogstring: 0x3bcc9
   __TEXT.__gcc_except_tab: 0xf4a0
   __TEXT.__dlopen_cstrs: 0x1d2
   __TEXT.__ustring: 0x90

   __TEXT.__swift5_builtin: 0x78
   __TEXT.__swift5_protos: 0x30
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0x12840
+  __TEXT.__unwind_info: 0x12870
   __TEXT.__eh_frame: 0x262c
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__objc_protolist: 0x4d0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x10
-  __DATA_CONST.__objc_selrefs: 0x1bf80
+  __DATA_CONST.__objc_selrefs: 0x1bfe0
   __DATA_CONST.__objc_protorefs: 0xb0
   __DATA_CONST.__objc_superrefs: 0x14f8
   __DATA_CONST.__objc_arraydata: 0x12f0
   __DATA_CONST.__got: 0x39c8
-  __AUTH_CONST.__const: 0x8d58
-  __AUTH_CONST.__cfstring: 0x3b240
-  __AUTH_CONST.__objc_const: 0x83ba0
+  __AUTH_CONST.__const: 0x8d38
+  __AUTH_CONST.__cfstring: 0x3b2c0
+  __AUTH_CONST.__objc_const: 0x83be8
   __AUTH_CONST.__weak_auth_got: 0x20
   __AUTH_CONST.__objc_intobj: 0x3450
   __AUTH_CONST.__objc_arrayobj: 0x1098
   __AUTH_CONST.__objc_dictobj: 0xf0
   __AUTH_CONST.__objc_floatobj: 0x30
   __AUTH_CONST.__objc_doubleobj: 0x40
-  __AUTH_CONST.__auth_got: 0x21d8
+  __AUTH_CONST.__auth_got: 0x21e0
   __AUTH.__objc_data: 0x4008
   __AUTH.__data: 0x2178
   __DATA.__objc_ivar: 0x4aac

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 25705
-  Symbols:   46701
-  CStrings:  12400
+  Functions: 25714
+  Symbols:   46726
+  CStrings:  12407
 
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
+ ___block_descriptor_40_e49_v24?0"ATXFaceGalleryConfiguration"8"NSError"16l
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
- ___block_descriptor_32_e49_v24?0"ATXFaceGalleryConfiguration"8"NSError"16l
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
+ "error regenerating gallery for role %ld after process restart due to language change: %@"
+ "launchCountForBundleId"
+ "successfully regenerated gallery for role %ld after process restart due to language change"
- "%s: no section order provided in ambient asset parameters, or asset parameters missing!"
- "%s: using locale: %@"
- "%{public}s: Using empty internal state because loadInternalState failed (dataFromDisk is nil)"
- "%{public}s: Using empty internal state because loadInternalState failed (unarchiveErr %@, internalState %@)"
- "-[ATXFaceGalleryLayoutGenerator _ambientFaceGallerySectionsWithWidgetDescriptorsAdditionalData:aggregatedAppLaunchData:bundleIdToCompanionBundleId:ambientParameters:]"
- "FaceSuggestionAssetParametersAmbient"
- "error regenerating gallery after process restart due to language change: %@"
- "successfully regenerated gallery after process restart due to language change"
```
