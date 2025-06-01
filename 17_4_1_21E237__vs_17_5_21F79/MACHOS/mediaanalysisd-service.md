## mediaanalysisd-service

> `/System/Library/PrivateFrameworks/MediaAnalysis.framework/mediaanalysisd-service`

```diff

-215.7.1.0.0
-  __TEXT.__text: 0xef3c4
-  __TEXT.__auth_stubs: 0x1240
-  __TEXT.__objc_stubs: 0xe360
-  __TEXT.__objc_methlist: 0x6448
-  __TEXT.__cstring: 0xaa9a
-  __TEXT.__gcc_except_tab: 0x16ef4
+225.1.1.0.0
+  __TEXT.__text: 0xf0064
+  __TEXT.__auth_stubs: 0x1250
+  __TEXT.__objc_stubs: 0xe3c0
+  __TEXT.__objc_methlist: 0x6450
+  __TEXT.__cstring: 0xab09
+  __TEXT.__gcc_except_tab: 0x16fb8
   __TEXT.__const: 0x228
-  __TEXT.__oslogstring: 0x136a5
+  __TEXT.__oslogstring: 0x139ed
   __TEXT.__objc_classname: 0x159b
-  __TEXT.__objc_methname: 0x127fd
-  __TEXT.__objc_methtype: 0x2ab2
+  __TEXT.__objc_methname: 0x12879
+  __TEXT.__objc_methtype: 0x2ab8
   __TEXT.__dlopen_cstrs: 0x501
-  __TEXT.__unwind_info: 0x4264
+  __TEXT.__unwind_info: 0x4274
   __TEXT.__eh_frame: 0x38
-  __DATA_CONST.__auth_got: 0x938
-  __DATA_CONST.__got: 0x7b8
-  __DATA_CONST.__const: 0x42a8
-  __DATA_CONST.__cfstring: 0x5cc0
+  __DATA_CONST.__auth_got: 0x940
+  __DATA_CONST.__got: 0x7e0
+  __DATA_CONST.__const: 0x4308
+  __DATA_CONST.__cfstring: 0x5d60
   __DATA_CONST.__objc_classlist: 0x518
   __DATA_CONST.__objc_catlist: 0x48
   __DATA_CONST.__objc_protolist: 0xb0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x60
-  __DATA_CONST.__objc_classrefs: 0xa38
+  __DATA_CONST.__objc_classrefs: 0xa40
   __DATA_CONST.__objc_superrefs: 0x410
   __DATA_CONST.__objc_intobj: 0xb40
-  __DATA_CONST.__objc_arraydata: 0x470
-  __DATA_CONST.__objc_arrayobj: 0x360
+  __DATA_CONST.__objc_arraydata: 0x498
+  __DATA_CONST.__objc_arrayobj: 0x378
   __DATA_CONST.__objc_doubleobj: 0x10
   __DATA_CONST.__objc_floatobj: 0x10
   __DATA.__objc_const: 0xfa28
-  __DATA.__objc_selrefs: 0x3c90
+  __DATA.__objc_selrefs: 0x3ca8
   __DATA.__objc_ivar: 0xd0c
   __DATA.__objc_data: 0x32f0
   __DATA.__data: 0x850

   - /System/Library/Frameworks/Vision.framework/Vision
   - /System/Library/PrivateFrameworks/AXMediaUtilities.framework/AXMediaUtilities
   - /System/Library/PrivateFrameworks/AggregateDictionary.framework/AggregateDictionary
+  - /System/Library/PrivateFrameworks/BackgroundSystemTasks.framework/BackgroundSystemTasks
   - /System/Library/PrivateFrameworks/BiomeLibrary.framework/BiomeLibrary
   - /System/Library/PrivateFrameworks/BiomeStreams.framework/BiomeStreams
   - /System/Library/PrivateFrameworks/CloudPhotoLibrary.framework/CloudPhotoLibrary

   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: 2143F863-6C52-3BCD-9987-3F0D6A211DF1
-  Functions: 2839
-  Symbols:   738
-  CStrings:  6628
+  UUID: A5446B15-4965-3A09-8085-00C97A417EF5
+  Functions: 2841
+  Symbols:   745
+  CStrings:  6653
 
Symbols:
+ _BGSystemTaskCustomCheckpointMax
+ _BGSystemTaskCustomCheckpointMin
+ _MajorOSVersionNumberKey
+ _MinorOSVersionNumberKey
+ _OBJC_CLASS_$_BGSystemTaskCheckpoints
+ _VCPBGSTCheckpointTimestampKeyForTask
+ _VCPKeyValuePrioritizedFaceCheckpointReportedTimestamp
CStrings:
+ "@80@0:8Q16Q24@32@40@48@56@64@72"
+ "MADTaskIdentifierForBackgroundTask: Unsupported analysis type %lu"
+ "No corresponding checkpoint key found for taskID %lu"
+ "[%@] Failed to report BGST Custom Checkpoint %lu for taskIdentifier %@. Error: %@"
+ "[%@] MADBGCheckpoint %lu is not within range [%lu, %lu]"
+ "[%@] Reported BGST Custom Checkpoint %lu for task taskIdentifier %@"
+ "[%@] checkpoint reported on %@ (timestamp: %lld)"
+ "[%@] taskIdentifier not found"
+ "[VCPDatabaseWriter] Failed to check/update OS version"
+ "[VCPDatabaseWriter] Failed to query major os version for %@"
+ "[VCPDatabaseWriter] Failed to query minor os version for %@"
+ "[VCPDatabaseWriter] Failed to remove checkpoint timestamp for %@"
+ "[VCPDatabaseWriter] Failed to set major os version for %@"
+ "[VCPDatabaseWriter] Failed to set minor os version for %@"
+ "[VCPDatabaseWriter] Operating System version changed from %lld.%lld to %lld.%lld"
+ "_getCompleteDateBasedOn:forTaskID:fromDatabase:withCompleteTimestampKey:checkpointTimestampKey:coreAnalyticsEventKey:currentDate:andStartDate:"
+ "_updateOperatingSystemVersion"
+ "checkpointReportedTimestampQueryKey"
+ "com.apple.mediaanalysisd.photos.full"
+ "com.apple.mediaanalysisd.photos.scene"
+ "operatingSystemVersion"
+ "reportCustomCheckpoint:forTask:error:"
- "@64@0:8Q16@24@32@40@48@56"
- "_getCompleteDateBasedOn:fromDatabase:withCompleteTimestampKey:coreAnalyticsEventKey:currentDate:andStartDate:"

```
