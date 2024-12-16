## mediaanalysisd-service

> `/System/Library/PrivateFrameworks/MediaAnalysis.framework/mediaanalysisd-service`

```diff

-290.13.1.3.0
-  __TEXT.__text: 0x173894
+300.5.2.0.0
+  __TEXT.__text: 0x174fc0
   __TEXT.__auth_stubs: 0x1100
-  __TEXT.__objc_stubs: 0x128e0
-  __TEXT.__objc_methlist: 0x84d4
-  __TEXT.__cstring: 0x13271
+  __TEXT.__objc_stubs: 0x12980
+  __TEXT.__objc_methlist: 0x8524
+  __TEXT.__cstring: 0x13482
   __TEXT.__objc_classname: 0x1bd1
-  __TEXT.__objc_methname: 0x192fd
-  __TEXT.__objc_methtype: 0x36ce
+  __TEXT.__objc_methname: 0x194ad
+  __TEXT.__objc_methtype: 0x36df
   __TEXT.__const: 0x498
-  __TEXT.__gcc_except_tab: 0x2ed08
-  __TEXT.__oslogstring: 0x1f5f1
+  __TEXT.__gcc_except_tab: 0x2ef54
+  __TEXT.__oslogstring: 0x1f8b0
   __TEXT.__dlopen_cstrs: 0x60a
-  __TEXT.__unwind_info: 0x5a18
+  __TEXT.__unwind_info: 0x5a68
   __DATA_CONST.__auth_got: 0x898
   __DATA_CONST.__got: 0xdc0
-  __DATA_CONST.__const: 0x5bf0
-  __DATA_CONST.__cfstring: 0xd7e0
+  __DATA_CONST.__const: 0x5c38
+  __DATA_CONST.__cfstring: 0xda20
   __DATA_CONST.__objc_classlist: 0x658
   __DATA_CONST.__objc_catlist: 0x48
   __DATA_CONST.__objc_protolist: 0xd0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x80
   __DATA_CONST.__objc_classrefs: 0x10
-  __DATA_CONST.__objc_superrefs: 0x4e8
+  __DATA_CONST.__objc_superrefs: 0x4f0
   __DATA_CONST.__objc_intobj: 0x2370
   __DATA_CONST.__objc_arraydata: 0x7e8
   __DATA_CONST.__objc_arrayobj: 0x5b8
   __DATA_CONST.__objc_doubleobj: 0xd0
   __DATA_CONST.__objc_dictobj: 0x28
-  __DATA.__objc_const: 0x13a10
-  __DATA.__objc_selrefs: 0x4f90
-  __DATA.__objc_ivar: 0x108c
+  __DATA.__objc_const: 0x13ad8
+  __DATA.__objc_selrefs: 0x4fb8
+  __DATA.__objc_ivar: 0x10a4
   __DATA.__objc_data: 0x3f70
   __DATA.__data: 0xa10
-  __DATA.__bss: 0x578
+  __DATA.__bss: 0x588
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/Contacts.framework/Contacts

   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 3810
+  Functions: 3825
   Symbols:   723
-  CStrings:  8818
+  CStrings:  8858
 
CStrings:
+ "%@ Compute sync not supported for Photo Library; skipping backfill"
+ "%@ Failed to build VSKDB"
+ "%@ Failed to create PFClientSideEncryptionManager"
+ "%@ Failed to query VSK asset count: %@"
+ "%@ Failed to sync VSK database (non-fatal); Skipping - %@"
+ "%@ Failed to update vector database with %lu localIdentifiers: %@"
+ "%@ MAD database does not exist; Skipping ..."
+ "%@ MAD database does not exist; skipping backfill"
+ "%@ MADB not exist; Skipping ..."
+ "%@ Not System Photo Library; Skipping ..."
+ "%@ Not ready for analysis; Skipping ..."
+ "%@ Photo Library is not ready for analysis; Skipping ..."
+ "%@ Syndication library; Skipping ..."
+ "%@_Line%llu"
+ "Asset failed processing. Failure: %@"
+ "B40@0:8@16Q24@32"
+ "FaceAnalysisFailureDate"
+ "FaceProcessingFailureReportTime"
+ "FailedVideoDuration"
+ "FullAnalysisFailureDate"
+ "FullProcessingFailureReportTime"
+ "OCRAnalysisFailureDate"
+ "OCRProcessingFailureReportTime"
+ "PECAnalysisFailureDate"
+ "PECProcessingFailureReportTime"
+ "ProcessedVideoDuration"
+ "ProcessingFailure"
+ "SceneAnalysisFailureDate"
+ "SceneProcessingFailureReportTime"
+ "TotalVideoDuration"
+ "Unable to determine timestamp of last ABC failure report for task %u"
+ "VisualSearchAnalysisFailureDate"
+ "VisualSearchProcessingFailureReportTime"
+ "[FullCluster] (not disrupting) Failed to build vector database"
+ "[MADProgressManager] Video duration equal to 0, skipping reporting."
+ "[VCPAssetMaintenanceTask] Asset maintenance: nil %s at index %zu/%zu"
+ "[VCPAssetMaintenanceTask] Deleted asset detection/removal process failed"
+ "[VCPAssetMaintenanceTask] Failed to sync VSK database (non-fatal) - %@"
+ "[VCPAssetMaintenanceTask] Performing asset book-keeping..."
+ "[VCPAssetMaintenanceTask][%@] Asset found; recovering analysis"
+ "[VCPAssetMaintenanceTask][%@] Asset in trash; marking analysis for deletion"
+ "[VCPAssetMaintenanceTask][%@] Asset purged; removing analysis"
+ "[VCPAutoBugCapture] %@ processing failure report was rate-limited (Expected non-report)"
+ "[VCPAutoBugCapture] %@ processing failure was reported"
+ "[VCPAutoBugCapture] Asset failed processing. Asset: %@, signature: %@"
+ "[VCPAutoBugCapture] Failed to report %@ processing failure. reason: %d, signature: %@"
+ "[VCPAutoBugCapture] Last report for task %u was %@"
+ "[VCPAutoBugCapture] Unable to set date of last processing failure for task %u"
+ "[VCPPhotosMaintenanceProcessingTask] Failed during processing (%d)"
+ "[VCPPhotosMaintenanceProcessingTask][Backup][%@]"
+ "[VCPPhotosMaintenanceProcessingTask][CS][%@]"
+ "[VCPPhotosMaintenanceProcessingTask][Cluster][%@]"
+ "[VCPPhotosMaintenanceProcessingTask][VSKVideo][%@]"
+ "[VCPPhotosMaintenanceProcessingTask][VSK][%@]"
+ "captureProcessingFailure:taskID:asset:"
+ "processingFailureReportTimeForTask:"
+ "queryVideoTotalDuration:processedDuration:failedDuration:photoLibrary:taskID:cancelOrExtendTimeoutBlock:"
+ "rebuildWithForce:cancelBlock:extendTimeoutBlock:"
+ "setLastProcessingFailureReportTime:forTask:"
+ "sharedCapturer"
+ "videoDuration-failed"
+ "videoDuration-processed"
- "  [%@] Asset found; recovering analysis"
- "  [%@] Asset in trash; marking analysis for deletion"
- "  [%@] Asset purged; removing analysis"
- "%@ Failed to build VSKDB - %@"
- "%@ Failed to remove embeddings from VSKDB"
- "%@ Failed to update vector database with %lu localIdentifiers"
- "Asset maintenance: nil %s at index %zu/%zu"
- "Backup only supported for system Photo Library; skipping library (%@)"
- "Compute sync not supported for Photo Library (%@); skipping backfill"
- "Deleted asset detection/removal process failed"
- "Error maintaining library (%d); skip processing"
- "Failed to create PFClientSideEncryptionManager; backup failed"
- "MAD database does not exist, skip progress query"
- "MAD database does not exist; skipping backfill"
- "MAD database does not exist; skipping backup"
- "Performing asset book-keeping..."
- "Photo Library is not ready for analysis (%@); skipping backup"
- "Photo Library is not ready for analysis (%@); skipping vectorDB sync"
- "Photo Library is not ready for analysis (%@); skipping vectorEmbeddingVersion backfill"
- "Skip full clustering for syndication library"
- "[FullCluster] (not disrupting) Failed to build vector database - %@"
- "rebuildWithForce:cancelBlock:extendTimeoutBlock:error:"

```
