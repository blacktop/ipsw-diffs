## mediaanalysisd-service

> `/System/Library/PrivateFrameworks/MediaAnalysis.framework/mediaanalysisd-service`

```diff

-305.10.3.0.0
-  __TEXT.__text: 0x1aea44
+305.13.7.0.0
+  __TEXT.__text: 0x1b4c70
   __TEXT.__auth_stubs: 0x1120
-  __TEXT.__objc_stubs: 0x130c0
-  __TEXT.__objc_methlist: 0x9150
-  __TEXT.__cstring: 0x156bf
+  __TEXT.__objc_stubs: 0x132a0
+  __TEXT.__objc_methlist: 0x9160
+  __TEXT.__cstring: 0x15e76
   __TEXT.__objc_classname: 0x1bf4
-  __TEXT.__objc_methname: 0x1a222
-  __TEXT.__objc_methtype: 0x37e1
-  __TEXT.__const: 0x4a0
-  __TEXT.__gcc_except_tab: 0x32f04
-  __TEXT.__oslogstring: 0x2267e
+  __TEXT.__objc_methname: 0x1a7df
+  __TEXT.__objc_methtype: 0x37dc
+  __TEXT.__const: 0x4b0
+  __TEXT.__gcc_except_tab: 0x33490
+  __TEXT.__oslogstring: 0x2294c
   __TEXT.__dlopen_cstrs: 0x60a
-  __TEXT.__unwind_info: 0x6008
+  __TEXT.__unwind_info: 0x60c8
   __DATA_CONST.__auth_got: 0x8a8
-  __DATA_CONST.__got: 0xde0
-  __DATA_CONST.__const: 0x6450
-  __DATA_CONST.__cfstring: 0xe2e0
+  __DATA_CONST.__got: 0xe10
+  __DATA_CONST.__const: 0x6788
+  __DATA_CONST.__cfstring: 0xeea0
   __DATA_CONST.__objc_classlist: 0x660
   __DATA_CONST.__objc_catlist: 0x48
   __DATA_CONST.__objc_protolist: 0xd0

   __DATA_CONST.__objc_protorefs: 0x80
   __DATA_CONST.__objc_classrefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x4f8
-  __DATA_CONST.__objc_intobj: 0x23b8
-  __DATA_CONST.__objc_arraydata: 0x7f8
-  __DATA_CONST.__objc_arrayobj: 0x5d0
+  __DATA_CONST.__objc_intobj: 0x23e8
+  __DATA_CONST.__objc_arraydata: 0x9c8
+  __DATA_CONST.__objc_arrayobj: 0x678
   __DATA_CONST.__objc_doubleobj: 0xd0
-  __DATA_CONST.__objc_dictobj: 0x28
+  __DATA_CONST.__objc_dictobj: 0x50
   __DATA.__objc_const: 0x12dc0
-  __DATA.__objc_selrefs: 0x5270
+  __DATA.__objc_selrefs: 0x52e8
   __DATA.__objc_ivar: 0x1108
   __DATA.__objc_data: 0x3fc0
   __DATA.__data: 0xa70
-  __DATA.__bss: 0x6c0
+  __DATA.__bss: 0x6d0
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/Contacts.framework/Contacts

   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 4777
-  Symbols:   729
-  CStrings:  9313
+  Functions: 4831
+  Symbols:   735
+  CStrings:  9439
 
Symbols:
+ _OBJC_CLASS_$_BMMediaAnalysisPerAsset
+ _OBJC_CLASS_$_BMMediaAnalysisPerLibrary
+ _PHMediaProcessingAssetCountLivePhotoKey
+ _PHMediaProcessingAssetCountStillImageKey
+ _VCPMediaAnalyzerOption_AllowOnDemand
+ _VCPMediaAnalyzerOption_MetadataWithHighlight
CStrings:
+ "%@ Expected faceID for face result but none found %@"
+ "%@ Failed to call MediaAnalyzer on asset, skipping"
+ "%@ Failed to get total assets breakdown count from Photos (%@)"
+ "-[VCPDatabaseWriter(ProcessingStatus) queryAssetCountForTaskID:minimumAttempts:]"
+ "/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/Daemon/Photos/MADBiome.m"
+ "00"
+ "0E"
+ "1C"
+ "2A"
+ "38"
+ "46"
+ "54"
+ "62"
+ "70"
+ "7E"
+ "8C"
+ "9A"
+ "@96@0:8@16Q24Q32Q40B48@52Q60B68@72@80@88"
+ "A8"
+ "B6"
+ "Biome per-asset bucket report failed with error %d"
+ "Biome per-library report failed with error %d"
+ "C4"
+ "CloudShared"
+ "D2"
+ "DaysToComplete50SinceOSUpdate"
+ "DaysToComplete50WithFails"
+ "DaysToComplete50WithFailsSinceOSUpdate"
+ "DaysToComplete90SinceOSUpdate"
+ "DaysToComplete90WithFails"
+ "DaysToComplete90WithFailsSinceOSUpdate"
+ "DaysToComplete99SinceOSUpdate"
+ "DaysToComplete99WithFails"
+ "DaysToComplete99WithFailsSinceOSUpdate"
+ "E0"
+ "EE"
+ "Error(%d) during per-asset biome report for asset %@"
+ "Error(%d) during per-library biome report for lib %@"
+ "FaceAnalysisOSMajorOfLastVersionUpdate"
+ "FaceAnalysisOSMinorOfLastVersionUpdate"
+ "FullImageAnalysisOSMajorOfLastVersionUpdate"
+ "FullImageAnalysisOSMinorOfLastVersionUpdate"
+ "LastPerAssetBiomeReportBucket"
+ "LastPerAssetBiomeReportEndTimestamp"
+ "LastPerAssetBiomeReportStartTimestamp"
+ "LastPerLibraryBiomeReportEndTimestamp"
+ "LastPerLibraryBiomeReportStartTimestamp"
+ "MediaAnalysisOSMajorOfLastVersionUpdate"
+ "MediaAnalysisOSMinorOfLastVersionUpdate"
+ "NA"
+ "OCRAnalysisOSMajorOfLastVersionUpdate"
+ "OCRAnalysisOSMinorOfLastVersionUpdate"
+ "OSMajorOfLastVersionUpdate"
+ "OSMinorOfLastVersionUpdate"
+ "PECAnalysisOSMajorOfLastVersionUpdate"
+ "PECAnalysisOSMinorOfLastVersionUpdate"
+ "PerAsset"
+ "PerLibrary"
+ "SELECT count(*) FROM ProcessingStatus WHERE taskID=(?) AND attempts>=(?);"
+ "SceneAnalysisOSMajorOfLastVersionUpdate"
+ "SceneAnalysisOSMinorOfLastVersionUpdate"
+ "SystemPhotoLibrary"
+ "UserLibrary"
+ "VideoAnalysis"
+ "VisualSearchAnalysisOSMajorOfLastVersionUpdate"
+ "VisualSearchAnalysisOSMinorOfLastVersionUpdate"
+ "ZZ"
+ "[Biome][PerAssetReport]"
+ "[Biome][PerLibraryReport]"
+ "[VCPDatabaseWriter] Failed to remove checkpoint_with_sticky_failure timestamp for %@"
+ "[VCPDatabaseWriter] Failed to remove complete_with_sticky_failure timestamp for %@"
+ "[VCPDatabaseWriter] Failed to set major os version of analysis version update %lld for %@"
+ "[VCPDatabaseWriter] Failed to set minor os version of analysis version update %lld for %@"
+ "_calculateCompleteDateWithEvent:progress:taskID:checkpoint:featureAvailableCheck:database:completeThreshold:withStickyFailure:checkpointTimestampKey:currentDate:startDate:"
+ "_prepareBGSTCheckpointWithEvent:taskID:checkpoint:featureAvailableCheck:database:checkpointTimestampKey:currentDate:"
+ "beach"
+ "bungee"
+ "camping"
+ "canyon"
+ "cat"
+ "cave"
+ "celestial_body"
+ "checkpointWithStickyFailureTimestampQueryKey"
+ "cityscape"
+ "cliff"
+ "countOfAssetsByMediaTypeForMediaProcessingTaskID:processed:algorithmVersion:error:"
+ "countStickyFailedQueryKey"
+ "desert"
+ "dog"
+ "fetchPersonsInAsset:options:"
+ "fishing"
+ "forest"
+ "glacier"
+ "hamster"
+ "hiking"
+ "hill"
+ "iTunesSynced"
+ "initWithContentType:shootingCategory:shootingMode:duration:highlightCount:highlightDuration:temporalFaceCount:temporalSceneCount:containNamedPerson:containNamedPet:containNatureOrNaturalLandmarks:containSkyline:containLandmarks:containAction:containHighMotion:containAudioTypes:atFavoritedLocation:durationOriginal:highlightCountOriginal:highlightDurationOriginal:temporalFaceCountOriginal:temporalSceneCountOriginal:"
+ "initWithLibraryType:imageAssetCount:livePhotoAssetCount:movieAssetCount:movieAssetDurations:editedMovieCount:sharedMovieCount:favoritedMovieCount:spatialMoviePercentage:cinematicMoviePercentage:slomoMoviePercentage:timelapsePercentage:portraitModePercentage:landscapeModePercentage:withHighlightsPercentage:withPeoplePercentage:withPetsPercentage:withNatureOrNaturalLandmarksPercentage:withSkylinePercentage:wthLandmarksPercentage:withActionPercentage:withHighMotionPercentage:highlightsWithPeoplePercentage:highlightsWithPetsPercentage:highlightsWithNatureOrNaturalLandmarksPercentage:highlightsWithSkylinePercentage:highlightsWithLandmarksPercentage:highlightsWithActionPercentage:highlightsWithHighMotionPercentage:"
+ "isCloudSharedAsset"
+ "isFavorite"
+ "isIndexed"
+ "isMediaSubtype:"
+ "island"
+ "landmarks"
+ "mountain"
+ "nature"
+ "people"
+ "performance"
+ "pets"
+ "progressPercentageWithStickyFailureQueryKey"
+ "queryAssetCountForTaskID:minimumAttempts:"
+ "requestAnalysis:forAssets:withOptions:andProgressHandler:andError:"
+ "sharedMediaAnalyzer"
+ "shore"
+ "skating"
+ "skydiving"
+ "skyline"
+ "sport"
+ "sticky-failed"
+ "timescale"
+ "uuid >= %s AND uuid < %s"
+ "v32@?0@\"NSString\"8@\"NSArray\"16^B24"
+ "v32@?0@\"PHPerson\"8Q16^B24"
+ "v40@?0@\"NSDate\"8q16^q24^q32"
+ "v68@0:8@16Q24Q32B40@44@52@60"
+ "value"
+ "vcp_isVideoTimelapse"
+ "volcano"
+ "water_body"
- "@100@0:8@16Q24Q32Q40B48@52@60Q68@76@84@92"
- "_calculateCompleteDateWithEvent:progress:taskID:checkpoint:featureAvailableCheck:database:completeTimestampKey:completeThreshold:checkpointTimestampKey:currentDate:startDate:"
- "_prepareBGSTCheckpointWithEvent:taskID:checkpoint:featureAvailableCheck:database:databaseModified:checkpointTimestampKey:currentDate:"
- "countFailedQueryKey"
- "v76@0:8@16Q24Q32B40@44^B52@60@68"

```
