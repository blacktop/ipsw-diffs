## PhotoLibraryServices

> `/System/Library/PrivateFrameworks/PhotoLibraryServices.framework/PhotoLibraryServices`

```diff

-710.22.200.0.0
-  __TEXT.__text: 0x6862d4
+712.0.160.0.0
+  __TEXT.__text: 0x686a08
   __TEXT.__auth_stubs: 0x3f00
   __TEXT.__delay_stubs: 0x2c
   __TEXT.__delay_helper: 0xa4
-  __TEXT.__objc_methlist: 0x3a17c
-  __TEXT.__const: 0x5c50
-  __TEXT.__gcc_except_tab: 0x22030
-  __TEXT.__oslogstring: 0x76874
-  __TEXT.__cstring: 0x5feea
+  __TEXT.__objc_methlist: 0x3a1d4
+  __TEXT.__const: 0x5cc8
+  __TEXT.__gcc_except_tab: 0x22044
+  __TEXT.__oslogstring: 0x769d3
+  __TEXT.__cstring: 0x5ff40
   __TEXT.__ustring: 0x582
   __TEXT.__dlopen_cstrs: 0xa03
-  __TEXT.__unwind_info: 0x14028
-  __TEXT.__objc_classname: 0x9a30
-  __TEXT.__objc_methname: 0xb92bf
-  __TEXT.__objc_methtype: 0x11d5b
-  __TEXT.__objc_stubs: 0x75f20
-  __DATA_CONST.__got: 0x4988
-  __DATA_CONST.__const: 0x146a8
-  __DATA_CONST.__objc_classlist: 0x2080
+  __TEXT.__unwind_info: 0x14050
+  __TEXT.__objc_classname: 0x9a4f
+  __TEXT.__objc_methname: 0xb9420
+  __TEXT.__objc_methtype: 0x11d7e
+  __TEXT.__objc_stubs: 0x76020
+  __DATA_CONST.__got: 0x4990
+  __DATA_CONST.__const: 0x146c0
+  __DATA_CONST.__objc_classlist: 0x2088
   __DATA_CONST.__objc_catlist: 0xf0
-  __DATA_CONST.__objc_protolist: 0x688
+  __DATA_CONST.__objc_protolist: 0x680
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x222f8
+  __DATA_CONST.__objc_selrefs: 0x22330
   __DATA_CONST.__objc_protorefs: 0x90
   __DATA_CONST.__objc_superrefs: 0x14f0
   __DATA_CONST.__objc_arraydata: 0x1968
   __AUTH_CONST.__auth_got: 0x1f98
   __AUTH_CONST.__auth_ptr: 0x8
-  __AUTH_CONST.__const: 0x5088
-  __AUTH_CONST.__cfstring: 0x4bd20
-  __AUTH_CONST.__objc_const: 0x71ee8
+  __AUTH_CONST.__const: 0x50a8
+  __AUTH_CONST.__cfstring: 0x4bd60
+  __AUTH_CONST.__objc_const: 0x71fe8
   __AUTH_CONST.__objc_intobj: 0x46e0
   __AUTH_CONST.__objc_arrayobj: 0x1248
   __AUTH_CONST.__objc_doubleobj: 0xf0
   __AUTH_CONST.__objc_dictobj: 0x348
   __AUTH_CONST.__objc_floatobj: 0x40
-  __AUTH.__objc_data: 0x11170
-  __DATA.__objc_ivar: 0x3b9c
-  __DATA.__data: 0x5eb0
+  __AUTH.__objc_data: 0x111c0
+  __DATA.__objc_ivar: 0x3ba0
+  __DATA.__data: 0x5e50
   __DATA.__crash_info: 0x40
   __DATA.__bss: 0x24f8
   __DATA.__common: 0xc

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 25474
-  Symbols:   31282
-  CStrings:  46603
+  Functions: 25484
+  Symbols:   31298
+  CStrings:  46622
 
Symbols:
+ _OBJC_CLASS_$_PLModelMigrationAction_ResetLastCompletePrefetchDate
+ _OBJC_METACLASS_$_PLModelMigrationAction_ResetLastCompletePrefetchDate
+ _PLFeatureAvailabilityJobDidFailKey
+ _PLPhotoAnalysisPhotoLibraryServiceExtendedCuratedAssetsOptionsFinalPassTimeInterval
+ _PLPhotoAnalysisPhotoLibraryServiceExtendedCuratedAssetsOptionsPerformFinalPass
+ _kPLFirstDateToConsiderForFrequentLocations
CStrings:
+ "\x01\x12\xb2"
+ "-[PLAssetsdLibraryInternalService failAvailabilityWithReply:]"
+ "-[PLGlobalValues setFeatureAvailabilityJobDidFail:]"
+ "@\"<CPLRecordComputeStateDelegate>\""
+ "FeatureAvailability - FailAvailability"
+ "FeatureAvailabilityJobDidFailKey"
+ "No photo library available to simulate  availability job failure"
+ "PLBackgroundJobFeatureAvailabilityWorker - Previous job failed (%!f(MISSING) seconds ago), throttling to avoid failure loop"
+ "PLBackgroundJobFeatureAvailabilityWorker - Previous job failed (%!f(MISSING) seconds ago), trying again"
+ "PLModelMigrationAction_ResetLastCompletePrefetchDate"
+ "ProcessFrequentLocationsWithSortedMoments"
+ "T@\"<CPLRecordComputeStateDelegate>\",W,N,V_recordComputeStateDelegate"
+ "[Badge Count] Changed application badge count from %!l(MISSING)u to %!l(MISSING)u"
+ "_failAvailabilityForPhotoLibrary:error:"
+ "_installOrUpdateExistingComputeSyncResourceToIndicateRemoteAvailabilityShouldRemoveLocalFile:error:"
+ "_recordComputeStateDelegate"
+ "_resetAllMediaProcessingVersionsIncludingVideo:"
+ "badgeNumber"
+ "failAvailabilityForPhotoLibrary:error:"
+ "failAvailabilityWithReply:"
+ "featureAvailabilityJobDidFail"
+ "finalPassTimeInterval"
+ "installSparseFullStageComputeSyncResourceIfNeeded"
+ "minimumSecondsBetweenJobs"
+ "performFinalPass"
+ "recordComputeStateDelegate"
+ "setFeatureAvailabilityJobDidFail:"
+ "\xb4"
- "\x01\x12\xa2"
- "\n\nAsset Information:\n"
- "\nAsset: uuid: %!@(MISSING), filename: %!@(MISSING), dateCreated: %!@(MISSING), location: %!@(MISSING), width: %!l(MISSING)ld, height: %!l(MISSING)ld, modificationDate: %!@(MISSING), reverseLocationDataIsValid: %!d(MISSING)"
- "PLDiagnosticsProvider"
- "diagnosticInformation"
- "installFullStageComputeSyncResourceIfNeeded"
- "installOrUpdateExistingComputeSyncResourceToIndicateRemoteAvailabilityWithError:"
- "supportsDiagnosticInformation"
- "\xb3"

```
