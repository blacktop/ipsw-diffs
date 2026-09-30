## mediaanalysisd

> `/System/Library/PrivateFrameworks/MediaAnalysis.framework/mediaanalysisd`

```diff

-290.11.2.0.0
-  __TEXT.__text: 0x19e7cc
-  __TEXT.__auth_stubs: 0x1110
-  __TEXT.__objc_stubs: 0x12960
-  __TEXT.__objc_methlist: 0x84ec
-  __TEXT.__gcc_except_tab: 0x2fe08
-  __TEXT.__cstring: 0x15085
+290.13.1.2.0
+  __TEXT.__text: 0x173940
+  __TEXT.__auth_stubs: 0x1100
+  __TEXT.__objc_stubs: 0x128e0
+  __TEXT.__objc_methlist: 0x84d4
+  __TEXT.__gcc_except_tab: 0x2ed38
+  __TEXT.__cstring: 0x13271
   __TEXT.__objc_classname: 0x1bd1
-  __TEXT.__objc_methname: 0x19317
-  __TEXT.__objc_methtype: 0x36de
-  __TEXT.__const: 0x4a0
-  __TEXT.__oslogstring: 0x1fe58
+  __TEXT.__objc_methname: 0x192fd
+  __TEXT.__objc_methtype: 0x36ce
+  __TEXT.__const: 0x498
+  __TEXT.__oslogstring: 0x1f5f1
   __TEXT.__dlopen_cstrs: 0x60a
-  __TEXT.__unwind_info: 0x5ce0
-  __DATA_CONST.__auth_got: 0x8a0
+  __TEXT.__unwind_info: 0x5a28
+  __DATA_CONST.__auth_got: 0x898
   __DATA_CONST.__got: 0xdc0
-  __DATA_CONST.__const: 0x6080
-  __DATA_CONST.__cfstring: 0xdf40
+  __DATA_CONST.__const: 0x5c10
+  __DATA_CONST.__cfstring: 0xd7e0
   __DATA_CONST.__objc_classlist: 0x658
   __DATA_CONST.__objc_catlist: 0x48
   __DATA_CONST.__objc_protolist: 0xd0

   __DATA_CONST.__objc_arrayobj: 0x5b8
   __DATA_CONST.__objc_doubleobj: 0xd0
   __DATA_CONST.__objc_dictobj: 0x28
-  __DATA.__objc_const: 0x13a50
-  __DATA.__objc_selrefs: 0x4fa8
-  __DATA.__objc_ivar: 0x1094
+  __DATA.__objc_const: 0x13a10
+  __DATA.__objc_selrefs: 0x4f90
+  __DATA.__objc_ivar: 0x108c
   __DATA.__objc_data: 0x3f70
-  __DATA.__data: 0xa68
-  __DATA.__bss: 0x6a0
+  __DATA.__data: 0xa10
+  __DATA.__bss: 0x578
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/Contacts.framework/Contacts

   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 4680
-  Symbols:   724
-  CStrings:  9003
+  Functions: 3811
+  Symbols:   723
+  CStrings:  8818
 
Symbols:
+ _MediaAnalysisInsertMissingResultsFromDegradedAnalysis
+ _OBJC_CLASS_$_VCPSharedImageBackboneAnalyzer
- _mach_task_self_
- _puts
- _task_info
CStrings:
+ "\x03\x13\x11\x19"
+ "\x04!"
+ "    Existing analysis version up-to-date but missing %@; Update missing GM additional analysis only from new degraded analysis"
+ "Preheating canceled or timed out after %d/%d seconds"
+ "Preheating for %d/%d seconds"
+ "[FullCluster] (not disrupting) Failed to build vector database - %@"
+ "rebuildWithForce:cancelBlock:extendTimeoutBlock:error:"
+ "sharedAnalyzerWithRevision:"
+ "vcp_fullAnalysisGenerativeModelAdditionalTypes"
- "\x03\x13\x11\x1a"
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
- "%@ Failed to build VSKDB"
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
- "/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/Daemon/MediaAnalysisDaemon.mm"
- "/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/Daemon/Moments/MADMomentsDeferredProcessingTask.mm"
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
- "/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/Daemon/Photos/VCPMADFullAssetProcessingTask.m"
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
- "/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/Daemon/Photos/VCPSubsampledAnalysisTask.m"
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
- "Preheating canceled or timed out after %d/%d minutes"
- "Preheating for %d/%d minutes"
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
- "[CoreAnalyticManager] %@ days with %lld schedules since Database creation date %@"
- "[CoreAnalyticManager] %@ days with %lld schedules since Version creation date %@"
- "[CoreAnalyticManager] %@ invalid taskID %lu (%@); ignore"
- "[CoreAnalyticManager] %@: invalid allowed assets count %lu; ignore"
- "[CoreAnalyticManager] %@: invalid progress %lu%%; ignore"
- "[DAS QoS] Memory usage after %@ block: %@"
- "[FaceLibraryProcessing] Running with: "
- "[FullCluster] Continue gallery update with failed vector database rebuild"
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
- "disabled"
- "displayName"
- "faceTorsoprint"
- "parseCommandLine:argv:"
- "printUsageAndExitWith:andMessage:"
- "rebuildWithError:force:"
- "resident: %@, virtual: %@, phys_footprint: %@, phys_footprint_peak: %@."
- "resident: N/A, virtual: N/A, phys_footprint: N/A, phys_footprint_peak: N/A."
- "stringWithCString:encoding:"
- "v24@?0@\"NSUUID\"8^B16"
- "v28@0:8i16r^*20"

```
