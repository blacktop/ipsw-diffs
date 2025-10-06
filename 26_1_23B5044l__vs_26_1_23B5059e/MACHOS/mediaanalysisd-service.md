## mediaanalysisd-service

> `/System/Library/PrivateFrameworks/MediaAnalysis.framework/mediaanalysisd-service`

```diff

-375.6.1.0.0
-  __TEXT.__text: 0x1c0a24
-  __TEXT.__auth_stubs: 0x1f20
-  __TEXT.__objc_stubs: 0x14ba0
-  __TEXT.__objc_methlist: 0x9d28
-  __TEXT.__cstring: 0x10365
+375.8.1.11.1
+  __TEXT.__text: 0x1f0f3c
+  __TEXT.__auth_stubs: 0x1f50
+  __TEXT.__objc_stubs: 0x14d80
+  __TEXT.__objc_methlist: 0x9d70
+  __TEXT.__cstring: 0x12475
   __TEXT.__objc_classname: 0x1e57
-  __TEXT.__objc_methname: 0x1c1f4
-  __TEXT.__objc_methtype: 0x3a95
+  __TEXT.__objc_methname: 0x1c4f8
+  __TEXT.__objc_methtype: 0x3ad9
   __TEXT.__const: 0x6c2
-  __TEXT.__gcc_except_tab: 0x332c8
-  __TEXT.__oslogstring: 0x28c3c
+  __TEXT.__gcc_except_tab: 0x34c6c
+  __TEXT.__oslogstring: 0x29d3c
   __TEXT.__dlopen_cstrs: 0x2de
   __TEXT.__swift5_typeref: 0x2bb
   __TEXT.__swift5_reflstr: 0x93

   __TEXT.__swift5_capture: 0x48
   __TEXT.__swift_as_entry: 0x1c
   __TEXT.__swift_as_ret: 0x24
-  __TEXT.__unwind_info: 0x6af8
+  __TEXT.__unwind_info: 0x6e88
   __TEXT.__eh_frame: 0x498
-  __DATA_CONST.__auth_got: 0xfa8
+  __DATA_CONST.__auth_got: 0xfc0
   __DATA_CONST.__got: 0x16a8
   __DATA_CONST.__auth_ptr: 0x1b8
-  __DATA_CONST.__const: 0x6290
-  __DATA_CONST.__cfstring: 0xa5e0
+  __DATA_CONST.__const: 0x68e8
+  __DATA_CONST.__cfstring: 0xad40
   __DATA_CONST.__objc_classlist: 0x6e0
   __DATA_CONST.__objc_catlist: 0x50
   __DATA_CONST.__objc_protolist: 0xf0

   __DATA_CONST.__objc_arrayobj: 0x768
   __DATA_CONST.__objc_doubleobj: 0x20
   __DATA_CONST.__objc_dictobj: 0xa0
-  __DATA.__objc_const: 0x14028
-  __DATA.__objc_selrefs: 0x59a0
-  __DATA.__objc_ivar: 0x11b4
+  __DATA.__objc_const: 0x14048
+  __DATA.__objc_selrefs: 0x5a10
+  __DATA.__objc_ivar: 0x11b8
   __DATA.__objc_data: 0x45e0
-  __DATA.__data: 0xee8
-  __DATA.__bss: 0x960
+  __DATA.__data: 0xf40
+  __DATA.__bss: 0xac0
   __DATA.__common: 0x8
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/Accelerate.framework/Accelerate

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 50AE7C28-C993-3E00-85B2-809DE3569E98
-  Functions: 4459
-  Symbols:   1298
-  CStrings:  10689
+  UUID: DC4F8E30-5A2A-3782-B0DF-A9285D8C128C
+  Functions: 5418
+  Symbols:   1301
+  CStrings:  10999
 
Symbols:
+ _MADBumpEmbeddingVersionInFullAnalysisResults
+ _VCPMADGetReadableMemoryUsageInformation
+ _puts
CStrings:
+ "\nUsage:\n\t-f,--full-interval   Interval to schedule full background analysis at (seconds)\n\t-h,--help            Display this usage information and exit\n"
+ "%@ --> rejected person %@"
+ "%@ Add face %@ (%lu)"
+ "%@ Adding FaceOnly to Gallery"
+ "%@ Adding FaceTorso to Gallery"
+ "%@ Adding TorsoOnly to Gallery"
+ "%@ Adding observation without valid print"
+ "%@ Bumping image embedding v%d->v%d to avoid reprocessing"
+ "%@ Bumping video embedding v%d->v%d to avoid reprocessing"
+ "%@ Client FaceCrop %@"
+ "%@ Client asset %@"
+ "%@ Deleting unverified person %@ (%@)"
+ "%@ Directly set v2 to MACD"
+ "%@ Entity to update %ld"
+ "%@ Face %@ confirms graph verified person %@"
+ "%@ Face %@ confirms user verified person %@"
+ "%@ Face %@ rejects %lu persons"
+ "%@ Face %@ rejects person %@"
+ "%@ Failed fetching from VSK database - %@"
+ "%@ Failed to fetch processed image assets: %@\n"
+ "%@ Failed to fetch processed video assets: %@\n"
+ "%@ Failed to migrate image assets"
+ "%@ Failed to migrate video assets"
+ "%@ Failed to publish VSKAssets - %@"
+ "%@ Fetched %lu assets for migrating Image Embeddings"
+ "%@ Fetched %lu assets for migrating Video Embeddings"
+ "%@ Gallery indexed FaceCrop %@"
+ "%@ Gallery indexed asset %@"
+ "%@ Latest bookmark from VU %@"
+ "%@ Migrating Image Embeddings from %d -> %d"
+ "%@ Migrating Video Embeddings from %d -> %d"
+ "%@ Migrating database to v2 for photo library %@"
+ "%@ No face for observation %@"
+ "%@ Orphan training face %@"
+ "%@ Person not in Photos DB (should be according to bookmark %@)"
+ "%@ Person not in Photos DB (should be according to bookmark) from bookmark %@ to bookmark %@"
+ "%@ Photos post-capture processing"
+ "%@ Setting v2 to MACD"
+ "%@ Start migrating %lu assets ..."
+ "%@ Unexpected person update with %lu VU observations, %lu in PhotosDB from bookmark %@ to bookmark %@"
+ "%@ Will merge person %@(%@)(VerifyType-%ld) to person %@(%@)(VerifyType-%ld)"
+ "%@ changeBookmark changed from query %@ to store %@"
+ "%@ failed to encode changeBookmark %@"
+ "%@ failed to encode currentChangeBookmark %@"
+ "%@ failed to encode previousChangeBookmark %@"
+ "%@ missing: %@"
+ "%@[%@] Asset imageEmbeddingVersion %d does not meet expected version %d; ignore"
+ "%@[%@] Asset videoEmbeddingVersion %d does not meet expected version %d; ignore"
+ "%@[%@] Bumping Photos version"
+ "%@[%@] Failed to package new attributes; ignore"
+ "%@[%@] No matching asset; ignore"
+ "%lu %@"
+ "%lu-day scheduling history (%lu records) for background activity %@:"
+ "(Forced) "
+ "--full-interval"
+ "--help"
+ "-f"
+ "-h"
+ "./Utilities/CGUtilities.h"
+ "/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/Daemon/Background/Contacts/MADContactsPersonProcessingTask.mm"
+ "/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/Daemon/Background/Home/MADHomePersonProcessingTask.mm"
+ "/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/Daemon/Background/MADPhotosFaceAssetProcessingTask.mm"
+ "/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/Daemon/Background/MADPhotosFullAssetProcessingTask.mm"
+ "/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/Daemon/Background/MADPhotosOCRAssetProcessingTask.mm"
+ "/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/Daemon/Background/MADPhotosPersonProcessingTask.mm"
+ "/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/Daemon/Background/MADPhotosTaskProvider.m"
+ "/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/Daemon/Background/MADPhotosVisualSearchAssetProcessingTask.mm"
+ "/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/Daemon/HomeKit/VCPHomeKitAnalysisServiceTask.mm"
+ "/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/Daemon/MADPreheatingTask.mm"
+ "/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/Daemon/MADVUUtilities.m"
+ "/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/Daemon/MADVectorDatabaseUtilities.mm"
+ "/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/Daemon/MediaAnalysisDaemon.mm"
+ "/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/Daemon/Moments/MADMomentsDeferredProcessingTask.mm"
+ "/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/Daemon/Photos/MADBiome.m"
+ "/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/Daemon/Photos/MADFullAnalysisResultsSynchronizationTask.mm"
+ "/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/Daemon/Photos/MADFullAssetBatch.m"
+ "/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/Daemon/Photos/MADPhotosBackupAnalysisTask.mm"
+ "/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/Daemon/Photos/MADPhotosBackupProcessingTask.mm"
+ "/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/Daemon/Photos/MADPhotosDatabaseMigrationProcessingTask.mm"
+ "/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/Daemon/Photos/MADPhotosLibraryRestoreTask.mm"
+ "/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/Daemon/Photos/MADPhotosRestoreAnalysisTask.mm"
+ "/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/Daemon/Photos/MADPhotosTelemetryProcessingTask.mm"
+ "/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/Daemon/Photos/MADProgressManager.mm"
+ "/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/Daemon/Photos/MediaAnalysisServiceTask.mm"
+ "/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/Daemon/Photos/NSInputStream+VCPRestore.mm"
+ "/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/Daemon/Photos/PHAssetResourceManager+InMemoryDownload.m"
+ "/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/Daemon/Photos/PHPhotoLibrary+MediaAnalysisDaemonAnalysisMigration.m"
+ "/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/Daemon/Photos/VCPAssetAnalysisTask.mm"
+ "/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/Daemon/Photos/VCPAssetMaintenanceTask.mm"
+ "/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/Daemon/Photos/VCPBackgroundProcessingMetrics.mm"
+ "/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/Daemon/Photos/VCPBackupEntryHeader.mm"
+ "/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/Daemon/Photos/VCPBackupFileHeader.mm"
+ "/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/Daemon/Photos/VCPBatchAnalysisTask.mm"
+ "/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/Daemon/Photos/VCPDataCollectionTask.mm"
+ "/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/Daemon/Photos/VCPDatabaseManager.m"
+ "/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/Daemon/Photos/VCPEditAnalysisTask.mm"
+ "/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/Daemon/Photos/VCPEffectsAssetProcessingTask.mm"
+ "/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/Daemon/Photos/VCPFaceAssetProcessingTask.mm"
+ "/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/Daemon/Photos/VCPFaceLibraryProcessingTask.mm"
+ "/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/Daemon/Photos/VCPFaceProcessingTask.mm"
+ "/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/Daemon/Photos/VCPFailedAssetAnalysisTask.mm"
+ "/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/Daemon/Photos/VCPMADFullAssetProcessingTask.mm"
+ "/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/Daemon/Photos/VCPMADOCRAssetBatch.mm"
+ "/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/Daemon/Photos/VCPMADPECAssetBatch.mm"
+ "/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/Daemon/Photos/VCPMADPECLibraryProcessingTask.mm"
+ "/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/Daemon/Photos/VCPMADPECSingleRequestProcessingTask.mm"
+ "/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/Daemon/Photos/VCPMADPhotoAssetProcessingTask.m"
+ "/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/Daemon/Photos/VCPMADPhotosFetchProcessingTask.m"
+ "/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/Daemon/Photos/VCPMADPhotosLibraryProcessingTask.mm"
+ "/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/Daemon/Photos/VCPMADPhotosProcessingTask.m"
+ "/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/Daemon/Photos/VCPMADQuickFaceIDAssetBatch.mm"
+ "/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/Daemon/Photos/VCPMADSceneAssetBatch.mm"
+ "/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/Daemon/Photos/VCPMADSceneLibraryProcessingTask.mm"
+ "/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/Daemon/Photos/VCPMADVisualSearchAssetBatch.mm"
+ "/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/Daemon/Photos/VCPMediaTypeAnalysisTask.mm"
+ "/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/Daemon/Photos/VCPPausedAnalysis.mm"
+ "/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/Daemon/Photos/VCPPhotosAssetChangeManager.mm"
+ "/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/Daemon/Photos/VCPPhotosAssetProcessingTask.m"
+ "/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/Daemon/Photos/VCPPhotosCaptureProcessingTask.mm"
+ "/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/Daemon/Photos/VCPPhotosCoreAnalytics.mm"
+ "/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/Daemon/Photos/VCPPhotosFaceIdentificationTask.m"
+ "/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/Daemon/Photos/VCPPhotosMaintenanceProcessingTask.mm"
+ "/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/Daemon/Photos/VCPRestoreDatabaseTask.mm"
+ "/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/Daemon/Photos/VCPResumePausedAnalysisTask.mm"
+ "/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/Daemon/Photos/VCPSystemMonitor.mm"
+ "/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/Daemon/Photos/VCPUnifiedFullAnalysisTask.mm"
+ "/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/Daemon/Spotlight/MADSpotlightImageProcessingTask.mm"
+ "/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/Daemon/Spotlight/MADSpotlightMovieProcessingTask.mm"
+ "/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/Daemon/VCPCompoundMADTask.mm"
+ "/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/Service/VCPMADRemoteActivityTask.mm"
+ "All the Photos BGST activities disabled via defaults"
+ "AllowStreaming"
+ "AutoCounter "
+ "BlurExposureRotationConcurrentQueueCount"
+ "CollectionShared"
+ "ConcurrentAssetCountFullImage"
+ "ConcurrentAssetCountFullLivePhoto"
+ "ConcurrentAssetCountFullVideo"
+ "ConcurrentFaceAnalysis"
+ "ConcurrentPreAnalysis"
+ "DAS cancellation %s via default"
+ "Dis"
+ "DisableAllBGSTForPhotosProcessing"
+ "DisablePhotosPostCaptureProcessing"
+ "DisablePreheatActivity"
+ "Disabling"
+ "En"
+ "EnableLegacyAssetResultPersistence"
+ "EnablePerFrameHomeKitAnalysis"
+ "EnableRemoteActivity"
+ "Enabling"
+ "Error: This option is currently unsupported."
+ "FaceAnalysisConcurrentQueueCount"
+ "FaceClustering "
+ "FaceCropProcessing "
+ "FaceDetection "
+ "FaceProcessingConcurrentQueueCount"
+ "FaceStagingConcurrency"
+ "ForceInitialScanNoResource"
+ "FrequentProgressReporting"
+ "IgnoreDASCancellation"
+ "JITCameraFaceOnly"
+ "Legacy persistence is %@ for Asset and Result tables for validation purpose"
+ "MigrationDelete"
+ "MomentsGracePeriod"
+ "MomentsPriority"
+ "No scheduling history for background activity %@ in database"
+ "NoResultStrip"
+ "ParseConcurrentAssetCount"
+ "Per client scheduled request limit set to %d"
+ "PerClientScheduledRequestLimit"
+ "Persist full-range signals %@"
+ "PersistFullRangeSignals"
+ "PersonBuilding "
+ "PersonPromoting "
+ "ProcessCapturedFace"
+ "QuickFaceID "
+ "Remote DAS activity %s via default"
+ "Runtime assert for database writer is %@ via defaults"
+ "RuntimeAssertForDatabaseWriter"
+ "SceneNetConcurrentQueueCount"
+ "SceneProcessing "
+ "Unknown option \"%@\" specified"
+ "Unknown priority %@, default to Maintenance"
+ "Utility"
+ "Watchdog disabled"
+ "WatchdogTimeoutSeconds"
+ "[%@] %sabled via user defaults"
+ "[%@] Concurrent asset count set via defaults (%d)"
+ "[%@][MACD] Failed to update MA DB: %@"
+ "[%@][MACD] Failed to update Photos DB: %@"
+ "[%@][PhotosCapture] Persisting matching face %@ with person %@"
+ "[%@][PhotosCapture] Persisting unrecognized face %@"
+ "[CoreAnalyticManager] %@ %@ days with since Version %llu created %@"
+ "[CoreAnalyticManager] %@ invalid taskID %lu (%@); ignore"
+ "[CoreAnalyticManager] %@: invalid allowed assets count %lu; ignore"
+ "[CoreAnalyticManager] %@: invalid progress %lu%%; ignore"
+ "[FaceCrop] Processed %lu facecrop for person %@"
+ "[FaceLibraryProcessing] Running with: "
+ "[LOG_ERROR] %s[%d]: code %d\n"
+ "[MACDMigration] Deleting legacy while migrating is allowed"
+ "[MACDMigration] Deleting legacy while migrating is disabled"
+ "[MACDMigration] Failed to migrate to v2 MACD"
+ "[MACDMigration] Failed to rebuild VSKDB"
+ "[MACDMigration] Failed to update database version to v2"
+ "[MACDMigration][ImageEmbedding][v%d->v%d]"
+ "[MACDMigration][VSKEmbedding][v%lu->v%lu][%lu]"
+ "[MACDMigration][VideoEmbedding][v%d->v%d]"
+ "[MACDMigration|v2]"
+ "[MAClientHandler] Completed reportMADUserSafetyPolicy"
+ "[MAClientHandler] Starting reportMADUserSafetyPolicy, type: %u"
+ "[MAClientHandler] Starting subscribeUserSafety"
+ "[MAClientHandler] Successfully subscribed for MADUserSafetyPolicy"
+ "[MAClientHandler] Updated user safety scanning policy (%@)"
+ "[MAClientHandler] already subscribed for MADUserSafetyPolicy"
+ "[MADServicePublic] Starting subscribeUserSafety"
+ "[MADServicePublic] already subscribed for MADUserSafetyPolicy"
+ "[Perf] Memory usage before running the first task: %@"
+ "[Perf] Memory usage on finishing all scheduled tasks: %@"
+ "[Perf] Memory usage: %@"
+ "[Preheat] Activity disabled via defaults"
+ "[QuickFaceID][%@] Persisting matching face %@ with person %@"
+ "[QuickFaceID][%@] Persisting unrecognized face %@"
+ "[Scene] Defaults to fail initial scan with no resource"
+ "[VisualSearch] Concurrent asset count set via default (%d)"
+ "_bumpImageEmbeddingVersionWithAssetBatch:fromImageEmbeddingVersion:fromUnifiedEmbeddingVersion:toImageEmbeddingVersion:toUnifiedEmbeddingVersion:photoLibrary:"
+ "_bumpVectorDatabaseVersionWithLocalIdentifiers:embeddingType:fromUnifiedEmbeddingVersion:toUnifiedEmbeddingVersion:updatedLocalIdentifiers:photoLibrary:"
+ "_bumpVideoEmbeddingVersionWithAssetBatch:fromVideoEmbeddingVersion:fromUnifiedEmbeddingVersion:toVideoEmbeddingVersion:toUnifiedEmbeddingVersion:photoLibrary:"
+ "_memoryUsageMonitor"
+ "_migrateDatabaseToV2ForPhotoLibrary:"
+ "base64EncodedStringWithOptions:"
+ "disabled"
+ "displayName"
+ "faceTorsoprint"
+ "i56@0:8@16i24Q28i36Q40@48"
+ "i64@0:8@16Q24Q32Q40@48@56"
+ "mad_embeddingVersion"
+ "mad_isShared"
+ "mad_updateAssetWithEmbeddingVersion:"
+ "parseCommandLine:argv:"
+ "printUsageAndExitWith:andMessage:"
+ "setImageEmbeddingAsset:"
+ "setVideoEmbeddingAsset:"
+ "stringWithCString:encoding:"
+ "v24@?0@\"NSUUID\"8^B16"
+ "v24@?0@\"VUWGalleryEntityIdentifier\"8^B16"
+ "v24@?0@8^B16"
+ "v28@0:8i16r^*20"
+ "v32@?0@\"NSNumber\"8@\"NSMutableSet\"16^B24"
- "isCloudSharedAsset"

```
