## mediaanalysisd-service

> `/System/Library/PrivateFrameworks/MediaAnalysis.framework/mediaanalysisd-service`

```diff

-305.14.1.0.0
-  __TEXT.__text: 0x1b4ca8
-  __TEXT.__auth_stubs: 0x1120
-  __TEXT.__objc_stubs: 0x132a0
-  __TEXT.__objc_methlist: 0x9160
-  __TEXT.__cstring: 0x15e76
-  __TEXT.__objc_classname: 0x1bf4
-  __TEXT.__objc_methname: 0x1a7df
-  __TEXT.__objc_methtype: 0x37dc
-  __TEXT.__const: 0x4b0
-  __TEXT.__gcc_except_tab: 0x33490
-  __TEXT.__oslogstring: 0x2294c
+305.15.1.0.0
+  __TEXT.__text: 0x188860
+  __TEXT.__auth_stubs: 0x1100
+  __TEXT.__objc_stubs: 0x131e0
+  __TEXT.__objc_methlist: 0x9148
+  __TEXT.__cstring: 0x13f6a
+  __TEXT.__objc_classname: 0x1bf1
+  __TEXT.__objc_methname: 0x1a75b
+  __TEXT.__objc_methtype: 0x37cc
+  __TEXT.__const: 0x4a8
+  __TEXT.__gcc_except_tab: 0x322c0
+  __TEXT.__oslogstring: 0x220f8
   __TEXT.__dlopen_cstrs: 0x60a
-  __TEXT.__unwind_info: 0x60c8
-  __DATA_CONST.__auth_got: 0x8a8
-  __DATA_CONST.__got: 0xe10
-  __DATA_CONST.__const: 0x6788
-  __DATA_CONST.__cfstring: 0xeea0
+  __TEXT.__unwind_info: 0x5db8
+  __DATA_CONST.__auth_got: 0x898
+  __DATA_CONST.__got: 0xe08
+  __DATA_CONST.__const: 0x62b8
+  __DATA_CONST.__cfstring: 0xe6e0
   __DATA_CONST.__objc_classlist: 0x660
   __DATA_CONST.__objc_catlist: 0x48
   __DATA_CONST.__objc_protolist: 0xd0

   __DATA_CONST.__objc_arrayobj: 0x678
   __DATA_CONST.__objc_doubleobj: 0xd0
   __DATA_CONST.__objc_dictobj: 0x50
-  __DATA.__objc_const: 0x12dc0
-  __DATA.__objc_selrefs: 0x52e8
-  __DATA.__objc_ivar: 0x1108
+  __DATA.__objc_const: 0x12da0
+  __DATA.__objc_selrefs: 0x52c0
+  __DATA.__objc_ivar: 0x1104
   __DATA.__objc_data: 0x3fc0
-  __DATA.__data: 0xa70
-  __DATA.__bss: 0x6d0
+  __DATA.__data: 0xa18
+  __DATA.__bss: 0x5a8
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/Contacts.framework/Contacts

   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 4831
-  Symbols:   735
-  CStrings:  9439
+  Functions: 3928
+  Symbols:   732
+  CStrings:  9247
 
Symbols:
- _mach_task_self_
- _puts
- _task_info
CStrings:
- "\x04\""
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
- "%@ Entity to update: %@"
- "%@ Face %@ confirms graph verified person %@"
- "%@ Face %@ confirms user verified person %@"
- "%@ Face %@ rejects %lu persons"
- "%@ Face %@ rejects person %@"
- "%@ Gallery indexed FaceCrop %@"
- "%@ Gallery indexed asset %@"
- "%@ Orphan training face %@"
- "%@ Person not in Photos DB (should be according to bookmark %@)"
- "%@ Photos post-capture processing"
- "%@ Will merge person %@(%@)(VerifyType-%ld) to person %@(%@)(VerifyType-%ld)"
- "%llu %@"
- "%lu %@"
- "%lu-day scheduling history (%lu records) for background activity %@:"
- "--full-interval"
- "--help"
- "-f"
- "-h"
- "./Utilities/CGUtilities.h"
- "/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/Daemon/Background/Contacts/MADContactsPersonProcessingTask.mm"
- "/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/Daemon/Background/Home/MADHomePersonProcessingTask.mm"
- "/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/Daemon/Background/MADPhotosFaceAssetProcessingTask.mm"
- "/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/Daemon/Background/MADPhotosFullAssetProcessingTask.mm"
- "/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/Daemon/Background/MADPhotosOCRAssetProcessingTask.mm"
- "/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/Daemon/Background/MADPhotosPersonProcessingTask.mm"
- "/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/Daemon/Background/MADPhotosTaskProvider.m"
- "/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/Daemon/Background/MADPhotosVisualSearchAssetProcessingTask.mm"
- "/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/Daemon/HomeKit/VCPHomeKitAnalysisServiceTask.mm"
- "/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/Daemon/MADGDUtilities.m"
- "/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/Daemon/MADPreheatBackgroundSystemTask.mm"
- "/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/Daemon/MADVectorDatabaseUtilities.mm"
- "/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/Daemon/MediaAnalysisDaemon.mm"
- "/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/Daemon/Moments/MADMomentsDeferredProcessingTask.mm"
- "/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/Daemon/Photos/MADBiome.m"
- "/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/Daemon/Photos/MADFullAnalysisResultsSynchronizationTask.mm"
- "/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/Daemon/Photos/MADPhotosBackupAnalysisTask.mm"
- "/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/Daemon/Photos/MADPhotosLibraryRestoreTask.mm"
- "/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/Daemon/Photos/MADPhotosRestoreAnalysisTask.mm"
- "/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/Daemon/Photos/MediaAnalysisServiceTask.mm"
- "/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/Daemon/Photos/NSInputStream+VCPRestore.mm"
- "/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/Daemon/Photos/PHAssetResourceManager+InMemoryDownload.m"
- "/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/Daemon/Photos/PHPhotoLibrary+MediaAnalysisDaemonAnalysisMigration.m"
- "/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/Daemon/Photos/VCPAssetAnalysisTask.mm"
- "/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/Daemon/Photos/VCPAssetMaintenanceTask.mm"
- "/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/Daemon/Photos/VCPBackgroundProcessingMetrics.mm"
- "/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/Daemon/Photos/VCPBackupEntryHeader.mm"
- "/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/Daemon/Photos/VCPBackupFileHeader.mm"
- "/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/Daemon/Photos/VCPBatchAnalysisTask.mm"
- "/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/Daemon/Photos/VCPDataCollectionTask.mm"
- "/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/Daemon/Photos/VCPEditAnalysisTask.mm"
- "/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/Daemon/Photos/VCPEffectsAssetProcessingTask.mm"
- "/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/Daemon/Photos/VCPFaceAssetProcessingTask.mm"
- "/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/Daemon/Photos/VCPFaceLibraryProcessingTask.mm"
- "/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/Daemon/Photos/VCPFaceProcessingTask.mm"
- "/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/Daemon/Photos/VCPFailedAssetAnalysisTask.mm"
- "/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/Daemon/Photos/VCPMADFullAssetProcessingTask.mm"
- "/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/Daemon/Photos/VCPMADOCRAssetBatch.mm"
- "/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/Daemon/Photos/VCPMADPECAssetBatch.mm"
- "/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/Daemon/Photos/VCPMADPECLibraryProcessingTask.mm"
- "/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/Daemon/Photos/VCPMADPECSingleRequestProcessingTask.mm"
- "/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/Daemon/Photos/VCPMADPhotoAssetProcessingTask.m"
- "/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/Daemon/Photos/VCPMADPhotosFetchProcessingTask.m"
- "/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/Daemon/Photos/VCPMADPhotosLibraryProcessingTask.mm"
- "/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/Daemon/Photos/VCPMADPhotosProcessingTask.m"
- "/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/Daemon/Photos/VCPMADQuickFaceIDAssetBatch.mm"
- "/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/Daemon/Photos/VCPMADSceneAssetBatch.mm"
- "/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/Daemon/Photos/VCPMADSceneLibraryProcessingTask.mm"
- "/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/Daemon/Photos/VCPMADVisualSearchAssetBatch.mm"
- "/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/Daemon/Photos/VCPMediaTypeAnalysisTask.mm"
- "/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/Daemon/Photos/VCPPausedAnalysis.mm"
- "/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/Daemon/Photos/VCPPhotosAssetChangeManager.mm"
- "/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/Daemon/Photos/VCPPhotosAssetProcessingTask.m"
- "/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/Daemon/Photos/VCPPhotosCaptureProcessingTask.mm"
- "/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/Daemon/Photos/VCPPhotosCoreAnalytics.mm"
- "/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/Daemon/Photos/VCPPhotosFaceIdentificationTask.m"
- "/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/Daemon/Photos/VCPPhotosMaintenanceProcessingTask.mm"
- "/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/Daemon/Photos/VCPRestoreDatabaseTask.mm"
- "/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/Daemon/Photos/VCPResumePausedAnalysisTask.mm"
- "/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/Daemon/Photos/VCPSubsampledAnalysisTask.mm"
- "/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/Daemon/Photos/VCPSystemMonitor.mm"
- "/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/Daemon/Photos/VCPUnifiedFullAnalysisTask.mm"
- "/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/Daemon/Spotlight/MADSpotlightImageProcessingTask.mm"
- "/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/Daemon/Spotlight/MADSpotlightMovieProcessingTask.mm"
- "/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/Daemon/VCPCompoundMADTask.mm"
- "/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/Service/VCPMADRemoteActivityTask.mm"
- "All the Photos BGST activities disabled via defaults"
- "AllowStreaming"
- "AutoCounter "
- "BlurExposureRotationConcurrentQueueCount"
- "Bytes"
- "ConcurrentAssetCountFullImage"
- "ConcurrentAssetCountFullLivePhoto"
- "ConcurrentAssetCountFullVideo"
- "ConcurrentFaceAnalysis"
- "ConcurrentPreAnalysis"
- "DAS cancellation %s via default"
- "Defaults override person face VIP matching threshold: %f"
- "Dis"
- "DisableAllBGSTForPhotosProcessing"
- "DisablePhotosPostCaptureProcessing"
- "DisablePreheatActivity"
- "Disabling"
- "En"
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
- "Failed to get memory information"
- "FrequentProgressReporting"
- "GB"
- "IgnoreDASCancellation"
- "JITCameraFaceOnly"
- "KB"
- "MB"
- "MomentsGracePeriod"
- "MomentsPriority"
- "No scheduling history for background activity %@ in database"
- "NoResultStrip"
- "PB"
- "ParseConcurrentAssetCount"
- "Per client scheduled request limit set to %d"
- "PerClientScheduledRequestLimit"
- "Persist full-range signals %@"
- "PersistFullRangeSignals"
- "PersonBuilding "
- "PersonFaceVIPMatchingThreshold"
- "PersonPromoting "
- "ProcessCapturedFace"
- "QuickFaceID "
- "Remote DAS activity %s via default"
- "SceneNetConcurrentQueueCount"
- "SceneProcessing "
- "TB"
- "UnifiedBackgroundProcessing"
- "Unknown option \"%@\" specified"
- "Unknown priority %@, default to Maintenance"
- "Watchdog disabled"
- "WatchdogTimeoutSeconds"
- "[%@] %sabled via user defaults"
- "[%@] Concurrent asset count set via defaults (%d)"
- "[%@][PhotosCapture] Persisting matching face %@ with person %@"
- "[%@][PhotosCapture] Persisting unrecognized face %@"
- "[CoreAnalyticManager] %@ %@ days with since Version %llu created %@"
- "[CoreAnalyticManager] %@ invalid taskID %lu (%@); ignore"
- "[CoreAnalyticManager] %@: invalid allowed assets count %lu; ignore"
- "[CoreAnalyticManager] %@: invalid progress %lu%%; ignore"
- "[DAS QoS] Memory usage after %@ block: %@"
- "[FaceCrop] Processed %lu facecrop for person %@"
- "[FaceLibraryProcessing] Running with: "
- "[LOG_ERROR] %s[%d]: code %d\n"
- "[Override] Unified background processing %s"
- "[Perf] Memory usage before running the first task: %@"
- "[Perf] Memory usage on finishing all scheduled tasks: %@"
- "[Perf] Memory usage: %@"
- "[Preheat] Activity disabled via defaults"
- "[QuickFaceID][%@] Persisting matching face %@ with person %@"
- "[QuickFaceID][%@] Persisting unrecognized face %@"
- "[VisualSearch] Concurrent asset count set via default (%d)"
- "_memoryUsageMonitor"
- "checkpointWithFailureTimestampQueryKey"
- "disabled"
- "displayName"
- "faceTorsoprint"
- "parseCommandLine:argv:"
- "printUsageAndExitWith:andMessage:"
- "progressPercentageWithFailureQueryKey"
- "resident: %@, virtual: %@, phys_footprint: %@, phys_footprint_peak: %@."
- "resident: N/A, virtual: N/A, phys_footprint: N/A, phys_footprint_peak: N/A."
- "stringWithCString:encoding:"
- "v24@?0@\"NSUUID\"8^B16"
- "v28@0:8i16r^*20"

```
