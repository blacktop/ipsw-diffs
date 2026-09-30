## CoreMedia

> `/System/Library/Frameworks/CoreMedia.framework/Versions/A/CoreMedia`

```diff

-3300.3.1.0.0
-  __TEXT.__text: 0x245284
+3300.4.1.0.0
+  __TEXT.__text: 0x2452a4
   __TEXT.__auth_stubs: 0x3090
   __TEXT.__objc_methlist: 0x318
   __TEXT.__const: 0x19b4
   __TEXT.__cstring: 0x4ffe8
-  __TEXT.__oslogstring: 0x27052
+  __TEXT.__oslogstring: 0x27049
   __TEXT.__dlopen_cstrs: 0x4f
   __TEXT.__unwind_info: 0x4788
   __TEXT.__eh_frame: 0x38

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libspindump.dylib
   - /usr/lib/libz.1.dylib
-  UUID: DC4EF7A4-0C22-3A12-AEAA-CA780507C886
+  UUID: 223BEF95-5D7F-3FBD-B760-99CD087F1374
   Functions: 9914
   Symbols:   15620
   CStrings:  15646
Functions:
~ _curll_getURLDispatch : 684 -> 712
~ _FigXPCConnectionCopyMemoryOriginForConnectedProcess : 488 -> 480
~ _FigXPCConnectionCopyMemoryRecipientForConnectedProcess : 580 -> 572
~ _FigMemoryOriginSetBlockBufferInIPCMessageData : 776 -> 796
CStrings:
+ "/AppleInternal/Library/BuildRoots/4~CGCxugBT9kz2KyA9HQuXrUyiMfAIBCG7QWz7H2o/Library/Caches/com.apple.xbs/Sources/CoreMedia_CoreMedia/Prototypes/Endpoint/FigEndpointManagerUtilities.c %s: Nothing to do"
+ "/AppleInternal/Library/BuildRoots/4~CGCxugBT9kz2KyA9HQuXrUyiMfAIBCG7QWz7H2o/Library/Caches/com.apple.xbs/Sources/CoreMedia_CoreMedia/Prototypes/IPC/FigOSEventLink.m"
+ "/AppleInternal/Library/BuildRoots/4~CGCxugBT9kz2KyA9HQuXrUyiMfAIBCG7QWz7H2o/Library/Caches/com.apple.xbs/Sources/CoreMedia_CoreMedia/Prototypes/Player/ClientServer/FigSampleBufferAtomSerialization.c"
+ "/AppleInternal/Library/BuildRoots/4~CGCxugBT9kz2KyA9HQuXrUyiMfAIBCG7QWz7H2o/Library/Caches/com.apple.xbs/Sources/CoreMedia_CoreMedia/Sources/Core/FigFormatDescription/FigMPEG4Bridge.c %s: iacb box has unknown codec_id %c%c%c%c"
+ "/AppleInternal/Library/BuildRoots/4~CGCxugBT9kz2KyA9HQuXrUyiMfAIBCG7QWz7H2o/Library/Caches/com.apple.xbs/Sources/CoreMedia_CoreMedia/Sources/Core/FigFormatDescription/FigVideoFormatDescription.c %s: PointCloud format description %p [ %c%c%c%c ] does not have a NumberOfPointsPerSample extension"
+ "/AppleInternal/Library/BuildRoots/4~CGCxugBT9kz2KyA9HQuXrUyiMfAIBCG7QWz7H2o/Library/Caches/com.apple.xbs/Sources/CoreMedia_CoreMedia/Sources/Core/FigFormatDescription/HapticDescriptionBridge.c %s: Warning: HapticFormatDescription has ignored a \"%@\" extension when converting to the sample description."
+ "/AppleInternal/Library/BuildRoots/4~CGCxugBT9kz2KyA9HQuXrUyiMfAIBCG7QWz7H2o/Library/Caches/com.apple.xbs/Sources/CoreMedia_CoreMedia/Sources/Core/FigFormatDescription/PointCloudDescriptionBridge.c %s: Warning: PointCloudFormatDescription has ignored a \"%@\" extension when converting to the sample description."
+ "/AppleInternal/Library/BuildRoots/4~CGCxugBT9kz2KyA9HQuXrUyiMfAIBCG7QWz7H2o/Library/Caches/com.apple.xbs/Sources/CoreMedia_CoreMedia/Sources/Core/FigFormatDescription/SceneDescriptionBridge.c %s: Warning: SceneFormatDescription has ignored a \"%@\" extension when converting to the sample description."
+ "/AppleInternal/Library/BuildRoots/4~CGCxugBT9kz2KyA9HQuXrUyiMfAIBCG7QWz7H2o/Library/Caches/com.apple.xbs/Sources/CoreMedia_CoreMedia/Sources/Core/FigNotificationCenter/FigNotificationCenterCF.c %s: %d weak listener%s registered"
+ "/AppleInternal/Library/BuildRoots/4~CGCxugBT9kz2KyA9HQuXrUyiMfAIBCG7QWz7H2o/Library/Caches/com.apple.xbs/Sources/CoreMedia_CoreMedia/Sources/Core/FigNotificationCenter/FigNotificationCenterCF.c %s: Will dump weak listener hashes on USR2 signals and in sysdiagnoses -- thank you for setting \"defaults write com.apple.coremedia weak_hash_dump -bool YES\""
+ "/AppleInternal/Library/BuildRoots/4~CGCxugBT9kz2KyA9HQuXrUyiMfAIBCG7QWz7H2o/Library/Caches/com.apple.xbs/Sources/CoreMedia_CoreMedia/Sources/Core/FigNotificationCenter/FigNotificationCenterCF.c %s: Will not use CF ObjC SPI to implement weak listeners -- thank you for setting \"defaults write com.apple.coremedia weak_avoid_cf_spi -bool YES\""
+ "/AppleInternal/Library/BuildRoots/4~CGCxugBT9kz2KyA9HQuXrUyiMfAIBCG7QWz7H2o/Library/Caches/com.apple.xbs/Sources/CoreMedia_CoreMedia/Sources/Core/FigNotificationCenter/FigNotificationCenterCF.c %s: hash %@ already registered -- suggests weak listener abandonment"
+ "/AppleInternal/Library/BuildRoots/4~CGCxugBT9kz2KyA9HQuXrUyiMfAIBCG7QWz7H2o/Library/Caches/com.apple.xbs/Sources/CoreMedia_CoreMedia/Sources/Core/FigNotificationCenter/FigNotificationCenterCF.c %s: hash %@ not found -- confirm parameters to FigNotificationCenterRemoveWeakListener are correct"
+ "/AppleInternal/Library/BuildRoots/4~CGCxugBT9kz2KyA9HQuXrUyiMfAIBCG7QWz7H2o/Library/Caches/com.apple.xbs/Sources/CoreMedia_CoreMedia/Sources/Core/FigSync/FigHostTimeClock.c %s: Singleton FigHostTimeClock was overreleased"
+ "/AppleInternal/Library/BuildRoots/4~CGCxugBT9kz2KyA9HQuXrUyiMfAIBCG7QWz7H2o/Library/Caches/com.apple.xbs/Sources/CoreMedia_CoreMedia/Sources/Platform/Darwin/DarwinDebug.c %s: %s to log URLs -- thank you for setting \"defaults write com.apple.coremedia logurls -bool %s\""
+ "/AppleInternal/Library/BuildRoots/4~CGCxugBT9kz2KyA9HQuXrUyiMfAIBCG7QWz7H2o/Library/Caches/com.apple.xbs/Sources/CoreMedia_CoreMedia/Sources/Platform/Darwin/DarwinDebug.c %s: dlopen(QuartzCore) failed: \"%s\""
+ "/AppleInternal/Library/BuildRoots/4~CGCxugBT9kz2KyA9HQuXrUyiMfAIBCG7QWz7H2o/Library/Caches/com.apple.xbs/Sources/CoreMedia_CoreMedia/Sources/Platform/Darwin/DarwinGzip.c %s: zlib error: %d: %s"
+ "/AppleInternal/Library/BuildRoots/4~CGCxugBT9kz2KyA9HQuXrUyiMfAIBCG7QWz7H2o/Library/Caches/com.apple.xbs/Sources/CoreMedia_CoreMedia/Sources/Platform/Darwin/DarwinSynchronization.c %s: pthread_cond_destroy ERROR %d mutex %p; just leaking it"
+ "/AppleInternal/Library/BuildRoots/4~CGCxugBT9kz2KyA9HQuXrUyiMfAIBCG7QWz7H2o/Library/Caches/com.apple.xbs/Sources/CoreMedia_CoreMedia/Sources/Platform/Darwin/DarwinSynchronization.c %s: pthread_mutex_destroy ERROR %d mutex %p; just leaking it"
+ "/AppleInternal/Library/BuildRoots/4~CGCxugBT9kz2KyA9HQuXrUyiMfAIBCG7QWz7H2o/Library/Caches/com.apple.xbs/Sources/CoreMedia_CoreMedia/Sources/Platform/Darwin/FigMachUtilitiesFigOnly.c"
+ "/AppleInternal/Library/BuildRoots/4~CGCxugBT9kz2KyA9HQuXrUyiMfAIBCG7QWz7H2o/Library/Caches/com.apple.xbs/Sources/CoreMedia_CoreMedia/Sources/Platform/Darwin/FigMachUtilitiesFigOnly.c %s: NULL machPortHolder"
+ "/AppleInternal/Library/BuildRoots/4~CGCxugBT9kz2KyA9HQuXrUyiMfAIBCG7QWz7H2o/Library/Caches/com.apple.xbs/Sources/CoreMedia_CoreMedia/Sources/Utilities/FigBlockBufferUtilities.c %s: I don't expect to be called"
+ "/AppleInternal/Library/BuildRoots/4~CGCxugBT9kz2KyA9HQuXrUyiMfAIBCG7QWz7H2o/Library/Caches/com.apple.xbs/Sources/CoreMedia_CoreMedia/Sources/Utilities/FigDispatchUtilities.c %s: Couldn't create pthread root queue for priority %d"
+ "/AppleInternal/Library/BuildRoots/4~CGCxugBT9kz2KyA9HQuXrUyiMfAIBCG7QWz7H2o/Library/Caches/com.apple.xbs/Sources/CoreMedia_CoreMedia/Sources/Utilities/FigDispatchUtilities.c %s: FigDispatchAsyncSetPropertyImplementation callback returned %d; this async error will be discarded"
+ "/AppleInternal/Library/BuildRoots/4~CGCxugBT9kz2KyA9HQuXrUyiMfAIBCG7QWz7H2o/Library/Caches/com.apple.xbs/Sources/CoreMedia_CoreMedia/Sources/Utilities/FigDispatchUtilities.c %s: IMPORTANT NOTE TO FIG ENGINEERING: don't use DISPATCH_QUEUE_CONCURRENT with FigDispatchQueueCreateWithPriority; please migrate to FigDispatchQueueCreateTargetingPThreadRootQueueWithPriority"
+ "/AppleInternal/Library/BuildRoots/4~CGCxugBT9kz2KyA9HQuXrUyiMfAIBCG7QWz7H2o/Library/Caches/com.apple.xbs/Sources/CoreMedia_CoreMedia/Sources/Utilities/FigDispatchUtilities.c %s: sandbox check for creating dispatch workloop failed"
+ "/AppleInternal/Library/BuildRoots/4~CGCxugBT9kz2KyA9HQuXrUyiMfAIBCG7QWz7H2o/Library/Caches/com.apple.xbs/Sources/CoreMedia_CoreMedia/Sources/Utilities/FigJSONParser.c %s: JSONObjectWithData:options:error: failed but returned NSError with out-of-OSStatus-range error code %lld"
+ "/AppleInternal/Library/BuildRoots/4~CGCxugBT9kz2KyA9HQuXrUyiMfAIBCG7QWz7H2o/Library/Caches/com.apple.xbs/Sources/CoreMedia_CoreMedia/Sources/Utilities/FigJSONParser.c %s: dataWithJSONObjec:options:error: failed but returned NSError with out-of-OSStatus-range error code %lld"
+ "/AppleInternal/Library/BuildRoots/4~CGCxugBT9kz2KyA9HQuXrUyiMfAIBCG7QWz7H2o/Library/Caches/com.apple.xbs/Sources/CoreMedia_CoreMedia/Sources/Utilities/FigRetainProxy.c %s: [%p] Deallocating FigRetainProxy with with non-zero lockCount. See <rdar://155142378>"
+ "<<<< FigCustomURLHandling >>>> %s: %p: URL: %@ requestID: %llu"
- "/AppleInternal/Library/BuildRoots/4~CDysugAgE32mH30Ltu2Mh1wjhCNxpG0APl_vdTo/Library/Caches/com.apple.xbs/Sources/CoreMedia_CoreMedia/Prototypes/Endpoint/FigEndpointManagerUtilities.c %s: Nothing to do"
- "/AppleInternal/Library/BuildRoots/4~CDysugAgE32mH30Ltu2Mh1wjhCNxpG0APl_vdTo/Library/Caches/com.apple.xbs/Sources/CoreMedia_CoreMedia/Prototypes/IPC/FigOSEventLink.m"
- "/AppleInternal/Library/BuildRoots/4~CDysugAgE32mH30Ltu2Mh1wjhCNxpG0APl_vdTo/Library/Caches/com.apple.xbs/Sources/CoreMedia_CoreMedia/Prototypes/Player/ClientServer/FigSampleBufferAtomSerialization.c"
- "/AppleInternal/Library/BuildRoots/4~CDysugAgE32mH30Ltu2Mh1wjhCNxpG0APl_vdTo/Library/Caches/com.apple.xbs/Sources/CoreMedia_CoreMedia/Sources/Core/FigFormatDescription/FigMPEG4Bridge.c %s: iacb box has unknown codec_id %c%c%c%c"
- "/AppleInternal/Library/BuildRoots/4~CDysugAgE32mH30Ltu2Mh1wjhCNxpG0APl_vdTo/Library/Caches/com.apple.xbs/Sources/CoreMedia_CoreMedia/Sources/Core/FigFormatDescription/FigVideoFormatDescription.c %s: PointCloud format description %p [ %c%c%c%c ] does not have a NumberOfPointsPerSample extension"
- "/AppleInternal/Library/BuildRoots/4~CDysugAgE32mH30Ltu2Mh1wjhCNxpG0APl_vdTo/Library/Caches/com.apple.xbs/Sources/CoreMedia_CoreMedia/Sources/Core/FigFormatDescription/HapticDescriptionBridge.c %s: Warning: HapticFormatDescription has ignored a \"%@\" extension when converting to the sample description."
- "/AppleInternal/Library/BuildRoots/4~CDysugAgE32mH30Ltu2Mh1wjhCNxpG0APl_vdTo/Library/Caches/com.apple.xbs/Sources/CoreMedia_CoreMedia/Sources/Core/FigFormatDescription/PointCloudDescriptionBridge.c %s: Warning: PointCloudFormatDescription has ignored a \"%@\" extension when converting to the sample description."
- "/AppleInternal/Library/BuildRoots/4~CDysugAgE32mH30Ltu2Mh1wjhCNxpG0APl_vdTo/Library/Caches/com.apple.xbs/Sources/CoreMedia_CoreMedia/Sources/Core/FigFormatDescription/SceneDescriptionBridge.c %s: Warning: SceneFormatDescription has ignored a \"%@\" extension when converting to the sample description."
- "/AppleInternal/Library/BuildRoots/4~CDysugAgE32mH30Ltu2Mh1wjhCNxpG0APl_vdTo/Library/Caches/com.apple.xbs/Sources/CoreMedia_CoreMedia/Sources/Core/FigNotificationCenter/FigNotificationCenterCF.c %s: %d weak listener%s registered"
- "/AppleInternal/Library/BuildRoots/4~CDysugAgE32mH30Ltu2Mh1wjhCNxpG0APl_vdTo/Library/Caches/com.apple.xbs/Sources/CoreMedia_CoreMedia/Sources/Core/FigNotificationCenter/FigNotificationCenterCF.c %s: Will dump weak listener hashes on USR2 signals and in sysdiagnoses -- thank you for setting \"defaults write com.apple.coremedia weak_hash_dump -bool YES\""
- "/AppleInternal/Library/BuildRoots/4~CDysugAgE32mH30Ltu2Mh1wjhCNxpG0APl_vdTo/Library/Caches/com.apple.xbs/Sources/CoreMedia_CoreMedia/Sources/Core/FigNotificationCenter/FigNotificationCenterCF.c %s: Will not use CF ObjC SPI to implement weak listeners -- thank you for setting \"defaults write com.apple.coremedia weak_avoid_cf_spi -bool YES\""
- "/AppleInternal/Library/BuildRoots/4~CDysugAgE32mH30Ltu2Mh1wjhCNxpG0APl_vdTo/Library/Caches/com.apple.xbs/Sources/CoreMedia_CoreMedia/Sources/Core/FigNotificationCenter/FigNotificationCenterCF.c %s: hash %@ already registered -- suggests weak listener abandonment"
- "/AppleInternal/Library/BuildRoots/4~CDysugAgE32mH30Ltu2Mh1wjhCNxpG0APl_vdTo/Library/Caches/com.apple.xbs/Sources/CoreMedia_CoreMedia/Sources/Core/FigNotificationCenter/FigNotificationCenterCF.c %s: hash %@ not found -- confirm parameters to FigNotificationCenterRemoveWeakListener are correct"
- "/AppleInternal/Library/BuildRoots/4~CDysugAgE32mH30Ltu2Mh1wjhCNxpG0APl_vdTo/Library/Caches/com.apple.xbs/Sources/CoreMedia_CoreMedia/Sources/Core/FigSync/FigHostTimeClock.c %s: Singleton FigHostTimeClock was overreleased"
- "/AppleInternal/Library/BuildRoots/4~CDysugAgE32mH30Ltu2Mh1wjhCNxpG0APl_vdTo/Library/Caches/com.apple.xbs/Sources/CoreMedia_CoreMedia/Sources/Platform/Darwin/DarwinDebug.c %s: %s to log URLs -- thank you for setting \"defaults write com.apple.coremedia logurls -bool %s\""
- "/AppleInternal/Library/BuildRoots/4~CDysugAgE32mH30Ltu2Mh1wjhCNxpG0APl_vdTo/Library/Caches/com.apple.xbs/Sources/CoreMedia_CoreMedia/Sources/Platform/Darwin/DarwinDebug.c %s: dlopen(QuartzCore) failed: \"%s\""
- "/AppleInternal/Library/BuildRoots/4~CDysugAgE32mH30Ltu2Mh1wjhCNxpG0APl_vdTo/Library/Caches/com.apple.xbs/Sources/CoreMedia_CoreMedia/Sources/Platform/Darwin/DarwinGzip.c %s: zlib error: %d: %s"
- "/AppleInternal/Library/BuildRoots/4~CDysugAgE32mH30Ltu2Mh1wjhCNxpG0APl_vdTo/Library/Caches/com.apple.xbs/Sources/CoreMedia_CoreMedia/Sources/Platform/Darwin/DarwinSynchronization.c %s: pthread_cond_destroy ERROR %d mutex %p; just leaking it"
- "/AppleInternal/Library/BuildRoots/4~CDysugAgE32mH30Ltu2Mh1wjhCNxpG0APl_vdTo/Library/Caches/com.apple.xbs/Sources/CoreMedia_CoreMedia/Sources/Platform/Darwin/DarwinSynchronization.c %s: pthread_mutex_destroy ERROR %d mutex %p; just leaking it"
- "/AppleInternal/Library/BuildRoots/4~CDysugAgE32mH30Ltu2Mh1wjhCNxpG0APl_vdTo/Library/Caches/com.apple.xbs/Sources/CoreMedia_CoreMedia/Sources/Platform/Darwin/FigMachUtilitiesFigOnly.c"
- "/AppleInternal/Library/BuildRoots/4~CDysugAgE32mH30Ltu2Mh1wjhCNxpG0APl_vdTo/Library/Caches/com.apple.xbs/Sources/CoreMedia_CoreMedia/Sources/Platform/Darwin/FigMachUtilitiesFigOnly.c %s: NULL machPortHolder"
- "/AppleInternal/Library/BuildRoots/4~CDysugAgE32mH30Ltu2Mh1wjhCNxpG0APl_vdTo/Library/Caches/com.apple.xbs/Sources/CoreMedia_CoreMedia/Sources/Utilities/FigBlockBufferUtilities.c %s: I don't expect to be called"
- "/AppleInternal/Library/BuildRoots/4~CDysugAgE32mH30Ltu2Mh1wjhCNxpG0APl_vdTo/Library/Caches/com.apple.xbs/Sources/CoreMedia_CoreMedia/Sources/Utilities/FigDispatchUtilities.c %s: Couldn't create pthread root queue for priority %d"
- "/AppleInternal/Library/BuildRoots/4~CDysugAgE32mH30Ltu2Mh1wjhCNxpG0APl_vdTo/Library/Caches/com.apple.xbs/Sources/CoreMedia_CoreMedia/Sources/Utilities/FigDispatchUtilities.c %s: FigDispatchAsyncSetPropertyImplementation callback returned %d; this async error will be discarded"
- "/AppleInternal/Library/BuildRoots/4~CDysugAgE32mH30Ltu2Mh1wjhCNxpG0APl_vdTo/Library/Caches/com.apple.xbs/Sources/CoreMedia_CoreMedia/Sources/Utilities/FigDispatchUtilities.c %s: IMPORTANT NOTE TO FIG ENGINEERING: don't use DISPATCH_QUEUE_CONCURRENT with FigDispatchQueueCreateWithPriority; please migrate to FigDispatchQueueCreateTargetingPThreadRootQueueWithPriority"
- "/AppleInternal/Library/BuildRoots/4~CDysugAgE32mH30Ltu2Mh1wjhCNxpG0APl_vdTo/Library/Caches/com.apple.xbs/Sources/CoreMedia_CoreMedia/Sources/Utilities/FigDispatchUtilities.c %s: sandbox check for creating dispatch workloop failed"
- "/AppleInternal/Library/BuildRoots/4~CDysugAgE32mH30Ltu2Mh1wjhCNxpG0APl_vdTo/Library/Caches/com.apple.xbs/Sources/CoreMedia_CoreMedia/Sources/Utilities/FigJSONParser.c %s: JSONObjectWithData:options:error: failed but returned NSError with out-of-OSStatus-range error code %lld"
- "/AppleInternal/Library/BuildRoots/4~CDysugAgE32mH30Ltu2Mh1wjhCNxpG0APl_vdTo/Library/Caches/com.apple.xbs/Sources/CoreMedia_CoreMedia/Sources/Utilities/FigJSONParser.c %s: dataWithJSONObjec:options:error: failed but returned NSError with out-of-OSStatus-range error code %lld"
- "/AppleInternal/Library/BuildRoots/4~CDysugAgE32mH30Ltu2Mh1wjhCNxpG0APl_vdTo/Library/Caches/com.apple.xbs/Sources/CoreMedia_CoreMedia/Sources/Utilities/FigRetainProxy.c %s: [%p] Deallocating FigRetainProxy with with non-zero lockCount. See <rdar://155142378>"
- "<<<< FigCustomURLHandling >>>> %s: %p: URL: %{private}@ requestID: %llu"

```
