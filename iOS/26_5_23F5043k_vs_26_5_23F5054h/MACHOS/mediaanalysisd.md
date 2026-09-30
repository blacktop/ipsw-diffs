## mediaanalysisd

> `filesystem/System/Library/PrivateFrameworks/MediaAnalysis.framework/mediaanalysisd`

```diff

-405.0.1.0.0
-  __TEXT.__text: 0x203d9c
-  __TEXT.__auth_stubs: 0x2350
-  __TEXT.__objc_stubs: 0x15780
-  __TEXT.__objc_methlist: 0xa2e8
-  __TEXT.__gcc_except_tab: 0x3615c
-  __TEXT.__cstring: 0x13945
+405.2.1.0.0
+  __TEXT.__text: 0x1e0c54
+  __TEXT.__auth_stubs: 0x2330
+  __TEXT.__objc_stubs: 0x156a0
+  __TEXT.__objc_methlist: 0xa2d0
+  __TEXT.__gcc_except_tab: 0x34e20
+  __TEXT.__cstring: 0x10675
   __TEXT.__const: 0x950
-  __TEXT.__objc_methname: 0x1d20b
+  __TEXT.__objc_methname: 0x1d17b
   __TEXT.__objc_classname: 0x2097
-  __TEXT.__objc_methtype: 0x3d72
-  __TEXT.__oslogstring: 0x2adac
+  __TEXT.__objc_methtype: 0x3d62
+  __TEXT.__oslogstring: 0x2a38c
   __TEXT.__dlopen_cstrs: 0x2de
   __TEXT.__swift5_typeref: 0x397
   __TEXT.__constg_swiftt: 0x31c

   __TEXT.__swift5_assocty: 0x30
   __TEXT.__swift5_builtin: 0x28
   __TEXT.__swift5_proto: 0x20
-  __TEXT.__unwind_info: 0x76f8
+  __TEXT.__unwind_info: 0x7338
   __TEXT.__eh_frame: 0x7d8
-  __DATA_CONST.__auth_got: 0x11c0
+  __DATA_CONST.__auth_got: 0x11b0
   __DATA_CONST.__got: 0x17e0
   __DATA_CONST.__auth_ptr: 0x228
-  __DATA_CONST.__const: 0x6b38
-  __DATA_CONST.__cfstring: 0xb000
+  __DATA_CONST.__const: 0x65f8
+  __DATA_CONST.__cfstring: 0xa980
   __DATA_CONST.__objc_classlist: 0x730
   __DATA_CONST.__objc_catlist: 0x50
   __DATA_CONST.__objc_protolist: 0xf0

   __DATA_CONST.__objc_arrayobj: 0x798
   __DATA_CONST.__objc_doubleobj: 0x20
   __DATA_CONST.__objc_dictobj: 0xa0
-  __DATA.__objc_const: 0x14d50
-  __DATA.__objc_selrefs: 0x5cb8
-  __DATA.__objc_ivar: 0x1270
+  __DATA.__objc_const: 0x14d30
+  __DATA.__objc_selrefs: 0x5c88
+  __DATA.__objc_ivar: 0x126c
   __DATA.__objc_data: 0x4b50
-  __DATA.__data: 0x1070
-  __DATA.__bss: 0xb50
+  __DATA.__data: 0x1018
+  __DATA.__bss: 0xa10
   __DATA.__common: 0x28
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/Accelerate.framework/Accelerate

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 88F4F5E6-F555-3FF8-B9E9-8EBB7E794167
-  Functions: 5754
-  Symbols:   1415
-  CStrings:  11287
+  UUID: AADCB97F-D0E9-3602-B37C-29793037FEB5
+  Functions: 4735
+  Symbols:   1413
+  CStrings:  11038
 
Symbols:
- _VCPMADGetReadableMemoryUsageInformation
- _puts
CStrings:
- "\nUsage:\n\t-f,--full-interval   Interval to schedule full background analysis at (seconds)\n\t-h,--help            Display this usage information and exit\n"
- "%@ --> rejected person %@"
- "%@ Add face %@ (%lu)"
- "%@ Adding FaceOnly to Gallery"
- "%@ Adding FaceTorso to Gallery"
- "%@ Adding TorsoOnly to Gallery"
- "%@ Adding observation without valid print"
- "%@ Client FaceCrop %@"
- "%@ Client asset %@"
- "%@ Deleting unverified person %@ (%@)"
- "%@ Entity to update %ld"
- "%@ Face %@ confirms graph verified person %@"
- "%@ Face %@ confirms user verified person %@"
- "%@ Face %@ rejects %lu persons"
- "%@ Face %@ rejects person %@"
- "%@ Gallery indexed FaceCrop %@"
- "%@ Gallery indexed asset %@"
- "%@ Latest bookmark from VU %@"
- "%@ No face for observation %@"
- "%@ Orphan training face %@"
- "%@ Person not in Photos DB (should be according to bookmark %@)"
- "%@ Person not in Photos DB (should be according to bookmark) from bookmark %@ to bookmark %@"
- "%@ Photos post-capture processing"
- "%@ Unexpected person update with %lu VU observations, %lu in PhotosDB from bookmark %@ to bookmark %@"
- "%@ Will merge person %@(%@)(VerifyType-%ld) to person %@(%@)(VerifyType-%ld)"
- "%@ changeBookmark changed from query %@ to store %@"
- "%@ failed to encode changeBookmark %@"
- "%@ failed to encode currentChangeBookmark %@"
- "%@ failed to encode previousChangeBookmark %@"
- "%@ missing: %@"
- "%lu %@"
- "%lu-day scheduling history (%lu records) for background activity %@:"
- "(Forced) "
- "--full-interval"
- "--help"
- "-f"
- "-h"
- "./Utilities/CGUtilities.h"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/MediaAnalysis/Daemon/Background/Contacts/MADContactsPersonProcessingTask.mm"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/MediaAnalysis/Daemon/Background/Home/MADHomePersonProcessingTask.mm"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/MediaAnalysis/Daemon/Background/MADPhotosFaceAssetProcessingTask.mm"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/MediaAnalysis/Daemon/Background/MADPhotosFullAssetProcessingTask.mm"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/MediaAnalysis/Daemon/Background/MADPhotosOCRAssetProcessingTask.mm"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/MediaAnalysis/Daemon/Background/MADPhotosPersonProcessingTask.mm"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/MediaAnalysis/Daemon/Background/MADPhotosTaskProvider.m"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/MediaAnalysis/Daemon/Background/MADPhotosVisualSearchAssetProcessingTask.mm"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/MediaAnalysis/Daemon/HomeKit/VCPHomeKitAnalysisServiceTask.mm"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/MediaAnalysis/Daemon/MADPreheatingTask.mm"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/MediaAnalysis/Daemon/MADVUUtilities.m"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/MediaAnalysis/Daemon/MADVectorDatabaseUtilities.mm"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/MediaAnalysis/Daemon/MediaAnalysisDaemon.mm"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/MediaAnalysis/Daemon/Moments/MADMomentsDeferredProcessingTask.mm"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/MediaAnalysis/Daemon/Photos/MADBiome.m"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/MediaAnalysis/Daemon/Photos/MADFullAnalysisResultsSynchronizationTask.mm"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/MediaAnalysis/Daemon/Photos/MADFullAssetBatch.m"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/MediaAnalysis/Daemon/Photos/MADPhotosBackupAnalysisTask.mm"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/MediaAnalysis/Daemon/Photos/MADPhotosBackupProcessingTask.mm"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/MediaAnalysis/Daemon/Photos/MADPhotosDatabaseMigrationProcessingTask.mm"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/MediaAnalysis/Daemon/Photos/MADPhotosLibraryRestoreTask.mm"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/MediaAnalysis/Daemon/Photos/MADPhotosRestoreAnalysisTask.mm"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/MediaAnalysis/Daemon/Photos/MADPhotosTelemetryProcessingTask.mm"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/MediaAnalysis/Daemon/Photos/MADProgressManager.mm"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/MediaAnalysis/Daemon/Photos/MADTUAssetBatch.mm"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/MediaAnalysis/Daemon/Photos/MADTULibraryProcessingTask.mm"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/MediaAnalysis/Daemon/Photos/MediaAnalysisServiceTask.mm"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/MediaAnalysis/Daemon/Photos/NSInputStream+VCPRestore.mm"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/MediaAnalysis/Daemon/Photos/PHAssetResourceManager+InMemoryDownload.m"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/MediaAnalysis/Daemon/Photos/PHPhotoLibrary+MediaAnalysisDaemonAnalysisMigration.m"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/MediaAnalysis/Daemon/Photos/VCPAssetAnalysisTask.mm"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/MediaAnalysis/Daemon/Photos/VCPAssetMaintenanceTask.mm"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/MediaAnalysis/Daemon/Photos/VCPBackgroundProcessingMetrics.mm"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/MediaAnalysis/Daemon/Photos/VCPBackupEntryHeader.mm"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/MediaAnalysis/Daemon/Photos/VCPBackupFileHeader.mm"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/MediaAnalysis/Daemon/Photos/VCPBatchAnalysisTask.mm"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/MediaAnalysis/Daemon/Photos/VCPDataCollectionTask.mm"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/MediaAnalysis/Daemon/Photos/VCPDatabaseManager.m"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/MediaAnalysis/Daemon/Photos/VCPEditAnalysisTask.mm"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/MediaAnalysis/Daemon/Photos/VCPEffectsAssetProcessingTask.mm"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/MediaAnalysis/Daemon/Photos/VCPFaceAssetProcessingTask.mm"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/MediaAnalysis/Daemon/Photos/VCPFaceLibraryProcessingTask.mm"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/MediaAnalysis/Daemon/Photos/VCPFaceProcessingTask.mm"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/MediaAnalysis/Daemon/Photos/VCPFailedAssetAnalysisTask.mm"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/MediaAnalysis/Daemon/Photos/VCPMADFullAssetProcessingTask.mm"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/MediaAnalysis/Daemon/Photos/VCPMADOCRAssetBatch.mm"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/MediaAnalysis/Daemon/Photos/VCPMADPECAssetBatch.mm"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/MediaAnalysis/Daemon/Photos/VCPMADPECLibraryProcessingTask.mm"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/MediaAnalysis/Daemon/Photos/VCPMADPECSingleRequestProcessingTask.mm"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/MediaAnalysis/Daemon/Photos/VCPMADPhotoAssetProcessingTask.m"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/MediaAnalysis/Daemon/Photos/VCPMADPhotosFetchProcessingTask.m"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/MediaAnalysis/Daemon/Photos/VCPMADPhotosLibraryProcessingTask.mm"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/MediaAnalysis/Daemon/Photos/VCPMADPhotosProcessingTask.m"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/MediaAnalysis/Daemon/Photos/VCPMADQuickFaceIDAssetBatch.mm"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/MediaAnalysis/Daemon/Photos/VCPMADSceneAssetBatch.mm"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/MediaAnalysis/Daemon/Photos/VCPMADSceneLibraryProcessingTask.mm"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/MediaAnalysis/Daemon/Photos/VCPMADVisualSearchAssetBatch.mm"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/MediaAnalysis/Daemon/Photos/VCPMediaTypeAnalysisTask.mm"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/MediaAnalysis/Daemon/Photos/VCPPausedAnalysis.mm"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/MediaAnalysis/Daemon/Photos/VCPPhotosAssetChangeManager.mm"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/MediaAnalysis/Daemon/Photos/VCPPhotosAssetProcessingTask.m"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/MediaAnalysis/Daemon/Photos/VCPPhotosCaptureProcessingTask.mm"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/MediaAnalysis/Daemon/Photos/VCPPhotosCoreAnalytics.mm"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/MediaAnalysis/Daemon/Photos/VCPPhotosFaceIdentificationTask.m"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/MediaAnalysis/Daemon/Photos/VCPPhotosMaintenanceProcessingTask.mm"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/MediaAnalysis/Daemon/Photos/VCPRestoreDatabaseTask.mm"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/MediaAnalysis/Daemon/Photos/VCPResumePausedAnalysisTask.mm"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/MediaAnalysis/Daemon/Photos/VCPSystemMonitor.mm"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/MediaAnalysis/Daemon/Photos/VCPUnifiedFullAnalysisTask.mm"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/MediaAnalysis/Daemon/Spotlight/MADSpotlightImageProcessingTask.mm"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/MediaAnalysis/Daemon/Spotlight/MADSpotlightMovieProcessingTask.mm"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/MediaAnalysis/Daemon/VCPCompoundMADTask.mm"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/MediaAnalysis/Service/VCPMADRemoteActivityTask.mm"
- "AllowStreaming"
- "AutoCounter "
- "BlurExposureRotationConcurrentQueueCount"
- "ConcurrentAssetCountFullImage"
- "ConcurrentAssetCountFullLivePhoto"
- "ConcurrentAssetCountFullVideo"
- "ConcurrentFaceAnalysis"
- "ConcurrentPreAnalysis"
- "DAS cancellation %s via default"
- "DisablePhotosPostCaptureProcessing"
- "Disabling"
- "EnableLegacyAssetResultPersistence"
- "EnablePerFrameHomeKitAnalysis"
- "EnableRemoteActivity"
- "Enabling"
- "Error: This option is currently unsupported."
- "FaceAnalysisConcurrentQueueCount"
- "FaceClustering "
- "FaceCropProcessing "
- "FaceDetection "
- "FaceProcessingConcurrentQueueCount"
- "FaceStagingConcurrency"
- "ForceInitialScanNoResource"
- "FrequentProgressReporting"
- "IgnoreDASCancellation"
- "JITCameraFaceOnly"
- "Legacy persistence is %@ for Asset and Result tables for validation purpose"
- "MigrationDelete"
- "MomentsGracePeriod"
- "MomentsPriority"
- "No scheduling history for background activity %@ in database"
- "NoResultStrip"
- "ParseConcurrentAssetCount"
- "Per client scheduled request limit set to %d"
- "PerClientScheduledRequestLimit"
- "Persist full-range signals %@"
- "PersistFullRangeSignals"
- "PersonBuilding "
- "PersonPromoting "
- "ProcessCapturedFace"
- "QuickFaceID "
- "Remote DAS activity %s via default"
- "Runtime assert for database writer is %@ via defaults"
- "RuntimeAssertForDatabaseWriter"
- "SceneNetConcurrentQueueCount"
- "SceneProcessing "
- "Unknown option \"%@\" specified"
- "Unknown priority %@, default to Maintenance"
- "Utility"
- "Watchdog disabled"
- "WatchdogTimeoutSeconds"
- "[%@] Concurrent asset count set via defaults (%d)"
- "[%@][PhotosCapture] Persisting matching face %@ with person %@"
- "[%@][PhotosCapture] Persisting unrecognized face %@"
- "[CoreAnalyticManager] %@ %@ days with since Version %llu created %@"
- "[CoreAnalyticManager] %@ invalid taskID %lu (%@); ignore"
- "[CoreAnalyticManager] %@: invalid allowed assets count %lu; ignore"
- "[CoreAnalyticManager] %@: invalid progress %lu%%; ignore"
- "[FaceCrop] Processed %lu facecrop for person %@"
- "[FaceLibraryProcessing] Running with: "
- "[LOG_ERROR] %s[%d]: code %d\n"
- "[MACDMigration] Deleting legacy while migrating is allowed"
- "[MACDMigration] Deleting legacy while migrating is disabled"
- "[Perf] Memory usage before running the first task: %@"
- "[Perf] Memory usage on finishing all scheduled tasks: %@"
- "[Perf] Memory usage: %@"
- "[QuickFaceID][%@] Persisting matching face %@ with person %@"
- "[QuickFaceID][%@] Persisting unrecognized face %@"
- "[Scene] Defaults to fail initial scan with no resource"
- "[VisualSearch] Concurrent asset count set via default (%d)"
- "_memoryUsageMonitor"
- "base64EncodedStringWithOptions:"
- "disabled"
- "displayName"
- "faceTorsoprint"
- "parseCommandLine:argv:"
- "printUsageAndExitWith:andMessage:"
- "stringWithCString:encoding:"
- "v24@?0@\"NSUUID\"8^B16"
- "v24@?0@\"VUWGalleryEntityIdentifier\"8^B16"
- "v24@?0@8^B16"
- "v28@0:8i16r^*20"
- "v32@?0@\"NSNumber\"8@\"NSMutableSet\"16^B24"

```
